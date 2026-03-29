<div align="center">

# 🌐 Portfolio Sites

**Sites estáticos interativos dos projetos de Data Science e Full-Stack de Athos Roque**

[![Cloudflare Pages](https://img.shields.io/badge/Deploy-Cloudflare_Pages-F38020?style=flat-square&logo=cloudflare&logoColor=white)](#)
[![projetoathos.com.br](https://img.shields.io/badge/Domínio-projetoathos.com.br-00D4AA?style=flat-square)](#)

</div>

---

## 📁 Estrutura

Cada subpasta é um projeto independente no Cloudflare Pages, servido em seu próprio subdomínio.

```text
portfolio-sites/
├── numpy-ecommerce-stats/       → numpy-ecommerce-stats.projetoathos.com.br
│   ├── index.html
│   └── data.json
├── analise-de-vendas-e-commerce/ → analise-de-vendas-e-commerce.projetoathos.com.br
│   ├── index.html
│   └── data.json
└── genesys-manager/             → genesys-manager.projetoathos.com.br
    ├── index.html
    └── data.json
```

## 🚀 Projetos

| Projeto | Tipo | Subdomínio |
|---|---|---|
| **E-commerce Analytics NumPy** | Data Science (EDA) | `numpy-ecommerce-stats.projetoathos.com.br` |
| **Análise de Vendas E-commerce** | Data Science (EDA) | `analise-de-vendas-e-commerce.projetoathos.com.br` |
| **Genesys Manager** | Full-Stack (FastAPI + Vue 3) | `genesys-manager.projetoathos.com.br` |

## ⚙️ Deploy

Cada subpasta deve ser configurada como um **projeto separado** no Cloudflare Pages:

1. `dash.cloudflare.com` → Workers & Pages → Create → Pages
2. Connect to Git → selecionar `portfolio-sites`
3. Build output directory: `/{nome-da-pasta}`
4. Custom Domain: `{nome-da-pasta}.projetoathos.com.br`

---

<div align="center">
  <sub>Gerado pelo sistema multi-agentes Antigravity · <a href="https://github.com/athosroque">athosroque</a></sub>
</div>
