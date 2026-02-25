# -*- coding: utf-8 -*-
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

OUTPUT = r"c:\Users\Loris\Documents\bricoloc\maelJtm\07-presentation\BricoLoc2_Presentation.pptx"
prs = Presentation(OUTPUT)

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

def add_down_arrow(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False

def add_right_arrow(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False

def add_left_arrow(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.LEFT_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False

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
# SLIDE 10 : COMPARAISON STYLES
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "7. Comparaison des styles architecturaux")

styles_data = [
    ("Monolithe modulaire", "40/55", "✅ Retenu", ACCENT_GREEN),
    ("Événementiel ciblé", "40/55", "✅ Retenu", ACCENT_GREEN),
    ("Microservices", "39/55", "❌ Trop complexe pour 5 devs", ACCENT_RED),
    ("SOA / ESB", "33/55", "❌ ESB disproportionné", ACCENT_RED),
    ("N-tiers (actuel)", "23/55", "❌ Source des problèmes", ACCENT_RED),
]

# Header
add_box(slide, Inches(1), Inches(1.3), Inches(11), Inches(0.55), RGBColor(0x25, 0x25, 0x45), ACCENT_BLUE, Pt(1))
txt(slide, Inches(1.2), Inches(1.35), Inches(3.5), Inches(0.4), "Style", size=15, color=ACCENT_BLUE, bold=True)
txt(slide, Inches(5), Inches(1.35), Inches(2), Inches(0.4), "Score", size=15, color=ACCENT_BLUE, bold=True, align=PP_ALIGN.CENTER)
txt(slide, Inches(7), Inches(1.35), Inches(4.5), Inches(0.4), "Verdict BricoLoc", size=15, color=ACCENT_BLUE, bold=True)

for i, (style, score, verdict, color) in enumerate(styles_data):
    y = Inches(1.95 + i * 0.65)
    bg = RGBColor(0x1e, 0x2e, 0x1e) if "✅" in verdict else RGBColor(0x2e, 0x1e, 0x1e)
    add_box(slide, Inches(1), y, Inches(11), Inches(0.55), bg, color, Pt(1))
    txt(slide, Inches(1.2), y + Inches(0.08), Inches(3.5), Inches(0.4), style, size=15, color=WHITE, bold=True)
    txt(slide, Inches(5), y + Inches(0.08), Inches(2), Inches(0.4), score, size=15, color=color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, Inches(7), y + Inches(0.08), Inches(4.5), Inches(0.4), verdict, size=14, color=color)

txt(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.8), "Recommandation : architecture hybride\nMonolithe modulaire + Événementiel ciblé + APIs REST (SOA légère sans ESB)", size=18, color=ACCENT_GREEN, bold=True, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════
# SLIDE 11 : STYLES RETENUS
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "8. Styles retenus & justification")

retained = [
    ("Monolithe modulaire", "Core applicatif", "1 JAR, 9 modules Maven isolés\nFaisable par 5 devs, ACID natif\nStrangler Fig compatible", ACCENT_PURPLE),
    ("Événementiel ciblé", "Stocks & notifications", "RabbitMQ sur flux asynchrones\nRemplace batch CSV quotidien\nIsole les pannes", ACCENT_ORANGE),
    ("APIs REST", "Intégrations & marque blanche", "Contrats OpenAPI versionnés\nSOA légère sans ESB\nPartenaires en self-service", ACCENT_TEAL),
]
for i, (title, scope, desc, color) in enumerate(retained):
    x = Inches(0.8 + i * 4.0)
    add_box(slide, x, Inches(1.3), Inches(3.6), Inches(3.8), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.2), Inches(1.45), Inches(3.2), Inches(0.5), title, size=20, color=color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.2), Inches(2.0), Inches(3.2), Inches(0.4), scope, size=14, color=ACCENT_YELLOW, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.2), Inches(2.6), Inches(3.2), Inches(2), desc, size=13, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

txt(slide, Inches(0.8), Inches(5.5), Inches(11), Inches(0.5), "Styles écartés :", size=16, color=ACCENT_RED, bold=True)
txt(slide, Inches(0.8), Inches(6.0), Inches(11), Inches(1), "Microservices purs (complexité DevOps)  ·  SOA/ESB (disproportionné PME)  ·  N-tiers reconduit (source des problèmes)  ·  Serverless (incompatible état persistant)", size=14, color=SUBTLE_WHITE)

# ═══════════════════════════════════════
# SLIDE 12 : CHOIX TECHNOLOGIQUES
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "9. Choix technologiques")

