/**
 * app.js - Lógica Interativa do Portal de Urgências e Emergências Obstétricas
 * Baseado no Guia Obstetrícia e Ginecologia Parte 4 (USMLE Step 2 CK / FEBRASGO / SUS / ACOG)
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileNav();
  initSearch();
  initShockIndexCalculator();
  initMTXCalculator();
  initMagnesiumCalculator();
  initAntiHypertensiveCalculator();
  initHELLPClassifier();
  initHELPERRSimulator();
  initSepsisBundleTracker();
  initFlashcards();
  initQuiz();
  initLightbox();
});

/* ==========================================================================
   1. GERENCIAMENTO DE TEMA (DARK / LIGHT)
   ========================================================================== */
function initTheme() {
  const themeToggles = document.querySelectorAll('.theme-toggle-btn, #theme-toggle, #mobile-theme-toggle');
  const html = document.documentElement;

  function updateThemeUI() {
    const isDark = html.classList.contains('dark');
    themeToggles.forEach(btn => {
      btn.setAttribute('aria-label', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
      btn.setAttribute('title', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
    });
  }

  function toggleTheme() {
    const isDark = html.classList.contains('dark');
    if (isDark) {
      html.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
    updateThemeUI();
  }

  themeToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleTheme();
    });
  });

  updateThemeUI();
}

/* ==========================================================================
   1.1 MENU MOBILE & GAVETA RESPONSIVA
   ========================================================================== */
function initMobileNav() {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-menu-drawer');
  const menuIcon = document.getElementById('mobile-menu-icon');
  if (!toggleBtn || !drawer) return;

  function setOpen(isOpen) {
    if (isOpen) {
      drawer.classList.remove('hidden');
      toggleBtn.setAttribute('aria-expanded', 'true');
      if (menuIcon && window.lucide) {
        menuIcon.setAttribute('data-lucide', 'x');
        lucide.createIcons();
      }
    } else {
      drawer.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon && window.lucide) {
        menuIcon.setAttribute('data-lucide', 'menu');
        lucide.createIcons();
      }
    }
  }

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isHidden = drawer.classList.contains('hidden');
    setOpen(isHidden);
  });

  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => setOpen(false));
  });

  document.addEventListener('click', (e) => {
    if (!drawer.contains(e.target) && !toggleBtn.contains(e.target) && !drawer.classList.contains('hidden')) {
      setOpen(false);
    }
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !drawer.classList.contains('hidden')) {
      setOpen(false);
    }
  });
}

/* ==========================================================================
   2. SISTEMA DE BUSCA E FILTRO RÁPIDO
   ========================================================================== */
function initSearch() {
  const searchInputs = [
    document.getElementById('global-search'),
    document.getElementById('mobile-search')
  ].filter(Boolean);

  if (searchInputs.length === 0) return;

  function handleSearch(query) {
    const q = query.toLowerCase().trim();
    const modules = document.querySelectorAll('.module-card');
    
    searchInputs.forEach(input => {
      if (input.value !== query) input.value = query;
    });

    let matchCount = 0;
    modules.forEach((mod) => {
      const text = mod.textContent.toLowerCase();
      if (!q || text.includes(q)) {
        mod.style.display = '';
        matchCount++;
      } else {
        mod.style.display = 'none';
      }
    });

    const noResults = document.getElementById('search-no-results');
    if (noResults) {
      if (matchCount === 0 && q) {
        noResults.classList.remove('hidden');
      } else {
        noResults.classList.add('hidden');
      }
    }
  }

  searchInputs.forEach(input => {
    input.addEventListener('input', (e) => handleSearch(e.target.value));
  });

  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      const primary = document.getElementById('global-search') || searchInputs[0];
      if (primary) {
        primary.focus();
        primary.select();
      }
    }
  });
}

/* ==========================================================================
   3. CALCULADORA DO ÍNDICE DE CHOQUE OBSTÉTRICO & MEOWS
   ========================================================================== */
function initShockIndexCalculator() {
  const hrInput = document.getElementById('si-hr');
  const sbpInput = document.getElementById('si-sbp');
  const scoreOut = document.getElementById('si-score');
  const statusBadge = document.getElementById('si-status');
  const actionText = document.getElementById('si-action');
  const warningBox = document.getElementById('si-warning');

  if (!hrInput || !sbpInput || !scoreOut) return;

  function calculateSI() {
    const hr = parseFloat(hrInput.value) || 0;
    const sbp = parseFloat(sbpInput.value) || 0;

    if (sbp <= 0 || hr <= 0) {
      scoreOut.textContent = "0.00";
      statusBadge.textContent = "Aguardando dados";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-slate-200 text-slate-800";
      actionText.innerHTML = "Insira a Frequência Cardíaca e a Pressão Sistólica da gestante.";
      if (warningBox) warningBox.classList.add('hidden');
      return;
    }

    const si = hr / sbp;
    scoreOut.textContent = si.toFixed(2);

    if (si < 0.7) {
      statusBadge.textContent = "Risco Baixo (IC < 0,7)";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300";
      actionText.innerHTML = `
        <strong class="text-emerald-700 dark:text-emerald-400">Classificação: Parâmetro Hemodinâmico Fisiológico.</strong><br>
        Manter vigilância rotineira. Na gestação, a taquicardia leve e hemodiluição são normais, mas a PA deve ser correlacionada aos sintomas clínicos.
      `;
      if (warningBox) warningBox.classList.add('hidden');
    } else if (si >= 0.7 && si < 1.0) {
      statusBadge.textContent = "Zona de Alerta Moderado (IC 0,7 a 0,9)";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300";
      actionText.innerHTML = `
        <strong class="text-amber-700 dark:text-amber-400">Alerta: Possível Choque Inicial ou Compensado.</strong><br>
        A gestante pode perder até 1.500 mL antes de manifestar hipotensão clássica. Abrir 2 acessos calibrosos (14-16G), tipagem ABO/Rh, dosar fibrinogênio e monitorar diurese por sonda vesical de demora.
      `;
      if (warningBox) warningBox.classList.add('hidden');
    } else if (si >= 1.0 && si < 1.4) {
      statusBadge.textContent = "ALERTA VERMELHO: Choque Compensado Grave (IC >= 1,0)";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300";
      actionText.innerHTML = `
        <strong class="text-rose-700 dark:text-rose-400">Conduta Imediata: Ressuscitação Hemodinâmica Agressiva!</strong><br>
        • Deslocamento uterino para a esquerda (DUE 15-30°) se >= 20 semanas.<br>
        • Cristaloide aquecido (máx 1.000 a 1.500 mL para evitar coagulopatia dilucional).<br>
        • <strong>Ácido Tranexâmico 1g IV em 10 min</strong> imediatamente (até 3h do início da hemorragia).<br>
        • Acionar equipe multidisciplinar e reservar hemocomponentes.
      `;
      if (warningBox) {
        warningBox.classList.remove('hidden');
        warningBox.innerHTML = "⚠️ ATENÇÃO: Índice de Choque >= 1,0 indica perda volêmica de 20 a 30% da volemia materna!";
      }
    } else {
      statusBadge.textContent = "EMERGÊNCIA CRÍTICA: Choque Grave / Transfusão Maciça (IC >= 1,4)";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-red-600 text-white animate-pulse";
      actionText.innerHTML = `
        <strong class="text-rose-700 dark:text-rose-400">Gatilho Formal para Protocolo de Transfusão Maciça (PTM):</strong><br>
        • Iniciar transfusão equilibrada em <strong>razão 1:1:1</strong> (Hemácias : Plasma Fresco : Plaquetas).<br>
        • Se Fibrinogênio < 200 mg/dL: Administrar <strong>Crioprecipitado (10 unidades)</strong> ou concentrado de fibrinogênio.<br>
        • Ácido Tranexâmico 1g IV imediato + 1g após 30 min se sangramento contínuo.<br>
        • Evitar hipotermia, acidose e hipocalcemia (corrigir cálcio com Gluconato de Cálcio 10%).
      `;
      if (warningBox) {
        warningBox.classList.remove('hidden');
        warningBox.innerHTML = "🚨 GATILHO DE TRANSFUSÃO MACIÇA: Alta probabilidade de colapso cardiovascular e óbito materno sem transfusão imediata de hemocomponentes em proporção 1:1:1!";
      }
    }
  }

  hrInput.addEventListener('input', calculateSI);
  sbpInput.addEventListener('input', calculateSI);
  calculateSI();
}

