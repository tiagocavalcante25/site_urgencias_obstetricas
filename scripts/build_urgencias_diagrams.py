"""
build_urgencias_diagrams.py
Gera infográficos médicos de alta resolução para Urgências e Emergências Obstétricas.
Padrão visual: FEBRASGO / Ministério da Saúde / SUS / USMLE Step 2 CK.
"""

import os
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_urgencias_obstetricas\assets\img"
os.makedirs(IMG_DIR, exist_ok=True)

# Fontes do sistema
FONT_REG = "C:/Windows/Fonts/segoeui.ttf"
FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"

def get_font(size, bold=False):
    path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_badge(draw, text, xy, bg_color, text_color, font, pad_x=12, pad_y=4, r=8):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x, y = xy
    draw.rounded_rectangle([x, y, x + w + pad_x*2, y + h + pad_y*2], radius=r, fill=bg_color)
    draw.text((x + pad_x, y + pad_y), text, fill=text_color, font=font)
    return x + w + pad_x*2 + 8

def draw_card(draw, box, fill_color, border_color, r=14, border_w=2):
    draw.rounded_rectangle(box, radius=r, fill=fill_color, outline=border_color, width=border_w)

# ==============================================================================
# DIAGRAMA 1: Abortamento e Gravidez Ectópica
# ==============================================================================
def create_abortamento_ectopica():
    W, H = 1600, 900
    img = Image.new("RGB", (W, H), "#0b1329")
    draw = ImageDraw.Draw(img)

    # Top Header
    draw.rectangle([0, 0, W, 90], fill="#0f1f3d")
    draw.line([0, 90, W, 90], fill="#1e3a8a", width=2)
    
    draw.text((40, 22), "SANGRAMENTO DA PRIMEIRA METADE: ABORTAMENTO & GRAVIDEZ ECTÓPICA", fill="#ffffff", font=get_font(26, True))
    draw.text((40, 56), "Diagnóstico Diferencial, Zona Discriminatória e Conduta Clínica • Diretrizes FEBRASGO / SUS / ACOG", fill="#94a3b8", font=get_font(15))
    
    # Badges Top Right
    bx = 1100
    bx = draw_badge(draw, "FEBRASGO / SUS", (bx, 30), "#0369a1", "#ffffff", get_font(13, True))
    bx = draw_badge(draw, "USMLE Step 2 CK", (bx, 30), "#047857", "#ffffff", get_font(13, True))
    draw_badge(draw, "PCDT Emergência", (bx, 30), "#b45309", "#ffffff", get_font(13, True))

    # Grid de 3 Colunas
    # Coluna 1: Formas Clínicas de Abortamento
    c1_box = [30, 110, 530, 860]
    draw_card(draw, c1_box, "#132144", "#1e3a8a")
    draw.rounded_rectangle([30, 110, 530, 160], radius=14, fill="#1e3a8a")
    draw.text((50, 124), "1. Formas Clínicas do Abortamento", fill="#38bdf8", font=get_font(20, True))

    abort_items = [
        ("Ameaça de Abortamento", "Colo FECHADO | Embrião VIVO | Sangramento discreto", "Conduta: Repouso relativo, sintomáticos, NÃO prescrever progesterona de rotina.", "#38bdf8"),
        ("Abortamento Inevitável", "Colo ABERTO | Membranas íntegras/rotas | Cólicas intensas", "Conduta: Esvaziamento uterino (AMIU se <= 12 sem; Curetagem se > 12 sem) ou Misoprostol.", "#f59e0b"),
        ("Abortamento Incompleto", "Colo ABERTO | Eliminação parcial | Restos ao USG > 15 mm", "Conduta: AMIU ou Curetagem aspirativa. Se instável: ocitocina IV + esvaziamento imediato.", "#ef4444"),
        ("Abortamento Completo", "Colo FECHADO | Eliminação total de restos | Útero reduzido", "Conduta: Expectante; controle de sangramento e analgesia. Solicitar beta-hCG se dúvida.", "#10b981"),
        ("Abortamento Retido", "Colo FECHADO | Embrião sem BCF (CCN >= 7 mm) ou saco vazio", "Conduta: Misoprostol 800 mcg vaginal ou AMIU/Curetagem programada.", "#a855f7"),
        ("Abortamento Séptico", "Colo ABERTO/FECHADO | Febre, dor uterina, secreção fétida", "ALERTA: Clindamicina + Gentamicina IV + AMIU imediato pós-início de ATB!", "#f43f5e")
    ]

    y_pos = 175
    for title, desc1, desc2, col in abort_items:
        draw.rounded_rectangle([45, y_pos, 515, y_pos + 102], radius=8, fill="#0f172a", outline="#334155")
        draw.rectangle([45, y_pos, 51, y_pos + 102], fill=col)
        draw.text((60, y_pos + 8), title, fill=col, font=get_font(15, True))
        draw.text((60, y_pos + 32), desc1, fill="#e2e8f0", font=get_font(12, True))
        draw.text((60, y_pos + 56), desc2, fill="#94a3b8", font=get_font(11))
        y_pos += 112

    # Coluna 2: Gravidez Ectópica (Topografia e Zona Discriminatória)
    c2_box = [550, 110, 1060, 860]
    draw_card(draw, c2_box, "#132144", "#1e3a8a")
    draw.rounded_rectangle([550, 110, 1060, 160], radius=14, fill="#1e3a8a")
    draw.text((570, 124), "2. Gravidez Ectópica & Diagnóstico", fill="#f59e0b", font=get_font(20, True))

    # Topografia
    draw.text((570, 180), "Localizações Anatômicas Tubárias & Raras:", fill="#ffffff", font=get_font(15, True))
    topos = [
        ("Ampola Tubária", "70 - 80%", "Local mais comum; distensão progressiva, sangramento."),
        ("Ístmo Tubário", "12%", "Porção estreita; rotura mais precoce (6-8 semanas)."),
        ("Fímbrias", "5%", "Pode haver abortamento tubário para cavidade peritoneal."),
        ("Cornual / Intersticial", "2 - 3%", "Gravíssimo: rotura tardia (12-16 sem) com hemorragia maciça cataclísmica!"),
        ("Cicatriz de Cesárea", "1 - 2%", "Risco de acretismo placentário e rotura uterina precoce.")
    ]
    ty = 210
    for t_name, t_pct, t_detail in topos:
        draw.rounded_rectangle([570, ty, 1040, ty + 50], radius=6, fill="#0f172a", outline="#334155")
        draw_badge(draw, t_pct, (580, ty + 12), "#f59e0b" if "Cornual" not in t_name else "#ef4444", "#ffffff", get_font(12, True))
        draw.text((660, ty + 8), t_name, fill="#ffffff", font=get_font(14, True))
        draw.text((660, ty + 28), t_detail, fill="#94a3b8", font=get_font(11))
        ty += 58

    # Zona Discriminatória Box
    draw.rounded_rectangle([570, 520, 1040, 840], radius=10, fill="#1e293b", outline="#0284c7", width=2)
    draw.text((590, 535), "Zona Discriminatória do beta-hCG (USTV)", fill="#38bdf8", font=get_font(17, True))
    
    disc_text = (
        "• Definição: Nível sérico de beta-hCG no qual um saco gestacional intrauterino DEVE\n"
        "  ser visualizado obrigatoriamente por ultrassonografia transvaginal (USTV).\n\n"
        "• Padrão Ouro: 1.500 a 3.500 mUI/mL (maioria dos serviços adota >= 2.000 mUI/mL).\n\n"
        "• Regra de Conduta Clínica:\n"
        "  - beta-hCG >= 2.000 + ÚTERO VAZIO = Forte suspeita de Gravidez Ectópica.\n"
        "  - beta-hCG < 2.000 + Útero Vazio + Estável = Dosar beta-hCG em 48h.\n"
        "    * Gestação Tópica Viável: Aumento de >= 35% a 50% em 48h.\n"
        "    * Ectópica ou Não-viável: Aumento em platô ou queda lenta."
    )
    draw.text((590, 575), disc_text, fill="#e2e8f0", font=get_font(13))

    # Coluna 3: Tratamento da Ectópica (MTX vs Cirurgia)
    c3_box = [1080, 110, 1570, 860]
    draw_card(draw, c3_box, "#132144", "#1e3a8a")
    draw.rounded_rectangle([1080, 110, 1570, 160], radius=14, fill="#1e3a8a")
    draw.text((1100, 124), "3. Algoritmo Terapêutico da Ectópica", fill="#10b981", font=get_font(20, True))

    # MTX Card
    draw.rounded_rectangle([1100, 180, 1550, 490], radius=10, fill="#0f172a", outline="#059669", width=2)
    draw.text((1120, 195), "Critérios de Metotrexato (MTX 50 mg/m² IM)", fill="#34d399", font=get_font(16, True))
    
    mtx_criteria = (
        "TODOS os critérios devem estar preenchidos:\n"
        " [OK] Paciente hemodinamicamente ESTÁVEL\n"
        " [OK] Massa anexial íntegra com diâmetro < 3,5 cm\n"
        " [OK] Ausência de atividade cardíaca embrionária (sem BCF)\n"
        " [OK] beta-hCG sérico inicial < 5.000 mUI/mL (ideal < 1.500)\n"
        " [OK] Ausência de líquido livre moderado/grave na cavidade\n"
        " [OK] Função hepática, renal e hematológica normais\n\n"
        "Protocolo de Seguimento D4 e D7:\n"
        " • O beta-hCG pode aumentar até o D4 (efeito de lise celular).\n"
        " • Meta terapêutica: Queda de >= 15% entre o D4 e o D7!\n"
        " • Se queda < 15%: Repetir 2ª dose de MTX ou converter para cirurgia."
    )
    draw.text((1120, 230), mtx_criteria, fill="#e2e8f0", font=get_font(12))

    # Cirurgia Card
    draw.rounded_rectangle([1100, 510, 1550, 840], radius=10, fill="#0f172a", outline="#e11d48", width=2)
    draw.text((1120, 525), "Tratamento Cirúrgico (Laparoscopia / Laparotomia)", fill="#fb7185", font=get_font(16, True))
    
    surg_criteria = (
        "Indicações Formais de Cirurgia de Emergência:\n"
        " [!] Instabilidade hemodinâmica (Choque, rotura tubária, peritonite)\n"
        " [!] Massa >= 3,5 cm ou presença de BCF positivo\n"
        " [!] beta-hCG > 5.000 mUI/mL ou falha documentada do MTX\n"
        " [!] Contraindicações ao MTX (imunodeficiência, úlcera péptica)\n\n"
        "Escolha da Técnica Cirúrgica:\n"
        " • Salpingectomia (Remoção da trompa):\n"
        "   Padrão-ouro na trompa rota, hemorragia grave ou prole definida.\n"
        " • Salpingostomia Linear (Preservação tubária):\n"
        "   Indicada se trompa íntegra e desejo reprodutivo na trompa única.\n"
        "   * Alerta: Exige monitorar beta-hCG semanal até zerar (risco de trofoblasto residual persistente!)."
    )
    draw.text((1120, 560), surg_criteria, fill="#e2e8f0", font=get_font(12))

    img.save(os.path.join(IMG_DIR, "abortamento_e_gravidez_ectopica.jpg"), quality=95)
    print("Salvo: abortamento_e_gravidez_ectopica.jpg")

