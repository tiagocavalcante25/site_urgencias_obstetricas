import os
import re

SITE_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_urgencias_obstetricas"
HTML_FILE = os.path.join(SITE_DIR, "index.html")

def update_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    print(f"Original HTML length: {len(html)}")

    # 1. Update <head>: viewport with viewport-fit=cover, apple tags, pre-render font-size script
    old_head_script = r"""  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro -->
  <script>
    (function() {
      try {
        const saved = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (saved === 'dark' || (!saved && prefersDark)) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      } catch (e) {}
    })();
  </script>"""

    new_head_meta_and_script = r"""  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Urgências e Emergências Obstétricas | Portal Médico Interativo</title>
  <meta name="description" content="Guia Completo e Interativo de Urgências e Emergências Obstétricas. Nível USMLE Step 2 CK / Step 3, Residência Médica, FEBRASGO, ACOG e Ministério da Saúde / SUS.">
  <meta name="theme-color" content="#e11d48">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro e escala de fonte -->
  <script>
    (function() {
      try {
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
        const savedFontSize = localStorage.getItem('urgencias_font_size') || 'normal';
        document.documentElement.setAttribute('data-font-size', savedFontSize);
      } catch (e) {}
    })();
  </script>"""

    # Replace viewport through old script
    old_head_pattern = r'<meta name="viewport" content="width=device-width, initial-scale=1\.0">.*?<!-- Previne Flash of Unstyled Content \(FOUC\) ao carregar tema escuro -->\s*<script>.*?</script>'
    html, count_head = re.subn(old_head_pattern, new_head_meta_and_script, html, flags=re.DOTALL)
    print(f"Head replaced: {count_head} match")

    # 2. Replace Header (lines ~60 to ~295) with Fixed Header without mobile drawer
    new_header = r"""  <!-- ======================================================================
       HEADER / NAVBAR FIXA COM DESIGN FLUIDO, NAVEGAÇÃO DIRETA E SEM GAVETA REDUNDANTE
       ====================================================================== -->
  <header class="glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">
    <!-- Nível 1: Barra Principal Superior -->
    <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-14 sm:h-16 gap-2 sm:gap-4">
        
        <!-- Logo e Título com Identidade Visual SUS / FEBRASGO / ACOG -->
        <a href="#" class="flex items-center gap-2 sm:gap-3 flex-shrink-0 group" title="Ir para o início">
          <div class="w-8 h-8 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-tr from-rose-600 via-red-500 to-amber-500 flex items-center justify-center text-white shadow-md shadow-rose-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i data-lucide="siren" class="w-4 h-4 sm:w-5 sm:h-5"></i>
          </div>
          <div class="flex flex-col">
            <div class="flex items-center gap-1.5 sm:gap-2">
              <span class="nav-brand-title font-extrabold tracking-tight text-slate-900 dark:text-white leading-none">Urgências Obstétricas</span>
              <span class="text-[9px] sm:text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-200 dark:border-rose-800">PCDT/SUS</span>
            </div>
            <span class="text-[10px] sm:text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">USMLE Step 2 CK • Residência Médica • FEBRASGO</span>
          </div>
        </a>

        <!-- Barra de Busca Global Inteligente (Desktop & Tablet) -->
        <div class="flex items-center flex-1 max-w-xs sm:max-w-sm lg:max-w-md mx-1 sm:mx-4">
          <div class="relative w-full">
            <i data-lucide="search" class="w-3.5 h-3.5 sm:w-4 sm:h-4 absolute left-2.5 sm:left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            <input type="text" id="global-search" placeholder="Buscar módulos, condutas, escores..." 
              class="w-full pl-8 sm:pl-9 pr-8 sm:pr-12 py-1.5 sm:py-2 text-xs rounded-xl bg-slate-100/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all">
            <kbd class="hidden lg:inline-flex items-center absolute right-2.5 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[9px] font-semibold text-slate-400 dark:text-slate-500 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded shadow-sm">Ctrl K</kbd>
          </div>
        </div>

        <!-- Ações Rápidas: Hubs de Estudo, Seletor de Tamanho de Fonte e Tema -->
        <div class="flex items-center gap-1 sm:gap-2 flex-shrink-0">
          
          <!-- Hubs de Treinamento Rápido -->
          <nav class="hidden md:flex items-center gap-1 sm:gap-1.5">
            <a href="#high-yield" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg text-xs font-bold text-amber-700 dark:text-amber-300 bg-amber-50 hover:bg-amber-100 dark:bg-amber-950/40 dark:hover:bg-amber-900/40 border border-amber-200/80 dark:border-amber-800/60 transition-colors">
              <i data-lucide="star" class="w-3 h-3 sm:w-3.5 sm:h-3.5 text-amber-500"></i>
              <span>Top 20</span>
            </a>
            <a href="#flashcards" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg text-xs font-bold text-sky-700 dark:text-sky-300 bg-sky-50 hover:bg-sky-100 dark:bg-sky-950/40 dark:hover:bg-sky-900/40 border border-sky-200/80 dark:border-sky-800/60 transition-colors">
              <i data-lucide="layers" class="w-3 h-3 sm:w-3.5 sm:h-3.5 text-sky-500"></i>
              <span>Flashcards</span>
            </a>
            <a href="#quiz" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg text-xs font-bold text-emerald-700 dark:text-emerald-300 bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/40 border border-emerald-200/80 dark:border-emerald-800/60 transition-colors">
              <i data-lucide="check-square" class="w-3 h-3 sm:w-3.5 sm:h-3.5 text-emerald-500"></i>
              <span>14 Casos</span>
            </a>
          </nav>

          <div class="h-4 sm:h-5 w-px bg-slate-200 dark:bg-slate-800 mx-0.5"></div>

          <!-- Controle de Tamanho de Fonte (Legibilidade Fluida) -->
          <div class="flex items-center bg-slate-100 dark:bg-slate-900 rounded-xl p-0.5 border border-slate-200 dark:border-slate-800" role="group" aria-label="Controle de tamanho de fonte">
            <button type="button" class="font-size-btn px-2 py-1 rounded-lg text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-rose-600 transition-colors" data-font-size-target="normal" title="Fonte Padrão (Normal)" aria-pressed="true">
              A
            </button>
            <button type="button" class="font-size-btn px-2 py-1 rounded-lg text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-rose-600 transition-colors" data-font-size-target="large" title="Fonte Grande (+15%)" aria-pressed="false">
              A+
            </button>
            <button type="button" class="font-size-btn px-2 py-1 rounded-lg text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-rose-600 transition-colors" data-font-size-target="xlarge" title="Fonte Extra Grande (+28%)" aria-pressed="false">
              A++
            </button>
          </div>

          <!-- Botão de Alternância de Tema Claro/Escuro -->
          <button id="theme-toggle" type="button" aria-label="Alternar modo claro/escuro" title="Alternar modo claro/escuro" 
            class="theme-toggle-btn p-1.5 sm:p-2 rounded-xl text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white bg-slate-100 hover:bg-slate-200 dark:bg-slate-900 hover:dark:bg-slate-800 border border-slate-200 dark:border-slate-800 transition-colors flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-rose-500">
            <i data-lucide="sun" class="w-4 h-4 icon-sun text-amber-500"></i>
            <i data-lucide="moon" class="w-4 h-4 icon-moon text-slate-700 dark:text-slate-300"></i>
          </button>

        </div>

      </div>
    </div>

    <!-- Nível 2: Faixa Subnav de Módulos & Ferramentas (Scroll Horizontal Fluido sem quebra) -->
    <div class="border-t border-slate-200/70 dark:border-slate-800/70 bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md">
      <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1.5 text-xs font-semibold whitespace-nowrap">
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-1 flex items-center gap-1 flex-shrink-0">
            <i data-lucide="siren" class="w-3 h-3 text-rose-500"></i> Módulos:
          </span>
          <a href="#modulo-29" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">29</span>
            Choque & Cesárea
          </a>
          <a href="#modulo-30" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">30</span>
            Abortamento
          </a>
          <a href="#modulo-31" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">31</span>
            Ectópica
          </a>
          <a href="#modulo-32" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">32</span>
            Mola / DTG
          </a>
          <a href="#modulo-33" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">33</span>
            DPP & Placenta Prévia
          </a>
          <a href="#modulo-34" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">34</span>
            Pré-Eclâmpsia & MgSO₄
          </a>
          <a href="#modulo-35" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">35</span>
            HELLP
          </a>
          <a href="#modulo-36" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">36</span>
            Sepse
          </a>
          <a href="#modulo-37" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">37</span>
            Prolapso de Cordão
          </a>
          <a href="#modulo-38" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">38</span>
            Distócia de Ombros
          </a>
          <a href="#modulo-39" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">39</span>
            Embolia Amniótica (ELA)
          </a>

          <!-- Separador -->
          <span class="h-4 w-px bg-slate-300 dark:bg-slate-700 mx-1 flex-shrink-0"></span>

          <!-- Ferramentas Clínicas Diretas -->
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-1 flex items-center gap-1 flex-shrink-0">
            <i data-lucide="zap" class="w-3 h-3 text-amber-500"></i> Ferramentas:
          </span>
          <a href="#calc-si" class="subnav-pill px-2.5 py-1 rounded-lg text-rose-700 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="activity" class="w-3 h-3"></i>
            Índice de Choque
          </a>
          <a href="#calc-mtx" class="subnav-pill px-2.5 py-1 rounded-lg text-emerald-700 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="check-circle" class="w-3 h-3"></i>
            MTX Ectópica
          </a>
          <a href="#calc-mg" class="subnav-pill px-2.5 py-1 rounded-lg text-indigo-700 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="shield-alert" class="w-3 h-3"></i>
            MgSO₄ & Antídoto
          </a>
          <a href="#calc-helperr" class="subnav-pill px-2.5 py-1 rounded-lg text-amber-700 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="timer" class="w-3 h-3"></i>
            HELPERR 5min
          </a>

          <!-- Atalhos em Mobile -->
          <span class="h-4 w-px bg-slate-300 dark:bg-slate-700 mx-1 flex-shrink-0 md:hidden"></span>
          <a href="#high-yield" class="subnav-pill md:hidden px-2 py-1 rounded-lg text-amber-700 dark:text-amber-300 bg-amber-50/80 dark:bg-amber-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="star" class="w-3 h-3 text-amber-500"></i>
            Top 20
          </a>
          <a href="#flashcards" class="subnav-pill md:hidden px-2 py-1 rounded-lg text-sky-700 dark:text-sky-300 bg-sky-50/80 dark:bg-sky-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="layers" class="w-3 h-3 text-sky-500"></i>
            Flashcards
          </a>
          <a href="#quiz" class="subnav-pill md:hidden px-2 py-1 rounded-lg text-emerald-700 dark:text-emerald-300 bg-emerald-50/80 dark:bg-emerald-950/40 transition-colors flex items-center gap-1">
            <i data-lucide="check-square" class="w-3 h-3 text-emerald-500"></i>
            14 Casos
          </a>
        </div>
      </div>
    </div>

    <!-- Barra de Progresso de Leitura -->
    <div id="reading-progress-bar" class="h-0.5 bg-gradient-to-r from-rose-500 via-amber-500 to-rose-600 transition-all duration-150" style="width: 0%;"></div>
  </header>"""

    # Replace header: from <header class="sticky ..."> to </header>
    old_header_pattern = r'<header class="sticky top-0 z-40 glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">.*?</header>'
    html, count_header = re.subn(old_header_pattern, new_header, html, flags=re.DOTALL)
    print(f"Header replaced: {count_header} match")

    # 3. Add Floating Action Button (FAB) before </body>
    if 'id="fab-back-to-top"' not in html:
        fab_html = r"""  <!-- Botão Flutuante Voltar ao Topo (FAB) -->
  <button id="fab-back-to-top" type="button" aria-label="Voltar ao topo da página" title="Voltar ao topo" 
    class="fab-hidden p-3 rounded-full bg-rose-600 hover:bg-rose-700 active:scale-95 text-white shadow-xl shadow-rose-600/30 border border-white/20 flex items-center justify-center transition-all cursor-pointer">
    <i data-lucide="arrow-up" class="w-5 h-5"></i>
  </button>

</body>"""
        html = html.replace('</body>', fab_html)
        print("FAB button added before </body>")

    # 4. Update the 9 clinical images to ensure fluid container and fluid img attributes
    # Dict of image configs with (width, height)
    img_configs = {
        "choque_obstetrico_cesarea_perimortem.jpg": (1376, 768),
        "abortamento_e_gravidez_ectopica.jpg": (1600, 900),
        "doenca_trofoblastica_mola_hidatiforme.jpg": (1600, 900),
        "hemorragias_segunda_metade_dpp_vs_pp.jpg": (1376, 768),
        "hemorragia_pos_parto_balao_bakri.jpg": (1376, 768),
        "preeclampsia_grave_hellp_magnesio.jpg": (1376, 768),
        "sofrimento_fetal_ctg_desaceleracoes.jpg": (1376, 768),
        "distocia_ombros_helperr_algoritmo.jpg": (1376, 768),
        "embolia_liquido_amniotico_sepse.jpg": (1600, 900)
    }

    # Ensure class="img-fluid-container" on outer container and fluid attributes on img
    for img_name, (w, h) in img_configs.items():
        # First check if img tag exists
        img_pattern = rf'<img src="assets/img/{re.escape(img_name)}"[^>]*>'
        match = re.search(img_pattern, html)
        if match:
            old_tag = match.group(0)
            # Build new img tag preserving alt, data-lightbox, data-title
            alt_match = re.search(r'alt="([^"]*)"', old_tag)
            title_match = re.search(r'data-title="([^"]*)"', old_tag)
            alt = alt_match.group(1) if alt_match else ""
            title = title_match.group(1) if title_match else ""

            new_tag = f'<img src="assets/img/{img_name}" alt="{alt}" class="fluid-img w-full h-auto object-cover zoom-cursor max-w-full" width="{w}" height="{h}" loading="lazy" style="aspect-ratio: 16/9;" data-lightbox="assets/img/{img_name}" data-title="{title}">'
            html = html.replace(old_tag, new_tag)
            print(f"Updated img tag for: {img_name}")

    # For container divs with class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white"
    # add img-fluid-container
    html = re.sub(
        r'<div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">(\s*<img src="assets/img/)',
        r'<div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white img-fluid-container">\1',
        html
    )

    # For images 4 and 5 (hemorragias_segunda_metade_dpp_vs_pp and balao_bakri), wrap them if not wrapped
    for img_special in ["hemorragias_segunda_metade_dpp_vs_pp.jpg", "hemorragia_pos_parto_balao_bakri.jpg"]:
        special_pattern = rf'(<img src="assets/img/{re.escape(img_special)}"[^>]*>)'
        # If preceding text does not have img-fluid-container
        # Check if already inside an img-fluid-container
        if f'img-fluid-container">\n          <img src="assets/img/{img_special}' not in html and f'img-fluid-container"><img src="assets/img/{img_special}' not in html:
            html = re.sub(
                special_pattern,
                r'<div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white img-fluid-container">\1</div>',
                html
            )
            print(f"Wrapped in img-fluid-container: {img_special}")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully updated {HTML_FILE}. New length: {len(html)}")

if __name__ == "__main__":
    update_html()
