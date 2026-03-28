# Workflow: Atualizar Projeto Existente

## Uso
/atualizar-projeto [slug-do-projeto] [o-que-mudou]

## Quando usar
Quando o notebook foi refinado, o README foi atualizado, ou screenshots
foram adicionados — e você quer regenerar os outputs sem reprocessar tudo do zero.

## Passos
1. Ler `contexto/{slug}.json` atual (versão anterior)
2. Ler a fonte atualizada (notebook ou repo, conforme `tipo_projeto`)
3. Identificar diff: o que mudou? (métricas, código, visualizações, conclusão, screenshots)
4. Regenerar apenas os agentes cujos inputs mudaram
5. @agente-revisor compara versão anterior vs nova
6. Mostrar diff dos outputs ao usuário
7. Confirmar antes de sobrescrever arquivos e fazer deploy
8. Atualizar `antigravity/brain/projetos/{slug}.md` com a nova versão
