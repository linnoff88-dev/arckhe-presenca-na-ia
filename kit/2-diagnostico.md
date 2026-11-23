# 2. Diagnóstico: o que as IAs dizem da empresa hoje

É a porta de entrada do serviço e o "antes" que você mostra ao dono.

## Passo a passo

1. Preencha `kit/exemplo-empresa.json` com nome, cidade, serviço, site e concorrentes conhecidos.
2. Gere as perguntas: `python3 kit/diagnostico.py perguntas kit/exemplo-empresa.json`.
3. Abra cada IA numa conversa nova, sem login de quem tem ligação com a empresa (janela anônima ajuda):
   ChatGPT, Gemini, Claude e Perplexity. Faça as mesmas perguntas, na mesma ordem.
4. Cole cada resposta num arquivo de respostas (modelo: `kit/exemplo-respostas-antes.json`), uma lista por IA, na ordem das perguntas. Um arquivo para o "antes" e outro para o "depois".
5. Gere o relatório: `python3 kit/diagnostico.py relatorio kit/exemplo-empresa.json kit/exemplo-respostas-antes.json`.

## As perguntas (o script troca os nomes)

1. O que você sabe da empresa {nome}?
2. Quais são as melhores empresas de {servico} em {cidade}?
3. Qual é o site oficial da {nome}?
4. Você recomenda uma empresa de {servico} em {cidade}?

## O que o relatório marca em cada resposta

| Marca | Quer dizer |
|---|---|
| ✅ aparece | o nome da empresa está na resposta (palavra inteira), sem estar trocado pela organização que a IA confunde |
| ✅ site certo | o domínio oficial está na resposta |
| ⚠️ concorrente | um concorrente da lista aparece |
| ❌ confusão | aparece um nome da lista `confunde_com` (ex.: o instituto do meio ambiente, no nosso caso) |
| ❌ ausente | a empresa não aparece |

A nota vai de 0 a 100 (aparece 40, site certo 30, sem confusão 20, sem concorrente 10). É só uma régua
para comparar o antes e o depois do mesmo cliente, não uma medida oficial de nenhuma IA.
