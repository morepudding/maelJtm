# -*- coding: utf-8 -*-
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# ═══════════════════════════════════════
# COULEURS
# ═══════════════════════════════════════
DARK_BG = RGBColor(0x1a, 0x1a, 0x2e)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
ACCENT_BLUE = RGBColor(0x00, 0x96, 0xD6)
ACCENT_PURPLE = RGBColor(0x7C, 0x4D, 0xFF)
ACCENT_GREEN = RGBColor(0x00, 0xC9, 0xA7)
ACCENT_ORANGE = RGBColor(0xFF, 0x6B, 0x35)
ACCENT_RED = RGBColor(0xFF, 0x45, 0x57)
ACCENT_TEAL = RGBColor(0x00, 0xB4, 0xD8)
ACCENT_YELLOW = RGBColor(0xFF, 0xD9, 0x3D)
SUBTLE_WHITE = RGBColor(0xAA, 0xAA, 0xBB)
CARD_BG = RGBColor(0x22, 0x22, 0x3a)

def set_slide_bg(slide, color=DARK_BG):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_box(slide, left, top, width, height, fill_color, border_color=None, border_w=Pt(1)):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = border_w
    else:
        shape.line.fill.background()
    shape.shadow.inherit = False
    return shape

def add_arrow(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape

def add_down_arrow(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape

def txt(slide, left, top, width, height, text, size=18, color=WHITE, bold=False, align=PP_ALIGN.LEFT):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = "Segoe UI"
    p.alignment = align
    return txBox

def bullets(slide, left, top, width, height, items, size=14, color=WHITE):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = item
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.name = "Segoe UI"
        p.space_after = Pt(6)
    return txBox

def slide_title(slide, title):
    txt(slide, Inches(0.8), Inches(0.4), Inches(10), Inches(0.7), title, size=36, color=ACCENT_BLUE, bold=True)
    add_box(slide, Inches(0.8), Inches(1.0), Inches(5), Inches(0.04), ACCENT_BLUE)

# ═══════════════════════════════════════
# SLIDE 1 : TITRE
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
add_box(slide, Inches(0), Inches(3.2), Inches(13.333), Inches(0.08), ACCENT_PURPLE)
txt(slide, Inches(1), Inches(1.5), Inches(11), Inches(1.5), "BricoLoc 2.0", size=54, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(3.5), Inches(11), Inches(1), "Architecture logicielle — Dossier de conception", size=28, color=ACCENT_BLUE, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(5.0), Inches(11), Inches(0.5), "Master 1 Architecte d'Application — CESI", size=18, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.5), "Romain  ·  Maëlle  ·  Loris", size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════
# SLIDE 2 : SOMMAIRE
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "Sommaire")
bullets(slide, Inches(1), Inches(1.4), Inches(5), Inches(5), [
    "1.  Organisation du groupe",
    "2.  Contexte & objectifs du projet",
    "3.  Analyse du SI existant",
    "4.  Points faibles identifiés",
    "5.  Exigences non fonctionnelles (ENF)",
    "6.  Axes d'amélioration",
], size=20, color=WHITE)
bullets(slide, Inches(7), Inches(1.4), Inches(5), Inches(5), [
    "7.   Comparaison des styles architecturaux",
    "8.   Styles retenus & justification",
    "9.   Choix technologiques",
    "10.  Architecture logique cible",
    "11.  Stratégie de migration",
    "12.  Conclusion & perspectives",
], size=20, color=WHITE)

# ═══════════════════════════════════════
# SLIDE 3 : ORGANISATION DU GROUPE (CORRIGÉ - ajout axes d'amélioration)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "1. Organisation du groupe")

txt(slide, Inches(0.8), Inches(1.2), Inches(5), Inches(0.4), "Équipe initiale : 4 membres", size=16, color=ACCENT_YELLOW, bold=True)
txt(slide, Inches(0.8), Inches(1.55), Inches(8), Inches(0.4), "Steven (Analyste) — a quitté le groupe en cours de projet", size=13, color=ACCENT_RED)

members = [
    ("Romain", "Chef de projet", "Coordination, planification", ACCENT_BLUE),
    ("Maëlle", "Lead Back-end & BDD", "Architecture back-end, BDD", ACCENT_PURPLE),
    ("Loris", "Lead Front-end & reste", "Front-end, intégrations", ACCENT_GREEN),
]
for i, (name, role, desc, color) in enumerate(members):
    x = Inches(0.8 + i * 4.0)
    add_box(slide, x, Inches(1.95), Inches(3.5), Inches(1.6), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.15), Inches(2.0), Inches(3.2), Inches(0.4), name, size=18, color=color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.15), Inches(2.4), Inches(3.2), Inches(0.4), role, size=12, color=WHITE, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.15), Inches(2.8), Inches(3.2), Inches(0.4), desc, size=11, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)

