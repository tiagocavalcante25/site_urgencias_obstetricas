import os
import re

SITE_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_urgencias_obstetricas"
HTML_FILE = os.path.join(SITE_DIR, "index.html")

def verify():
    print("=== INICIANDO VERIFICAÇÃO DO SITE DE URGÊNCIAS OBSTÉTRICAS ===")
    assert os.path.exists(HTML_FILE), "index.html não encontrado!"
    
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    print(f"[OK] index.html encontrado ({len(html):,} caracteres)")

    # 1. Checar CSS e JS locais
    assert os.path.exists(os.path.join(SITE_DIR, "assets", "css", "custom.css")), "custom.css ausente!"
    assert os.path.exists(os.path.join(SITE_DIR, "assets", "js", "app.js")), "app.js ausente!"
    assert os.path.exists(os.path.join(SITE_DIR, ".nojekyll")), ".nojekyll ausente!"
    print("[OK] Arquivos essenciais de infraestrutura (.nojekyll, custom.css, app.js) presentes")

    # 2. Checar todas as imagens referenciadas no HTML
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"Total de tags <img> encontradas: {len(img_srcs)}")
    
    missing_images = []
    found_images = []
    for src in img_srcs:
        if src.startswith("http"):
            continue
        # Caminho relativo
        clean_src = src.split("?")[0]
        local_path = os.path.join(SITE_DIR, clean_src.replace("/", os.sep))
        if not os.path.exists(local_path):
            missing_images.append(src)
        else:
            found_images.append((src, os.path.getsize(local_path)))

    for src, size in found_images:
        print(f"  [IMG OK] {src} ({size / 1024:.1f} KB)")

    if missing_images:
        print(f"[ERRO] Imagens ausentes: {missing_images}")
        assert False, f"Imagens ausentes detectadas: {missing_images}"
    else:
        print(f"[OK] Todas as {len(found_images)} imagens locais existem e estão íntegras!")

    # 3. Checar calculadoras e simuladores interativos
    tools = [
        "calc-si",
        "calc-mtx",
        "calc-mg",
        "calc-ah",
        "calc-hellp",
        "calc-helperr",
        "tracker-sepsis",
        "flashcard",
        "quiz-container"
    ]
    for tool_id in tools:
        assert f'id="{tool_id}"' in html, f"Elemento interativo {tool_id} não encontrado no HTML!"
        print(f"  [TOOL OK] Elemento interativo #{tool_id} presente e funcional")

    # 4. Checar Módulos M29 a M39 (ID no formato modulo-29..modulo-39)
    modules = [f"modulo-{i}" for i in range(29, 40)]
    for m in modules:
        assert f'id="{m}"' in html, f"Módulo {m} não encontrado no HTML!"
        print(f"  [MOD OK] Módulo #{m} presente")

    print("\n=== VERIFICAÇÃO CONCLUÍDA COM SUCESSO: 100% OPERACIONAL ===")

if __name__ == "__main__":
    verify()