# ==============================================================================
# DIAGRAMA 2: Doença Trofoblástica Gestacional (DTG)
# ==============================================================================
def create_dtg():
    W, H = 1600, 900
    img = Image.new("RGB", (W, H), "#0b1329")
    draw = ImageDraw.Draw(img)

    # Top Header
    draw.rectangle([0, 0, W, 90], fill="#1e1b4b")
    draw.line([0, 90, W, 90], fill="#4338ca", width=2)
    
    draw.text((40, 22), "DOENÇA TROFOBLÁSTICA GESTACIONAL (DTG) & SEGUIMENTO ONCOLÓGICO", fill="#ffffff", font=get_font(26, True))
    draw.text((40, 56), "Mola Completa vs Parcial, Curva de Regressão de beta-hCG e Rastreio de Neoplasia Trofoblástica (NTG)", fill="#c7d2fe", font=get_font(15))
    
    bx = 1100
    bx = draw_badge(draw, "FEBRASGO / MS", (bx, 30), "#4338ca", "#ffffff", get_font(13, True))
    bx = draw_badge(draw, "Critérios FIGO", (bx, 30), "#059669", "#ffffff", get_font(13, True))
    draw_badge(draw, "Escore de Charing Cross", (bx, 30), "#d97706", "#ffffff", get_font(13, True))

    # Grid 3 Colunas
    # Col 1: Mola Completa vs Parcial
    c1_box = [30, 110, 530, 860]
    draw_card(draw, c1_box, "#132144", "#3730a3")
    draw.rounded_rectangle([30, 110, 530, 160], radius=14, fill="#3730a3")
    draw.text((50, 124), "1. Mola Completa vs Mola Parcial", fill="#e0e7ff", font=get_font(20, True))

    # Completa Box
    draw.rounded_rectangle([45, 175, 515, 500], radius=10, fill="#0f172a", outline="#818cf8", width=2)
    draw.text((60, 190), "MOLA HIDATIFORME COMPLETA", fill="#a5b4fc", font=get_font(16, True))
    comp_text = (
        "• Genética: Diploide (46,XX em 90%, 46,XY em 10%).\n"
        "  100% de origem PATERNÓGENA (óvulo anucleado fecundado\n"
        "  por espermatozoide duplicado ou dispermia).\n"
        "• Embrião/Feto: AUSENTE (apenas tecido trofoblástico).\n"
        "• Histopatologia: Degeneração hidrópica DIFUSA das vilosidades\n"
        "  com aspecto clássico macroscópico de 'cachos de uva'.\n"
        "• beta-hCG: Extremamente elevado (> 100.000 mUI/mL).\n"
        "• Quadro Clínico:\n"
        "  - Sangramento vermelho vivo de repetição;\n"
        "  - Útero desproporcionalmente MAIOR que a IG;\n"
        "  - Hiperêmese gravídica intensa (hCG estimula centro do vômito);\n"
        "  - Cistos tecaluteínicos ovarianos volumosos bilaterais;\n"
        "  - Pré-eclâmpsia em idade precoce (< 20 semanas);\n"
        "  - Hipertireoidismo (hCG compartilha subunidade alfa com TSH).\n"
        "• Risco de Malignização (NTG): ALTO (15 a 20%)."
    )
    draw.text((60, 220), comp_text, fill="#e2e8f0", font=get_font(12))

    # Parcial Box
    draw.rounded_rectangle([45, 515, 515, 840], radius=10, fill="#0f172a", outline="#6366f1", width=2)
    draw.text((60, 530), "MOLA HIDATIFORME PARCIAL", fill="#c7d2fe", font=get_font(16, True))
    parc_text = (
        "• Genética: Triploide (69,XXY, 69,XXX ou 69,XYY).\n"
        "  Origem mista: 1 óvulo normal fecundado por 2 espermatozoides.\n"
        "• Embrião/Feto: PRESENTE, porém gravemente malformado\n"
        "  e não viável (com partes fetais e hemácias fetais).\n"
        "• Histopatologia: Degeneração hidrópica FOCAL / irregular.\n"
        "• beta-hCG: Leve a moderadamente elevado (< 100.000 mUI/mL).\n"
        "• Quadro Clínico: Muitas vezes simula um abortamento retido\n"
        "  ou incompleto comum. Útero compatível ou menor que a IG.\n"
        "  Complicações médicas (DHEG precoce, cistos) são raras.\n"
        "• Risco de Malignização (NTG): BAIXO (1 a 5%)."
    )
    draw.text((60, 560), parc_text, fill="#e2e8f0", font=get_font(12))

    # Col 2: Esvaziamento e Seguimento
    c2_box = [550, 110, 1060, 860]
    draw_card(draw, c2_box, "#132144", "#3730a3")
    draw.rounded_rectangle([550, 110, 1060, 160], radius=14, fill="#3730a3")
    draw.text((570, 124), "2. Esvaziamento & Curva de beta-hCG", fill="#38bdf8", font=get_font(20, True))

    draw.rounded_rectangle([570, 175, 1040, 480], radius=10, fill="#0f172a", outline="#0284c7", width=2)
    draw.text((590, 190), "Conduta de Esvaziamento Uterino", fill="#38bdf8", font=get_font(16, True))
    esvaz_text = (
        "1. Método de Escolha: VÁCUO-ASPIRAÇÃO (AMIU ou Elétrica).\n"
        "   - Evitar curetagem cortante de início pelo altíssimo risco de perfuração\n"
        "     uterina (miométrio delgado e amolecido) e disseminação trofoblástica.\n"
        "2. Ocitocina IV: Iniciar APENAS DURANTE a aspiração para promover\n"
        "   contração e hemostasia (nunca antes para não embolizar trofoblasto!).\n"
        "3. Exame Histopatológico: Obrigatório enviar todo o material aspirado.\n"
        "4. Raio-X de Tórax Inicial: Realizar antes do esvaziamento para rastrear\n"
        "   metástases pulmonares precoces.\n"
        "5. Histerectomia com mola in situ: Opção para multíparas > 40 anos com prole\n"
        "   concluída (reduz risco de NTG local, mas NÃO elimina metástases!)."
    )
    draw.text((590, 225), esvaz_text, fill="#e2e8f0", font=get_font(12))

    # Cronograma beta-hCG
    draw.rounded_rectangle([570, 495, 1040, 840], radius=10, fill="#0f172a", outline="#10b981", width=2)
    draw.text((590, 510), "Cronograma Obrigatório de beta-hCG", fill="#34d399", font=get_font(16, True))
    crono_text = (
        "• Fase Semanal:\n"
        "  Dosar beta-hCG sérico quantitativo toda semana até obter\n"
        "  3 RESULTADOS CONSECUTIVOS NEGATIVOS (< 5 mUI/mL).\n\n"
        "• Fase Mensal:\n"
        "  Após a negativação, dosar mensalmente por:\n"
        "  - 6 MESES consecutivos na Mola Completa;\n"
        "  - 1 a 3 MESES na Mola Parcial.\n\n"
        "• Anticoncepção Rigorosa OBRIGATÓRIA durante todo o seguimento:\n"
        "  - Métodos hormonais (ACO, injetável ou implante).\n"
        "  - CONTRAINDICADO DIU até remissão completa (risco de perfuração e infecção).\n"
        "  - Nova gravidez altera o beta-hCG e impede diferenciar recidiva de gestação!"
    )
    draw.text((590, 545), crono_text, fill="#e2e8f0", font=get_font(12))

    # Col 3: Diagnóstico de NTG e Quimioterapia
    c3_box = [1080, 110, 1570, 860]
    draw_card(draw, c3_box, "#132144", "#3730a3")
    draw.rounded_rectangle([1080, 110, 1570, 160], radius=14, fill="#3730a3")
    draw.text((1100, 124), "3. Malignização: Critérios de NTG", fill="#f43f5e", font=get_font(20, True))

    draw.rounded_rectangle([1100, 175, 1550, 500], radius=10, fill="#0f172a", outline="#e11d48", width=2)
    draw.text((1120, 190), "Critérios Diagnósticos de NTG (FIGO / OMS)", fill="#fb7185", font=get_font(16, True))
    ntg_text = (
        "A paciente desenvolveu Neoplasia Trofoblástica se houver:\n\n"
        " 1. PLATÔ DO beta-hCG:\n"
        "    Estabilidade de valores em 4 dosagens semanais ao longo\n"
        "    de 3 semanas (dias 1, 7, 14 e 21).\n\n"
        " 2. ELEVAÇÃO DO beta-hCG:\n"
        "    Subida >= 10% em 3 dosagens semanais consecutivas ao longo\n"
        "    de 2 semanas (dias 1, 7 e 14).\n\n"
        " 3. PERSISTÊNCIA DO beta-hCG:\n"
        "    Níveis detectáveis após 6 meses de acompanhamento pós-esvaziamento.\n\n"
        " 4. DIAGNÓSTICO HISTOLÓGICO DE CORIOCARCINOMA:\n"
        "    Neoplasia altamente vascularizada, agressiva e metastática.\n\n"
        " 5. METÁSTASES À DISTÂNCIA:\n"
        "    Pulmão (80%), vagina (30%), fígado (10%), cérebro (10%)."
    )
    draw.text((1120, 220), ntg_text, fill="#e2e8f0", font=get_font(12))

    # Estadiamento e Quimio
    draw.rounded_rectangle([1100, 515, 1550, 840], radius=10, fill="#0f172a", outline="#d97706", width=2)
    draw.text((1120, 530), "Estadiamento e Tratamento Quimioterápico", fill="#fbbf24", font=get_font(16, True))
    quimio_text = (
        "• Estadiamento Anatômico (FIGO):\n"
        "  - Estágio I: Restrito ao corpo uterino.\n"
        "  - Estágio II: Vagina, pelve ou anexos.\n"
        "  - Estágio III: Metástases pulmonares com ou sem pelve.\n"
        "  - Estágio IV: Todas as outras metástases (fígado, cérebro).\n\n"
        "• Escore de Risco Prognóstico OMS/FIGO (Idade, hCG, tamanho, metástases):\n"
        "  - BAIXO RISCO (Escore <= 6):\n"
        "    Monodroga: METOTREXATO (com resgate de ácido folínico) ou Actinomicina D.\n"
        "    * Taxa de cura > 98%!\n"
        "  - ALTO RISCO (Escore >= 7):\n"
        "    Poliquimioterapia agressiva: Regime EMA-CO (Etoposídeo, Metotrexato,\n"
        "    Actinomicina D, Ciclofosfamida, Oncovin/Vincristina)."
    )
    draw.text((1120, 560), quimio_text, fill="#e2e8f0", font=get_font(12))

    img.save(os.path.join(IMG_DIR, "doenca_trofoblastica_mola_hidatiforme.jpg"), quality=95)
    print("Salvo: doenca_trofoblastica_mola_hidatiforme.jpg")

