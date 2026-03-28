# Workflow: Atualizar README do Perfil GitHub

## Uso
/atualizar-perfil

## Passos
1. Ler `antigravity/brain/projetos/index.md` (todos os projetos)
2. Para cada projeto, ler `contexto/{slug}.json`
3. Verificar `diferencial_portfolio` de cada projeto para evitar repetição
4. @agente-readme gera o README.md completo do perfil em layout grade 2 colunas
   incluindo thumbnails de cada projeto
5. Ordenar projetos por tipo: fullstack primeiro, depois notebooks por complexidade
6. Mostrar preview como Artifact
7. Instruções para publicar no GitHub (repo `athosroque/athosroque`)

## Formato da grade
Cada card tem: thumbnail (og-image), título, 1 linha de descrição,
badges de libs, link para o site do projeto.

## Regra
O `portfolio-sites` NÃO é o repo do perfil GitHub.
O README do perfil fica em `athosroque/athosroque`.
O `portfolio-sites` serve apenas para hospedar sites estáticos.