tech_choices = [
    ("Framework back-end", "Spring Boot 3", "4,90/5", "Compétences équipe\nMigration incrémentale Spring 5\nOpen-source", ACCENT_GREEN),
    ("SGBDR", "PostgreSQL 16", "4,60/5", "Open-source, cloud-natif\nÉlimine surcoût Oracle\nPL/pgSQL compatible", ACCENT_TEAL),
    ("Bus de messages", "RabbitMQ", "4,55/5", "Simple pour 5 devs\nCompatible Spring AMQP\nAdapté aux volumes BricoLoc", ACCENT_ORANGE),
    ("Cloud", "Microsoft Azure", "4,75/5", "Continuité écosystème MS\nAzure AD, Power BI, Office 365\nSupport PostgreSQL managé", ACCENT_PURPLE),
]
for i, (decision, tech, score, justif, color) in enumerate(tech_choices):
    x = Inches(0.6 + (i % 2) * 6.2)
    y = Inches(1.3 + (i // 2) * 3.0)
    add_box(slide, x, y, Inches(5.8), Inches(2.5), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.2), y + Inches(0.1), Inches(3.5), Inches(0.5), decision, size=14, color=SUBTLE_WHITE)
    txt(slide, x + Inches(0.2), y + Inches(0.5), Inches(3.5), Inches(0.5), tech, size=22, color=color, bold=True)
    txt(slide, x + Inches(4), y + Inches(0.3), Inches(1.5), Inches(0.5), score, size=20, color=ACCENT_YELLOW, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.2), y + Inches(1.1), Inches(5.2), Inches(1.2), justif, size=12, color=LIGHT_GRAY)

# ═══════════════════════════════════════
# SLIDE 13 : ARCHITECTURE LOGIQUE (CORRIGÉ - avec interactions fléchées)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "10. Architecture logique — Vue d'ensemble")

# --- COUCHE CLIENTS ---
add_box(slide, Inches(2), Inches(1.2), Inches(9), Inches(0.7), RGBColor(0x1a, 0x3a, 0x5c), ACCENT_BLUE, Pt(2))
txt(slide, Inches(2.2), Inches(1.25), Inches(8.5), Inches(0.3), "🌐 Couche Clients — Web · Mobile · Partenaires · Salariés SSO", size=14, color=ACCENT_BLUE, bold=True)

# Arrow down
add_down_arrow(slide, Inches(6.4), Inches(1.92), Inches(0.4), Inches(0.35), ACCENT_BLUE)
txt(slide, Inches(6.9), Inches(1.92), Inches(1.5), Inches(0.3), "HTTPS", size=10, color=ACCENT_BLUE, bold=True)

# --- API GATEWAY ---
add_box(slide, Inches(2), Inches(2.3), Inches(9), Inches(0.7), RGBColor(0x1a, 0x3c, 0x3a), ACCENT_TEAL, Pt(2))
txt(slide, Inches(2.2), Inches(2.35), Inches(8.5), Inches(0.3), "🔒 API Gateway — Spring Cloud Gateway — JWT · Rate Limit · TLS · Routage /api/v1/", size=14, color=ACCENT_TEAL, bold=True)

# Arrow down
add_down_arrow(slide, Inches(6.4), Inches(3.02), Inches(0.4), Inches(0.35), ACCENT_TEAL)
txt(slide, Inches(6.9), Inches(3.02), Inches(2.5), Inches(0.3), "Route authentifiée", size=10, color=ACCENT_TEAL, bold=True)