# Points forts
txt(slide, Inches(0.8), Inches(3.8), Inches(5.5), Inches(0.4), "✅ Points forts", size=15, color=ACCENT_GREEN, bold=True)
bullets(slide, Inches(0.8), Inches(4.15), Inches(5.5), Inches(1.5), [
    "✓ Absorption de la charge (-25%) sans retard",
    "✓ Cohérence architecturale (traçabilité PF → ENF → AXE)",
    "✓ Revue croisée systématique de chaque livrable",
], size=12, color=LIGHT_GRAY)

# NOUVEAU : Axes d'amélioration du groupe
txt(slide, Inches(7), Inches(3.8), Inches(5.5), Inches(0.4), "📈 Axes d'amélioration du groupe", size=15, color=ACCENT_ORANGE, bold=True)
bullets(slide, Inches(7), Inches(4.15), Inches(5.5), Inches(2.5), [
    "△ Anticiper les risques de départ d'un membre",
    "   (planifier un bus factor ≥ 2 dès le départ)",
    "△ Documenter les décisions d'architecture plus tôt",
    "   (ADR dès la phase de cadrage, pas en rédaction)",
    "△ Renforcer les compétences DevOps dans l'équipe",
    "   (formation CI/CD, conteneurisation, IaC)",
    "△ Formaliser les cérémonies de revue pour pérenniser",
    "   (processus écrit, pas uniquement oral)",
], size=12, color=LIGHT_GRAY)

# ═══════════════════════════════════════
# SLIDE 4 : CONTEXTE & OBJECTIFS
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "2. Contexte & objectifs")

txt(slide, Inches(0.8), Inches(1.3), Inches(5.5), Inches(0.5), "BricoLoc — Location d'outils de bricolage", size=20, color=WHITE, bold=True)
bullets(slide, Inches(0.8), Inches(1.9), Inches(5.5), Inches(4), [
    "• Application en production depuis 2013 — stack obsolète",
    "• Perte de clients depuis 2020 (bugs, stocks incohérents)",
    "• 10 entrepôts (Toulouse siège + 9 régionaux)",
    "• Expansion européenne prévue (Bruxelles, Lausanne, Francfort)",
    "• Nouveaux segments : location P2P, B2B grands comptes",
    "• Marque blanche pour partenaires hypermarchés",
    "• Équipe DSI : 5 développeurs internes",
], size=15, color=LIGHT_GRAY)

txt(slide, Inches(7), Inches(1.3), Inches(5.5), Inches(0.5), "Objectif du projet", size=20, color=ACCENT_GREEN, bold=True)
bullets(slide, Inches(7), Inches(1.9), Inches(5.5), Inches(4), [
    "🎯 Concevoir l'architecture logicielle de BricoLoc 2.0",
    "📋 Analyser l'existant et identifier les points faibles",
    "⚖️ Comparer et justifier les choix architecturaux",
    "🔧 Proposer les technologies adaptées",
    "📐 Définir l'architecture logique cible",
    "🗓️ Planifier la migration progressive (Strangler Fig)",
], size=15, color=LIGHT_GRAY)

# ═══════════════════════════════════════
# SLIDE 5 : DEMARCHE
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "Démarche de conception")

steps = [
    ("Étape 1", "Analyse de l'existant", ACCENT_BLUE),
    ("Étape 2", "Exigences non fonctionnelles", ACCENT_TEAL),
    ("Étape 3", "Points faibles & axes d'amélioration", ACCENT_ORANGE),
    ("Étape 4", "Comparaison des styles architecturaux", ACCENT_PURPLE),
    ("Étape 5", "Matrice de choix technologique", ACCENT_YELLOW),
    ("Étape 6", "Styles retenus & justification", ACCENT_GREEN),
    ("Étape 7", "Architecture logique cible", ACCENT_RED),
]
for i, (step, desc, color) in enumerate(steps):
    y = Inches(1.4 + i * 0.78)
    add_box(slide, Inches(1.5), y, Inches(10), Inches(0.6), CARD_BG, color, Pt(2))
    txt(slide, Inches(1.7), y + Inches(0.08), Inches(2), Inches(0.45), step, size=16, color=color, bold=True)
    txt(slide, Inches(4), y + Inches(0.08), Inches(7), Inches(0.45), desc, size=16, color=WHITE)

