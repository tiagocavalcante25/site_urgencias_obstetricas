"""
build_site.py - Gerador do Portal Interativo de Urgências e Emergências Obstétricas
Compatível com GitHub Pages • Padrão USMLE Step 2 CK / FEBRASGO / SUS / ACOG
"""

import os

BASE_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_urgencias_obstetricas"
OUTPUT_HTML = os.path.join(BASE_DIR, "index.html")

def generate_html():
    html = """<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Urgências e Emergências Obstétricas | Portal Médico Interativo</title>
  <meta name="description" content="Guia Completo e Interativo de Urgências e Emergências Obstétricas. Nível USMLE Step 2 CK / Step 3, Residência Médica, FEBRASGO, ACOG e Ministério da Saúde / SUS.">

  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro -->
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
  </script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          screens: {
            'xs': '480px'
          },
          colors: {
            sus: {
              blue: '#0284c7',
              navy: '#0f172a',
              sky: '#38bdf8',
              emerald: '#059669',
              amber: '#d97706',
              rose: '#e11d48'
            }
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Custom CSS -->
  <link rel="stylesheet" href="assets/css/custom.css">
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-screen flex flex-col antialiased transition-colors duration-200">

  <!-- ======================================================================
       HEADER / NAVBAR COM DESIGN MULTI-NÍVEL RESPONSIVO & ELEGANTE
       ====================================================================== -->
  <header class="sticky top-0 z-40 glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">
    <!-- Nível 1: Barra Principal -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 gap-3 lg:gap-4">
        
        <!-- Logo e Título com Identidade Visual SUS / FEBRASGO / ACOG -->
        <a href="#" class="flex items-center gap-3 flex-shrink-0 group" title="Ir para o início">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-rose-600 via-red-500 to-amber-500 flex items-center justify-center text-white shadow-md shadow-rose-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i data-lucide="siren" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-extrabold text-sm sm:text-base tracking-tight text-slate-900 dark:text-white">Urgências Obstétricas</span>
              <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-200 dark:border-rose-800 hidden xs:inline-block">PCDT / SUS</span>
            </div>
            <span class="text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">USMLE Step 2 CK • Residência Médica • FEBRASGO</span>
          </div>
        </a>

        <!-- Barra de Busca Global Inteligente (Desktop & Tablet) -->
        <div class="hidden md:flex items-center flex-1 max-w-sm lg:max-w-md mx-2 lg:mx-4">
          <div class="relative w-full">
            <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            <input type="text" id="global-search" placeholder="Buscar módulos, escores (ex: Choque, MTX, Zuspan, HELLP...)" 
              class="w-full pl-9 pr-14 py-2 text-xs rounded-xl bg-slate-100/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all">
            <kbd class="hidden lg:inline-flex items-center absolute right-2.5 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-semibold text-slate-400 dark:text-slate-500 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded shadow-sm">Ctrl K</kbd>
          </div>
        </div>

        <!-- Ações Rápidas de Estudo, Botão de Tema e Menu Mobile -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          
          <!-- Hubs de Treinamento Rápido -->
          <nav class="hidden lg:flex items-center gap-1.5">
            <a href="#high-yield" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-bold text-amber-700 dark:text-amber-300 bg-amber-50 hover:bg-amber-100 dark:bg-amber-950/40 dark:hover:bg-amber-900/40 border border-amber-200/80 dark:border-amber-800/60 transition-colors">
              <i data-lucide="star" class="w-3.5 h-3.5 text-amber-500"></i>
              <span>Top 20</span>
            </a>
            <a href="#flashcards" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-bold text-sky-700 dark:text-sky-300 bg-sky-50 hover:bg-sky-100 dark:bg-sky-950/40 dark:hover:bg-sky-900/40 border border-sky-200/80 dark:border-sky-800/60 transition-colors">
              <i data-lucide="layers" class="w-3.5 h-3.5 text-sky-500"></i>
              <span>Flashcards</span>
            </a>
            <a href="#quiz" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-bold text-emerald-700 dark:text-emerald-300 bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/40 border border-emerald-200/80 dark:border-emerald-800/60 transition-colors">
              <i data-lucide="check-square" class="w-3.5 h-3.5 text-emerald-500"></i>
              <span>14 Casos</span>
            </a>
          </nav>

          <div class="h-5 w-px bg-slate-200 dark:border-slate-800 hidden sm:block mx-0.5"></div>

          <!-- Botão de Alternância de Tema Claro/Escuro -->
          <button id="theme-toggle" type="button" aria-label="Alternar modo claro/escuro" title="Alternar modo claro/escuro" 
            class="theme-toggle-btn p-2 rounded-xl text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white bg-slate-100 hover:bg-slate-200 dark:bg-slate-900 hover:dark:bg-slate-800 border border-slate-200 dark:border-slate-800 transition-colors flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-rose-500">
            <i data-lucide="sun" class="w-4 h-4 icon-sun text-amber-500"></i>
            <i data-lucide="moon" class="w-4 h-4 icon-moon text-slate-700 dark:text-slate-300"></i>
          </button>

          <!-- Botão Hambúrguer Mobile / Gaveta -->
          <button id="mobile-menu-toggle" type="button" aria-label="Abrir menu de navegação" aria-expanded="false" 
            class="lg:hidden p-2 rounded-xl text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white bg-slate-100 hover:bg-slate-200 dark:bg-slate-900 hover:dark:bg-slate-800 border border-slate-200 dark:border-slate-800 transition-colors flex items-center justify-center">
            <i data-lucide="menu" id="mobile-menu-icon" class="w-5 h-5"></i>
          </button>

        </div>

      </div>
    </div>

    <!-- Nível 2: Faixa Subnav de Módulos & Ferramentas (Scroll Horizontal Suave) -->
    <div class="border-t border-slate-200/70 dark:border-slate-800/70 bg-slate-50/70 dark:bg-slate-950/70 backdrop-blur-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-2 text-xs font-semibold whitespace-nowrap">
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
        </div>
      </div>
    </div>

    <!-- Nível 3: Gaveta Mobile Inteligente -->
    <div id="mobile-menu-drawer" class="hidden lg:hidden border-t border-slate-200 dark:border-slate-800 bg-white/95 dark:bg-slate-950/95 backdrop-blur-xl px-4 py-4 space-y-4 max-h-[80vh] overflow-y-auto">
      
      <!-- Busca Mobile -->
      <div class="relative w-full">
        <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
        <input type="text" id="mobile-search" placeholder="Buscar módulos, temas ou condutas..." 
          class="w-full pl-9 pr-4 py-2.5 text-xs rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200 placeholder-slate-400">
      </div>

      <!-- Links Rápidos de Estudo no Mobile -->
      <div class="grid grid-cols-3 gap-2 pt-1">
        <a href="#high-yield" class="flex flex-col items-center justify-center p-2.5 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200/80 dark:border-amber-800/60 text-amber-800 dark:text-amber-300 text-xs font-bold gap-1 text-center">
          <i data-lucide="star" class="w-4 h-4 text-amber-500"></i>
          <span>Top 20</span>
        </a>
        <a href="#flashcards" class="flex flex-col items-center justify-center p-2.5 rounded-xl bg-sky-50 dark:bg-sky-950/40 border border-sky-200/80 dark:border-sky-800/60 text-sky-800 dark:text-sky-300 text-xs font-bold gap-1 text-center">
          <i data-lucide="layers" class="w-4 h-4 text-sky-500"></i>
          <span>Flashcards</span>
        </a>
        <a href="#quiz" class="flex flex-col items-center justify-center p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200/80 dark:border-emerald-800/60 text-emerald-800 dark:text-emerald-300 text-xs font-bold gap-1 text-center">
          <i data-lucide="check-square" class="w-4 h-4 text-emerald-500"></i>
          <span>14 Casos</span>
        </a>
      </div>

      <!-- Lista Completa de Módulos Clínicos -->
      <div class="space-y-1 pt-2">
        <div class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 px-2 mb-1">Módulos de Urgência & Emergência:</div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-1 text-xs">
          <a href="#modulo-29" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">29</span>
            Choque & Cesárea Perimortem (4 min)
          </a>
          <a href="#modulo-30" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">30</span>
            Abortamento & Formas Clínicas
          </a>
          <a href="#modulo-31" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">31</span>
            Gravidez Ectópica & MTX
          </a>
          <a href="#modulo-32" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">32</span>
            Doença Trofoblástica (DTG / NTG)
          </a>
          <a href="#modulo-33" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">33</span>
            Hemorragias da 2ª Metade & PAS
          </a>
          <a href="#modulo-34" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">34</span>
            Pré-Eclâmpsia Grave & MgSO₄
          </a>
          <a href="#modulo-35" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">35</span>
            Síndrome HELLP & Swansea
          </a>
          <a href="#modulo-36" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">36</span>
            Sepse Materna & Bundle da 1ª Hora
          </a>
          <a href="#modulo-37" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">37</span>
            Prolapso de Cordão Umbilical
          </a>
          <a href="#modulo-38" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">38</span>
            Distócia de Ombros & HELPERR
          </a>
          <a href="#modulo-39" class="flex items-center gap-2.5 p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium">
            <span class="w-5 h-5 rounded-md bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">39</span>
            Embolia por Líquido Amniótico (ELA)
          </a>
        </div>
      </div>

      <!-- Alternador de Tema no Mobile -->
      <div class="pt-2 border-t border-slate-200 dark:border-slate-800">
        <button id="mobile-theme-toggle" type="button" 
          class="theme-toggle-btn w-full p-2.5 rounded-xl bg-slate-100 dark:bg-slate-900 hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 text-xs font-bold flex items-center justify-center gap-2 transition-colors">
          <i data-lucide="sun" class="w-4 h-4 icon-sun text-amber-500"></i>
          <i data-lucide="moon" class="w-4 h-4 icon-moon text-slate-700 dark:text-slate-300"></i>
          <span>Alternar Modo Claro / Escuro</span>
        </button>
      </div>

    </div>
  </header>

  <!-- ======================================================================
       HERO / DASHBOARD DE EMERGÊNCIA
       ====================================================================== -->
  <section class="relative overflow-hidden bg-gradient-to-b from-rose-50 via-slate-50 to-white dark:from-slate-950 dark:via-slate-900 dark:to-slate-950 pt-10 pb-14 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Top Badges -->
      <div class="flex flex-wrap items-center gap-2 mb-4">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-rose-100 text-rose-900 dark:bg-rose-950/80 dark:text-rose-300 border border-rose-300 dark:border-rose-800">
          <i data-lucide="alert-triangle" class="w-3.5 h-3.5 text-rose-600 dark:text-rose-400"></i>
          Código Vermelho • Urgências & Emergências Obstétricas
        </span>
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-900 dark:bg-amber-950/80 dark:text-amber-300 border border-amber-300 dark:border-amber-800">
          <i data-lucide="award" class="w-3.5 h-3.5 text-amber-600 dark:text-amber-400"></i>
          FEBRASGO • ACOG • USMLE Step 2 CK & 3
        </span>
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-900 dark:bg-emerald-950/80 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800">
          <i data-lucide="github" class="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400"></i>
          GitHub Pages Ready • 100% Interativo
        </span>
      </div>

      <!-- Main Heading -->
      <div class="max-w-4xl">
        <h1 class="text-3xl sm:text-5xl font-black tracking-tight text-slate-900 dark:text-white leading-tight">
          Guia Definitivo de <span class="bg-gradient-to-r from-rose-600 via-red-600 to-amber-600 bg-clip-text text-transparent">Urgências & Emergências Obstétricas</span>
        </h1>
        <p class="text-base sm:text-lg text-slate-600 dark:text-slate-300 mt-4 leading-relaxed font-normal">
          Abordagem completa do suporte avançado à vida em obstetrícia (ALSO / ACLS materno). Da ressuscitação volêmica à cesárea perimortem em 4 minutos, diagnóstico diferencial dos sangramentos da 1ª e 2ª metades, pré-eclâmpsia grave, Síndrome HELLP, distócia de ombros, prolapso de cordão e embolia amniótica.
        </p>
      </div>

      <!-- Dashboard Quick Metrics -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4 mt-8">
        <div class="p-4 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-rose-600 dark:text-rose-400">11 Módulos</div>
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mt-0.5">M29 ao M39 Completos</div>
        </div>
        <div class="p-4 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-amber-600 dark:text-amber-400">9 Infográficos</div>
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mt-0.5">Ultra-HD com Zoom</div>
        </div>
        <div class="p-4 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-emerald-600 dark:text-emerald-400">6 Calculadoras</div>
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mt-0.5">Choque, MTX, MgSO₄...</div>
        </div>
        <div class="p-4 rounded-2xl glass-panel border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-2xl sm:text-3xl font-black text-indigo-600 dark:text-indigo-400">14 Casos</div>
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mt-0.5">Vinhetas Comentadas</div>
        </div>
      </div>

    </div>
  </section>

  <!-- ======================================================================
       MAIN CONTENT CONTAINER
       ====================================================================== -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-16 flex-1">

    <div id="search-no-results" class="hidden p-8 text-center glass-panel rounded-2xl">
      <i data-lucide="search-x" class="w-10 h-10 text-slate-400 mx-auto mb-2"></i>
      <h3 class="text-base font-bold text-slate-800 dark:text-slate-200">Nenhum módulo encontrado para a busca</h3>
      <p class="text-xs text-slate-500 mt-1">Tente buscar por termos como "Choque", "Ectópica", "Zuspan", "HELLP", "Cordão" ou "ELA".</p>
    </div>

    <!-- ====================================================================
         MÓDULO 29: ABORDAGEM INICIAL DA EMERGÊNCIA OBSTÉTRICA
         ==================================================================== -->
    <section id="modulo-29" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="siren" class="w-4 h-4"></i> Módulo 29
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Abordagem Inicial da Emergência Obstétrica
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          A regra de ouro (salvar o barco para salvar o passageiro), alterações fisiológicas críticas, ABCDE obstétrico, escore MEOWS, índice de choque, transfusão maciça 1:1:1 e cesárea perimortem em 4 minutos.
        </p>
      </div>

      <!-- Analogia & Regra de Ouro -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="p-4 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800 space-y-2">
          <span class="px-2 py-0.5 font-bold rounded bg-amber-200 text-amber-900 dark:bg-amber-900 dark:text-amber-200 text-[10px]">🎈 Analogia Didática</span>
          <h4 class="font-bold text-amber-900 dark:text-amber-300 text-sm">O Barco e o Passageiro</h4>
          <p class="text-slate-700 dark:text-slate-300 leading-relaxed">
            A gestante é um <strong>barco com um passageiro</strong> (o feto). Se o barco afundar, o passageiro afunda junto. Logo, <strong>primeiro salvamos o barco (a mãe)</strong>, e com isso salvamos o feto. O bebê só é retirado prioritariamente quando tirá-lo <em>ajuda a salvar o barco</em> — como na histerotomia perimortem que alivia o esmagamento da veia cava inferior!
          </p>
        </div>
        <div class="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800 space-y-2">
          <span class="px-2 py-0.5 font-bold rounded bg-rose-200 text-rose-900 dark:bg-rose-900 dark:text-rose-200 text-[10px]">🩺 Princípio Clínico</span>
          <h4 class="font-bold text-rose-900 dark:text-rose-300 text-sm">Ressuscitação Materna = Fetal</h4>
          <p class="text-slate-700 dark:text-slate-300 leading-relaxed">
            Uma desaceleração ou bradicardia na cardiotocografia frequentemente é a <strong>primeira manifestação de que a mãe está entrando em choque hipovolêmico compensado</strong>, pois a circulação uteroplacentária não possui autorregulação e é a primeira sacrificada para preservar coração e cérebro maternos.
          </p>
        </div>
      </div>

      <!-- Tabela: Fisiologia que Altera a Emergência -->
      <div class="p-5 rounded-2xl glass-panel space-y-3">
        <h3 class="font-bold text-base text-slate-900 dark:text-white flex items-center gap-2">
          <i data-lucide="activity" class="w-4 h-4 text-rose-600"></i> Fisiologia da Gravidez que Mascara e Altera a Emergência
        </h3>
        <div class="overflow-x-auto text-xs">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-slate-200 dark:border-slate-800 text-slate-500 font-bold">
                <th class="py-2.5 px-3">Alteração Fisiológica Normal</th>
                <th class="py-2.5 px-3">Impacto Clínico na Emergência</th>
                <th class="py-2.5 px-3">Conduta Obrigatória</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800/60 text-slate-700 dark:text-slate-300">
              <tr>
                <td class="py-2.5 px-3 font-semibold text-rose-600 dark:text-rose-400">Volume plasmático ↑ 40–50%</td>
                <td class="py-2.5 px-3">Perde até <strong>1.500 mL antes de apresentar hipotensão</strong> (a PA mente!)</td>
                <td class="py-2.5 px-3">Monitorar Índice de Choque (FC/PAS); não confiar em PA isolada.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-semibold text-rose-600 dark:text-rose-400">Compressão Aortocava (>= 20 sem)</td>
                <td class="py-2.5 px-3">Útero esmaga veia cava inferior em decúbito dorsal -> Débito cardíaco ↓ até 30%</td>
                <td class="py-2.5 px-3"><strong>Deslocamento Uterino para a Esquerda (DUE) 15–30°</strong> em toda manobra.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-semibold text-rose-600 dark:text-rose-400">Estado Pró-coagulante Fisiológico</td>
                <td class="py-2.5 px-3">Fibrinogênio normal na gravidez é 400–600 mg/dL</td>
                <td class="py-2.5 px-3"><strong>Fibrinogênio &lt; 200 mg/dL é sinal gravíssimo</strong> de CIVD e hemorragia maciça.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-semibold text-rose-600 dark:text-rose-400">Capacidade Residual Funcional ↓</td>
                <td class="py-2.5 px-3">Dessatura muito rápido em apneia durante sequência rápida de intubação</td>
                <td class="py-2.5 px-3">Pré-oxigenação com O₂ a 100% por 3–5 min; via aérea com tubo 0,5 a 1 mm menor.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- INFOGRÁFICO 1: Choque Obstétrico & Cesárea Perimortem -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Choque Hemorrágico, Índice de Choque e Cesárea Perimortem (4 Minutos)</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/choque_obstetrico_cesarea_perimortem.jpg" data-title="Choque Hemorrágico, Compressão Aortocava e Cesárea Perimortem">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/choque_obstetrico_cesarea_perimortem.jpg" alt="Choque Hemorrágico Obstétrico e Cesárea Perimortem" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/choque_obstetrico_cesarea_perimortem.jpg" data-title="Choque Hemorrágico, Compressão Aortocava e Cesárea Perimortem">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Anatomia da compressão aortocava e alívio com ângulo de 15–30°; fluxograma de triagem do Índice de Choque (FC/PAS); linha do tempo da Histerotomia Ressuscitativa em 4 minutos com RCP em andamento. Padrão SUS e FEBRASGO.
        </p>
      </div>

      <!-- FERRAMENTA INTERATIVA: Calculadora do Índice de Choque -->
      <div id="calc-si" class="p-6 rounded-2xl glass-panel border-2 border-rose-500/40 shadow-lg shadow-rose-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Ferramenta Clínica de Triagem Rápida</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Calculadora do Índice de Choque Obstétrico (IC = FC ÷ PAS)</h3>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-500">Índice Calculado:</span>
            <span id="si-score" class="text-2xl font-black text-rose-600 dark:text-rose-400">0.00</span>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Frequência Cardíaca Materna (FC - bpm):</label>
            <input type="number" id="si-hr" value="120" min="40" max="220" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Ex: 110, 125, 140 bpm</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Pressão Arterial Sistólica (PAS - mmHg):</label>
            <input type="number" id="si-sbp" value="100" min="40" max="260" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Ex: 100, 90, 80 mmHg</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-500 uppercase">Status Hemodinâmico:</span>
            <span id="si-status" class="px-3 py-1 text-xs font-bold rounded-full bg-slate-200 text-slate-800">Calculando...</span>
          </div>
          <div id="si-action" class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
            Carregando análise...
          </div>
          <div id="si-warning" class="hidden p-3 rounded-lg bg-rose-50 dark:bg-rose-950/40 border border-rose-300 dark:border-rose-800 text-xs text-rose-800 dark:text-rose-200 font-bold">
            <!-- Renderizado dinamicamente -->
          </div>
        </div>
      </div>

      <!-- Protocolo de Transfusão Maciça & BEAU-CHOPS -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="p-5 rounded-2xl glass-panel space-y-3">
          <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
            <i data-lucide="droplet" class="w-4 h-4 text-rose-600"></i> Protocolo de Transfusão Maciça (PTM 1:1:1)
          </h4>
          <p class="text-slate-700 dark:text-slate-300 leading-relaxed">
            • <strong>Razão 1:1:1:</strong> 1 Concentrado de Hemácias : 1 Plasma Fresco Congelado : 1 Unidade de Plaquetas.<br>
            • <strong>Ácido Tranexâmico:</strong> 1 g IV em 10 min até 3h do sangramento (Estudo WOMAN); repetir 1 g após 30 min se sangramento contínuo.<br>
            • <strong>Fibrinogênio:</strong> Se &lt; 200 mg/dL, prescrever 10 U de Crioprecipitado ou 2 g de concentrado de fibrinogênio.<br>
            • <strong>Tríade Letal:</strong> Prevenir e tratar hipotermia, acidose e hipocalcemia (citrato consome cálcio -> Gluconato de Cálcio).
          </p>
        </div>
        <div class="p-5 rounded-2xl glass-panel space-y-3">
          <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
            <i data-lucide="heart-pulse" class="w-4 h-4 text-rose-600"></i> Parada Cardíaca & Mnemônico BEAU-CHOPS
          </h4>
          <p class="text-slate-700 dark:text-slate-300 leading-relaxed">
            • <strong>B:</strong> Bleeding / DIC (Hemorragia maciça e coagulopatia)<br>
            • <strong>E:</strong> Embolism (Embolia amniótica, pulmonar ou gasosa)<br>
            • <strong>A:</strong> Anesthetic complications (Raquidiana alta, toxicidade)<br>
            • <strong>U:</strong> Uterine atony (Atonia pós-parto)<br>
            • <strong>C:</strong> Cardiac disease (Miocardiopatia periparto, dissecção)<br>
            • <strong>H:</strong> Hypertension / Preeclampsia / Eclampsia<br>
            • <strong>O:</strong> Other (5 H's e 5 T's do ACLS)<br>
            • <strong>P:</strong> Placenta (DPP ou Placenta prévia/acretismo)<br>
            • <strong>S:</strong> Sepsis (Choque séptico)
          </p>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 30: ABORTAMENTO
         ==================================================================== -->
    <section id="modulo-30" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="heart-crack" class="w-4 h-4"></i> Módulo 30
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Abortamento: Diagnóstico Diferencial & Manejo Clínico-Cirúrgico
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Definições internacionais (OMS vs ACOG), etiologia genética e anatômica, comparação das formas clínicas pelo orifício interno do colo, técnicas de esvaziamento (AMIU vs Curetagem) e incompetência istmocervical.
        </p>
      </div>

      <!-- Tabela Comparativa das Formas de Aborto -->
      <div class="p-5 rounded-2xl glass-panel space-y-3">
        <h3 class="font-bold text-base text-slate-900 dark:text-white">
          Classificação Clínica do Abortamento
        </h3>
        <div class="overflow-x-auto text-xs">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-slate-200 dark:border-slate-800 text-slate-500 font-bold">
                <th class="py-2.5 px-3">Forma Clínica</th>
                <th class="py-2.5 px-3">Orifício Cervical Interno</th>
                <th class="py-2.5 px-3">Vitalidade Fetal / USG</th>
                <th class="py-2.5 px-3">Conduta Recomendada</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800/60 text-slate-700 dark:text-slate-300">
              <tr>
                <td class="py-2.5 px-3 font-bold text-sky-600">Ameaça</td>
                <td class="py-2.5 px-3 font-semibold text-emerald-600">FECHADO</td>
                <td class="py-2.5 px-3">Embrião vivo com BCF presente</td>
                <td class="py-2.5 px-3">Repouso relativo, sintomáticos. Não usar progesterona se colo normal.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-bold text-amber-600">Inevitável</td>
                <td class="py-2.5 px-3 font-semibold text-rose-600">ABERTO</td>
                <td class="py-2.5 px-3">Membranas visíveis/rotas, cólicas intensas</td>
                <td class="py-2.5 px-3">Esvaziamento uterino (AMIU se &le; 12 sem; Curetagem se &gt; 12 sem) ou Misoprostol.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-bold text-rose-600">Incompleto</td>
                <td class="py-2.5 px-3 font-semibold text-rose-600">ABERTO</td>
                <td class="py-2.5 px-3">Eliminação parcial; eco endometrial &gt; 15 mm</td>
                <td class="py-2.5 px-3">AMIU ou Curetagem aspirativa. Se instável: ocitocina IV + AMIU imediato.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-bold text-emerald-600">Completo</td>
                <td class="py-2.5 px-3 font-semibold text-emerald-600">FECHADO</td>
                <td class="py-2.5 px-3">Eliminação total; eco endometrial &lt; 15 mm</td>
                <td class="py-2.5 px-3">Expectante. Confirmar beta-hCG em queda se houver dúvida com ectópica.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-bold text-indigo-600">Retido</td>
                <td class="py-2.5 px-3 font-semibold text-emerald-600">FECHADO</td>
                <td class="py-2.5 px-3">CCN &ge; 7 mm sem BCF ou saco &ge; 25 mm vazio</td>
                <td class="py-2.5 px-3">Misoprostol 800 mcg vaginal ou AMIU/Curetagem programada.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-bold text-red-600">Séptico</td>
                <td class="py-2.5 px-3 font-semibold">ABERTO / FECHADO</td>
                <td class="py-2.5 px-3">Febre, dor à palpação, secreção fétida</td>
                <td class="py-2.5 px-3"><strong>Clindamicina + Gentamicina IV + AMIU imediato</strong> pós-início do antibiótico.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Incompetência Istmocervical -->
      <div class="p-5 rounded-2xl glass-panel space-y-3">
        <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
          <i data-lucide="unlock" class="w-4 h-4 text-amber-600"></i> Incompetência Istmocervical (IIC) & Circlagem Cervical
        </h4>
        <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
          • <strong>Quadro Clínico Clássico:</strong> Perdas gestacionais repetidas de segundo trimestre (16–22 semanas), caracterizadas por dilatação cervical <strong>indolor</strong>, protrusão de membranas em bolsa e expulsão fetal rápida sem contrações prévias dolorosas.<br>
          • <strong>Circlagem Cervical (Técnica de McDonald ou Shirodkar):</strong> Realizada eletivamente entre <strong>12 e 14 semanas</strong> após ultrassom morfológico de 1º trimestre afastar anomalias cromossômicas.<br>
          • <strong>Fio Inabsorvível (Mercilene / prolene):</strong> Retirado ambulatorialmente com <strong>36 a 37 semanas</strong> para permitir parto vaginal espontâneo, ou imediatamente se entrar em trabalho de parto ativo prematuro para evitar laceração cervical!
        </p>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 31: GRAVIDEZ ECTÓPICA
         ==================================================================== -->
    <section id="modulo-31" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="git-commit" class="w-4 h-4"></i> Módulo 31
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Gravidez Ectópica: Localização, Zona Discriminatória e Decisão Terapêutica
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Topografia anatômica da trompa, zona discriminatória do beta-hCG (1.500–3.500 mUI/mL), critérios de inclusão do Metotrexato (MTX) e indicações cirúrgicas de emergência (Salpingectomia vs Salpingostomia).
        </p>
      </div>

      <!-- INFOGRÁFICO 2: Abortamento & Ectópica -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Espectro do Abortamento, Topografia da Gravidez Ectópica & Algoritmo de MTX</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/abortamento_e_gravidez_ectopica.jpg" data-title="Abortamento e Gravidez Ectópica">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/abortamento_e_gravidez_ectopica.jpg" alt="Abortamento e Gravidez Ectópica" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/abortamento_e_gravidez_ectopica.jpg" data-title="Abortamento e Gravidez Ectópica">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Comparação das 6 formas de abortamento; localizações anatômicas da ectópica (ampola 80%, ístmo 12%, cornual 2%); zona discriminatória e critérios rigorosos para Metotrexato 50 mg/m² com curva D4/D7.
        </p>
      </div>

      <!-- FERRAMENTA INTERATIVA: Calculadora de Elegibilidade ao MTX -->
      <div id="calc-mtx" class="p-6 rounded-2xl glass-panel border-2 border-emerald-500/40 shadow-lg shadow-emerald-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300">Algoritmo Decisório Farmacológico</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Calculadora de Elegibilidade ao Metotrexato (MTX na Ectópica)</h3>
          </div>
          <span class="text-xs text-slate-500">Diretrizes ACOG & FEBRASGO</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">beta-hCG Sérico Inicial (mUI/mL):</label>
            <input type="number" id="mtx-hcg" value="2800" min="0" max="100000" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Ponto de corte ideal: &lt; 5.000 mUI/mL</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Maior Diâmetro da Massa Anexial (cm):</label>
            <input type="number" id="mtx-size" value="2.5" step="0.1" min="0" max="15" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Ponto de corte estrito: &lt; 3,5 cm</span>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <label class="flex items-center gap-2 p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 cursor-pointer">
            <input type="checkbox" id="mtx-stable" checked class="w-4 h-4 rounded text-emerald-600 focus:ring-emerald-500">
            <span class="font-bold text-slate-800 dark:text-slate-200">Paciente Estável Hemodinamicamente?</span>
          </label>
          <label class="flex items-center gap-2 p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 cursor-pointer">
            <input type="checkbox" id="mtx-fhr" class="w-4 h-4 rounded text-rose-600 focus:ring-rose-500">
            <span class="font-bold text-slate-800 dark:text-slate-200">Batimento Cardíaco Embrionário (BCF)?</span>
          </label>
          <label class="flex items-center gap-2 p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 cursor-pointer">
            <input type="checkbox" id="mtx-fluid" class="w-4 h-4 rounded text-rose-600 focus:ring-rose-500">
            <span class="font-bold text-slate-800 dark:text-slate-200">Líquido Livre Moderado a Grave?</span>
          </label>
        </div>

        <div id="mtx-result" class="p-4 rounded-xl border-2 transition-all">
          <!-- Renderizado dinamicamente pelo app.js -->
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 32: DOENÇA TROFOBLÁSTICA GESTACIONAL (DTG)
         ==================================================================== -->
    <section id="modulo-32" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="dna" class="w-4 h-4"></i> Módulo 32
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Doença Trofoblástica Gestacional: Mola Hidatiforme & Neoplasia (NTG)
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Genética comparada (Mola Completa 46,XX vs Mola Parcial 69,XXY), aspiração uterina por vácuo, curva de regressão de beta-hCG, critérios FIGO de malignização e quimioterapia.
        </p>
      </div>

      <!-- INFOGRÁFICO 3: DTG & Mola -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Mola Hidatiforme Completa vs Parcial, Seguimento e Diagnóstico de NTG</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/doenca_trofoblastica_mola_hidatiforme.jpg" data-title="Doença Trofoblástica Gestacional">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/doenca_trofoblastica_mola_hidatiforme.jpg" alt="Doença Trofoblástica Gestacional" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/doenca_trofoblastica_mola_hidatiforme.jpg" data-title="Doença Trofoblástica Gestacional">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Patologia macroscópica em cachos de uva; cariótipo paternógeno vs triploide; cronograma semanal e mensal de dosagem do beta-hCG e estadiamento FIGO/OMS com quimioterapia EMA-CO.
        </p>
      </div>

      <!-- Critérios FIGO de Malignização -->
      <div class="p-5 rounded-2xl glass-panel space-y-3">
        <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
          <i data-lucide="alert-circle" class="w-4 h-4 text-rose-600"></i> Critérios FIGO para Diagnóstico de Neoplasia Trofoblástica (NTG)
        </h4>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs text-slate-700 dark:text-slate-300">
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <strong class="text-slate-900 dark:text-slate-100 block mb-1">1. Platô de beta-hCG</strong>
            Estabilidade dos valores (variação &plusmn; 10%) em 4 dosagens semanais consecutivas ao longo de 3 semanas (Dias 1, 7, 14 e 21).
          </div>
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <strong class="text-slate-900 dark:text-slate-100 block mb-1">2. Elevação de beta-hCG</strong>
            Subida &ge; 10% em 3 dosagens semanais consecutivas ao longo de 2 semanas (Dias 1, 7 e 14).
          </div>
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <strong class="text-slate-900 dark:text-slate-100 block mb-1">3. Persistência ou Histologia</strong>
            beta-hCG detectável após 6 meses pós-esvaziamento OU diagnóstico anatomopatológico de Coriocarcinoma.
          </div>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 33: HEMORRAGIAS DA SEGUNDA METADE DA GESTAÇÃO
         ==================================================================== -->
    <section id="modulo-33" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="droplets" class="w-4 h-4"></i> Módulo 33
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Hemorragias da Segunda Metade da Gestação & Espectro PAS
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Diagnóstico diferencial das 5 grandes causas: DPP, Placenta Prévia, Rotura Uterina, Vasa Prévia e Rotura de Seio Marginal. Espectro do Acretismo Placentário (Acreta, Increta, Percreta) e tamponamento com Balão de Bakri.
        </p>
      </div>

      <!-- Grid 2 Infográficos: DPP vs Prévia e Balão de Bakri -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <!-- Infográfico DPP vs PP -->
        <div class="p-5 rounded-2xl glass-panel space-y-3 border border-rose-500/20">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">DPP vs Placenta Prévia</h4>
            <button type="button" class="text-xs font-bold text-rose-600 hover:underline flex items-center gap-1" data-lightbox="assets/img/hemorragias_segunda_metade_dpp_vs_pp.jpg" data-title="Descolamento Prematuro de Placenta vs Placenta Prévia">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Zoom
            </button>
          </div>
          <img src="assets/img/hemorragias_segunda_metade_dpp_vs_pp.jpg" alt="DPP vs Placenta Prévia" class="w-full h-auto rounded-xl object-cover zoom-cursor" data-lightbox="assets/img/hemorragias_segunda_metade_dpp_vs_pp.jpg" data-title="Descolamento Prematuro de Placenta vs Placenta Prévia">
          <p class="text-[11px] text-slate-500">Comparativo visual de sangue escuro com hipertonia (DPP) vs vermelho vivo indolor (PP) e profundidade de acretismo (PAS).</p>
        </div>

        <!-- Infográfico Balão de Bakri -->
        <div class="p-5 rounded-2xl glass-panel space-y-3 border border-rose-500/20">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-sm text-slate-900 dark:text-white">Balão de Bakri & Tamponamento</h4>
            <button type="button" class="text-xs font-bold text-rose-600 hover:underline flex items-center gap-1" data-lightbox="assets/img/hemorragia_pos_parto_balao_bakri.jpg" data-title="Manejo da Hemorragia com Balão de Bakri">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Zoom
            </button>
          </div>
          <img src="assets/img/hemorragia_pos_parto_balao_bakri.jpg" alt="Balão de Bakri" class="w-full h-auto rounded-xl object-cover zoom-cursor" data-lightbox="assets/img/hemorragia_pos_parto_balao_bakri.jpg" data-title="Manejo da Hemorragia com Balão de Bakri">
          <p class="text-[11px] text-slate-500">Manejo cirúrgico e conservador da hemorragia pós-parto atônica com insuflação de 300 a 500 mL de SF 0,9% estéril.</p>
        </div>

      </div>

      <!-- Tabela Comparativa das 5 Hemorragias -->
      <div class="p-5 rounded-2xl glass-panel space-y-3">
        <h3 class="font-bold text-base text-slate-900 dark:text-white">
          Diagnóstico Diferencial das 5 Hemorragias da 2ª Metade
        </h3>
        <div class="overflow-x-auto text-xs">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-slate-200 dark:border-slate-800 text-slate-500 font-bold">
                <th class="py-2 px-2.5">Etiologia</th>
                <th class="py-2 px-2.5">Tipo de Sangue</th>
                <th class="py-2 px-2.5">Dor Abdominal</th>
                <th class="py-2 px-2.5">Tônus Uterino</th>
                <th class="py-2 px-2.5">Vitalidade Fetal</th>
                <th class="py-2 px-2.5">Conduta Chave</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800/60 text-slate-700 dark:text-slate-300">
              <tr>
                <td class="py-2.5 px-2.5 font-bold text-rose-600">DPP</td>
                <td class="py-2.5 px-2.5">Escuro com coágulos</td>
                <td class="py-2.5 px-2.5 font-bold text-rose-600">INTENSA</td>
                <td class="py-2.5 px-2.5 font-bold text-rose-600">HIPERTONIA (útero em tábua)</td>
                <td class="py-2.5 px-2.5 font-bold text-rose-600">Sofrimento precoce</td>
                <td class="py-2.5 px-2.5">Estabilizar + Cesárea de emergência (se feto vivo). Não retardar!</td>
              </tr>
              <tr>
                <td class="py-2.5 px-2.5 font-bold text-amber-600">Placenta Prévia</td>
                <td class="py-2.5 px-2.5">Vermelho vivo brilhante</td>
                <td class="py-2.5 px-2.5 font-semibold text-emerald-600">INDOLOR</td>
                <td class="py-2.5 px-2.5 font-semibold text-emerald-600">Relaxado / Normal</td>
                <td class="py-2.5 px-2.5">Normal inicialmente</td>
                <td class="py-2.5 px-2.5">NÃO FAZER TOQUE VAGINAL! USTV + programar parto com 36–37 sem.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-2.5 font-bold text-red-700">Rotura Uterina</td>
                <td class="py-2.5 px-2.5">Variável (pode ser oculto)</td>
                <td class="py-2.5 px-2.5">Lancinante súbita</td>
                <td class="py-2.5 px-2.5">Perda de tônus / partes palpáveis</td>
                <td class="py-2.5 px-2.5">Morte / Bradicardia grave</td>
                <td class="py-2.5 px-2.5">Laparotomia imediata + Histerorrafia ou Histerectomia.</td>
              </tr>
              <tr>
                <td class="py-2.5 px-2.5 font-bold text-purple-600">Vasa Prévia</td>
                <td class="py-2.5 px-2.5">Vermelho vivo na rotura</td>
                <td class="py-2.5 px-2.5">Indolor</td>
                <td class="py-2.5 px-2.5">Normal</td>
                <td class="py-2.5 px-2.5 font-bold text-rose-600">Bradicardia/Morte fetal imediata</td>
                <td class="py-2.5 px-2.5">Cesariana ultra-emergente! O sangue que sai é do próprio feto!</td>
              </tr>
              <tr>
                <td class="py-2.5 px-2.5 font-bold text-slate-600">Rotura de Seio Marginal</td>
                <td class="py-2.5 px-2.5">Discreto vermelho vivo</td>
                <td class="py-2.5 px-2.5">Indolor</td>
                <td class="py-2.5 px-2.5">Normal</td>
                <td class="py-2.5 px-2.5">Normal / Excelente</td>
                <td class="py-2.5 px-2.5">Diagnóstico de exclusão; conduta expectante sob vigilância.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 34: PRÉ-ECLÂMPSIA GRAVE E ECLÂMPSIA
         ==================================================================== -->
    <section id="modulo-34" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="zap" class="w-4 h-4"></i> Módulo 34
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Pré-Eclâmpsia com Sinais de Gravidade, Eclâmpsia & Esquemas de MgSO₄
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Definições de gravidade (PA &ge; 160/110, plaquetopenia, disfunção orgânica), esquemas de Sulfato de Magnésio (Zuspan vs Pritchard), vigilância de intoxicação (antídoto Gluconato de Cálcio 10%) e anti-hipertensivos rápidos.
        </p>
      </div>

      <!-- INFOGRÁFICO 4: Pré-Eclâmpsia & HELLP -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Fisiopatologia da Pré-Eclâmpsia, Infusão de Sulfato de Magnésio e Síndrome HELLP</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/preeclampsia_grave_hellp_magnesio.jpg" data-title="Pré-Eclâmpsia Grave e Síndrome HELLP">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/preeclampsia_grave_hellp_magnesio.jpg" alt="Pré-Eclâmpsia Grave e Síndrome HELLP" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/preeclampsia_grave_hellp_magnesio.jpg" data-title="Pré-Eclâmpsia Grave e Síndrome HELLP">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Disfunção endotelial multissistêmica; protocolos comparados de Zuspan e Pritchard; tríade de intoxicação magnésica e diagnóstico de HELLP com esquizócitos.
        </p>
      </div>

      <!-- FERRAMENTA INTERATIVA: Calculadora de Sulfato de Magnésio -->
      <div id="calc-mg" class="p-6 rounded-2xl glass-panel border-2 border-indigo-500/40 shadow-lg shadow-indigo-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-indigo-100 text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300">Protocolo Anticonvulsivante de Referência</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Calculadora de Esquemas de MgSO₄ & Manejo de Intoxicação</h3>
          </div>
          <span class="text-xs text-slate-500">Padrão Zuspan / Pritchard</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Selecione o Protocolo Clínico de MgSO₄:</label>
            <select id="mg-protocol" class="w-full p-2.5 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 font-bold">
              <option value="zuspan">Esquema Zuspan (4g IV ataque + 1g/h contínuo) - Padrão Ouro</option>
              <option value="pritchard">Esquema Pritchard (4g IV + 10g IM ataque + 5g IM 4/4h) - Transporte</option>
              <option value="sibai">Esquema Sibai (6g IV ataque + 2g/h contínuo) - Protocolo SMFM</option>
            </select>
          </div>
          <div>
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Sinal Clínico / Alerta do Exame Físico:</label>
            <select id="mg-tox-select" class="w-full p-2.5 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 font-bold">
              <option value="none">Paciente estável: Reflexos normais, FR > 16, Diurese > 25 mL/h</option>
              <option value="hyporeflexia">Reflexo patelar abolido ou hiporreflexia (Alerta Precoce)</option>
              <option value="apnea">Bradipneia severa (&lt; 12 irpm) / Parada Respiratória (Emergência Crítica!)</option>
            </select>
          </div>
        </div>

        <div id="mg-dose-plan">
          <!-- Renderizado dinamicamente -->
        </div>

        <div id="mg-antidote-alert" class="hidden transition-all">
          <!-- Alerta de antídoto -->
        </div>
      </div>

      <!-- FERRAMENTA INTERATIVA: Calculadora de Anti-Hipertensivos Rápidos -->
      <div id="calc-ah" class="p-6 rounded-2xl glass-panel border-2 border-rose-500/40 shadow-lg shadow-rose-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Controle de Pico Pressórico (PA &ge; 160/110)</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Guia Posológico de Anti-Hipertensivos de Ação Rápida</h3>
          </div>
          <span class="text-xs text-slate-500">Meta: PAS 140-150 / PAD 90-100</span>
        </div>

        <div class="text-xs">
          <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Selecione o Medicamento:</label>
          <select id="ah-drug" class="w-full p-2.5 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 font-bold">
            <option value="hidralazina">Hidralazina IV (5 mg IV a cada 20 min, máx 20 mg) - Padrão SUS</option>
            <option value="labetalol">Labetalol IV (20 mg -> 40 mg -> 80 mg a cada 10-20 min, máx 220 mg) - Padrão ACOG</option>
            <option value="nifedipina">Nifedipina Oral Liberação Rápida (10 a 20 mg VO, nunca mastigar/sublingual!)</option>
          </select>
        </div>

        <div id="ah-guide" class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
          <!-- Renderizado dinamicamente -->
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 35: SÍNDROME HELLP
         ==================================================================== -->
    <section id="modulo-35" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="microscope" class="w-4 h-4"></i> Módulo 35
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Síndrome HELLP: Critérios de Tennessee / Mississippi & Diagnóstico Diferencial
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Tríade laboratorial (Hemólise, AST/ALT elevada, Plaquetas baixas), casos normotensos, e diferenciação rigorosa com Esteatose Hepática Aguda da Gestação (AFLP / Critérios de Swansea), PTT e SHU.
        </p>
      </div>

      <!-- FERRAMENTA INTERATIVA: Classificador HELLP -->
      <div id="calc-hellp" class="p-6 rounded-2xl glass-panel border-2 border-purple-500/40 shadow-lg shadow-purple-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300">Simulador Laboratorial</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Classificador da Síndrome HELLP (Critérios de Tennessee & Mississippi)</h3>
          </div>
          <span class="text-xs text-slate-500">Interpretação automática</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">Plaquetas (/mm³):</label>
            <input type="number" id="hellp-plt" value="65000" min="5000" max="450000" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Corte: &lt; 100.000 (Tennessee)</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">LDH / DHL Sérico (U/L):</label>
            <input type="number" id="hellp-ldh" value="820" min="100" max="5000" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Corte: &ge; 600 U/L</span>
          </div>
          <div class="p-3 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700">
            <label class="block font-bold mb-1 text-slate-800 dark:text-slate-200">AST / TGO Sérica (U/L):</label>
            <input type="number" id="hellp-ast" value="180" min="10" max="2000" class="w-full p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-bold text-sm">
            <span class="text-[10px] text-slate-500">Corte: &ge; 70 U/L</span>
          </div>
        </div>

        <div id="hellp-result" class="transition-all">
          <!-- Renderizado dinamicamente -->
        </div>
      </div>

      <!-- Tabela HELLP vs AFLP vs PTT/SHU -->
      <div class="p-5 rounded-2xl glass-panel space-y-3">
        <h4 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
          <i data-lucide="scale" class="w-4 h-4 text-purple-600"></i> Diagnóstico Diferencial Crítico: HELLP vs Esteatose Hepática Aguda (AFLP)
        </h4>
        <div class="overflow-x-auto text-xs">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-slate-200 dark:border-slate-800 text-slate-500 font-bold">
                <th class="py-2 px-3">Parâmetro</th>
                <th class="py-2 px-3">Síndrome HELLP</th>
                <th class="py-2 px-3">Esteatose Hepática Aguda (AFLP)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800/60 text-slate-700 dark:text-slate-300">
              <tr>
                <td class="py-2.5 px-3 font-semibold">Glicemia</td>
                <td class="py-2.5 px-3">Normal</td>
                <td class="py-2.5 px-3 font-bold text-rose-600">HIPOGLICEMIA GRAVE (&lt; 50 mg/dL)</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-semibold">Coagulograma / Fibrinogênio</td>
                <td class="py-2.5 px-3">Geralmente normal no início</td>
                <td class="py-2.5 px-3 font-bold text-rose-600">COAGULOPATIA PRECOCE (INR alto, Fibrinogênio baixo)</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-semibold">Amônia Sérica & Encefalopatia</td>
                <td class="py-2.5 px-3">Rara</td>
                <td class="py-2.5 px-3 font-bold text-rose-600">FREQUENTE (Amônia elevada, letargia precoce)</td>
              </tr>
              <tr>
                <td class="py-2.5 px-3 font-semibold">Associação Genética Fetal</td>
                <td class="py-2.5 px-3">Não estabelecida</td>
                <td class="py-2.5 px-3"><strong>Deficiência da LCHAD fetal</strong> (exige triagem do neonato)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 36: SEPSE OBSTÉTRICA
         ==================================================================== -->
    <section id="modulo-36" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="shield-alert" class="w-4 h-4"></i> Módulo 36
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Sepse Obstétrica & Bundle de Ressuscitação na 1ª Hora
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Identificação precoce pelo qSOFA obstétrico, principais focos (corioamnionite, endometrite, aborto séptico, pielonefrite) e o pacote de intervenção imediata da Surviving Sepsis Campaign adaptado à gestante.
        </p>
      </div>

      <!-- FERRAMENTA INTERATIVA: Bundle da Sepse na 1ª Hora -->
      <div id="tracker-sepsis" class="p-6 rounded-2xl glass-panel border-2 border-teal-500/40 shadow-lg shadow-teal-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-teal-100 text-teal-800 dark:bg-teal-950 dark:text-teal-300">Surviving Sepsis Obstétrica</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Bundle de Ressuscitação da 1ª Hora (Checklist Clínico)</h3>
          </div>
          <span id="sepsis-progress-text" class="text-xs font-bold text-slate-600 dark:text-slate-300">0 de 5 cumpridos (0%)</span>
        </div>

        <div class="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-800 overflow-hidden">
          <div id="sepsis-progress-bar" class="h-full bg-gradient-to-r from-teal-500 to-emerald-500 transition-all duration-300" style="width: 0%"></div>
        </div>

        <div class="space-y-2.5 text-xs">
          <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-100 transition-colors">
            <input type="checkbox" class="sepsis-check w-4 h-4 mt-0.5 rounded text-teal-600">
            <div>
              <strong class="text-slate-900 dark:text-white block">1. Dosar Lactato Sérico Imediato</strong>
              <span class="text-slate-600 dark:text-slate-400">Lactato &gt; 2 mmol/L indica hipoperfusão; &ge; 4 mmol/L define choque séptico e indica ressuscitação agressiva com repetição em 2–4 horas.</span>
            </div>
          </label>
          <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-100 transition-colors">
            <input type="checkbox" class="sepsis-check w-4 h-4 mt-0.5 rounded text-teal-600">
            <div>
              <strong class="text-slate-900 dark:text-white block">2. Coletar Hemoculturas (2 pares)</strong>
              <span class="text-slate-600 dark:text-slate-400">Coletar sítios distintos antes de iniciar a antibioticoterapia, sem atrasar o início dos antimicrobianos além de 45 minutos.</span>
            </div>
          </label>
          <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-100 transition-colors">
            <input type="checkbox" class="sepsis-check w-4 h-4 mt-0.5 rounded text-teal-600">
            <div>
              <strong class="text-slate-900 dark:text-white block">3. Iniciar Antibiótico de Amplo Espectro IV na 1ª Hora</strong>
              <span class="text-slate-600 dark:text-slate-400">Corioamnionite (Ampicilina + Gentamicina); Endometrite (Clindamicina + Gentamicina); Choque grave (Piperacilina-Tazobactam ou Meropenem + Vancomicina).</span>
            </div>
          </label>
          <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-100 transition-colors">
            <input type="checkbox" class="sepsis-check w-4 h-4 mt-0.5 rounded text-teal-600">
            <div>
              <strong class="text-slate-900 dark:text-white block">4. Ressuscitação Volêmica com Cristaloide (30 mL/kg)</strong>
              <span class="text-slate-600 dark:text-slate-400">Indicar se hipotensão (PAS &lt; 90 ou PAM &lt; 65) ou lactato &ge; 4 mmol/L. Administrar Ringer Lactato aquecido nas primeiras 3 horas.</span>
            </div>
          </label>
          <label class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-100 transition-colors">
            <input type="checkbox" class="sepsis-check w-4 h-4 mt-0.5 rounded text-teal-600">
            <div>
              <strong class="text-slate-900 dark:text-white block">5. Vasopressor Precoce (Noradrenalina)</strong>
              <span class="text-slate-600 dark:text-slate-400">Iniciar precocemente em bomba de infusão se hipotensão refratária para manter PAM alvo &ge; 65 mmHg e garantir perfusão placentária.</span>
            </div>
          </label>
        </div>

        <div id="sepsis-complete-alert" class="hidden p-4 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 border border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200 text-xs font-semibold flex items-center gap-3">
          <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600 flex-shrink-0"></i>
          <span>Bundle da 1ª Hora concluído com sucesso! Manter monitorização contínua de diurese (meta &ge; 0,5 mL/kg/h) e vigilância em UTI obstétrica.</span>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 37: PROLAPSO DE CORDÃO UMBILICAL
         ==================================================================== -->
    <section id="modulo-37" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="bell-ring" class="w-4 h-4"></i> Módulo 37
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Prolapso de Cordão Umbilical: Manobras de Alívio & Cardiotocografia
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Emergência cirúrgica máxima com bradicardia aguda após amniorrexe. Elevação manual da apresentação fetal, posição genupeitoral/Trendelenburg, infusão vesical e cesárea sob código vermelho.
        </p>
      </div>

      <!-- INFOGRÁFICO: CTG & Sofrimento Fetal -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Padrões de Cardiotocografia: DIP I, DIP II e Desacelerações Variáveis (DIP III)</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/sofrimento_fetal_ctg_desaceleracoes.jpg" data-title="Cardiotocografia e Sofrimento Fetal">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/sofrimento_fetal_ctg_desaceleracoes.jpg" alt="Cardiotocografia e Sofrimento Fetal" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/sofrimento_fetal_ctg_desaceleracoes.jpg" data-title="Cardiotocografia e Sofrimento Fetal">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Classificação das desacelerações intraparto: DIP precoce cefálico (DIP I), DIP tardio hipóxico (DIP II) e DIP variável por compressão funicular (DIP III) no prolapso de cordão.
        </p>
      </div>

      <!-- Sequência das 4 Manobras no Prolapso -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
          <span class="w-6 h-6 rounded-full bg-rose-600 text-white font-bold flex items-center justify-center text-xs mb-1">1</span>
          <strong class="text-slate-900 dark:text-slate-100 block">Elevação Manual Vaginal</strong>
          <p class="text-slate-600 dark:text-slate-400">Examinador introduz a mão na vagina e empurra a apresentação cefálica para cima, aliviando a compressão sobre o cordão até a extração fetal no bloco!</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
          <span class="w-6 h-6 rounded-full bg-rose-600 text-white font-bold flex items-center justify-center text-xs mb-1">2</span>
          <strong class="text-slate-900 dark:text-slate-100 block">Posição Genupeitoral</strong>
          <p class="text-slate-600 dark:text-slate-400">Manter a gestante de joelhos com o peito no leito (prece maometana) ou em Trendelenburg acentuado para usar a gravidade a favor do descolamento fetal.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
          <span class="w-6 h-6 rounded-full bg-rose-600 text-white font-bold flex items-center justify-center text-xs mb-1">3</span>
          <strong class="text-slate-900 dark:text-slate-100 block">Enchimento Vesical</strong>
          <p class="text-slate-600 dark:text-slate-400">Passar sonda Foley e instilar 500 mL de SF 0,9% estéril morno na bexiga; a bexiga distendida empurra a apresentação fetal para cima durante o transporte.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
          <span class="w-6 h-6 rounded-full bg-rose-600 text-white font-bold flex items-center justify-center text-xs mb-1">4</span>
          <strong class="text-slate-900 dark:text-slate-100 block">Cesárea Imediata</strong>
          <p class="text-slate-600 dark:text-slate-400">Código vermelho de cesariana ultra-emergente. Parto vaginal só é tentado se a dilatação for total com polo fetal já desprendendo no períneo!</p>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 38: DISTÓCIA DE OMBROS
         ==================================================================== -->
    <section id="modulo-38" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="clock" class="w-4 h-4"></i> Módulo 38
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Distócia de Ombros: Sinal da Tartaruga & Algoritmo HELPERR
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Impacto do ombro anterior contra a sínfise púbica materna, sinal da tartaruga, protocolo estruturado HELPERR com cronômetro de 5 minutos e proibição absoluta da manobra de Kristeller.
        </p>
      </div>

      <!-- INFOGRÁFICO: Distócia de Ombros -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Mecanismo do Impacto Ósseo, Manobra de McRoberts e Pressão Suprapúbica (Rubin I)</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/distocia_ombros_helperr_algoritmo.jpg" data-title="Distócia de Ombros e Manobra de McRoberts">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/distocia_ombros_helperr_algoritmo.jpg" alt="Distócia de Ombros e Manobra de McRoberts" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/distocia_ombros_helperr_algoritmo.jpg" data-title="Distócia de Ombros e Manobra de McRoberts">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Anatomia do descolamento da sínfise púbica pela hiperflexão das coxas (McRoberts) e vetor de pressão suprapúbica em sentido adutor no ombro anterior.
        </p>
      </div>

      <!-- FERRAMENTA INTERATIVA: Simulador HELPERR com Cronômetro -->
      <div id="calc-helperr" class="p-6 rounded-2xl glass-panel border-2 border-amber-500/40 shadow-lg shadow-amber-500/5 space-y-5 scroll-mt-28">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300">Simulador de Treinamento em Sala de Parto</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Simulador Passo a Passo do Algoritmo HELPERR</h3>
          </div>
          <div class="flex items-center gap-3">
            <span id="helperr-timer" class="text-xl font-black text-amber-600 dark:text-amber-400">00:00</span>
            <button type="button" id="helperr-timer-toggle" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition-colors">Iniciar Cronômetro</button>
          </div>
        </div>

        <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-4">
          <div class="flex items-center gap-3">
            <span id="helperr-letter" class="w-12 h-12 rounded-xl bg-gradient-to-tr from-rose-600 to-amber-500 text-white font-black text-2xl flex items-center justify-center flex-shrink-0 shadow-md">
              H
            </span>
            <div>
              <h4 id="helperr-name" class="font-bold text-base text-slate-900 dark:text-white">1. Help (Pedir Ajuda)</h4>
              <span class="text-xs text-slate-400">Manobra Sequencial do Algoritmo Internacional ALSO / ACOG</span>
            </div>
          </div>

          <div id="helperr-action" class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed font-medium">
            Carregando instruções...
          </div>

          <div class="p-3 rounded-lg bg-rose-50 dark:bg-rose-950/40 border border-rose-300 dark:border-rose-800 text-xs text-rose-800 dark:text-rose-200 font-bold">
            <i data-lucide="alert-octagon" class="w-3.5 h-3.5 inline mr-1 text-rose-600"></i>
            <span id="helperr-prohibition">Carregando alerta...</span>
          </div>

          <div class="flex items-center justify-between pt-2 border-t border-slate-100 dark:border-slate-800">
            <button type="button" id="helperr-prev" class="px-3.5 py-1.5 rounded-lg border border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-xs font-bold disabled:opacity-40">
              &larr; Manobra Anterior
            </button>
            <button type="button" id="helperr-next" class="px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold transition-colors disabled:opacity-40">
              Próxima Manobra &rarr;
            </button>
          </div>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         MÓDULO 39: EMBOLIA POR LÍQUIDO AMNIÓTICO (ELA)
         ==================================================================== -->
    <section id="modulo-39" class="module-card scroll-mt-28 space-y-8">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wider mb-1">
          <i data-lucide="activity" class="w-4 h-4"></i> Módulo 39
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Embolia por Líquido Amniótico (ELA / Síndrome Anafilactoide)
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Colapso cardiopulmonar anafilactoide periparto, hipertensão pulmonar aguda com falência de VD, CIVD fulminante com fibrinogênio &lt; 100 mg/dL e suporte de terapia intensiva.
        </p>
      </div>

      <!-- INFOGRÁFICO: ELA & Sepse -->
      <div class="p-6 rounded-2xl glass-panel space-y-4 border border-rose-500/30">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="px-2.5 py-1 text-[10px] font-bold uppercase rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Infográfico Médico Oficial • Alta Definição</span>
            <h3 class="font-bold text-lg text-slate-900 dark:text-white mt-1">Fisiopatologia da ELA em 3 Fases, Falência de VD e Bundle da Sepse</h3>
          </div>
          <button type="button" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 hover:bg-rose-200 transition-colors" data-lightbox="assets/img/embolia_liquido_amniotico_sepse.jpg" data-title="Embolia por Líquido Amniótico e Sepse">
            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expandir HD
          </button>
        </div>
        <div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white">
          <img src="assets/img/embolia_liquido_amniotico_sepse.jpg" alt="Embolia por Líquido Amniótico e Sepse" class="w-full h-auto object-cover zoom-cursor" data-lightbox="assets/img/embolia_liquido_amniotico_sepse.jpg" data-title="Embolia por Líquido Amniótico e Sepse">
        </div>
        <p class="text-xs text-slate-500 dark:text-slate-400 italic">
          Tríade da ELA (choque cardiogênico de VD, hipóxia e CIVD com sangramento incontrolável); suporte com inotrópicos, vasodilatadores pulmonares, restrição de volume e protocolo de transfusão maciça precoce.
        </p>
      </div>

    </section>

    <!-- ====================================================================
         REVISÃO DE ALTO RENDIMENTO (TOP 20 HIGH-YIELD)
         ==================================================================== -->
    <section id="high-yield" class="scroll-mt-28 space-y-6">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wider mb-1">
          <i data-lucide="star" class="w-4 h-4"></i> Revisão de Alto Rendimento
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Top 20 Regras de Ouro: Os Primeiros Passos que a Banca Quer
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Mapeamento das decisões prioritárias mais cobradas no USMLE Step 2 CK, Step 3, Revalida e Concursos de Residência Médica.
        </p>
      </div>

      <div class="p-6 rounded-2xl glass-panel space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">1. Mulher em idade fértil com dor ou sangramento</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>beta-hCG</strong> imediato (nunca assuma que não está grávida!).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">2. Gestante instável + beta-hCG positivo + útero vazio</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Cirurgia de emergência</strong> (não aguardar dosagens seriadas de beta-hCG ou USTV formal).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">3. Sangramento indolor no 3º trimestre</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Ultrassom</strong>. TOQUE VAGINAL FORMALMENTE CONTRAINDICADO até descartar placenta prévia!</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">4. Sangramento doloroso + útero lenhoso em tábua</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Estabilizar + Cesárea</strong> (DPP é diagnóstico clínico; ultrassom negativo NÃO afasta!).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">5. Sangramento pós-amniorrexe + bradicardia fetal fulminante</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Cesariana de emergência imediata</strong> (Vasa Prévia; o sangue perdido é fetal!).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">6. PA &ge; 160/110 mmHg confirmada</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Anti-hipertensivo rápido</strong> em até 30–60 min (Hidralazina IV, Labetalol IV ou Nifedipina VO).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">7. Pré-eclâmpsia com sinal de gravidade</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Sulfato de Magnésio</strong> imediato para prevenção de convulsões (Zuspan ou Pritchard).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">8. Convulsão em gestante &gt; 20 semanas</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Sulfato de Magnésio</strong> (MgSO₄ é superior a diazepam e fenitoína na eclâmpsia!).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">9. Paciente em MgSO₄ sem reflexo patelar / bradipneica</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Suspender MgSO₄ + Gluconato de Cálcio 10% 10 mL IV lento</strong>.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">10. Dor epigástrica em barra &gt; 20 semanas</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Hemograma + LDH + AST/TGO</strong> (suspeitar de HELLP syndrome ou rotura hepática!).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">11. Bradicardia súbita pós-amniotomia</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Toque vaginal imediato</strong> pesquisando Prolapso de Cordão Umbilical.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">12. Cordão palpável pulsátil na vagina</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Elevação manual da cabeça fetal</strong> + posição genupeitoral + cesárea de emergência.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">13. Cabeça fetal retrai contra o períneo (Sinal da Tartaruga)</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Chamar ajuda + McRoberts + Pressão Suprapúbica</strong>. Kristeller é PROIBIDO!</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <span class="font-bold text-rose-600">14. PCR materna &ge; 20 semanas sem RCE aos 4 minutos</span>
            <p class="text-slate-600 dark:text-slate-400"><strong>Cesárea perimortem no local da parada</strong> (nascimento no 5º minuto).</p>
          </div>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         FLASHCARDS 3D INTERATIVOS
         ==================================================================== -->
    <section id="flashcards" class="scroll-mt-28 space-y-6">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-sky-600 dark:text-sky-400 uppercase tracking-wider mb-1">
          <i data-lucide="layers" class="w-4 h-4"></i> Memorização Ativa
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Flashcards Clínicos 3D de Emergência
        </h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
          Fixação dos conceitos de maior impacto e condutas de segundo a segundo nas urgências obstétricas.
        </p>
      </div>

      <div class="max-w-xl mx-auto perspective-1000">
        <div id="flashcard" class="relative w-full h-80 rounded-2xl glass-panel shadow-xl cursor-pointer transform-style-3d transition-transform duration-500 border border-slate-200 dark:border-slate-800">
          
          <!-- Frente -->
          <div class="absolute inset-0 p-6 flex flex-col justify-between backface-hidden">
            <div class="flex items-center justify-between">
              <span id="fc-category" class="px-2.5 py-1 text-[10px] font-bold rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">
                Categoria
              </span>
              <span class="text-xs text-slate-400 flex items-center gap-1">
                <i data-lucide="rotate-cw" class="w-3.5 h-3.5"></i> Clique para virar
              </span>
            </div>
            <div class="my-auto text-center px-4">
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-2">Pergunta Clínica:</span>
              <p id="fc-question" class="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-relaxed">
                Carregando pergunta...
              </p>
            </div>
            <div class="text-center text-[11px] text-slate-400">
              Toque no cartão para conferir a resposta e a conduta
            </div>
          </div>

          <!-- Verso -->
          <div class="absolute inset-0 p-6 flex flex-col justify-between backface-hidden rotate-y-180 bg-slate-900 text-white rounded-2xl border border-rose-500/40">
            <div class="flex items-center justify-between">
              <span class="px-2.5 py-1 text-[10px] font-bold rounded-md bg-emerald-500/20 text-emerald-300">
                Resposta / Conduta
              </span>
              <span class="text-xs text-slate-400">FEBRASGO / ACOG</span>
            </div>
            <div class="my-auto text-center px-4">
              <p id="fc-answer" class="text-xs sm:text-sm font-medium text-slate-200 leading-relaxed">
                Carregando resposta...
              </p>
            </div>
            <div class="text-center text-[11px] text-slate-400">
              Clique para voltar à pergunta
            </div>
          </div>

        </div>

        <!-- Controles dos Flashcards -->
        <div class="flex items-center justify-between mt-4 px-2">
          <button type="button" id="fc-prev" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-800 hover:bg-slate-200 dark:hover:bg-slate-800 text-xs font-bold transition-colors">
            <i data-lucide="chevron-left" class="w-4 h-4"></i>
          </button>
          <div class="flex items-center gap-3">
            <span id="fc-counter" class="text-xs font-bold text-slate-500">1 de 12</span>
            <button type="button" id="fc-flip" class="px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold transition-colors">
              Virar Cartão
            </button>
          </div>
          <button type="button" id="fc-next" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-800 hover:bg-slate-200 dark:hover:bg-slate-800 text-xs font-bold transition-colors">
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         SIMULADO: 14 VINHETAS CLÍNICAS (ESTILO USMLE STEP 2 CK / RESIDÊNCIA)
         ==================================================================== -->
    <section id="quiz" class="scroll-mt-28 space-y-6">
      
      <div class="border-b border-slate-200 dark:border-slate-800 pb-4">
        <div class="flex items-center gap-2 text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider mb-1">
          <i data-lucide="check-square" class="w-4 h-4"></i> Avaliação Prática
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
              Simulado Interativo: 14 Vinhetas Clínicas
            </h2>
            <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
              Casos clínicos reais das provas do USMLE Step 2 CK, Step 3, Revalida e Concursos Nacionais de Residência Médica.
            </p>
          </div>
          <span id="quiz-score-badge" class="px-3.5 py-1.5 rounded-xl text-xs font-black bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800 self-start sm:self-auto">
            0 / 14 Corretas (0%)
          </span>
        </div>
      </div>

      <div id="quiz-container" class="space-y-6 max-w-3xl mx-auto">
        <!-- Renderizado dinamicamente pelo app.js -->
      </div>

    </section>

  </main>

  <!-- ======================================================================
       MODAL DE LIGHTBOX HD INTERATIVO
       ====================================================================== -->
  <div id="lightbox-modal" class="hidden fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex flex-col items-center justify-center p-4">
    <div class="w-full max-w-7xl flex items-center justify-between text-white pb-3 px-2">
      <span id="lightbox-title" class="text-xs sm:text-sm font-bold truncate pr-4">Infográfico Médico em Alta Resolução</span>
      <div class="flex items-center gap-2 flex-shrink-0">
        <button type="button" id="lightbox-zoom-in" class="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors" title="Aumentar Zoom">
          <i data-lucide="zoom-in" class="w-4 h-4"></i>
        </button>
        <button type="button" id="lightbox-zoom-out" class="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors" title="Diminuir Zoom">
          <i data-lucide="zoom-out" class="w-4 h-4"></i>
        </button>
        <button type="button" id="lightbox-reset" class="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-white transition-colors" title="Restaurar Tamanho">
          <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
        </button>
        <button type="button" id="lightbox-close" class="p-2 rounded-lg bg-rose-600 hover:bg-rose-700 text-white transition-colors" title="Fechar (ESC)">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>
    </div>
    <div class="relative w-full max-w-7xl flex-1 flex items-center justify-center overflow-hidden rounded-2xl border border-white/10 bg-black/50">
      <img id="lightbox-image" src="" alt="Infográfico Expandido" class="lightbox-img max-w-full max-h-[82vh] object-contain select-none cursor-grab">
    </div>
  </div>

  <!-- ======================================================================
       FOOTER INSTITUCIONAL
       ====================================================================== -->
  <footer class="border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950 py-10 transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
      
      <div class="flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-rose-600 to-amber-500 flex items-center justify-center text-white">
            <i data-lucide="siren" class="w-4 h-4"></i>
          </div>
          <div>
            <span class="font-extrabold text-sm text-slate-900 dark:text-white">Urgências Obstétricas Interativas</span>
            <span class="block text-[11px] text-slate-500 dark:text-slate-400">Guia de Emergência Nível USMLE Step 2 CK / Step 3 & Residência Médica</span>
          </div>
        </div>
        <div class="flex flex-wrap items-center gap-4 text-xs font-medium text-slate-600 dark:text-slate-400">
          <a href="#modulo-29" class="hover:text-rose-600 transition-colors">Choque & Cesárea</a>
          <a href="#modulo-31" class="hover:text-rose-600 transition-colors">Ectópica</a>
          <a href="#modulo-34" class="hover:text-rose-600 transition-colors">Pré-Eclâmpsia</a>
          <a href="#modulo-38" class="hover:text-rose-600 transition-colors">Distócia</a>
          <a href="#high-yield" class="hover:text-amber-500 transition-colors font-bold">Top 20</a>
          <a href="#quiz" class="hover:text-emerald-500 transition-colors font-bold">14 Casos</a>
        </div>
      </div>

      <div class="border-t border-slate-100 dark:border-slate-900 pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-500">
        <p>&copy; 2026 Portal Médico de Urgências Obstétricas. Diretrizes FEBRASGO, SUS e ACOG. Otimizado para GitHub Pages.</p>
        <div class="flex items-center gap-2">
          <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-900 text-[10px] font-bold">v4.0 Definitiva</span>
        </div>
      </div>

    </div>
  </footer>

  <!-- Scripts -->
  <script src="assets/js/app.js"></script>
  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Sucesso: index.html gerado com {len(html):,} caracteres em {OUTPUT_HTML}")

if __name__ == "__main__":
    generate_html()
