# teste_parser_corrigido.py
# Use este arquivo para testar o parser fora do Streamlit.
# Comando:
# python teste_parser_corrigido.py "ABRIL ATUA.pdf" "ABRIL GW.pdf"

import sys
from decimal import Decimal
from auditoria_engine import testar_parser_basico, linhas_para_dataframe

if len(sys.argv) < 3:
    print("Uso: python teste_parser_corrigido.py caminho_ATUA.pdf caminho_GW.pdf")
    sys.exit(1)

atua = sys.argv[1]
gw = sys.argv[2]

resultado = testar_parser_basico(atua, gw)
df = linhas_para_dataframe(resultado["linhas"])
df.to_csv("resultado_teste_auditoria.csv", sep=";", index=False, encoding="utf-8-sig")

print("\nTop 20 maiores diferenças:")
print(df.sort_values("Maior Diferença", ascending=False).head(20).to_string(index=False))
print("\nCSV gerado: resultado_teste_auditoria.csv")
