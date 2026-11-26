ï»¿# PresenêÂ§a na IA

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![PresenêÂ§a na IA](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/arckhe-/guia/)

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

**PresenêÂ§a na IA** êÂ© um kit grêÂ¡tis para vocêÂª oferecer, como serviêÂ§o, a organizaêÂ§êÂ£o de uma empresa nas inteligêÂªncias artificiais: o cadastro na Central de NegêÂ³cios do ChatGPT (lanêÂ§ada em versêÂ£o beta pela OpenAI em 10/11/2026), a verificaêÂ§êÂ£o de que a empresa êÂ© do dono, a ficha com os dados certos e o acompanhamento todo mêÂªs. Serve para quem trabalha com tecnologia, marketing digital, consultoria ou agêÂªncia. Traz o diagnêÂ³stico do "antes", o checklist do cliente, a proposta, o relatêÂ³rio mensal e um pedido pronto para uma IA montar tudo com vocêÂª.

Empresas vêÂ£o pagar para aparecer no ChatGPT. O cliente pergunta para a IA quem faz o serviêÂ§o na cidade dele, e a empresa nêÂ£o aparece, ou aparece outra com nome parecido. Quase nenhum dono sabe que pode corrigir isso.

## ê°Å¸ââ Guia de uso

Guia completo (landing + passo a passo): **https://linnoff88-dev.github.io/arckhe-/guia/**

## Kit irmêÂ£o: o cadastro passo a passo