/* ==========================================================================
   4. SIMULADOR DE ELEGIBILIDADE DO METOTREXATO (ECTÓPICA)
   ========================================================================== */
function initMTXCalculator() {
  const hcgInput = document.getElementById('mtx-hcg');
  const sizeInput = document.getElementById('mtx-size');
  const fhrCheck = document.getElementById('mtx-fhr');
  const stableCheck = document.getElementById('mtx-stable');
  const fluidCheck = document.getElementById('mtx-fluid');
  const resultBox = document.getElementById('mtx-result');
  const detailsOut = document.getElementById('mtx-details');

  if (!hcgInput || !sizeInput || !resultBox) return;

  function evaluateMTX() {
    const hcg = parseFloat(hcgInput.value) || 0;
    const size = parseFloat(sizeInput.value) || 0;
    const hasFHR = fhrCheck ? fhrCheck.checked : false;
    const isStable = stableCheck ? stableCheck.checked : false;
    const hasFreeFluid = fluidCheck ? fluidCheck.checked : false;

    let contraindications = [];

    if (!isStable) contraindications.push("Instabilidade hemodinâmica (emergência cirúrgica)");
    if (hasFHR) contraindications.push("Atividade cardíaca embrionária presente (BCF positivo)");
    if (size >= 3.5) contraindications.push(`Massa anexial >= 3,5 cm (atual: ${size} cm)`);
    if (hcg >= 5000) contraindications.push(`beta-hCG sérico >= 5.000 mUI/mL (atual: ${hcg.toLocaleString()} mUI/mL)`);
    if (hasFreeFluid) contraindications.push("Líquido livre moderado a volumoso na cavidade peritoneal");

    if (contraindications.length === 0) {
      resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-emerald-700 dark:text-emerald-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> ELEGÍVEL PARA TRATAMENTO CLÍNICO COM METOTREXATO (MTX)
        </div>
        <p class="text-xs mt-2 leading-relaxed">
          <strong>Prescrição:</strong> Metotrexato 50 mg/m² IM em dose única.<br>
          <strong>Seguimento Rigoroso:</strong> Dosar beta-hCG no D4 e no D7 pós-injeção.<br>
          <strong>Meta:</strong> Queda de >= 15% entre D4 e D7. Se queda < 15%, considerar 2ª dose ou conversão cirúrgica.<br>
          <em>Orientações:</em> Suspender ácido fólico, evitar anti-inflamatórios e relações sexuais durante o tratamento.
        </p>
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border-2 bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-rose-700 dark:text-rose-400">
          <i data-lucide="alert-octagon" class="w-5 h-5"></i> CONTRAINDICADO METOTREXATO — CONDUTA CIRÚRGICA INDICADA
        </div>
        <p class="text-xs mt-2 leading-relaxed">
          <strong>Critérios Impeditivos Detectados:</strong>
          <ul class="list-disc list-inside mt-1 font-semibold text-rose-800 dark:text-rose-300">
            ${contraindications.map(c => `<li>${c}</li>`).join('')}
          </ul>
          <span class="block mt-2">
            <strong>Conduta Recomendada:</strong> Laparoscopia de urgência (Salpingectomia se trompa rota, hemorragia volumosa ou prole definida; Salpingostomia linear se desejo de preservação e trompa íntegra).
          </span>
        </p>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  [hcgInput, sizeInput].forEach(el => el.addEventListener('input', evaluateMTX));
  [fhrCheck, stableCheck, fluidCheck].forEach(el => {
    if (el) el.addEventListener('change', evaluateMTX);
  });

  evaluateMTX();
}

/* ==========================================================================
   5. CALCULADORA DE SULFATO DE MAGNÉSIO & INTOXICAÇÃO
   ========================================================================== */
function initMagnesiumCalculator() {
  const protocolSelect = document.getElementById('mg-protocol');
  const doseOut = document.getElementById('mg-dose-plan');
  const antidoteAlert = document.getElementById('mg-antidote-alert');
  const toxSelect = document.getElementById('mg-tox-select');

  if (!protocolSelect || !doseOut) return;

  function updateProtocol() {
    const p = protocolSelect.value;
    if (p === 'zuspan') {
      doseOut.innerHTML = `
        <div class="p-3 rounded-lg bg-sky-50 dark:bg-sky-950/40 border border-sky-300 dark:border-sky-800 text-xs text-sky-900 dark:text-sky-200">
          <strong>Esquema Zuspan (Exclusivamente Endovenoso - Mais Utilizado):</strong><br>
          • <strong>Dose de Ataque:</strong> 4 g de MgSO₄ a 50% (8 mL) diluídos em 100 mL de SG 5% ou SF 0,9%, correr em 15 a 20 minutos IV.<br>
          • <strong>Dose de Manutenção:</strong> 1 g/hora IV em bomba de infusão contínua (ex: 20 mL de MgSO₄ a 50% = 10 g em 480 mL de SG 5%, correr a 50 mL/h).<br>
          • <em>Duração:</em> Manter por 24 horas após o parto ou 24 horas após a última convulsão.
        </div>
      `;
    } else if (p === 'pritchard') {
      doseOut.innerHTML = `
        <div class="p-3 rounded-lg bg-indigo-50 dark:bg-indigo-950/40 border border-indigo-300 dark:border-indigo-800 text-xs text-indigo-900 dark:text-indigo-200">
          <strong>Esquema Pritchard (Intravenoso + Intramuscular - Ideal para Transporte / Sem BIC):</strong><br>
          • <strong>Dose de Ataque:</strong> 4 g IV lento (em 20 min) + 10 g IM profunda (5 g em cada glúteo com agulha longa).<br>
          • <strong>Dose de Manutenção:</strong> 5 g IM profunda a cada 4 horas, alternando os glúteos.<br>
          • <em>Dica Prática:</em> Adicionar 1 mL de lidocaína 2% sem vasoconstritor na seringa da dose IM para reduzir a dor local.
        </div>
      `;
    } else {
      doseOut.innerHTML = `
        <div class="p-3 rounded-lg bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800 text-xs text-amber-900 dark:text-amber-200">
          <strong>Esquema Sibai:</strong><br>
          • <strong>Dose de Ataque:</strong> 6 g IV em 20 minutos.<br>
          • <strong>Dose de Manutenção:</strong> 2 g/hora IV contínuo em bomba de infusão.<br>
          • Utilizado frequentemente em protocolos norte-americanos da SMFM.
        </div>
      `;
    }
  }

  function checkToxicity() {
    if (!toxSelect || !antidoteAlert) return;
    const tox = toxSelect.value;
    if (tox === 'none') {
      antidoteAlert.classList.add('hidden');
    } else if (tox === 'hyporeflexia') {
      antidoteAlert.classList.remove('hidden');
      antidoteAlert.className = "p-4 rounded-xl bg-amber-100 dark:bg-amber-950/60 border-2 border-amber-500 text-amber-900 dark:text-amber-200 text-xs font-semibold";
      antidoteAlert.innerHTML = `
        <strong>⚠️ ALERTA DE TOXICIDADE LEVE A MODERADA (Magnesemia ~7 a 10 mEq/L):</strong><br>
        • Abolição do reflexo patelar (primeiro sinal de intoxicação magnésica).<br>
        • <strong>Conduta:</strong> SUSPENDER imediatamente a infusão de Sulfato de Magnésio! Solicitar magnesemia sérica e função renal.<br>
        • Se FR > 16 irpm e diurese mantida, apenas a suspensão da infusão pode ser suficiente sob vigilância rigorosa.
      `;
    } else {
      antidoteAlert.classList.remove('hidden');
      antidoteAlert.className = "p-4 rounded-xl bg-rose-100 dark:bg-rose-950/60 border-2 border-rose-600 text-rose-900 dark:text-rose-100 text-xs font-semibold animate-flash-red";
      antidoteAlert.innerHTML = `
        <strong>🚨 INTOXICAÇÃO GRAVE POR MAGNÉSIO COM DEPRESSÃO RESPIRATÓRIA (Magnesemia > 10 mEq/L):</strong><br>
        1. <strong>SUSPENDER</strong> imediatamente a infusão do MgSO₄.<br>
        2. <strong>ADMINISTRAR O ANTÍDOTO ESPECÍFICO:</strong><br>
           <strong class="text-sm text-red-600 dark:text-red-400">GLUCONATO DE CÁLCIO 10% — 10 mL (1 g) IV LENTO (em 3 a 5 minutos)!</strong><br>
        3. Suporte ventilatório imediato com O₂ sob máscara ou intubação se apneia.<br>
        4. O cálcio atua como antagonista competitivo fisiológico nos canais de cálcio da placa motora.
      `;
    }
  }

  protocolSelect.addEventListener('change', updateProtocol);
  if (toxSelect) toxSelect.addEventListener('change', checkToxicity);
  updateProtocol();
}

/* ==========================================================================
   6. CALCULADORA DE ANTI-HIPERTENSIVOS DE AÇÃO RÁPIDA (PA >= 160/110)
   ========================================================================== */
function initAntiHypertensiveCalculator() {
  const drugSelect = document.getElementById('ah-drug');
  const guideOut = document.getElementById('ah-guide');

  if (!drugSelect || !guideOut) return;

  function updateDrugGuide() {
    const d = drugSelect.value;
    if (d === 'hidralazina') {
      guideOut.innerHTML = `
        <div class="space-y-2">
          <div class="font-bold text-rose-700 dark:text-rose-400">Hidralazina IV (Vasodilatador Direto Arterial):</div>
          <p class="text-xs text-slate-700 dark:text-slate-300">
            • <strong>Dose Inicial:</strong> 5 mg IV lento (em 2 minutos).<br>
            • <strong>Reavaliação:</strong> Medir PA a cada 15 a 20 minutos.<br>
            • <strong>Repetição:</strong> Se PA mantida >= 160/110, administrar 5 a 10 mg IV a cada 20 minutos.<br>
            • <strong>Dose Máxima Acumulada:</strong> 20 mg.<br>
            • <em>Efeitos adversos:</em> Taquicardia reflexa, cefaleia e hipotensão brusca.
          </p>
        </div>
      `;
    } else if (d === 'labetalol') {
      guideOut.innerHTML = `
        <div class="space-y-2">
          <div class="font-bold text-sky-700 dark:text-sky-400">Labetalol IV (Bloqueador Alfa e Beta Combinado):</div>
          <p class="text-xs text-slate-700 dark:text-slate-300">
            • <strong>Dose Inicial:</strong> 20 mg IV em bolus lento (em 2 minutos).<br>
            • <strong>Reavaliação:</strong> Medir PA após 10 a 20 minutos.<br>
            • <strong>Escalonamento de Doses:</strong> Se persistir hipertensa, dobrar a dose: 40 mg IV, depois 80 mg IV a cada 10-20 min.<br>
            • <strong>Dose Máxima Acumulada:</strong> 220 mg a 300 mg.<br>
            • <em>Contraindicações:</em> Asma grave, insuficiência cardíaca e bloqueio atrioventricular (BAV).
          </p>
        </div>
      `;
    } else {
      guideOut.innerHTML = `
        <div class="space-y-2">
          <div class="font-bold text-emerald-700 dark:text-emerald-400">Nifedipina Oral de Liberação Imediata (Bloqueador de Canal de Ca):</div>
          <p class="text-xs text-slate-700 dark:text-slate-300">
            • <strong>Dose Inicial:</strong> 10 a 20 mg VIA ORAL (comprimido deglutido inteiro).<br>
            • <strong>AVISO CRÍTICO:</strong> NUNCA mastigar ou administrar por via sublingual (risco de queda pressórica catastrófica e bradicardia fetal reflexa!).<br>
            • <strong>Reavaliação:</strong> Medir PA a cada 20 a 30 minutos.<br>
            • <strong>Repetição:</strong> Pode-se repetir 10 a 20 mg VO após 20 a 30 min (máx: 60 mg/dia).<br>
            • Excelente para situações sem acesso venoso imediato disponível.
          </p>
        </div>
      `;
    }
  }

  drugSelect.addEventListener('change', updateDrugGuide);
  updateDrugGuide();
}

/* ==========================================================================
   7. CLASSIFICADOR DA SÍNDROME HELLP
   ========================================================================== */
function initHELLPClassifier() {
  const pltInput = document.getElementById('hellp-plt');
  const ldhInput = document.getElementById('hellp-ldh');
  const astInput = document.getElementById('hellp-ast');
  const resOut = document.getElementById('hellp-result');

  if (!pltInput || !ldhInput || !astInput || !resOut) return;

  function classify() {
    const plt = parseFloat(pltInput.value) || 0;
    const ldh = parseFloat(ldhInput.value) || 0;
    const ast = parseFloat(astInput.value) || 0;

    const hasHemolysis = ldh >= 600;
    const hasLiver = ast >= 70;
    const hasThrombo = plt < 100000;

    const count = (hasHemolysis ? 1 : 0) + (hasLiver ? 1 : 0) + (hasThrombo ? 1 : 0);

    let status = "";
    let colorClass = "";
    let desc = "";

    if (count === 3) {
      status = "Síndrome HELLP Completa (Critérios de Tennessee Preenchidos)";
      colorClass = "bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-200 border-rose-500";
      
      let mississippi = "Classe 2 (Plaquetas 50.000 a 100.000)";
      if (plt < 50000) mississippi = "Classe 1 - Gravíssima (Plaquetas < 50.000 / Mortalidade elevada)";
      else if (plt >= 100000 && plt <= 150000) mississippi = "Classe 3 (Plaquetas 100.000 a 150.000)";

      desc = `
        <strong>Emergência Obstétrica Grave:</strong><br>
        • Classificação de Mississippi: <strong>${mississippi}</strong>.<br>
        • <strong>Conduta Obrigatória:</strong><br>
          1. Sulfato de Magnésio profilático contra eclâmpsia imediato.<br>
          2. Controle anti-hipertensivo se PAS >= 160 ou PAD >= 110.<br>
          3. <strong>Indicação de Parto:</strong> A única cura definitiva é o nascimento. Se >= 34 semanas, interrupção imediata após estabilização. Se < 34 semanas, avaliar corticoide se estabilidade permitir, sem protelar em casos graves.
      `;
    } else if (count >= 1) {
      status = "Síndrome HELLP Parcial / Incompleta (ELLP ou HEL)";
      colorClass = "bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-200 border-amber-500";
      desc = `
        A paciente preenche ${count} dos 3 critérios clássicos. Apresenta risco iminente de progressão rápida para HELLP completa. Repetir exames laboratoriais a cada 6 a 12 horas e manter sob vigilância de alta dependência obstétrica.
      `;
    } else {
      status = "Sem Critérios para Síndrome HELLP no Momento";
      colorClass = "bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200 border-emerald-500";
      desc = "Parâmetros laboratoriais abaixo dos pontos de corte para HELLP (Plaquetas >= 100k, LDH < 600, AST < 70 U/L).";
    }

    resOut.className = `p-4 rounded-xl border-2 text-xs ${colorClass}`;
    resOut.innerHTML = `
      <div class="font-black text-sm mb-1">${status}</div>
      <div>${desc}</div>
    `;
  }

  [pltInput, ldhInput, astInput].forEach(el => el.addEventListener('input', classify));
  classify();
}

/* ==========================================================================
   8. SIMULADOR DO ALGORITMO HELPERR (DISTÓCIA DE OMBROS)
   ========================================================================== */
function initHELPERRSimulator() {
  const steps = [
    {
      letter: "H",
      name: "Help (Pedir Ajuda)",
      action: "Chamar obstetra adicional, anestesista, equipe de neonatologia e enfermagem. Informar a hora exata da saída da cabeça fetal.",
      prohibition: "NUNCA realizar tração excessiva na cabeça ou torção cervical!"
    },
    {
      letter: "E",
      name: "Evaluate for Episiotomy (Avaliar Episiotomia)",
      action: "A distócia é óssea, não de partes moles. Episiotomia só é necessária se houver necessidade de espaço para manobras internas manuais.",
      prohibition: "Episiotomia rotineira NÃO desimpacta o ombro anterior!"
    },
    {
      letter: "L",
      name: "Legs (Manobra de McRoberts)",
      action: "Hiperflexão e abdução máxima das coxas da parturiente contra o abdômen. Achata a curvatura lombossacra e gira a sínfise púbica cefalicamente em até 10 mm (sucesso em até 70% isolada!).",
      prohibition: "Manter tração suave no eixo fetal durante a manobra."
    },
    {
      letter: "P",
      name: "Pressure (Pressão Suprapúbica - Rubin I)",
      action: "Pressão contínua ou pulsátil realizada pelo assistente com a palma da mão na região suprapúbica, no dorso do ombro anterior, para aduzir os ombros e reduzir o diâmetro biacromial.",
      prohibition: "⚠️ PROIBIÇÃO CATEGÓRICA: Manobra de Kristeller (pressão fúndica) é formalmente PROIBIDA pelo risco de rotura uterina e compressão fetal!"
    },
    {
      letter: "E",
      name: "Enter (Manobras Internas: Rubin II & Woods)",
      action: "Dedos do examinador introduzidos na vagina contra a face posterior do ombro anterior para empurrá-lo em direção ao tórax (Rubin II), ou manobra de Parafuso de Woods (gira o ombro posterior em 180°).",
      prohibition: "Não forçar rotação contra a resistência óssea."
    },
    {
      letter: "R",
      name: "Remove the Posterior Arm (Extração do Braço Posterior)",
      action: "Introduzir a mão na concavidade sacra, localizar o cotovelo posterior, flexionar o antebraço sobre o peito e tracionar a mão para fora da vulva. Reduz o diâmetro de 12 para 9,5 cm.",
      prohibition: "Risco calculado de fratura de clavícula/úmero (fratura controlada é melhor que asfixia grave)."
    },
    {
      letter: "R",
      name: "Roll the Patient (Posição de Quatro Apoios / Gaskin)",
      action: "Colocar a parturiente de quatro apoios (mãos e joelhos). A gravidade e a mudança nos diâmetros pélvicos costumam liberar o ombro impactado.",
      prohibition: "Último recurso de 3ª linha: Manobra de Zavanelli (reintrodução da cabeça e cesárea) ou Sinfisiotomia."
    }
  ];

  let currentStep = 0;
  let timerInterval = null;
  let seconds = 0;

  const letterBadge = document.getElementById('helperr-letter');
  const nameOut = document.getElementById('helperr-name');
  const actionOut = document.getElementById('helperr-action');
  const prohibOut = document.getElementById('helperr-prohibition');
  const prevBtn = document.getElementById('helperr-prev');
  const nextBtn = document.getElementById('helperr-next');
  const timerOut = document.getElementById('helperr-timer');
  const timerBtn = document.getElementById('helperr-timer-toggle');

  if (!letterBadge || !actionOut) return;

  function renderStep() {
    const s = steps[currentStep];
    letterBadge.textContent = s.letter;
    nameOut.textContent = `${currentStep + 1}. ${s.name}`;
    actionOut.textContent = s.action;
    prohibOut.textContent = s.prohibition;

    if (prevBtn) prevBtn.disabled = currentStep === 0;
    if (nextBtn) nextBtn.disabled = currentStep === steps.length - 1;
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentStep > 0) {
        currentStep--;
        renderStep();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (currentStep < steps.length - 1) {
        currentStep++;
        renderStep();
      }
    });
  }

  if (timerBtn && timerOut) {
    timerBtn.addEventListener('click', () => {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
        timerBtn.textContent = "Iniciar Cronômetro";
        timerBtn.className = "px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold";
      } else {
        seconds = 0;
        timerInterval = setInterval(() => {
          seconds++;
          const m = String(Math.floor(seconds / 60)).padStart(2, '0');
          const sec = String(seconds % 60).padStart(2, '0');
          timerOut.textContent = `${m}:${sec}`;
          if (seconds >= 300) {
            timerOut.className = "text-xl font-black text-rose-600 animate-pulse";
          }
        }, 1000);
        timerBtn.textContent = "Pausar Cronômetro";
        timerBtn.className = "px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold";
      }
    });
  }

  renderStep();
}

