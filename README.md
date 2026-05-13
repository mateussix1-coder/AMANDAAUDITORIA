# FreteScan Pro

Aplicativo Streamlit para auditar relatórios de frete ATUA x GW por CTE. O sistema lê os PDFs, cruza valores de empresa e motorista, separa divergências reais de arredondamentos e exporta os resultados em CSV, Excel e PDF.

## Arquivos

- `app.py`: interface Streamlit.
- `auditoria_engine.py`: motor de leitura, comparação, histórico e exportação.
- `validar_regressao.py`: teste rápido da regra de comparação e resumo financeiro.
- `teste_parser_corrigido.py`: teste completo usando os PDFs reais.
- `ABRIL ATUA.pdf` e `ABRIL GW.pdf`: arquivos de amostra.

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Como validar

Teste rápido da regra de negócio:

```bash
python validar_regressao.py
```

Teste completo com os PDFs reais:

```bash
python teste_parser_corrigido.py "ABRIL ATUA.pdf" "ABRIL GW.pdf"
```

## Primeiro debug esperado

ATUA:

- 1752 = Empresa 23919.00 / Motorista 24839.65
- 1753 = Empresa 12892.50 / Motorista 13388.62
- 1754 = Empresa 1860.00 / Motorista 1931.61

GW:

- 1752 = Empresa 23919.00 / Motorista 24839.88
- 1753 = Empresa 12892.50 / Motorista 12892.50
- 1754 = Empresa 1860.00 / Motorista 1931.61

Se o sistema ainda mostrar ATUA 0/0 ou GW 2391900, ele ainda está usando parser antigo ou cache.