txt(slide, Inches(1), Inches(7), Inches(11), Inches(0.4), "Chaque étape alimente la suivante — les ENF traversent toute la démarche comme fil directeur", size=13, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)

OUTPUT = r"c:\Users\Loris\Documents\bricoloc\maelJtm\07-presentation\BricoLoc2_Presentation.pptx"

# ═══════════════════════════════════════
# SLIDE 6 : SI EXISTANT (CORRIGÉ - schéma avec interactions)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "3. Schéma du SI existant")

# Les 5 composants positionnés comme un vrai schéma
# Front-end (haut gauche)
add_box(slide, Inches(0.5), Inches(1.3), Inches(3.2), Inches(1.5), CARD_BG, ACCENT_BLUE, Pt(2))
txt(slide, Inches(0.7), Inches(1.35), Inches(2.8), Inches(0.4), "🖥️ Front-end", size=16, color=ACCENT_BLUE, bold=True)
txt(slide, Inches(0.7), Inches(1.75), Inches(2.8), Inches(0.9), "Tomcat 8.5 / Spring 5\nApache (reverse proxy)\nLogique métier migrée ici ⚠️", size=11, color=LIGHT_GRAY)

# Back-end (haut droite)
add_box(slide, Inches(5.0), Inches(1.3), Inches(3.2), Inches(1.5), CARD_BG, ACCENT_PURPLE, Pt(2))
txt(slide, Inches(5.2), Inches(1.35), Inches(2.8), Inches(0.4), "⚙️ Back-end", size=16, color=ACCENT_PURPLE, bold=True)
txt(slide, Inches(5.2), Inches(1.75), Inches(2.8), Inches(0.9), "WebLogic 12c R1 / Java EE 6\nOracle Linux 6.5 (EOL)\nEJB / JPA legacy", size=11, color=LIGHT_GRAY)

# BDD (centre bas)
add_box(slide, Inches(2.5), Inches(3.7), Inches(4.0), Inches(1.5), CARD_BG, ACCENT_ORANGE, Pt(2))
txt(slide, Inches(2.7), Inches(3.75), Inches(3.6), Inches(0.4), "🗄️ Oracle 11g R2 (Cluster 2 nœuds)", size=14, color=ACCENT_ORANGE, bold=True)
txt(slide, Inches(2.7), Inches(4.15), Inches(3.6), Inches(0.9), "bricolocDB · autorisationDB · prixDB\nTables > 150 colonnes, PL/SQL métier\nCoût licences élevé", size=11, color=LIGHT_GRAY)

# Stocks SAP (droite)
add_box(slide, Inches(9.5), Inches(1.3), Inches(3.5), Inches(1.5), CARD_BG, ACCENT_RED, Pt(2))
txt(slide, Inches(9.7), Inches(1.35), Inches(3.1), Inches(0.4), "📦 Stocks & SAP", size=16, color=ACCENT_RED, bold=True)
txt(slide, Inches(9.7), Inches(1.75), Inches(3.1), Inches(0.9), "SAP B1 9.X → CSV quotidien\nBatch Java → PL/SQL\nWCF VB.NET (code perdu!) ☠️", size=11, color=LIGHT_GRAY)

# Infra (bas droite)
add_box(slide, Inches(9.5), Inches(3.7), Inches(3.5), Inches(1.5), CARD_BG, ACCENT_TEAL, Pt(2))
txt(slide, Inches(9.7), Inches(3.75), Inches(3.1), Inches(0.4), "🏗️ Infra", size=16, color=ACCENT_TEAL, bold=True)
txt(slide, Inches(9.7), Inches(4.15), Inches(3.1), Inches(0.9), "FTP (pas de Git!) · VM fantôme\nActive Directory · Exchange\nPartages fichiers + CSV", size=11, color=LIGHT_GRAY)

