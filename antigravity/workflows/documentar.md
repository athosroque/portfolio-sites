# Workflow: Documentar Projeto

## Uso
/documentar [caminho/para/notebook.ipynb]
/documentar [slug-do-projeto-fullstack]

## Modo recomendado
Checkpoint — o agente pausa para confirmação antes do deploy.

## Detecção de tipo
- Se o input é um `.ipynb` → tipo `notebook-eda` ou `notebook-ml`
- Se o input é um slug correspondente a uma pasta com `README.md` + código → tipo `fullstack-app`
- Se o input contém screenshots/relatórios exportados → tipo `dashboard-bi`

## Passos

### ETAPA 1 — Preparação

**Para notebooks** (Agent Manager spawna 2 agentes paralelos):

Agente A (@leitor-notebook):
  - Ler o arquivo .ipynb como JSON
  - Extrair: título, células markdown, células de código, outputs, imports
  - Criar slug em kebab-case a partir do título
  - Verificar se slug já existe em `contexto/` (projeto já processado?)
  - Gravar em `contexto/{slug}.json` (versão inicial)

Agente B (@agente-imagens):
  - Varrer o .ipynb em busca de outputs de imagem
  - Decodificar base64 e salvar em `assets/{slug}/plot_N.ext`
  - Gerar og-image.svg
  - Adicionar campo "imagens" ao `contexto/{slug}.json`

**Para fullstack** (sequencial):

@agente-contexto lê diretamente:
  - `README.md` do repositório
  - `docker-compose.yml`, `requirements.txt`, `package.json` (se existirem)
  - Código-fonte principal (rotas, modelos, componentes)
  - Grava `contexto/{slug}.json` com tipo `fullstack-app`

@agente-imagens:
  - Coleta screenshots existentes de `reports/figures/` ou `assets/`
  - Gera og-image.svg

### ETAPA 2 — Contexto (sequencial)
@agente-contexto:
  - Ler `contexto/{slug}.json` completo
  - Ler `antigravity/brain/projetos/index.md` para evitar narrativas duplicadas
  - Identificar domínio, problema, solução, decisões técnicas
  - Preencher `diferencial_portfolio`
  - Gerar headlines para GitHub e LinkedIn
  - Atualizar `contexto/{slug}.json` com campos de narrativa

### ETAPA 3 — Geração de outputs (Agent Manager spawna 3 agentes paralelos)
Agente A (@agente-readme):
  - Ler `contexto/{slug}.json`
  - Gerar bloco markdown com imagem principal embutida
  - Salvar em `outputs/readme-blocos/{slug}.md`

Agente B (@agente-linkedin):
  - Ler `contexto/{slug}.json`
  - Gerar post PT-BR (máx 1300 chars)
  - Gerar post EN (máx 1300 chars)
  - Salvar em `outputs/linkedin-posts/{slug}-pt.md` e `{slug}-en.md`

Agente C (@agente-site):
  - Ler `contexto/{slug}.json` + todos os assets em `assets/{slug}/`
  - Gerar `sites/{slug}/index.html` (completo, inline CSS/JS)
  - Gerar `sites/{slug}/data.json`
  - Copiar assets para `sites/{slug}/assets/`

### ETAPA 4 — Revisão (pausa para checkpoint)
@agente-revisor:
  - Verificar todos os outputs gerados (checklist completo)
  - Validar consistência do portfólio (narrativa não-duplicada)
  - Gerar relatório de revisão como Artifact
  - PAUSAR e mostrar relatório ao usuário antes de continuar

### ETAPA 5 — Deploy (após aprovação do usuário)
@agente-deploy:
  - Mostrar instruções exatas de terminal
  - Aguardar confirmação antes de qualquer git push

### ETAPA 6 — Brain
  - Salvar `contexto/{slug}.json` em `antigravity/brain/projetos/{slug}.md`
  - Atualizar `antigravity/brain/projetos/index.md`
