# Urgências e Emergências Obstétricas — Portal Interativo de Decisão Clínica

> **Guia Completo de Urgências e Emergências Obstétricas (Módulos 29 ao 39)**  
> Alinhado aos padrões: **USMLE Step 2 CK / Step 3**, **Residência Médica em GO / R+**, **FEBRASGO**, **PCDT / SUS** e **ACOG**.

---

## 🌟 Visão Geral

Este projeto é uma plataforma web estática, rica e moderna, desenvolvida para estudo aprofundado e tomada de decisão clínica rápida à beira do leito em emergências materno-fetais.

### 🔬 O Que Está Incluído:
1. **11 Módulos Clínicos Completos (M29 ao M39):**
   - **M29:** Choque em Obstetrícia, Ressuscitação Materna e Cesárea Perimortem (4-5 min)
   - **M30:** Sangramentos da 1ª Metade: Espectro do Abortamento
   - **M31:** Gravidez Ectópica (Tubária, Abdominal, Intersticial) e Elegibilidade ao MTX
   - **M32:** Doença Trofoblástica Gestacional (Mola Completa vs Parcial, Coriocarcinoma)
   - **M33:** Sangramentos da 2ª Metade (DPP, Placenta Prévia, Vasa Prévia, Rotura Uterina, PAS)
   - **M34:** Pré-Eclâmpsia Grave e Eclâmpsia (Protocolos de Sulfato de Magnésio e Anti-hipertensivos)
   - **M35:** Síndrome HELLP vs Fígado Gorduroso Agudo da Gestação (AFLP / Critérios de Swansea)
   - **M36:** Sepse Materna e Choque Séptico (Maternal qSOFA, SEP-1 Bundle)
   - **M37:** Sofrimento Fetal Agudo e Prolapso de Cordão Umbilical
   - **M38:** Distócia de Ombros (Mnemônico HELPERR passo a passo)
   - **M39:** Embolia por Líquido Amniótico (ELA / AFE) e Colapso Cardiovascular Súbito

2. **9 Infográficos Médicos de Alta Definição (HD) com Lightbox e Zoom/Pan:**
   - Diagramas anatômicos, fluxogramas de conduta e tabelas comparativas vetoriais.
   - Padrão visual SUS / FEBRASGO / ACOG com tipografia legível em português.

3. **6 Ferramentas e Calculadoras Clínicas Interativas:**
   - **Calculadora do Índice de Choque Obstétrico ($IC = FC / PAS$):** Com estratificação de risco (0,7 / 0,9 / 1,0 / 1,4) e gatilho de Protocolo de Transfusão Maciça (1:1:1).
   - **Calculadora de Elegibilidade para Metotrexato (MTX 50 mg/m²):** Análise em tempo real de critérios estritos ($\beta$-hCG, massa anexial, BCF, líquido livre e estabilidade).
   - **Calculadora de Sulfato de Magnésio e Manejo de Intoxicação:** Esquemas Zuspan, Pritchard e Sibai com conduta imediata para intoxicação (Gluconato de Cálcio 10%).
   - **Guia Dinâmico de Anti-hipertensivos de Ação Rápida:** Hidralazina IV, Labetalol IV e Nifedipina VO com metas pressóricas e contraindicações.
   - **Classificador de HELLP (Tennessee & Mississippi) vs AFLP (Critérios de Swansea):** Diagnóstico diferencial laboratorial instantâneo.
   - **Simulador Interativo do Algoritmo HELPERR com Cronômetro de 5 Minutos:** Treinamento cronometrado passo a passo para distócia de ombros.
   - **Rastreador do Pacote de Sepse Materna de 1 Hora:** Checklist dinâmico com barra de progresso em tempo real.

4. **Ferramentas Ativas de Aprendizado:**
   - **Flashcards 3D Interativos:** 12 cartões de alto rendimento com animação 3D de virada.
   - **Simulado Clínico Interativo (14 Vinhetas):** Questões no estilo USMLE Step 2 CK e provas de Residência Médica, com gabarito fundamentado e pontuação em tempo real.
   - **Busca Global Instantânea (`Ctrl + K`):** Localize tópicos, critérios e medicamentos instantaneamente.
   - **Modo Claro / Escuro (Dark Mode):** Alternância instantânea com persistência em `localStorage` e proteção anti-FOUC.

