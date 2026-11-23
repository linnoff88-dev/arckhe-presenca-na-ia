# AI Presence

[![AI Presence](guia/assets/banner-en.jpg)](https://inematds.github.io/presenca-na-ia/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

**Presence in AI** is a free kit for offering businesses a service to organize their presence in AI tools: registering with the ChatGPT Business Directory (launched in beta by OpenAI on 11/10/2026), verifying that the business belongs to its owner, preparing a profile with accurate information, and monitoring it every month. It’s designed for people working in technology, digital marketing, consulting, or agencies. It includes a “before” diagnosis, a client checklist, a proposal, a monthly report, and a ready-to-use prompt for an AI to put everything together with you.

Businesses will pay to appear in ChatGPT. A client asks AI who provides a service in their city, but the business doesn’t appear—or another business with a similar name does. Almost no business owners know they can fix this.

## 📖 User guide

Full guide (landing page + step-by-step instructions): **https://inematds.github.io/presenca-na-ia/guia/en/**

## Companion kit: step-by-step registration

The step-by-step guide to registering with the Business Directory, using real screens from our case (INEMATDS) and an agent that handles registration in the browser, is in **[inematds/empresa-no-chatgpt](https://github.com/inematds/empresa-no-chatgpt)** ([guide](https://inematds.github.io/empresa-no-chatgpt/guia/en/)). This repo is the **service** layer: how to diagnose, sell, deliver, and monitor this service for other businesses.

## Based on

- **OpenAI, “Businesses in ChatGPT” (11/10/2026):** beta; in the Business Directory, businesses can claim their profile, update their information, and see mentions, website clicks, and the topics they appear for; 1.2 billion people use ChatGPT each week. https://openai.com/pt-BR/index/introducing-businesses-chatgpt/
- **INEMATDS’s actual registration (11/22/2026):** before, searches for the brand showed an environmental institute. See the companion kit.

## Prompt to paste into Claude Code or Codex

See [`PEDIDO-AGENTE.md`](PEDIDO-AGENTE.md) (in Portuguese). It reads both kits, works with you to create the diagnosis, proposal, and profile, and won’t touch any account or DNS without your “yes.”

## What’s in the kit

| File | Purpose |
|---|---|
| [`kit/1-o-servico.md`](kit/1-o-servico.md) (in Portuguese) | the 5 deliverables, the 3 packages, how to calculate the price, and what not to promise |
| [`kit/2-diagnostico.md`](kit/2-diagnostico.md) (in Portuguese) | the 4 questions and how to interpret the results |
| [`kit/3-checklist-cliente.md`](kit/3-checklist-cliente.md) (in Portuguese) | what to ask the client for before starting |
| [`kit/4-proposta.md`](kit/4-proposta.md) (in Portuguese) | proposal template |
| [`kit/5-relatorio-mensal.md`](kit/5-relatorio-mensal.md) (in Portuguese) | monthly report template |
| [`kit/diagnostico.py`](kit/diagnostico.py) | generates the questions and scores the answers (0–100) |

---

## Technical setup

Prerequisites: Python 3.10+ (standard library only). No APIs are called: the questions are asked manually in the AI tools.

```bash
git clone https://github.com/inematds/presenca-na-ia && cd presenca-na-ia
python3 kit/diagnostico.py perguntas kit/exemplo-empresa.json
python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-antes.json --saida antes.md
python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-depois.json --saida depois.md
python3 -m unittest discover -s tests
```

- `exemplo-empresa.json`: `nome`, `apelidos`, `cidade`, `servico`, `site`, `concorrentes`, `confunde_com`.
- `exemplo-respostas-antes.json` / `exemplo-respostas-depois.json`: `{"<IA>": ["resposta 1", "resposta 2", "resposta 3", "resposta 4"]}`, one file for before and another for after; keys beginning with `_` are ignored. The sample answers are illustrative.
- Misidentified brand: a name mentioned alongside an organization in `confunde_com`, without the correct website, does not count as “appearing.” Names are compared as whole words (“INEMA” does not match “cinema”).
- Score per answer: appears 40 + correct website 30 + no confusion 20 + no competitor 10. Exits with 0 for the report, 2 for invalid JSON.
- Tests (12): full score, missing, confusion and competitor, misidentified brand, whole word, accents and case, domain, questions, before and after sample reports, missing field, empty answers, `--saida`.

## The process, from start to finish

🧠 = you with the agent · ⚙️ = script · 👤 = business owner

| # | Step | Command / what happens | Who |
|---|---|---|---|
| 1 | Business details | fill in `kit/exemplo-empresa.json` (or a copy) | 🧠 |
| 2 | Questions | `python3 kit/diagnostico.py perguntas <empresa.json>` | ⚙️ |
| 3 | Answers | ask the 4 questions in ChatGPT, Gemini, Claude, and Perplexity; paste the answers into `respostas.json` | 🧠 |
| 4 | Diagnosis | `python3 kit/diagnostico.py relatorio <empresa.json> <respostas.json> --saida antes.md` | ⚙️ |
| 5 | Proposal | fill in `kit/4-proposta.md` with the diagnosis | 🧠 |
| 6 | Checklist | ask the client for the items in `kit/3-checklist-cliente.md` | 🧠 + 👤 |
| 7 | Registration and verification | follow [empresa-no-chatgpt](https://github.com/inematds/empresa-no-chatgpt) (TXT in DNS; identity verification by the owner) | 🧠 + 👤 |
| 8 | After | repeat steps 3–4 with `--saida depois.md` and show the client | ⚙️ |
| 9 | Every month | steps 3–4 + Directory dashboard → `kit/5-relatorio-mensal.md` | 🧠 |

## License

MIT