/* ==========================================================================
   9. RASTREADOR DO BUNDLE DA SEPSE MATERNA NA 1ª HORA
   ========================================================================== */
function initSepsisBundleTracker() {
  const checkboxes = document.querySelectorAll('.sepsis-check');
  const progressText = document.getElementById('sepsis-progress-text');
  const progressBar = document.getElementById('sepsis-progress-bar');
  const alertSuccess = document.getElementById('sepsis-complete-alert');

  if (checkboxes.length === 0 || !progressBar) return;

  function update() {
    let checked = 0;
    checkboxes.forEach(c => {
      if (c.checked) checked++;
    });

    const pct = Math.round((checked / checkboxes.length) * 100);
    progressBar.style.width = `${pct}%`;
    if (progressText) progressText.textContent = `${checked} de ${checkboxes.length} itens cumpridos (${pct}%)`;

    if (alertSuccess) {
      if (checked === checkboxes.length) {
        alertSuccess.classList.remove('hidden');
      } else {
        alertSuccess.classList.add('hidden');
      }
    }
  }

  checkboxes.forEach(c => c.addEventListener('change', update));
  update();
}

/* ==========================================================================
   10. FLASHCARDS 3D INTERATIVOS (MEMORIZAÇÃO ATIVA)
   ========================================================================== */
