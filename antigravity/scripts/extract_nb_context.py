import json
import base64
import os

notebook_path = '/home/athos/Athos/notebook-docs/notebooks/DSA-Python-MiniProjeto3.ipynb'
slug = 'numpy-ecommerce-stats'
assets_dir = f'/home/athos/Athos/notebook-docs/assets/{slug}'
os.makedirs(assets_dir, exist_ok=True)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

extracted_images = []

count = 0
for cell in nb['cells']:
    if 'outputs' in cell:
        for output in cell['outputs']:
            if 'data' in output and 'image/png' in output['data']:
                img_data = output['data']['image/png']
                filename = f'plot_{count}.png'
                with open(os.path.join(assets_dir, filename), 'wb') as img_file:
                    img_file.write(base64.b64decode(img_data))
                
                # Infer description from cell source
                desc = "".join(cell.get('source', []))[:100].strip()
                extracted_images.append({
                    "filename": filename,
                    "cell_index": cell.get('id', 'unknown'),
                    "description": desc
                })
                count += 1

context = {
    "title": "Análise Estatística de Dados com NumPy Para a Área de Marketing",
    "slug": slug,
    "lib_usage": ["numpy", "pandas", "matplotlib", "seaborn"],
    "business_problem": "Determinar o perfil médio do usuário, clientes de alto valor e indicadores de conversão em plataforma de e-commerce.",
    "insights": [
        "Ticket médio de R$ 252,70.",
        "Clientes de alto valor visitam mais (33x/mês) e ficam mais tempo (37min).",
        "Alta correlação (0,83) entre visitas e tempo no site.",
        "Correlação perfeita (1.0) entre itens no carrinho e valor da compra (natural do modelo de negócio)."
    ],
    "images": extracted_images
}

with open(f'/home/athos/Athos/notebook-docs/contexto/{slug}.json', 'w', encoding='utf-8') as f:
    json.dump(context, f, indent=4, ensure_ascii=False)

print(f"Contexto e {count} imagens processados com sucesso.")