# --- MONOLITHE MODULAIRE ---
add_box(slide, Inches(2), Inches(3.4), Inches(9), Inches(1.5), RGBColor(0x2a, 0x1a, 0x4a), ACCENT_PURPLE, Pt(3))
txt(slide, Inches(2.2), Inches(3.42), Inches(8.5), Inches(0.35), "⚙️ Monolithe Modulaire — Spring Boot 3 / Java 21", size=14, color=ACCENT_PURPLE, bold=True)
# 9 modules as small boxes in a grid
mods = ["📦 Catalogue", "📅 Réservation", "📊 Stocks", "💳 Paiement", "👥 Utilisateurs", "🔔 Notifications", "🛠️ Admin", "🏷️ Marque Blanche", "🔗 Intégration"]
for mi, mod in enumerate(mods):
    mx = Inches(2.2 + (mi % 3) * 2.95)
    my = Inches(3.8 + (mi // 3) * 0.35)
    txt(slide, mx, my, Inches(2.8), Inches(0.3), mod, size=10, color=LIGHT_GRAY)

# Arrow down to event bus
add_down_arrow(slide, Inches(5.0), Inches(4.92), Inches(0.4), Inches(0.35), ACCENT_ORANGE)
txt(slide, Inches(5.5), Inches(4.92), Inches(1.5), Inches(0.3), "Publie", size=10, color=ACCENT_ORANGE, bold=True)
# Arrow up from event bus
shape = slide.shapes.add_shape(MSO_SHAPE.UP_ARROW, Inches(7.5), Inches(4.92), Inches(0.4), Inches(0.35))
shape.fill.solid()
shape.fill.fore_color.rgb = ACCENT_ORANGE
shape.line.fill.background()
shape.shadow.inherit = False
txt(slide, Inches(7.95), Inches(4.92), Inches(1.5), Inches(0.3), "Consomme", size=10, color=ACCENT_ORANGE, bold=True)

# --- BUS ÉVÉNEMENTIEL ---
add_box(slide, Inches(2), Inches(5.3), Inches(9), Inches(0.7), RGBColor(0x3a, 0x2a, 0x1a), ACCENT_ORANGE, Pt(2))
txt(slide, Inches(2.2), Inches(5.33), Inches(8.5), Inches(0.3), "📨 Bus Événementiel — RabbitMQ", size=14, color=ACCENT_ORANGE, bold=True)
txt(slide, Inches(2.2), Inches(5.63), Inches(8.5), Inches(0.3), "StockUpdated · ReservationCreated/Confirmed · PaymentValidated · PriceUpdated · StockLow", size=10, color=LIGHT_GRAY)

# Arrow down
add_down_arrow(slide, Inches(6.4), Inches(6.02), Inches(0.4), Inches(0.35), ACCENT_GREEN)
txt(slide, Inches(6.9), Inches(6.02), Inches(2.5), Inches(0.3), "Persistance & Cache", size=10, color=ACCENT_GREEN, bold=True)

# --- COUCHE DONNÉES ---
add_box(slide, Inches(2), Inches(6.4), Inches(9), Inches(0.7), RGBColor(0x1a, 0x3a, 0x1a), ACCENT_GREEN, Pt(2))
txt(slide, Inches(2.2), Inches(6.43), Inches(8.5), Inches(0.3), "💾 Couche Données — PostgreSQL 16 (schéma/module) · Redis (cache) · Azure Blob Storage", size=14, color=ACCENT_GREEN, bold=True)

# --- SYSTÈMES TIERS (côté droit) ---
add_box(slide, Inches(0.2), Inches(3.0), Inches(1.6), Inches(4.2), RGBColor(0x3a, 0x1a, 0x2a), ACCENT_RED, Pt(2))
txt(slide, Inches(0.25), Inches(3.05), Inches(1.5), Inches(0.35), "🌍 Systèmes Tiers", size=11, color=ACCENT_RED, bold=True, align=PP_ALIGN.CENTER)
bullets(slide, Inches(0.25), Inches(3.4), Inches(1.5), Inches(3.5), [
    "📋 SAP B1", "   (Stocks/Compta)", "",
    "💳 Stripe", "   (Paiement)", "",
    "📊 Comp. Prix", "   (SaaS)", "",
    "📈 Power BI", "   (Analytics)",
], size=9, color=LIGHT_GRAY)

# Arrows Tiers ↔ Monolithe
add_right_arrow(slide, Inches(1.82), Inches(3.8), Inches(0.5), Inches(0.25), ACCENT_RED)
add_left_arrow(slide, Inches(1.82), Inches(4.3), Inches(0.5), Inches(0.25), ACCENT_RED)
txt(slide, Inches(1.0), Inches(4.58), Inches(1.0), Inches(0.25), "REST &\nWebhooks", size=8, color=ACCENT_RED, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════
# SLIDE 14 : MODULES + INTERACTIONS (CORRIGÉ)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "10b. Modules & interactions événementielles")

# 9 modules as cards
modules = [
    ("📦 Catalogue", "Outils, catégories\nRecherche, prix\nCache Redis", ACCENT_BLUE),
    ("📅 Réservation", "Cycle de vie location\nCalendrier, P2P\nAnnulation", ACCENT_TEAL),
    ("📊 Stocks", "Source de vérité\nTemps réel SAP\nInter-entrepôts", ACCENT_ORANGE),
    ("💳 Paiement", "Stripe v3, PCI-DSS\nTransactions\nRemboursements", ACCENT_RED),
    ("👥 Utilisateurs", "Auth JWT, RBAC\n5 rôles métier\nRGPD, Azure AD", ACCENT_PURPLE),
    ("🔔 Notifications", "Emails transac.\nAlertes logisticiens\nChat, Push", ACCENT_YELLOW),
    ("🛠️ Admin", "Back-office\nGestion catalogue\nGestion partenaires", ACCENT_GREEN),
    ("🏷️ Marque Blanche", "Multi-tenant\nIsolation données\nAPIs partenaire", RGBColor(0xFF, 0x80, 0xAB)),
    ("🔗 Intégration", "Passerelle unique\nSAP, Prix, Power BI\nSpring Batch", RGBColor(0x82, 0xB1, 0xFF)),
]
for i, (name, desc, color) in enumerate(modules):
    x = Inches(0.4 + (i % 3) * 4.2)
    y = Inches(1.2 + (i // 3) * 1.65)
    add_box(slide, x, y, Inches(3.8), Inches(1.35), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.1), y + Inches(0.05), Inches(3.6), Inches(0.35), name, size=14, color=color, bold=True)
    txt(slide, x + Inches(0.1), y + Inches(0.4), Inches(3.6), Inches(0.9), desc, size=11, color=LIGHT_GRAY)

# Interactions panel on the right
add_box(slide, Inches(0.4), Inches(6.15), Inches(12.5), Inches(1.15), RGBColor(0x25, 0x20, 0x35), ACCENT_PURPLE, Pt(2))
txt(slide, Inches(0.6), Inches(6.18), Inches(12), Inches(0.35), "🔀 Flux événementiels (RabbitMQ)", size=14, color=ACCENT_PURPLE, bold=True)
bullets(slide, Inches(0.6), Inches(6.5), Inches(4), Inches(0.8), [
    "Stocks → StockUpdated → Catalogue, Notifications",
    "Stocks → StockLow → Admin, Notifications",
], size=11, color=LIGHT_GRAY)
bullets(slide, Inches(4.8), Inches(6.5), Inches(4), Inches(0.8), [
    "Réservation → ReservationCreated → Paiement, Notifications",
    "Paiement → PaymentValidated → Réservation",
], size=11, color=LIGHT_GRAY)
bullets(slide, Inches(9.2), Inches(6.5), Inches(3.5), Inches(0.8), [
    "Intégration → PriceUpdated → Catalogue",
    "Tous événements → Notifications",
], size=11, color=LIGHT_GRAY)

# ═══════════════════════════════════════
# SLIDE 15 : MIGRATION STRANGLER FIG
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "11. Stratégie de migration — Strangler Fig")

phases = [
    ("Phase 0", "2-3 mois", "Fondations\nGit, CI/CD\nPostgreSQL", ACCENT_BLUE),
    ("Phase 1", "3-4 mois", "Stocks\n+ RabbitMQ", ACCENT_TEAL),
    ("Phase 2", "2-3 mois", "Utilisateurs\n& Auth", ACCENT_GREEN),
    ("Phase 3", "4-6 mois", "Catalogue\n& Réservation", ACCENT_PURPLE),
    ("Phase 4", "2-3 mois", "Paiement\n& Notifications", ACCENT_ORANGE),
    ("Phase 5", "3-4 mois", "Marque blanche\n& i18n", ACCENT_YELLOW),
    ("Phase 6", "1-2 mois", "Extinction\nWCF & Legacy", ACCENT_RED),
]
for i, (phase, duration, desc, color) in enumerate(phases):
    x = Inches(0.5 + i * 1.75)
    add_box(slide, x, Inches(1.5), Inches(1.55), Inches(4.5), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.05), Inches(1.6), Inches(1.45), Inches(0.45), phase, size=14, color=color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.05), Inches(2.1), Inches(1.45), Inches(0.4), duration, size=12, color=ACCENT_YELLOW, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.05), Inches(2.6), Inches(1.45), Inches(3), desc, size=11, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

add_box(slide, Inches(0.5), Inches(6.3), Inches(12.3), Inches(0.06), ACCENT_GREEN)
txt(slide, Inches(0.5), Inches(6.5), Inches(12), Inches(0.4), "Migration progressive — coexistence ancien / nouveau système — aucun Big Bang", size=14, color=ACCENT_GREEN, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════
# SLIDE 16 : REGLES D'ARCHITECTURE
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "Règles d'architecture (garde-fous)")

rules = [
    ("R01", "Aucun module ne peut accéder directement aux tables d'un autre module"),
    ("R02", "Zéro logique métier dans les couches de persistance (pas de triggers/PL/SQL)"),
    ("R03", "Toute communication avec un système tiers passe par le module Intégration"),
    ("R04", "Toute requête externe passe par l'API Gateway avec un token JWT valide"),
    ("R05", "Aucune donnée de carte bancaire ne transite côté BricoLoc (tout chez Stripe)"),
    ("R06", "Chaque module possède son propre schéma de BDD logique"),
    ("R07", "Chaque événement publié sur RabbitMQ est versionné (v1.StockUpdated)"),
    ("R08", "Tout code est committé sur Git — aucun déploiement manuel FTP"),
]
for i, (rid, desc) in enumerate(rules):
    y = Inches(1.3 + i * 0.72)
    add_box(slide, Inches(1), y, Inches(11), Inches(0.6), CARD_BG, ACCENT_PURPLE, Pt(1))
    txt(slide, Inches(1.2), y + Inches(0.1), Inches(1), Inches(0.4), rid, size=15, color=ACCENT_PURPLE, bold=True)
    txt(slide, Inches(2.3), y + Inches(0.1), Inches(9.2), Inches(0.4), desc, size=14, color=WHITE)

# ═══════════════════════════════════════
# SLIDE 17 : EQUIPE DEV
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_title(slide, "Répartition équipe développeurs BricoLoc")

devs = [
    ("Marion H.", "Java back-end", "reservation\nstocks", ACCENT_BLUE),
    ("Piotr S.", "Java full-stack", "catalogue\nadmin", ACCENT_TEAL),
    ("Thibaut E.", "Java back-end", "utilisateurs\nmarque-blanche", ACCENT_PURPLE),
    ("Hervé D.", ".NET / Java", "paiement\nintégration", ACCENT_ORANGE),
    ("Isabelle A.", "Python / Data", "analytics\nPower BI · tests", ACCENT_GREEN),
]
for i, (name, profile, modules, color) in enumerate(devs):
    x = Inches(0.5 + i * 2.5)
    add_box(slide, x, Inches(1.5), Inches(2.3), Inches(3.5), CARD_BG, color, Pt(2))
    txt(slide, x + Inches(0.1), Inches(1.7), Inches(2.1), Inches(0.5), name, size=18, color=color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.1), Inches(2.3), Inches(2.1), Inches(0.5), profile, size=13, color=ACCENT_YELLOW, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.1), Inches(3.0), Inches(2.1), Inches(1.5), modules, size=13, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