const FLASHCARDS_DATA = [
  {
    category: "Módulo 29: Abordagem Inicial",
    q: "Qual o gatilho formal do Índice de Choque (IC = FC / PAS) para iniciar o Protocolo de Transfusão Maciça (PTM) na hemorragia obstétrica?",
    a: "Índice de Choque >= 1,4. Indica hemorragia maciça com perda > 30% da volemia. Iniciar PTM em razão equilibrada 1:1:1 (Hemácias : Plasma : Plaquetas) + Ácido Tranexâmico 1g IV imediato + Crioprecipitado se Fibrinogênio < 200 mg/dL."
  },
  {
    category: "Módulo 29: Cesárea Perimortem",
    q: "Quais são as regras de ouro de tempo e local da histerotomia de ressuscitação (cesárea perimortem)?",
    a: "Regra dos 4 a 5 minutos: incisão no 4º minuto de PCR e nascimento até o 5º minuto. Realizar NO LOCAL da parada (sala de parto/leito), SEM transportar para o bloco cirúrgico. Se gestação >= 20 semanas."
  },
  {
    category: "Módulo 30: Abortamento",
    q: "Qual a diferença semiológica crucial entre Ameaça de Abortamento e Abortamento Inevitável?",
    a: "O colo uterino! Na Ameaça de Abortamento o orifício interno está FECHADO e o embrião está vivo. No Abortamento Inevitável o colo está ABERTO/DILATADO, com cólicas progressivas e perda gestacional irreversível."
  },
  {
    category: "Módulo 31: Gravidez Ectópica",
    q: "Quais os 4 critérios clínicos mais estritos para elegibilidade ao tratamento com Metotrexato (MTX 50 mg/m²)?",
    a: "1. Estabilidade hemodinâmica;\n2. beta-hCG sérico < 5.000 mUI/mL;\n3. Massa anexial < 3,5 cm;\n4. Ausência de BCF embrionário."
  },
  {
    category: "Módulo 32: Doença Trofoblástica",
    q: "Qual a diferença citogenética e histopatológica entre Mola Hidatiforme Completa e Parcial?",
    a: "Mola Completa é 46,XX diploide 100% paterna (óvulo anucleado), sem feto, degeneração hidrópica difusa e hCG > 100k. Mola Parcial é 69,XXY triploide (dispermia), com feto malformado e hidropisia focal."
  },
  {
    category: "Módulo 33: Hemorragias 2ª Metade",
    q: "Como diferenciar o sangramento do DPP (Descolamento Prematuro de Placenta) da Placenta Prévia?",
    a: "DPP: Sangramento escuro, DOLOROSO, com hipertonia uterina (útero lenhoso) e sofrimento fetal. Placenta Prévia: Sangramento vermelho vivo, INDOLOR, repetitivo, útero relaxado e feto sem sofrimento agudo inicial."
  },
  {
    category: "Módulo 33: Acretismo Placentário",
    q: "Quais são os 3 graus do Espectro do Acretismo Placentário (PAS) segundo a profundidade de invasão?",
    a: "1. Placenta Acreta (aderência à superfície do miométrio);\n2. Placenta Increta (invasão profunda no miométrio);\n3. Placenta Percreta (invasão que ultrapassa a serosa e atinge órgãos vizinhos, como a bexiga)."
  },
  {
    category: "Módulo 34: Pré-Eclâmpsia",
    q: "Qual o antídoto de escolha para intoxicação por Sulfato de Magnésio e como administrá-lo?",
    a: "Gluconato de Cálcio 10%, administrar 10 mL (1 g) por via intravenosa lenta em 3 a 5 minutos. Atua antagonizando competitivamente os efeitos do magnésio na placa motora e miocárdio."
  },
  {
    category: "Módulo 35: Síndrome HELLP",
    q: "Quais os 3 critérios diagnósticos laboratoriais da Síndrome HELLP pelo critério de Tennessee?",
    a: "1. H (Hemólise): LDH >= 600 U/L e esquizócitos em sangue periférico;\n2. EL (Enzimas Hepáticas): AST/TGO >= 70 U/L;\n3. LP (Plaquetopenia): Plaquetas < 100.000/mm³."
  },
  {
    category: "Módulo 37: Prolapso de Cordão",
    q: "Qual a primeira conduta física IMEDIATA realizada pela equipe ao identificar prolapso franco de cordão?",
    a: "Elevação manual da apresentação fetal por toque vaginal sustentado (afastando a cabeça do cordão) + posição genupeitoral materna, preparando cesárea de emergência absoluta sob código vermelho!"
  },
  {
    category: "Módulo 38: Distócia de Ombros",
    q: "Por que a manobra de Kristeller (pressão fúndica) é formalmente proibida na distócia de ombros?",
    a: "Porque empurra ainda mais o ombro anterior contra a sínfise púbica, aumentando o impacto ósseo e causando rotura uterina, asfixia neonatal grave e lesão irreversível do plexo braquial (paralisia de Erb-Duchenne)!"
  },
  {
    category: "Módulo 39: Embolia por Líquido Amniótico",
    q: "Qual a tríade clínica clássica da Embolia por Líquido Amniótico (ELA)?",
    a: "1. Colapso cardiovascular súbito (choque cardiogênico de VD);\n2. Insuficiência respiratória aguda e hipóxia profunda;\n3. Coagulopatia de consumo fulminante (CIVD com sangramento incoercível)."
  }
];