# FLÈCHES D'INTERACTION
# Front → Back (SOAP)
add_arrow(slide, Inches(3.7), Inches(1.85), Inches(1.2), Inches(0.3), ACCENT_BLUE)
txt(slide, Inches(3.8), Inches(1.55), Inches(1), Inches(0.3), "SOAP", size=10, color=ACCENT_BLUE, bold=True, align=PP_ALIGN.CENTER)

# Front → BDD (accès direct JDBC - violation!)
add_down_arrow(slide, Inches(1.8), Inches(2.85), Inches(0.35), Inches(0.8), ACCENT_RED)
txt(slide, Inches(0.5), Inches(3.0), Inches(1.8), Inches(0.5), "JDBC direct ⚠️\n(violation archi)", size=9, color=ACCENT_RED, bold=True)

# Back → BDD
add_down_arrow(slide, Inches(6.3), Inches(2.85), Inches(0.35), Inches(0.8), ACCENT_PURPLE)
txt(slide, Inches(6.7), Inches(3.0), Inches(1.5), Inches(0.3), "JDBC / JPA", size=10, color=ACCENT_PURPLE)

# SAP → BDD (Batch CSV)
add_arrow(slide, Inches(8.3), Inches(2.0), Inches(1.1), Inches(0.3), ACCENT_RED)
txt(slide, Inches(7.9), Inches(2.3), Inches(2.0), Inches(0.3), "← Batch CSV →", size=9, color=ACCENT_RED, align=PP_ALIGN.CENTER)

# SAP/Stocks → BDD
add_down_arrow(slide, Inches(10.8), Inches(2.85), Inches(0.35), Inches(0.8), ACCENT_RED)
txt(slide, Inches(10.0), Inches(3.2), Inches(1.5), Inches(0.3), "PL/SQL", size=10, color=ACCENT_RED)

# Légende problèmes
add_box(slide, Inches(0.5), Inches(5.5), Inches(12.3), Inches(1.7), RGBColor(0x25, 0x15, 0x15), ACCENT_RED, Pt(2))
txt(slide, Inches(0.7), Inches(5.55), Inches(11.5), Inches(0.4), "⚠️ 9 anomalies architecturales majeures identifiées", size=16, color=ACCENT_RED, bold=True)
bullets(slide, Inches(0.7), Inches(5.95), Inches(5.5), Inches(1.2), [
    "🔴 Accès JDBC direct du front vers la BDD (contourne le back-end)",
    "🔴 Logique métier éparpillée : front + back + BDD (PL/SQL)",
    "🔴 WCF VB.NET sans code source — SPOF sur la gestion stocks",
], size=11, color=LIGHT_GRAY)
bullets(slide, Inches(6.5), Inches(5.95), Inches(6), Inches(1.2), [
    "🔴 Batch CSV quotidien SAP → 24h de latence sur les stocks",
    "🔴 FTP sans Git — aucun contrôle de version",
    "🟠 Oracle 11g R2 surdimensionné et coûteux",
], size=11, color=LIGHT_GRAY)

# ═══════════════════════════════════════
# SLIDE 7 : POINTS FAIBLES
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "4. Points faibles identifiés")

pf_data = [
    ("PF-01", "Monolithe obsolète", "🔴 Critique"),
    ("PF-02", "Logique métier éparpillée (3 couches)", "🔴 Critique"),
    ("PF-03", "Stocks incohérents — perte de clients", "🔴 Critique"),
    ("PF-04", "WCF sans code source — SPOF absolu", "🔴 Critique"),
    ("PF-05", "Pas de gestion de configuration (FTP)", "🔴 Critique"),
    ("PF-06", "BDD Oracle surdimensionnée & coûteuse", "🟠 Élevé"),
    ("PF-07", "Sécurité insuffisante", "🟠 Élevé"),
    ("PF-08", "Dette humaine & organisationnelle", "🟠 Élevé"),
    ("PF-09", "Marque blanche non compétitive", "🟡 Modéré"),
]
for i, (pid, desc, crit) in enumerate(pf_data):
    y = Inches(1.3 + i * 0.62)
    if "Critique" in crit:
        c, bg = ACCENT_RED, RGBColor(0x30, 0x1a, 0x1a)
    elif "Élevé" in crit:
        c, bg = ACCENT_ORANGE, RGBColor(0x30, 0x25, 0x1a)
    else:
        c, bg = ACCENT_YELLOW, RGBColor(0x30, 0x2e, 0x1a)
    add_box(slide, Inches(1), y, Inches(11), Inches(0.52), bg, c, Pt(1))
    txt(slide, Inches(1.2), y + Inches(0.05), Inches(1.5), Inches(0.4), pid, size=14, color=c, bold=True)
    txt(slide, Inches(2.8), y + Inches(0.05), Inches(7), Inches(0.4), desc, size=14, color=WHITE)
    txt(slide, Inches(10.2), y + Inches(0.05), Inches(1.5), Inches(0.4), crit, size=11, color=c, align=PP_ALIGN.RIGHT)

