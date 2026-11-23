# PresenÃ§a na IA

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![PresenÃ§a na IA](guia/assets/banner.jpg)](https://inematds.github.io/presenca-na-ia/guia/)

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

**PresenÃ§a na IA** Ã© um kit grÃ¡tis para vocÃª oferecer, como serviÃ§o, a organizaÃ§Ã£o de uma empresa nas inteligÃªncias artificiais: o cadastro na Central de NegÃ³cios do ChatGPT (lanÃ§ada em versÃ£o beta pela OpenAI em 10/11/2026), a verificaÃ§Ã£o de que a empresa Ã© do dono, a ficha com os dados certos e o acompanhamento todo mÃªs. Serve para quem trabalha com tecnologia, marketing digital, consultoria ou agÃªncia. Traz o diagnÃ³stico do "antes", o checklist do cliente, a proposta, o relatÃ³rio mensal e um pedido pronto para uma IA montar tudo com vocÃª.

Empresas vÃ£o pagar para aparecer no ChatGPT. O cliente pergunta para a IA quem faz o serviÃ§o na cidade dele, e a empresa nÃ£o aparece, ou aparece outra com nome parecido. Quase nenhum dono sabe que pode corrigir isso.

## ðŸ“– Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/presenca-na-ia/guia/**

## Kit irmÃ£o: o cadastro passo a passo

O passo a passo do cadastro na Central de NegÃ³cios, com as telas reais do nosso caso (INEMATDS) e um agente que faz o cadastro no navegador, estÃ¡ no **[inematds/empresa-no-chatgpt](https://github.com/inematds/empresa-no-chatgpt)** ([guia](https://inematds.github.io/empresa-no-chatgpt/guia/)). Este repo Ã© a camada de **serviÃ§o**: como diagnosticar, vender, entregar e acompanhar isso para outras empresas.

## Baseado em

- **OpenAI, "Empresas no ChatGPT" (10/11/2026):** beta; na Central de NegÃ³cios a empresa reivindica o perfil, atualiza as informaÃ§Ãµes e vÃª menÃ§Ãµes, cliques no site e os temas em que aparece; 1,2 bilhÃ£o de pessoas usam o ChatGPT por semana. https://openai.com/pt-BR/index/introducing-businesses-chatgpt/
- **O cadastro real da INEMATDS (22/11/2026):** antes, a busca pela marca mostrava um instituto do meio ambiente. Ver o kit irmÃ£o.

## Pedido para colar no Claude Code ou no Codex

Ver [`PEDIDO-AGENTE.md`](PEDIDO-AGENTE.md). Ele lÃª os dois kits, monta o diagnÃ³stico com vocÃª, a proposta e a ficha, e nÃ£o mexe em conta nem DNS sem o seu "sim".

## O que tem no kit

| Arquivo | Para quÃª |
|---|---|
| [`kit/1-o-servico.md`](kit/1-o-servico.md) | as 5 peÃ§as, os 3 pacotes, como calcular o preÃ§o e o que nÃ£o prometer |
| [`kit/2-diagnostico.md`](kit/2-diagnostico.md) | as 4 perguntas e como ler o resultado |
| [`kit/3-checklist-cliente.md`](kit/3-checklist-cliente.md) | o que pedir ao cliente antes de comeÃ§ar |
| [`kit/4-proposta.md`](kit/4-proposta.md) | modelo de proposta |
| [`kit/5-relatorio-mensal.md`](kit/5-relatorio-mensal.md) | modelo do relatÃ³rio de todo mÃªs |
| [`kit/diagnostico.py`](kit/diagnostico.py) | gera as perguntas e marca as respostas (nota 0â€“100) |

---

## InstalaÃ§Ã£o tÃ©cnica

PrÃ©-requisitos: Python 3.10+ (sÃ³ biblioteca padrÃ£o). Nenhuma API Ã© chamada: as perguntas sÃ£o feitas Ã  mÃ£o nas IAs.

```bash
git clone https://github.com/inematds/presenca-na-ia && cd presenca-na-ia
python3 kit/diagnostico.py perguntas kit/exemplo-empresa.json
python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-antes.json --saida antes.md
python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-depois.json --saida depois.md
python3 -m unittest discover -s tests
```

- `exemplo-empresa.json`: `nome`, `apelidos`, `cidade`, `servico`, `site`, `concorrentes`, `confunde_com`.
- `exemplo-respostas-antes.json` / `exemplo-respostas-depois.json`: `{"<IA>": ["resposta 1", "resposta 2", "resposta 3", "resposta 4"]}`, um arquivo para o antes e outro para o depois; chaves que comeÃ§am com `_` sÃ£o ignoradas. As respostas do exemplo sÃ£o ilustrativas.
- Marca trocada: nome citado junto com uma organizaÃ§Ã£o de `confunde_com`, sem o site certo, nÃ£o conta como "aparece". Nomes sÃ£o comparados como palavra inteira ("INEMA" nÃ£o casa com "cinema").
- Nota de cada resposta: aparece 40 + site certo 30 + sem confusÃ£o 20 + sem concorrente 10. Sai 0 com o relatÃ³rio, 2 com JSON errado.
- Testes (12): nota cheia, ausente, confusÃ£o e concorrente, marca trocada, palavra inteira, acento e caixa, domÃ­nio, perguntas, relatÃ³rio antes e depois do exemplo, campo faltando, respostas vazias, `--saida`.

## O processo, do inÃ­cio ao fim

ðŸ§  = vocÃª com o agente Â· âš™ï¸ = script Â· ðŸ‘¤ = o dono da empresa

| # | Passo | Comando / o que acontece | Quem |
|---|---|---|---|
| 1 | Dados da empresa | preencher `kit/exemplo-empresa.json` (ou uma cÃ³pia) | ðŸ§  |
| 2 | Perguntas | `python3 kit/diagnostico.py perguntas <empresa.json>` | âš™ï¸ |
| 3 | Respostas | fazer as 4 perguntas no ChatGPT, Gemini, Claude e Perplexity; colar no `respostas.json` | ðŸ§  |
| 4 | DiagnÃ³stico | `python3 kit/diagnostico.py relatorio <empresa.json> <respostas.json> --saida antes.md` | âš™ï¸ |
| 5 | Proposta | preencher `kit/4-proposta.md` com o diagnÃ³stico | ðŸ§  |
| 6 | Checklist | pedir ao cliente o que estÃ¡ em `kit/3-checklist-cliente.md` | ðŸ§  + ðŸ‘¤ |
| 7 | Cadastro e verificaÃ§Ã£o | seguir o [empresa-no-chatgpt](https://github.com/inematds/empresa-no-chatgpt) (TXT no DNS; identidade pelo dono) | ðŸ§  + ðŸ‘¤ |
| 8 | Depois | refazer os passos 3â€“4 com `--saida depois.md` e mostrar ao cliente | âš™ï¸ |
| 9 | Todo mÃªs | passos 3â€“4 + painel da Central â†’ `kit/5-relatorio-mensal.md` | ðŸ§  |

## LicenÃ§a

MIT

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>