function initFlashcards() {
  let currentIndex = 0;
  const card = document.getElementById('flashcard');
  const catOut = document.getElementById('fc-category');
  const qOut = document.getElementById('fc-question');
  const aOut = document.getElementById('fc-answer');
  const countOut = document.getElementById('fc-counter');
  const prevBtn = document.getElementById('fc-prev');
  const nextBtn = document.getElementById('fc-next');
  const flipBtn = document.getElementById('fc-flip');

  if (!card || !qOut || !aOut) return;

  function renderCard() {
    card.classList.remove('card-flipped');
    const item = FLASHCARDS_DATA[currentIndex];
    catOut.textContent = item.category;
    qOut.textContent = item.q;
    aOut.innerHTML = item.a.replace(/\n/g, '<br>');
    if (countOut) countOut.textContent = `${currentIndex + 1} de ${FLASHCARDS_DATA.length}`;
  }

  card.addEventListener('click', () => {
    card.classList.toggle('card-flipped');
  });

  if (flipBtn) {
    flipBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      card.classList.toggle('card-flipped');
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIndex > 0) {
        currentIndex--;
        renderCard();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIndex < FLASHCARDS_DATA.length - 1) {
        currentIndex++;
        renderCard();
      }
    });
  }

  renderCard();
}

/* ==========================================================================
   11. SIMULADO INTERATIVO COM 14 VINHETAS CLÍNICAS (ESTILO USMLE / RESIDÊNCIA)
   ========================================================================== */
