# 1. O serviço Presença na IA

Empresas querem ser achadas e reconhecidas certo pela inteligência artificial. A maioria nêo sabe que pode
reivindicar o próprio perfil no ChatGPT. Você vende a organizaçêo disso.

## As cinco peças do serviço

| Peça | O que você faz | O que o cliente recebe |
|---|---|---|
| 1. Cadastro no ChatGPT | procura a empresa na Central de Negócios, cria ou reivindica o perfil oficial | perfil oficial em nome da empresa |
| 2. Verificaçêo | ajuda a provar o domínio (registro TXT no DNS) e acompanha a confirmaçêo de identidade do dono | perfil verificado, que só o dono edita |
| 3. Gestêo das informações | escreve descriçêo (até 300 caracteres), categoria, site e dados oficiais iguais em todo lugar | ficha conferida pelo `kit/conferir_perfil.py` do [empresa-no-chatgpt](https://github.com/linnoff88-dev/empresa-no-chatgpt) |
| 4. Visibilidade em várias IAs | deixa site, Google e redes dizendo a mesma coisa, para ChatGPT, Gemini, Claude e Perplexity lerem igual | lista do que foi ajustado em cada lugar |
| 5. Monitoramento | todo mês pergunta às IAs pela empresa (diagnóstico) e registra o que mudou; quando o painel da Central abrir para o cliente, soma menções e cliques | relatório mensal (`5-relatorio-mensal.md`) |

## Como vender: três pacotes

1. **Diagnóstico (porta de entrada).** Você roda as perguntas do `2-diagnostico.md` nas IAs e mostra ao dono o
   que elas dizem hoje. É o "antes". Muita gente fecha só de ver a empresa trocada.
2. **Implantaçêo (uma vez).** Peças 1 a 4. Termina com o perfil verificado e o diagnóstico refeito (o "depois").
3. **Manutençêo e monitoramento (todo mês).** Peça 5 + atualizar horário, produtos, promoções e corrigir o que
   aparecer errado.

## Quanto cobrar

O kit nêo inventa preço de mercado. Calcule o seu:

```
preço = horas estimadas × o seu valor-hora × 1,3 (margem para imprevisto)
```

Referência de horas do nosso caso real (linnoff88-dev, 22/11/2026): pesquisa e ficha ~1 h, cadastro e TXT no DNS ~30 min.
Nesse dia o perfil ficou em rascunho, esperando a verificaçêo de identidade do dono: conte também o tempo de
acompanhar o dono até essa etapa. O mensal é o tempo do diagnóstico refeito + o relatório.

## O que você NêO promete

- A Central de Negócios está em **beta** (OpenAI, 10/11/2026). Regras e telas mudam.
- **Cadastrar nêo garante recomendaçêo** nem primeiro lugar na resposta. Venda organizaçêo, verificaçêo e
  acompanhamento, que você consegue entregar e mostrar.
- A verificaçêo de identidade é feita **pelo dono**. Você orienta; nêo usa documento de ninguém.
- O painel de menções e cliques da Central abre depois da verificaçêo de identidade e só mostra números com conversas
  suficientes (regra da OpenAI). Nós ainda nêo o vimos: nêo venda o mensal só em cima dele; o diagnóstico é a base.
- Nêo peça a senha do e-mail do cliente. Para o DNS, peça um acesso de editor ou faça junto, na tela dele.