O passo a passo do cadastro na Central de NegêÂ³cios, com as telas reais do nosso caso (linnoff88-dev) e um agente que faz o cadastro no navegador, estêÂ¡ no **[linnoff88-dev/empresa-no-chatgpt](https://github.com/linnoff88-dev/empresa-no-chatgpt)** ([guia](https://linnoff88-dev.github.io/arckhe-/guia/)). Este repo êÂ© a camada de **serviêÂ§o**: como diagnosticar, vender, entregar e acompanhar isso para outras empresas.

## Baseado em

- **OpenAI, "Empresas no ChatGPT" (10/11/2026):** beta; na Central de NegêÂ³cios a empresa reivindica o perfil, atualiza as informaêÂ§êÂµes e vêÂª menêÂ§êÂµes, cliques no site e os temas em que aparece; 1,2 bilhêÂ£o de pessoas usam o ChatGPT por semana. https://openai.com/pt-BR/index/introducing-businesses-chatgpt/
- **O cadastro real da linnoff88-dev (22/11/2026):** antes, a busca pela marca mostrava um instituto do meio ambiente. Ver o kit irmêÂ£o.

## Pedido para colar no Claude Code ou no Codex

Ver [`PEDIDO-AGENTE.md`](PEDIDO-AGENTE.md). Ele lêÂª os dois kits, monta o diagnêÂ³stico com vocêÂª, a proposta e a ficha, e nêÂ£o mexe em conta nem DNS sem o seu "sim".

## O que tem no kit

| Arquivo | Para quêÂª |
|---|---|
| [`kit/1-o-servico.md`](kit/1-o-servico.md) | as 5 peêÂ§as, os 3 pacotes, como calcular o preêÂ§o e o que nêÂ£o prometer |
| [`kit/2-diagnostico.md`](kit/2-diagnostico.md) | as 4 perguntas e como ler o resultado |
| [`kit/3-checklist-cliente.md`](kit/3-checklist-cliente.md) | o que pedir ao cliente antes de comeêÂ§ar |
| [`kit/4-proposta.md`](kit/4-proposta.md) | modelo de proposta |
| [`kit/5-relatorio-mensal.md`](kit/5-relatorio-mensal.md) | modelo do relatêÂ³rio de todo mêÂªs |
| [`kit/diagnostico.py`](kit/diagnostico.py) | gera as perguntas e marca as respostas (nota 0ê¢â¬â100) |

---

## InstalaêÂ§êÂ£o têÂ©cnica

PrêÂ©-requisitos: Python 3.10+ (sêÂ³ biblioteca padrêÂ£o). Nenhuma API êÂ© chamada: as perguntas sêÂ£o feitas êÂ  mêÂ£o nas IAs.

```bash
git clone https://github.com/linnoff88-dev/presenca-na-ia && cd presenca-na-ia
python3 kit/diagnostico.py perguntas kit/exemplo-empresa.json
python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-antes.json --saida antes.md
python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-depois.json --saida depois.md
python3 -m unittest discover -s tests
```

- `exemplo-empresa.json`: `nome`, `apelidos`, `cidade`, `servico`, `site`, `concorrentes`, `confunde_com`.
- `exemplo-respostas-antes.json` / `exemplo-respostas-depois.json`: `{"<IA>": ["resposta 1", "resposta 2", "resposta 3", "resposta 4"]}`, um arquivo para o antes e outro para o depois; chaves que comeêÂ§am com `_` sêÂ£o ignoradas. As respostas do exemplo sêÂ£o ilustrativas.
- Marca trocada: nome citado junto com uma organizaêÂ§êÂ£o de `confunde_com`, sem o site certo, nêÂ£o conta como "aparece". Nomes sêÂ£o comparados como palavra inteira ("ARCKHÉ" nêÂ£o casa com "cARCKHÉ").
- Nota de cada resposta: aparece 40 + site certo 30 + sem confusêÂ£o 20 + sem concorrente 10. Sai 0 com o relatêÂ³rio, 2 com JSON errado.
- Testes (12): nota cheia, ausente, confusêÂ£o e concorrente, marca trocada, palavra inteira, acento e caixa, domêÂ­nio, perguntas, relatêÂ³rio antes e depois do exemplo, campo faltando, respostas vazias, `--saida`.

## O processo, do inêÂ­cio ao fim

ê°Å¸Â§Â  = vocêÂª com o agente êÂ· ê¢Å¡â¢ê¯Â¸Â = script êÂ· ê°Å¸âÂ¤ = o dono da empresa

| # | Passo | Comando / o que acontece | Quem |
|---|---|---|---|
| 1 | Dados da empresa | preencher `kit/exemplo-empresa.json` (ou uma cêÂ³pia) | ê°Å¸Â§Â  |
| 2 | Perguntas | `python3 kit/diagnostico.py perguntas <empresa.json>` | ê¢Å¡â¢ê¯Â¸Â |
| 3 | Respostas | fazer as 4 perguntas no ChatGPT, Gemini, Claude e Perplexity; colar no `respostas.json` | ê°Å¸Â§Â  |
| 4 | DiagnêÂ³stico | `python3 kit/diagnostico.py relatorio <empresa.json> <respostas.json> --saida antes.md` | ê¢Å¡â¢ê¯Â¸Â |
| 5 | Proposta | preencher `kit/4-proposta.md` com o diagnêÂ³stico | ê°Å¸Â§Â  |
| 6 | Checklist | pedir ao cliente o que estêÂ¡ em `kit/3-checklist-cliente.md` | ê°Å¸Â§Â  + ê°Å¸âÂ¤ |
| 7 | Cadastro e verificaêÂ§êÂ£o | seguir o [empresa-no-chatgpt](https://github.com/linnoff88-dev/empresa-no-chatgpt) (TXT no DNS; identidade pelo dono) | ê°Å¸Â§Â  + ê°Å¸âÂ¤ |
| 8 | Depois | refazer os passos 3ê¢â¬â4 com `--saida depois.md` e mostrar ao cliente | ê¢Å¡â¢ê¯Â¸Â |
| 9 | Todo mêÂªs | passos 3ê¢â¬â4 + painel da Central ê¢â â `kit/5-relatorio-mensal.md` | ê°Å¸Â§Â  |

## LicenêÂ§a

MIT

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>