const QUIZ_DATA = [
  {
    id: 1,
    stem: "Mulher de 28 anos, DUM há 7 semanas, é trazida à emergência com dor intensa em fossa ilíaca direita e dor referida em ombro direito. Exame físico: PA 82/50 mmHg, FC 128 bpm, sudorese fria e abdômen peritoneal. Teste rápido de urina para beta-hCG é positivo. Ultrassom point-of-care (POCUS) revela útero vazio com espessamento endometrial e líquido livre anecoico abundante no espaço de Morrison. Qual é a conduta imediata mais apropriada?",
    options: [
      "Prescrever Metotrexato 50 mg/m² IM em dose única com controle de beta-hCG em 48 horas",
      "Solicitar dosagem sérica quantitativa de beta-hCG e ultrassonografia transvaginal formal do bloco",
      "Laparotomia ou laparoscopia de emergência imediata concomitante à ressuscitação volêmica e transfusão",
      "Realizar aspiração manual intrauterina (AMIU) para descartar abortamento incompleto"
    ],
    correct: 2,
    explanation: "Trata-se de choque hipovolêmico por Gravidez Ectópica Rota com hemoperitônio maciço (dor no ombro por irritação do nervo frênico - sinal de Lafond/Kehr). Diante de instabilidade hemodinâmica, não há indicação para MTX ou ultrassom formal ambulatorial. A indicação é cirurgia de emergência imediata (laparotomia/laparoscopia) e ressuscitação hemoterápica."
  },
  {
    id: 2,
    stem: "Mulher de 31 anos, estável, beta-hCG 2.800 mUI/mL, massa anexial íntegra de 2,5 cm sem BCF ao Doppler, sem líquido livre em pelve. Hemograma, creatinina e transaminases normais. Deseja preservar fertilidade. Conduta?",
    options: [
      "Salpingectomia total bilateral laparoscópica",
      "Metotrexato 50 mg/m² IM dose única, com dosagens de beta-hCG no D4 e D7",
      "Curetagem uterina aspirativa para esvaziamento profilático",
      "Conduta expectante sem medicamentos"
    ],
    correct: 1,
    explanation: "A paciente preenche todos os critérios de elegibilidade para Metotrexato (MTX): paciente estável, beta-hCG < 5.000 mUI/mL, massa < 3,5 cm, sem BCF e sem hemoperitônio. O seguimento exige dosagem de beta-hCG nos dias 4 e 7 pós-administração (meta: queda >= 15%)."
  },
  {
    id: 3,
    stem: "Primigesta de 19 anos, 16 semanas, sangramento vaginal em 'suco de ameixa', vômitos incoercíveis, PA 150/100 mmHg, fundo uterino palpável ao nível da cicatriz umbilical (compatível com 22 semanas). beta-hCG sérico > 280.000 mUI/mL. Ultrassom mostra imagem em 'flocos de neve' ou 'tempestade de neve' sem concepto. Diagnóstico e conduta inicial?",
    options: [
      "Ameaça de abortamento; prescrever repouso e dydrogesterona",
      "Mola hidatiforme completa; solicitar radiografia de tórax e realizar vácuo-aspiração uterina",
      "Gravidez ectópica cornual; laparotomia exploradora imediata",
      "Hipertensão gestacional transitória; hidralazina oral e alta hospitalar"
    ],
    correct: 1,
    explanation: "Quadro clássico de Mola Hidatiforme Completa: sangramento precoce, útero desproporcionalmente grande para a IG, hiperêmese grave, pré-eclâmpsia antes de 20 semanas e beta-hCG astronômico. A conduta é estadiamento inicial com radiografia de tórax (pesquisa de metástases) e esvaziamento por vácuo-aspiração (AMIU ou elétrica), evitando curetagem cortante inicial."
  },
  {
    id: 4,
    stem: "G3P2 (ambos os partos por cesariana anterior), 32 semanas de gestação, comparece ao pronto-socorro com sangramento vaginal vermelho vivo moderado, de início súbito, completamente indolor. Ao exame: útero normotônico e indolor, BCF 140 bpm reativo. O que NUNCA deve ser realizado neste momento e o que deve ser pesquisado?",
    options: [
      "Nunca fazer ultrassom abdominal; pesquisar incompetência cervical",
      "Nunca realizar toque vaginal; realizar ultrassom transvaginal para placenta prévia e pesquisar espectro de acretismo placentário (PAS)",
      "Nunca administrar corticoide antenatal; pesquisar rotura uterina",
      "Nunca colher hemograma; indicar cesárea imediata sem avaliação"
    ],
    correct: 1,
    explanation: "No sangramento indolor da 2ª metade, o TOQUE VAGINAL É FORMALMENTE CONTRAINDICADO até afastar placenta prévia, pois pode lacerar os cotilédones e deflagrar hemorragia catastrófica. Como a paciente tem 2 cesáreas prévias e suspeita de placenta prévia, há risco de acretismo placentário (PAS ~11%), exigindo ultrassom/Doppler especializado."
  },
  {
    id: 5,
    stem: "Gestante de 35 semanas, tabagista e usuária de cocaína, dá entrada com dor abdominal súbita em cólica de forte intensidade, sangramento vaginal escuro moderado e útero hipertonicamente rígido ('em tábua'). Ausculta fetal revela bradicardia sustentada de 90 bpm. Conduta indicada?",
    options: [
      "Prescrever nifedipina oral para inibir contrações e aguardar 48h para sulfato de magnésio",
      "Realizar amniorrexe artificial e induzir parto normal com ocitocina em altas doses",
      "Descolamento prematuro de placenta (DPP) com feto vivo e sofrimento agudo: estabilização materna e cesárea de emergência imediata",
      "Solicitar ressonância magnética pélvica para confirmar o diagnóstico antes de intervir"
    ],
    correct: 2,
    explanation: "Trata-se de Descolamento Prematuro de Placenta (DPP) clássico com feto vivo e sofrimento fetal agudo (bradicardia 90 bpm). O diagnóstico de DPP é essencialmente CLÍNICO. A presença de feto vivo com bradicardia e sofrimento exige cesariana de emergência imediata concomitante com reserva de sangue e ácido tranexâmico."
  },
  {
    id: 6,
    stem: "Primigesta de 37 semanas apresenta PA 168/112 mmHg confirmada em duas medidas com intervalo de 15 minutos, associada a cefaleia holocraniana intensa e escotomas cintilantes. Primeiras medidas de emergência?",
    options: [
      "Administrar diazepam 10 mg IV e liberar para acompanhamento pré-natal ambulatorial",
      "Prescrever sulfato de magnésio para neuroproteção/prevenção de eclâmpsia e anti-hipertensivo de ação rápida (hidralazina IV ou labetalol IV ou nifedipina VO), seguido de parto",
      "Aguardar início espontâneo do trabalho de parto sem intervir na pressão arterial",
      "Indicar sulfato de magnésio apenas se houver convulsão confirmada"
    ],
    correct: 1,
    explanation: "Quadro de Pré-Eclâmpsia com Sinais de Gravidade (PA >= 160/110 + sintomas cerebrais/visuais iminentes de eclâmpsia). A conduta mandatória é: 1. Sulfato de Magnésio imediatamente para profilaxia de convulsões; 2. Anti-hipertensivo de ação rápida para controle pressórico (reduzir 15-25% da PA); 3. Parto (idade gestacional >= 34 semanas)."
  },
  {
    id: 7,
    stem: "Paciente em uso de Sulfato de Magnésio contínuo há 10 horas para eclâmpsia evolui sonolenta, com frequência respiratória de 9 irpm, reflexos patelares abolidos bilateralmente e diurese de 15 mL/h nas últimas 2 horas. Conduta imediata?",
    options: [
      "Aumentar a infusão de magnésio para manter níveis terapêuticos",
      "Suspender o sulfato de magnésio e administrar gluconato de cálcio a 10% (10 mL IV lento em 3 a 5 minutos)",
      "Administrar furosemida IV e manter o magnésio",
      "Administrar naloxona 0,4 mg IV"
    ],
    correct: 1,
    explanation: "Intoxicação grave por Sulfato de Magnésio manifestada por hiporreflexia patelar, bradipneia grave (< 12 irpm) e oligúria (o magnésio é excretado exclusivamente pelos rins). A conduta salvadora imediata é: SUSPENDER a infusão e administrar o antídoto: GLUCONATO DE CÁLCIO 10% 10 mL IV lento (1 g)."
  },
  {
    id: 8,
    stem: "Gestante de 33 semanas queixa-se de mal-estar, náuseas e dor em hipocôndrio direito. PA 138/88 mmHg. Exames: Plaquetas 72.000/mm³, AST 240 U/L, LDH 890 U/L e presença de esquizócitos no esfregaço de sangue periférico. Diagnóstico mais provável?",
    options: [
      "Colestase intra-hepática da gravidez",
      "Síndrome HELLP (mesmo com PA < 140/90 mmHg)",
      "Apendicite aguda flegmonosa",
      "Esteatose hepática aguda com falência renal"
    ],
    correct: 1,
    explanation: "Síndrome HELLP! Até 15% a 20% dos casos de Síndrome HELLP ocorrem em pacientes normotensas ou com hipertensão apenas limítrofe. A tríade de microangiopatia hemolítica (esquizócitos, LDH elevado), disfunção hepática (AST elevada) e plaquetopenia (< 100k) confirma o diagnóstico."
  },
  {
    id: 9,
    stem: "Gestante de 34 semanas, com dor epigástrica, icterícia, náuseas e sonolência. Exames laboratoriais mostram hipoglicemia severa (glicemia 42 mg/dL), coagulopatia com INR 2,5, hiperamonemia e plaquetas de 135.000/mm³. Qual a suspeita diagnóstica principal e o teste neonatal recomendado?",
    options: [
      "Síndrome HELLP clássica; teste do pezinho ampliado normal",
      "Esteatose Hepática Aguda da Gravidez (AFLP); testar o recém-nascido para deficiência de LCHAD",
      "Hepatite Viral fulminante por vírus B; vacinar com 3 doses imediatas",
      "Púrpura Trombocitopênica Trombótica (PTT); plasmaférese sem interrupção da gravidez"
    ],
    correct: 1,
    explanation: "Esteatose Hepática Aguda da Gravidez (AFLP / Critérios de Swansea). Caracteriza-se por disfunção hepática fulminante com hipoglicemia grave, hiperamonemia e coagulopatia acentuada (diferente da HELLP onde a hipoglicemia e coagulopatia severa são raras precocemente). Está associada à mutação fetal na enzima LCHAD (cadeia longa de hidroxiacil-CoA desidrogenase), devendo o neonato ser testado!"
  },
  {
    id: 10,
    stem: "Multípara em trabalho de parto, 39 semanas, polidrâmnio, apresentação cefálica alta (-3 de De Lee). Imediatamente após a rotura espontânea de membranas, a frequência cardíaca fetal cai bruscamente de 145 para 70 bpm. Ao toque vaginal, palpa-se uma estrutura pulsátil à frente da apresentação fetal. Conduta imediata?",
    options: [
      "Empurrar o cordão para dentro do útero e prosseguir com parto normal",
      "Elevar manualmente a apresentação fetal por via vaginal, colocar em posição genupeitoral e indicar cesárea de emergência absoluta",
      "Iniciar infusão de ocitocina para acelerar a descida fetal",
      "Aguardar 30 minutos para confirmação da cardiotocografia"
    ],
    correct: 1,
    explanation: "Prolapso de cordão umbilical! A apresentação comprime o cordão contra a pelve materna, gerando hipóxia e bradicardia severa. A conduta salvadora imediata é: mão na vagina ELEVANDO a apresentação fetal para aliviar a compressão do cordão, colocar em posição genupeitoral (ou Trendelenburg) e correr para cesárea de emergência sob código vermelho."
  },
  {
    id: 11,
    stem: "Durante parto vaginal de concepto com peso estimado de 4.200 g de mãe diabética, ocorre o desprendimento do polo cefálico, que imediatamente retrai-se contra o períneo materno ('sinal da tartaruga'). A tração suave no eixo fetal não promove o desprendimento dos ombros. Qual é a primeira manobra combinada a ser executada?",
    options: [
      "Manobra de Kristeller com pressão enérgica no fundo uterino",
      "Pedir ajuda imediata + Manobra de McRoberts (hiperflexão das coxas) associada à pressão suprapúbica (Rubin I)",
      "Fratura intencional de fêmur fetal",
      "Manobra de Zavanelli como primeira linha de conduta"
    ],
    correct: 1,
    explanation: "Distócia de ombros com sinal da tartaruga! O primeiro passo do algoritmo HELPERR é pedir ajuda e executar a Manobra de McRoberts (hiperflexão das coxas) com pressão suprapúbica simultânea (Rubin I). A manobra de Kristeller (pressão no fundo uterino) é estritamente proibida."
  },
  {
    id: 12,
    stem: "Puérpera em pós-parto imediato de cesariana apresenta subitamente agitação, dispneia grave, cianose, dessaturação para 74% em ar ambiente, hipotensão com PA 60/30 mmHg, seguida de hemorragia maciça incoercível em lençol na incisão cirúrgica e sítios venosos. Fibrinogênio sérico dosado é de 70 mg/dL. Diagnóstico e conduta?",
    options: [
      "Atonia uterina isolada; massagem uterina e misoprostol retal",
      "Embolia por líquido amniótico (ELA); suporte ventilatório, noradrenalina/inotrópico e protocolo de transfusão maciça 1:1:1 com crioprecipitado e ácido tranexâmico",
      "Embolia pulmonar por trombo venoso; trombólise com alteplase imediata",
      "Pneumotórax hipertensivo; drenagem torácica em selo d'água"
    ],
    correct: 1,
    explanation: "Quadro clássico de Embolia por Líquido Amniótico (ELA / Síndrome Anafilactoide da Gestação). Manifesta-se pela tríade catastrófica de colapso cardiovascular súbito, insuficiência respiratória hipoxêmica grave e coagulopatia de consumo fulminante (CIVD com fibrinogênio < 100 mg/dL). Tratamento: suporte intensivo hemodinâmico e transfusão maciça precoce com crioprecipitado/fibrinogênio e ácido tranexâmico."
  },
  {
    id: 13,
    stem: "Puérpera no 4º dia pós-cesárea por trabalho de parto prolongado evolui com febre de 39,2 °C, calafrios, taquicardia, dor à palpação do corpo uterino (subinvoluído) e lóquios fétidos purulentos. Qual é o tratamento antimicrobiano de primeira escolha no SUS e na literatura internacional?",
    options: [
      "Amoxicilina oral 500 mg de 8/8h por 7 dias em domicílio",
      "Clindamicina 900 mg IV a cada 8h + Gentamicina 5 mg/kg IV a cada 24h até 24 a 48h afebril e assintomática",
      "Ciprofloxacino oral associado a metronidazol",
      "Azitromicina 500 mg dose única"
    ],
    correct: 1,
    explanation: "Endometrite pós-parto! Infecção polimicrobiana (flora vaginal ascendente anaeróbia e aeróbia). O esquema padrão-ouro intravenoso em ambiente hospitalar é Clindamicina (cobertura potente anaeróbia e Gram-positiva) + Gentamicina (Gram-negativos entéricos), mantido até a paciente completar 24 a 48 horas afebril e assintomática."
  },
  {
    id: 14,
    stem: "Mulher de 24 anos dá entrada com febre de 39,5 °C, calafrios, taquipneia (FR 28 irpm), PA 80/45 mmHg, útero muito doloroso e sangramento vaginal com secreção francamente purulenta e fétida, 3 dias após procedimento clandestino de interrupção da gravidez. Lactato sérico de 4,8 mmol/L. Conduta de emergência?",
    options: [
      "Prescrever analgésicos e liberar com consulta ginecológica eletiva",
      "Pacote da sepse da 1ª hora (culturas, ressuscitação volêmica 30 mL/kg, noradrenalina se hipotensão refratária, ATB de largo espectro IV) + esvaziamento uterino imediato pós-antibiótico",
      "Aguardar 48 horas de antibiótico antes de qualquer manipulação uterina",
      "Realizar curetagem imediatamente sem coletar exames ou iniciar antibiótico"
    ],
    correct: 1,
    explanation: "Abortamento séptico com choque séptico! Conduta prioritária na primeira hora: bundle da sepse (coleta de lactato e hemoculturas, antibióticos de amplo espectro IV como Clindamicina + Gentamicina + Ampicilina, expansão volêmica de 30 mL/kg de Ringer Lactato e noradrenalina precoce se PAM < 65) associado a esvaziamento uterino por AMIU/aspiração rápida pós-início da antibioticoterapia para controle da fonte infecciosa."
  }
];

