#!/usr/bin/env python3
"""Diagnóstico Presença na IA: o que as IAs dizem de uma empresa.

Não chama nenhuma IA nem API: você faz as perguntas à mão (ChatGPT, Gemini, Claude, Perplexity),
cola as respostas num JSON e este script marca cada uma e soma a nota.

Uso:
  python3 kit/diagnostico.py perguntas <empresa.json>
  python3 kit/diagnostico.py relatorio <empresa.json> <respostas.json> [--saida relatorio.md]

Nota por resposta (0-100): aparece 40 + site certo 30 + sem confusão 20 + sem concorrente 10.
Nome citado junto com uma organização de "confunde_com", sem o site certo, é marca trocada: não conta como "aparece".
Faça um arquivo de respostas para o "antes" e outro para o "depois" (não misture os dois no mesmo relatório).
Sai 0 com o relatório; 2 se o JSON estiver errado.
"""
import json
import re
import sys
import unicodedata

PERGUNTAS = [
    "O que você sabe da empresa {nome}?",
    "Quais são as melhores empresas de {servico} em {cidade}?",
    "Qual é o site oficial da {nome}?",
    "Você recomenda uma empresa de {servico} em {cidade}?",
]


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", t)


def dominio(site: str) -> str:
    s = norm(site)
    s = re.sub(r"^https?://", "", s)
    s = re.sub(r"^www\.", "", s)
    return s.split("/")[0]


def perguntas(emp: dict) -> list[str]:
    return [p.format(**emp) for p in PERGUNTAS]


def tem(r: str, termo: str) -> bool:
    """termo como palavra inteira ('INEMA' não casa com 'cinema')."""
    t = norm(termo).strip()
    return bool(t) and re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", r) is not None


def marcar(emp: dict, resposta: str) -> dict:
    r = norm(resposta)
    nomes = [emp["nome"]] + emp.get("apelidos", [])
    site = bool(emp.get("site")) and tem(r, dominio(emp["site"]))
    confusao = [c for c in emp.get("confunde_com", []) if tem(r, c)]
    concorr = [c for c in emp.get("concorrentes", []) if tem(r, c)]
    # nome citado junto com a organização que a IA confunde, sem o site certo = marca trocada, não conta
    aparece = any(tem(r, n) for n in nomes if n) and (site or not confusao)
    nota = 40 * aparece + 30 * site + 20 * (not confusao) + 10 * (not concorr)
    return {"aparece": aparece, "site": site, "confusao": confusao, "concorrentes": concorr, "nota": nota}


def validar(emp: dict) -> None:
    for c in ("nome", "cidade", "servico"):
        if not emp.get(c):
            raise ValueError(f"empresa.json sem '{c}'")


def relatorio(emp: dict, respostas: dict) -> tuple[str, int]:
    linhas = [f"# Diagnóstico Presença na IA — {emp['nome']}", "",
              "| IA | Pergunta | Aparece | Site | Confusão | Concorrente | Nota |",
              "|---|---|---|---|---|---|---|"]
    respostas = {k: v for k, v in respostas.items() if not k.startswith("_")}
    notas = []
    for ia, lista in respostas.items():
        for i, resp in enumerate(lista, 1):
            m = marcar(emp, resp)
            notas.append(m["nota"])
            linhas.append(
                f"| {ia} | {i} | {'✅' if m['aparece'] else '❌'} | {'✅' if m['site'] else '—'} | "
                f"{'❌ ' + ', '.join(m['confusao']) if m['confusao'] else '✅'} | "
                f"{'⚠️ ' + ', '.join(m['concorrentes']) if m['concorrentes'] else '✅'} | {m['nota']} |")
    if not notas:
        raise ValueError("respostas.json vazio")
    media = round(sum(notas) / len(notas))
    ias = [ia for ia, lista in respostas.items() if any(marcar(emp, r)["aparece"] for r in lista)]
    linhas += ["", f"**Nota geral: {media}/100** · a empresa aparece em {len(ias)} de {len(respostas)} IAs.",
               "", "Régua do kit para comparar antes e depois do mesmo cliente; não é medida oficial de nenhuma IA."]
    return "\n".join(linhas) + "\n", media


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] not in ("perguntas", "relatorio"):
        print(__doc__)
        return 2
    try:
        emp = json.load(open(argv[1], encoding="utf-8"))
        validar(emp)
        if argv[0] == "perguntas":
            for i, p in enumerate(perguntas(emp), 1):
                print(f"{i}. {p}")
            return 0
        resp = json.load(open(argv[2], encoding="utf-8"))
        texto, _ = relatorio(emp, resp)
    except (OSError, ValueError, KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2
    if "--saida" in argv:
        open(argv[argv.index("--saida") + 1], "w", encoding="utf-8").write(texto)
    print(texto, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
