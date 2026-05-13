from decimal import Decimal

import pandas as pd

from auditoria_engine import comparar, gerar_resumo_df, parse_money_br


def assert_close(label, atual, esperado, tolerancia=0.01):
    if abs(float(atual) - float(esperado)) > tolerancia:
        raise AssertionError(f"{label}: esperado {esperado}, recebido {atual}")


def main():
    df_a = pd.DataFrame([
        {"CTE": "1001", "EmpresaA": Decimal("100.00"), "MotoristaA": Decimal("120.00")},
        {"CTE": "1002", "EmpresaA": Decimal("50.00"), "MotoristaA": Decimal("80.20")},
        {"CTE": "1004", "EmpresaA": Decimal("10.00"), "MotoristaA": Decimal("10.00")},
    ])
    df_b = pd.DataFrame([
        {"CTE": "1002", "EmpresaB": Decimal("50.00"), "MotoristaB": Decimal("80.00")},
        {"CTE": "1003", "EmpresaB": Decimal("200.00"), "MotoristaB": Decimal("240.00")},
        {"CTE": "1004", "EmpresaB": Decimal("9.00"), "MotoristaB": Decimal("8.00")},
    ])

    df = comparar(df_a, df_b, Decimal("0.50"))
    por_cte = df.set_index("CTE")

    assert por_cte.loc["1001", "Status"] == "Faltante no B"
    assert_close("1001 Dif. Empresa", por_cte.loc["1001", "Dif. Empresa"], 100.00)
    assert_close("1001 Maior Diferenca", por_cte.loc["1001", "Maior Diferença"], 120.00)

    assert por_cte.loc["1002", "Status"] == "OK por arredondamento"
    assert_close("1002 Maior Diferenca", por_cte.loc["1002", "Maior Diferença"], 0.20)

    assert por_cte.loc["1003", "Status"] == "Faltante no A"
    assert_close("1003 Dif. Motorista", por_cte.loc["1003", "Dif. Motorista"], -240.00)
    assert_close("1003 Maior Diferenca", por_cte.loc["1003", "Maior Diferença"], 240.00)

    assert por_cte.loc["1004", "Status"] == "Divergente"
    assert_close("1004 Maior Diferenca", por_cte.loc["1004", "Maior Diferença"], 2.00)

    resumo = gerar_resumo_df(df)
    assert resumo["total"] == 4
    assert resumo["ok_arredondamento"] == 1
    assert resumo["divergentes"] == 1
    assert resumo["faltantes_a"] == 1
    assert resumo["faltantes_b"] == 1
    assert_close("Resumo dif empresa", resumo["dif_total_empresa"], -99.00)
    assert_close("Resumo dif motorista", resumo["dif_total_motorista"], -117.80)
    assert_close("Resumo impacto absoluto", resumo["impacto_absoluto"], 362.00)

    assert parse_money_br("23.919,00") == Decimal("23919.00")
    assert parse_money_br("24.839,65") == Decimal("24839.65")

    print("Regressao OK: comparacao, faltantes e resumo financeiro validados.")


if __name__ == "__main__":
    main()