# ==============================================================================
# DIAGRAMA 3: Embolia por Líquido Amniótico (ELA) & Sepse Obstétrica
# ==============================================================================
def create_ela_sepse():
    W, H = 1600, 900
    img = Image.new("RGB", (W, H), "#0b1329")
    draw = ImageDraw.Draw(img)

    # Top Header
    draw.rectangle([0, 0, W, 90], fill="#3b0764")
    draw.line([0, 90, W, 90], fill="#7e22ce", width=2)
    
    draw.text((40, 22), "EMBOLIA POR LÍQUIDO AMNIÓTICO (ELA) & SEPSE OBSTÉTRICA", fill="#ffffff", font=get_font(26, True))
    draw.text((40, 56), "Colapso Cardiopulmonar Agudo no Parto, qSOFA Materno e Bundle de Ressuscitação da 1ª Hora • Protocolos de UTI", fill="#e9d5ff", font=get_font(15))
    
    bx = 1100
    bx = draw_badge(draw, "FEBRASGO / AMIB", (bx, 30), "#7e22ce", "#ffffff", get_font(13, True))
    bx = draw_badge(draw, "Surviving Sepsis", (bx, 30), "#0284c7", "#ffffff", get_font(13, True))
    draw_badge(draw, "Suporte Crítico", (bx, 30), "#dc2626", "#ffffff", get_font(13, True))

    # Grid 2 Colunas Largas
    # Coluna 1: Embolia por Líquido Amniótico (ELA)
    c1_box = [30, 110, 785, 860]
    draw_card(draw, c1_box, "#132144", "#6b21a8")
    draw.rounded_rectangle([30, 110, 785, 160], radius=14, fill="#6b21a8")
    draw.text((50, 124), "1. Embolia por Líquido Amniótico (Síndrome Anafilactoide)", fill="#f3e8ff", font=get_font(20, True))

    # ELA Tríade
    draw.rounded_rectangle([45, 175, 770, 480], radius=10, fill="#0f172a", outline="#a855f7", width=2)
    draw.text((60, 190), "Tríade Clínica Fisiopatológica em 3 Fases", fill="#c084fc", font=get_font(17, True))
    ela_triad = (
        "FASE 1: VASOESPASMO PULMONAR HIPERAGUDO (Minutos iniciais)\n"
        " • Entrada de antígenos fetais/amnióticos na circulação materna desencadeia\n"
        "   reação imune do tipo anafilactoide com liberação maciça de mediadores químicos.\n"
        " • Hipertensão pulmonar aguda súbita -> Sobrecarga e falência do Ventrículo Direito (VD).\n"
        " • Sintomas: Agitação súbita, sensação de morte iminente, dispneia grave e cianose.\n\n"
        "FASE 2: CHOQUE CARDIOGÊNICO & EDEMA AGUDO DE PULMÃO\n"
        " • Desvio do septo interventricular para esquerda -> Colapso do Ventrículo Esquerdo (VE).\n"
        " • Hipotensão arterial severa, choque cardiogênico, perda de consciência e PCR.\n"
        " • Edema agudo pulmonar não-cardiogênico (aumento da permeabilidade capilar).\n\n"
        "FASE 3: COAGULOPATIA DE CONSUMO (CIVD Fulminante) (80% dos casos)\n"
        " • O líquido amniótico contém fator tecidual procoagulante maciço.\n"
        " • Consumo rápido de plaquetas e fibrinogênio (< 100 mg/dL) com hemorragia maciça\n"
        "   incoercível na histerotomia, lacerações e sítios de punção venosa!"
    )
    draw.text((60, 225), ela_triad, fill="#e2e8f0", font=get_font(12))

    # ELA Manejo
    draw.rounded_rectangle([45, 495, 770, 840], radius=10, fill="#0f172a", outline="#e11d48", width=2)
    draw.text((60, 510), "Manejo de Emergência em Sala de Parto / UTI", fill="#fb7185", font=get_font(17, True))
    ela_mgmt = (
        "1. SUPORTE VENTILATÓRIO IMEDIATO:\n"
        "   O2 a 100% via máscara com reservatório; intubação orotraqueal rápida e precoce.\n\n"
        "2. SUPORTE HEMODINÂMICO VOLUMÉTRICO:\n"
        "   - CUIDADO com excesso de cristaloide: o VD já está falimentar e hiperdistendido!\n"
        "   - Noradrenalina precoce (vasopressor) + Dobutamina / Milrinona (inotrópico de VD).\n"
        "   - Vasodilatador pulmonar se disponível: Óxido nítrico inalado (iNO) ou Sildenafila.\n\n"
        "3. PROTOCOLO DE TRANSFUSÃO MACIÇA (1:1:1):\n"
        "   - Concentrado de hemácias + Plasma fresco + Plaquetas em razão equilibrada 1:1:1.\n"
        "   - CRIOPRECIPITADO ou Fibrinogênio concentrado para manter fibrinogênio > 200 mg/dL.\n"
        "   - ÁCIDO TRANEXÂMICO 1 g IV em 10 min (repetir 1 g após 30 min se sangramento ativo).\n\n"
        "4. PARADA CARDIORRESPIRATÓRIA:\n"
        "   - RCP de alta qualidade com desvio manual do útero para esquerda (DUE).\n"
        "   - CESÁREA PERIMORTEM em 4 minutos se sem RCE (salva a mãe pelo alívio do VD)!"
    )
    draw.text((60, 545), ela_mgmt, fill="#e2e8f0", font=get_font(12))

    # Coluna 2: Sepse Obstétrica
    c2_box = [815, 110, 1570, 860]
    draw_card(draw, c2_box, "#132144", "#0369a1")
    draw.rounded_rectangle([815, 110, 1570, 160], radius=14, fill="#0369a1")
    draw.text((835, 124), "2. Sepse Obstétrica & Bundle da 1ª Hora", fill="#e0f2fe", font=get_font(20, True))

    # qSOFA Box
    draw.rounded_rectangle([830, 175, 1555, 480], radius=10, fill="#0f172a", outline="#0284c7", width=2)
    draw.text((845, 190), "Critérios de Alerta: qSOFA Obstétrico & MEOWS", fill="#38bdf8", font=get_font(17, True))
    sepse_criteria = (
        "Na gestação, os parâmetros habituais do SIRS são normais. Use o qSOFA adaptado:\n\n"
        "CRITÉRIOS DO qSOFA OBSTÉTRICO (Presença de >= 2 pontos = Risco de Sepse Grave):\n"
        " [!] Pressão Arterial Sistólica (PAS) <= 90 mmHg (ou queda de 40 mmHg na basal)\n"
        " [!] Frequência Respiratória (FR) >= 25 irpm\n"
        " [!] Alteração do Nível de Consciência (Escala de Coma de Glasgow < 15)\n\n"
        "PRINCIPAIS FOCOS INFECCIOSOS EM OBSTETRÍCIA:\n"
        " • Corioamnionite / Infecção Intra-amniótica (febre materna + taquicardia fetal + líquido fétido);\n"
        " • Endometrite Pós-Parto (tríade: febre + útero subinvoluído doloroso + lóquios fétidos);\n"
        " • Pielonefrite Aguda (Giordano positivo, náuseas, sepse urinária por E. coli);\n"
        " • Abortamento Séptico (infecção polimicrobiana pós-curetagem ou manobras clandestinas);\n"
        " • Infecção de Ferida Cirúrgica / Fasciíte Necrosante (pós-cesárea ou episiotomia)."
    )
    draw.text((845, 225), sepse_criteria, fill="#e2e8f0", font=get_font(12))

    # Bundle da 1ª Hora
    draw.rounded_rectangle([830, 495, 1555, 840], radius=10, fill="#0f172a", outline="#10b981", width=2)
    draw.text((845, 510), "Bundle da Sepse Materna na 1ª Hora (Surviving Sepsis)", fill="#34d399", font=get_font(17, True))
    bundle_text = (
        "PROTOCOLO DE INTERVENÇÃO IMEDIATA (Nos primeiros 60 minutos):\n\n"
        " 1. DOSAR LACTATO SÉRICO:\n"
        "    - Lactato > 2 mmol/L = Hipoperfusão tecidual.\n"
        "    - Lactato >= 4 mmol/L = Choque séptico grave (redosar em 2-4 horas).\n\n"
        " 2. COLETAR HEMOCULTURAS (2 pares) antes de iniciar os antimicrobianos.\n\n"
        " 3. ANTIBIOTICOTERAPIA EMPÍRICA DE LARGO ESPECTRO NA 1ª HORA:\n"
        "    - Corioamnionite: Ampicilina 2g 6/6h + Gentamicina 5 mg/kg 24/24h (+ Clinda se cesárea).\n"
        "    - Endometrite: Clindamicina 900mg 8/8h + Gentamicina 5 mg/kg 24/24h (+ Ampicilina se grave).\n"
        "    - Sepse com choque: Piperacilina-Tazobactam ou Meropenem + Vancomicina.\n\n"
        " 4. RESSUSCITAÇÃO VOLÊMICA RÁPIDA COM CRISTALOIDE:\n"
        "    30 mL/kg de Ringer Lactato se hipotensão (PAS < 90) ou lactato >= 4 mmol/L.\n\n"
        " 5. VASOPRESSOR PRECOCE:\n"
        "    Noradrenalina IV para manter PAM >= 65 mmHg se hipotensão refratária ao volume."
    )
    draw.text((845, 545), bundle_text, fill="#e2e8f0", font=get_font(12))

    img.save(os.path.join(IMG_DIR, "embolia_liquido_amniotico_sepse.jpg"), quality=95)
    print("Salvo: embolia_liquido_amniotico_sepse.jpg")

if __name__ == "__main__":
    print("Iniciando geração de infográficos médicos...")
    create_abortamento_ectopica()
    create_dtg()
    create_ela_sepse()
    print("Todos os diagramas gerados com sucesso!")
