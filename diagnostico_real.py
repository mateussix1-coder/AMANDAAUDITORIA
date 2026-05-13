import pdfplumber, re

MONEY_RE = re.compile(r"-?\d{1,3}(?:\.\d{3})*,\d{2}|-?\d+,\d{2}")

def dump_atua(caminho, n=50):
    print(f"\n{'='*60}  ATUA")
    linhas = []
    with pdfplumber.open(caminho) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            texto = page.extract_text() or ""
            for raw in texto.splitlines():
                t = raw.strip()
                if t:
                    linhas.append((page_num, t))
    for i, (pg, t) in enumerate(linhas[:n]):
        vals = MONEY_RE.findall(t)
        print(f"  [{i:03d}] pg{pg}  {repr(t[:120])}")
        if vals:
            print(f"         MONEY={vals}")

def dump_gw_line(caminho):
    print(f"\n{'='*60}  GW (linha 1752)")
    with pdfplumber.open(caminho) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            texto = page.extract_text() or ""
            for raw in texto.splitlines():
                t = raw.strip()
                if t.startswith("001752"):
                    vals = MONEY_RE.findall(t)
                    print(f"  pg{page_num}  {repr(t[:200])}")
                    print(f"  MONEY={vals}")
                    return

if __name__ == "__main__":
    atua = r"C:\Users\Mateus\Downloads\ABRIL ATUA.pdf"
    gw   = r"C:\Users\Mateus\Downloads\ABRIL GW.pdf"
    dump_atua(atua)
    dump_gw_line(gw)