---

## 🚀 Como Fazer o Deploy no GitHub Pages

O site é **100% estático** (HTML5, Tailwind CSS via CDN, Vanilla JavaScript e CSS moderno), sem necessidade de build complexo ou NodeJS no servidor.

### Opção A: Via Terminal Git (Recomendado)

1. Abra o terminal na pasta do projeto:
   ```bash
   cd "c:\Users\Admin\Downloads\INTERNATO GO\site_urgencias_obstetricas"
   ```

2. Inicialize o repositório e faça o primeiro commit:
   ```bash
   git init
   git add .
   git commit -m "feat: Portal Interativo de Urgências Obstétricas"
   ```

3. Crie um novo repositório no seu GitHub (exemplo: `urgencias-obstetricas`).

4. Conecte o repositório remoto e envie os arquivos:
   ```bash
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/urgencias-obstetricas.git
   git push -u origin main
   ```

5. Ative o **GitHub Pages**:
   - Vá no seu repositório no GitHub -> **Settings** -> **Pages** (menu lateral esquerdo).
   - Em **Build and deployment** > **Source**, selecione: **Deploy from a branch**.
   - Em **Branch**, selecione `main` e pasta `/ (root)`.
   - Clique em **Save**.
   - Em 1 a 2 minutos, seu site estará no ar na URL:  
     `https://SEU_USUARIO.github.io/urgencias-obstetricas/`

---

### Opção B: Upload Direto no GitHub Web

1. Crie um novo repositório no GitHub (ex: `urgencias-obstetricas`).
2. Clique em **Add file** -> **Upload files**.
3. Arraste todos os arquivos e pastas da pasta `site_urgencias_obstetricas`:
   - `index.html`
   - `.nojekyll` (fundamental para evitar que o GitHub ignore arquivos)
   - Pasta `assets/` (com `css/`, `js/` e `img/`)
4. Clique em **Commit changes**.
5. Em **Settings** -> **Pages**, selecione a branch `main` e `/ (root)` e clique em **Save**.

---

## 📂 Estrutura de Arquivos

```text
site_urgencias_obstetricas/
├── .nojekyll                  # Garante carregamento correto no GitHub Pages
├── index.html                 # Página principal completa com todos os módulos
├── README.md                  # Manual do projeto e instruções de deploy
├── assets/
│   ├── css/
│   │   └── custom.css         # Efeitos glassmorphism, 3D flip card, lightbox
│   ├── js/
│   │   └── app.js             # Motores de cálculo, simuladores, quiz, flashcards
│   └── img/
│       ├── choque_obstetrico_cesarea_perimortem.jpg
│       ├── abortamento_e_gravidez_ectopica.jpg
│       ├── doenca_trofoblastica_mola_hidatiforme.jpg
│       ├── hemorragias_segunda_metade_dpp_vs_pp.jpg
│       ├── preeclampsia_grave_hellp_magnesio.jpg
│       ├── hemorragia_pos_parto_balao_bakri.jpg
│       ├── sofrimento_fetal_ctg_desaceleracoes.jpg
│       ├── distocia_ombros_helperr_algoritmo.jpg
│       └── embolia_liquido_amniotico_sepse.jpg
└── scripts/
    ├── build_site.py          # Script gerador do index.html
    ├── build_urgencias_diagrams.py # Gerador autônomo dos infográficos em alta resolução
    ├── inspect_ids.py         # Validador de integridade JS/HTML
    └── verify_site.py         # Script de testes automatizados do site
```

---

## 🛡️ Licença e Referências Médicas
- **FEBRASGO:** Tratado de Obstetrícia e Manuais de Urgências e Emergências Obstétricas.
- **Ministério da Saúde do Brasil / SUS:** Manual Técnico de Gestação de Alto Risco & PCDT de Hemorragia Pós-Parto e Síndromes Hipertensivas.
- **ACOG:** Practice Bulletins (Gestational Hypertension, Preeclampsia, Postpartum Hemorrhage, Shoulder Dystocia).
- **USMLE Step 2 CK / UpToDate:** First Aid for the USMLE Step 2 CK & UpToDate Clinical Obstetric Emergencies.
