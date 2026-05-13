"""
diagnostico.py — Ferramenta de diagnóstico de PDF para FreteScan Pro
Rode: python diagnostico.py caminho_do_arquivo.pdf
"""
import sys, io
import pdfplumber
import pandas as pd

def diagnosticar_pdf(caminho: str):
    print(f"\n{'='*60}")
    print(f"DIAGNÓSTICO: {caminho}")
    print(f"{'='*60}\n")

    with open(caminho, "rb") as f:
        dados = f.read()

    with pdfplumber.open(io.BytesIO(dados)) as pdf:
        print(f"Total de páginas: {len(pdf.pages)}\n")

        for i, page in enumerate(pdf.pages, 1):
            print(f"─── PÁGINA {i} ───────────────────────────────────")

            # Tabelas
            tabs = page.extract_tables()
            print(f"  Tabelas encontradas: {len(tabs)}")
            for j, tab in enumerate(tabs):
                print(f"\n  [Tabela {j+1}]  Linhas: {len(tab)}")
                if tab:
                    print(f"  Cabeçalho: {tab[0]}")
                    if len(tab) > 1:
                        print(f"  Linha 1:   {tab[1]}")
                    if len(tab) > 2:
                        print(f"  Linha 2:   {tab[2]}")

            # Texto
            texto = page.extract_text()
            if texto:
                linhas = texto.split("\n")
                print(f"\n  Primeiras 10 linhas de texto:")
                for linha in linhas[:10]:
                    print(f"    {linha}")
            print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python diagnostico.py arquivo.pdf")
    else:
        diagnosticar_pdf(sys.argv[1])