function initQuiz() {
  const container = document.getElementById('quiz-container');
  const scoreBadge = document.getElementById('quiz-score-badge');
  if (!container) return;

  let userAnswers = {};

  function renderQuiz() {
    container.innerHTML = "";

    QUIZ_DATA.forEach((q, idx) => {
      const card = document.createElement('div');
      card.className = "p-6 rounded-2xl glass-panel space-y-4 border border-slate-200 dark:border-slate-800 transition-all";
      card.id = `quiz-q-${q.id}`;

      const answered = userAnswers[q.id] !== undefined;
      const selected = userAnswers[q.id];
      const isCorrect = selected === q.correct;

      let optionsHtml = "";
      q.options.forEach((opt, optIdx) => {
        let optClasses = "p-3.5 rounded-xl border text-xs font-medium cursor-pointer transition-all flex items-start gap-3 ";
        
        if (!answered) {
          optClasses += "border-slate-200 dark:border-slate-800 hover:border-sky-500 hover:bg-sky-50/50 dark:hover:bg-slate-900/50 text-slate-800 dark:text-slate-200";
        } else {
          if (optIdx === q.correct) {
            optClasses += "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 font-bold";
          } else if (optIdx === selected) {
            optClasses += "border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-900 dark:text-rose-200";
          } else {
            optClasses += "border-slate-200 dark:border-slate-800 opacity-60 text-slate-600 dark:text-slate-400";
          }
        }

        const letter = String.fromCharCode(65 + optIdx);
        optionsHtml += `
          <div class="${optClasses}" data-qid="${q.id}" data-opt="${optIdx}">
            <span class="w-5 h-5 rounded-md bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold flex items-center justify-center text-[10px] flex-shrink-0">${letter}</span>
            <span class="flex-1">${opt}</span>
          </div>
        `;
      });

      let feedbackHtml = "";
      if (answered) {
        feedbackHtml = `
          <div class="mt-4 p-4 rounded-xl text-xs ${isCorrect ? 'bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-300 text-emerald-900 dark:text-emerald-200' : 'bg-rose-50 dark:bg-rose-950/50 border border-rose-300 text-rose-900 dark:text-rose-200'}">
            <div class="font-bold mb-1 flex items-center gap-1.5">
              ${isCorrect ? '✓ RESPOSTA CORRETA' : '✗ RESPOSTA INCORRETA'}
            </div>
            <p class="leading-relaxed text-slate-700 dark:text-slate-300">${q.explanation}</p>
          </div>
        `;
      }

      card.innerHTML = `
        <div class="flex items-center justify-between">
          <span class="px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300">
            Questão ${idx + 1} de ${QUIZ_DATA.length}
          </span>
          <span class="text-xs font-semibold text-slate-400">USMLE / Residência Médica</span>
        </div>
        <p class="text-xs sm:text-sm font-semibold text-slate-900 dark:text-white leading-relaxed">
          ${q.stem}
        </p>
        <div class="space-y-2 pt-1">
          ${optionsHtml}
        </div>
        ${feedbackHtml}
      `;

      container.appendChild(card);
    });

    container.querySelectorAll('[data-opt]').forEach(item => {
      item.addEventListener('click', () => {
        const qid = parseInt(item.getAttribute('data-qid'));
        const opt = parseInt(item.getAttribute('data-opt'));
        if (userAnswers[qid] === undefined) {
          userAnswers[qid] = opt;
          updateScore();
          renderQuiz();
        }
      });
    });
  }

  function updateScore() {
    let correct = 0;
    const answeredCount = Object.keys(userAnswers).length;
    QUIZ_DATA.forEach(q => {
      if (userAnswers[q.id] === q.correct) correct++;
    });

    if (scoreBadge) {
      scoreBadge.textContent = `${correct} / ${QUIZ_DATA.length} Corretas (${Math.round((correct / QUIZ_DATA.length) * 100)}%)`;
    }
  }

  renderQuiz();
}