txt(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.5), "Chaque développeur possède un périmètre clair → limite les conflits Git, distribue la complexité", size=14, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════
# SLIDE 18 : CONCLUSION
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
add_box(slide, Inches(0), Inches(3.2), Inches(13.333), Inches(0.08), ACCENT_GREEN)
txt(slide, Inches(1), Inches(1.0), Inches(11), Inches(1), "12. Conclusion & perspectives", size=40, color=ACCENT_GREEN, bold=True, align=PP_ALIGN.CENTER)

bullets(slide, Inches(2), Inches(2.2), Inches(9), Inches(3), [
    "✅  Architecture hybride adaptée : monolithe modulaire + événementiel + REST",
    "✅  Stack maîtrisée par l'équipe : Spring Boot 3, PostgreSQL 16, RabbitMQ, Azure",
    "✅  Migration progressive Strangler Fig : 7 phases, zéro Big Bang",
    "✅  Tous les points faibles adressés (PF-01 → PF-09)",
    "✅  8 règles d'architecture pour éviter les dérives du SI actuel",
], size=18, color=WHITE)

txt(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.5), "Perspectives", size=22, color=ACCENT_BLUE, bold=True, align=PP_ALIGN.CENTER)
bullets(slide, Inches(2), Inches(6.0), Inches(9), Inches(1.5), [
    "📈 Expansion européenne (Phase 5) — i18n et multi-entrepôts",
    "🔄 Extraction future en microservices si l'équipe grandit",
    "📱 Application mobile native (post-migration)",
], size=15, color=LIGHT_GRAY)

# ═══════════════════════════════════════
# SLIDE 19 : MERCI
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
add_box(slide, Inches(0), Inches(3.4), Inches(13.333), Inches(0.08), ACCENT_PURPLE)
txt(slide, Inches(1), Inches(2.0), Inches(11), Inches(1.2), "Merci pour votre attention", size=48, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(3.8), Inches(11), Inches(0.8), "Questions ?", size=32, color=ACCENT_PURPLE, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.5), "Romain  ·  Maëlle  ·  Loris", size=22, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(6.0), Inches(11), Inches(0.5), "Master 1 Architecte d'Application — CESI", size=16, color=SUBTLE_WHITE, align=PP_ALIGN.CENTER)

prs.save(OUTPUT)
print(f"DONE: {OUTPUT}")
print(f"Total slides: {len(prs.slides)}")