# ═══════════════════════════════════════
# SLIDE 8 : ENF
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "5. Exigences Non Fonctionnelles")

enf_data = [
    ("ENF-01", "Performance", "Catalogue < 2s, APIs < 500ms, pics x3", "★★★★★", ACCENT_RED),
    ("ENF-02", "Disponibilité", "SLA ≥ 99,5%, RTO < 4h, RPO < 1h", "★★★★★", ACCENT_RED),
    ("ENF-03", "Scalabilité", "Scale-out, expansion EU, B2C/B2B", "★★★★☆", ACCENT_ORANGE),
    ("ENF-04", "Sécurité", "IAM centralisé, RGPD, PCI-DSS", "★★★★★", ACCENT_RED),
    ("ENF-05", "Maintenabilité", "Tests ≥ 70%, zéro PL/SQL, OpenAPI", "★★★★★", ACCENT_RED),
    ("ENF-06", "Interopérabilité", "REST SAP, Stripe v3, Power BI", "★★★★☆", ACCENT_ORANGE),
    ("ENF-07", "Portabilité", "Cloud-ready, Docker, CI/CD", "★★★☆☆", ACCENT_YELLOW),
    ("ENF-08", "Observabilité", "Logs centralisés, alertes auto", "★★★☆☆", ACCENT_YELLOW),
]
for i, (eid, name, desc, stars, color) in enumerate(enf_data):
    y = Inches(1.3 + i * 0.7)
    add_box(slide, Inches(1), y, Inches(11), Inches(0.58), CARD_BG, color, Pt(1))
    txt(slide, Inches(1.2), y + Inches(0.08), Inches(1.5), Inches(0.4), eid, size=13, color=color, bold=True)
    txt(slide, Inches(2.7), y + Inches(0.08), Inches(2), Inches(0.4), name, size=14, color=WHITE, bold=True)
    txt(slide, Inches(5), y + Inches(0.08), Inches(5), Inches(0.4), desc, size=12, color=LIGHT_GRAY)
    txt(slide, Inches(10.2), y + Inches(0.08), Inches(1.5), Inches(0.4), stars, size=13, color=ACCENT_YELLOW, align=PP_ALIGN.RIGHT)

# ═══════════════════════════════════════
# SLIDE 9 : AXES D'AMELIORATION
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "6. Axes d'amélioration")

axes = [
    ("AXE-01", "Refonte architecture modulaire", "→ PF-01, PF-02, PF-03", ACCENT_GREEN),
    ("AXE-02", "Stocks temps réel (événementiel SAP)", "→ PF-03, PF-04", ACCENT_TEAL),
    ("AXE-03", "Git + CI/CD", "→ PF-05, PF-08", ACCENT_BLUE),
    ("AXE-04", "Migration cloud & rationalisation coûts", "→ PF-01, PF-06", ACCENT_PURPLE),
    ("AXE-05", "Sécurité & conformité RGPD", "→ PF-07", ACCENT_ORANGE),
    ("AXE-06", "Marque blanche SaaS multi-tenant", "→ PF-09", ACCENT_YELLOW),
]
for i, (aid, desc, refs, color) in enumerate(axes):
    x = Inches(0.8 + (i % 3) * 4.0)
    y = Inches(1.4 + (i // 3) * 2.6)
    add_box(slide, x, y, Inches(3.6), Inches(2.0), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.2), y + Inches(0.15), Inches(3.2), Inches(0.5), aid, size=20, color=color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.2), y + Inches(0.7), Inches(3.2), Inches(0.6), desc, size=15, color=WHITE, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.2), y + Inches(1.3), Inches(3.2), Inches(0.4), refs, size=12, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)

# Save
prs.save(OUTPUT)
print(f"Part 1 saved: {OUTPUT}")