/* ==========================================================================
   12. LIGHTBOX HD INTERATIVO
   ========================================================================== */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-image');
  const title = document.getElementById('lightbox-title');
  const closeBtn = document.getElementById('lightbox-close');
  const zoomInBtn = document.getElementById('lightbox-zoom-in');
  const zoomOutBtn = document.getElementById('lightbox-zoom-out');
  const resetBtn = document.getElementById('lightbox-reset');

  if (!modal || !img) return;

  let scale = 1;
  let isDragging = false;
  let startX = 0, startY = 0;
  let translateX = 0, translateY = 0;

  function updateTransform() {
    img.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
  }

  function resetZoom() {
    scale = 1;
    translateX = 0;
    translateY = 0;
    updateTransform();
  }

  function openLightbox(src, caption) {
    img.src = src;
    if (title) title.textContent = caption || "Infográfico Médico em Alta Resolução";
    resetZoom();
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    resetZoom();
  }

  document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.addEventListener('click', () => {
      const src = el.getAttribute('data-lightbox') || el.getAttribute('src');
      const caption = el.getAttribute('data-title') || el.getAttribute('alt');
      openLightbox(src, caption);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeLightbox();
  });

  if (zoomInBtn) {
    zoomInBtn.addEventListener('click', () => {
      scale = Math.min(scale + 0.3, 3.5);
      updateTransform();
    });
  }

  if (zoomOutBtn) {
    zoomOutBtn.addEventListener('click', () => {
      scale = Math.max(scale - 0.3, 0.7);
      updateTransform();
    });
  }

  if (resetBtn) resetBtn.addEventListener('click', resetZoom);

  // Arrastar com mouse
  img.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.clientX - translateX;
    startY = e.clientY - translateY;
    img.style.cursor = 'grabbing';
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    translateX = e.clientX - startX;
    translateY = e.clientY - startY;
    updateTransform();
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
    img.style.cursor = 'grab';
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeLightbox();
    }
  });
}
