"""
Valida os parsers contra os PDFs reais.
Esperado:
  ATUA 1752 EmpresaA=23919.00  MotoristaA=24839.65
  GW   1752 EmpresaB=23919.00  MotoristaB=24839.88
"""
from decimal import Decimal
from auditoria_engine import extrair_atua, extrair_gw

ATUA = r"C:\Users\Mateus\Downloads\ABRIL ATUA.pdf"
GW   = r"C:\Users\Mateus\Downloads\ABRIL GW.pdf"

print("Extraindo ATUA...")
atua = extrair_atua(ATUA)
print(f"  Total ATUA: {len(atua)}")

print("Extraindo GW...")
gw = extrair_gw(GW)
print(f"  Total GW: {len(gw)}")

print()
print("=== Primeiros 5 CTEs ===")
for cte in ["1752", "1753", "1754", "1755", "1756"]:
    a = atua.get(cte)
    g = gw.get(cte)
    print(f"ATUA {cte}: EmpresaA={a['empresa'] if a else 'N/A'}  MotoristaA={a['motorista'] if a else 'N/A'}")
    print(f"GW   {cte}: EmpresaB={g['empresa'] if g else 'N/A'}  MotoristaB={g['motorista'] if g else 'N/A'}")
    print()

print("=== Validação 1752 ===")
a = atua.get("1752")
g = gw.get("1752")
assert a and a["empresa"] == Decimal("23919.00"), f"FALHOU EmpresaA: {a}"
assert a and a["motorista"] == Decimal("24839.65"), f"FALHOU MotoristaA: {a}"
assert g and g["empresa"] == Decimal("23919.00"), f"FALHOU EmpresaB: {g}"
assert g and g["motorista"] == Decimal("24839.88"), f"FALHOU MotoristaB: {g}"
print("  ✅ Todos os valores batem! Parser OK.")
