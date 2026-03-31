
# =====================================================================
# SLIDE 9 : STRATÉGIE DE MIGRATION
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "8. Stratégie de Migration (Strangler Fig)", "Mise en place progressive par remplacement du legacy")

phases = [
    ("0", "2-3 mois", "Fondations", "Mettre en place CI/CD\nGit et l'API Gateway"),
    ("1", "3-4 mois", "Stocks", "Remplacer le batch CSV\nRabbitMQ connecté à SAP"),
    ("2", "2-3 mois", "Comptes", "IAM centralisé (JWT)\nFin des accès BDD directs"),
    ("3", "4-6 mois", "Catalogue", "Migration du Core\nbricolocDB -> PostgreSQL"),
    ("4", "2-3 mois", "Paiement", "Sécurisation Stripe v3\nPaiements déportés"),
    ("5", "3-4 mois", "SaaS B2B", "Ouverture partenaires\nvia les nouvelles APIs"),
]

chevron_h = Inches(1.4)
chevron_w = Inches(1.8)
gap = Inches(0.1)
y_flow = Inches(1.4)

shades = [TERRACOTTA, TAUPE, BLUSH, SAND_LIGHT, TERRACOTTA, TAUPE]
txt_c = [WHITE_BG, WHITE_BG, TEXT_DARK, TEXT_DARK, WHITE_BG, WHITE_BG]

anim_groups = []
for i, (num, duration, label, desc) in enumerate(phases):
    x = Inches(0.5) + i * (chevron_w + gap)
    phase_shapes = []
    
    phase_shapes.append(add_chevron(slide, x, y_flow, chevron_w, chevron_h, shades[i]))
    phase_shapes.append(txt(slide, x + Inches(0.4), y_flow + Inches(0.15), Inches(0.9), Inches(0.35), num, size=24, color=txt_c[i], bold=True, align=PP_ALIGN.CENTER))
    phase_shapes.append(txt(slide, x + Inches(0.1), y_flow + Inches(0.6), Inches(1.6), Inches(0.7), label, size=11, color=txt_c[i], bold=True, align=PP_ALIGN.CENTER))
    
    y_card = Inches(3.1)
    phase_shapes.append(add_box(slide, x, y_card, chevron_w, Inches(2.2), WHITE_BG, BORDER, Pt(1)))
    phase_shapes.append(add_rect(slide, x, y_card, chevron_w, Inches(0.05), shades[i]))
    phase_shapes.append(txt(slide, x + Inches(0.05), y_card + Inches(0.15), chevron_w - Inches(0.1), Inches(0.35), duration, size=13, color=TERRACOTTA, bold=True, align=PP_ALIGN.CENTER))
    phase_shapes.append(txt(slide, x + Inches(0.05), y_card + Inches(0.65), chevron_w - Inches(0.1), Inches(1.5), desc, size=11, color=TEXT_MID, align=PP_ALIGN.CENTER))
    
    anim_groups.append(phase_shapes)

add_rect(slide, Inches(0.5), Inches(5.8), Inches(12.3), Inches(0.04), TERRACOTTA)
txt(slide, Inches(0.5), Inches(5.95), Inches(12.3), Inches(0.4), "Migration progressive de 18 à 24 mois sans interruption de service (Strangler Pattern)", size=14, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)

add_logo(slide)
add_fade_on_click(slide, anim_groups)
add_notes(slide, "Une refonte Big Bang étant impossible, nous utiliserons le Strangler Pattern. Nous commençons par brancher RabbitMQ sur SAP (Phase 1) pour stopper l'hémorragie des mauvaises locations.")

# =====================================================================
# SLIDE 10 : RISQUES & SÉCURITÉ
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "9. Analyse des Risques & Sécurité", "Politiques pour pérenniser l'architecture")

rules = [
    ("Sécurité IAM et Données", "Passage à une API Gateway et tokens JWT (plus d'accès directs depuis le front). Données de carte bancaire isolées (Stripe v3, aucune trace BDD locale)."),
    ("Prévention de la Dette Technique", "Fini le développement dans Oracle PL/SQL. Toute la logique métier est versionnée sur Git et testée automatiquement (CI/CD)."),
    ("Plan de Reprise (PRA)", "Infrastructure as Code. SI hébergé sur OVHcloud avec bases managées répliquées multi-AZ (vRack). Sauvegardes froides externalisées.")
]

anim_groups = []
for i, (cat, desc) in enumerate(rules):
    y = Inches(1.8 + i * 1.5)
    grp = []
    x = Inches(0.8)
    grp.append(add_box(slide, x, y, Inches(11.5), Inches(1.2), WHITE_BG, BORDER, Pt(1)))
    grp.append(add_rect(slide, x, y, Inches(0.08), Inches(1.2), TERRACOTTA))
    grp.append(txt(slide, x + Inches(0.3), y + Inches(0.2), Inches(3.0), Inches(0.8), cat, size=16, color=TEXT_DARK, bold=True))
    grp.append(txt(slide, x + Inches(3.5), y + Inches(0.2), Inches(7.5), Inches(0.8), desc, size=13, color=TEXT_MID))
    
    _rule_icons = ["shield", "gear", "cloud"]
    grp.append(add_icon(slide, _rule_icons[i], Inches(11.3), y + Inches(0.4), Inches(0.5)))
    anim_groups.append(grp)

add_logo(slide)
add_fade_on_click(slide, anim_groups)
add_notes(slide, "La sécurité est adressée via un point d'entrée unique API gateway. La dette technique est prévenue par la CI/CD.")

# =====================================================================
# SLIDE 11 : AMÉLIORATION CONTINUE & BILAN
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "10. Amélioration Continue & Bilan du Projet")

# Points forts
add_box(slide, Inches(0.8), Inches(1.5), Inches(5.5), Inches(3.5), WHITE_BG, BORDER, Pt(1))
add_rect(slide, Inches(0.8), Inches(1.5), Inches(5.5), Inches(0.08), TERRACOTTA)
txt(slide, Inches(1.0), Inches(1.7), Inches(5.0), Inches(0.4), "Points forts du groupe", size=16, color=TERRACOTTA, bold=True)
strengths = [
    "Absorption de la charge (-25 %) sans retards suite au départ d'un membre",
    "Forte traçabilité entre Les Exigences (ENF) et les Choix cloud/Archi",
    "Revue croisée de tous les livrables avant validation"
]
for i, item in enumerate(strengths):
    y = Inches(2.2 + i * 0.8)
    add_circle(slide, Inches(1.2), y + Inches(0.05), Inches(0.2), TERRACOTTA)
    txt(slide, Inches(1.6), y, Inches(4.5), Inches(0.7), item, size=13, color=TEXT_DARK)

# Axes d'amélioration
add_box(slide, Inches(6.8), Inches(1.5), Inches(5.5), Inches(3.5), WHITE_BG, BORDER, Pt(1))
add_rect(slide, Inches(6.8), Inches(1.5), Inches(5.5), Inches(0.08), TAUPE)
txt(slide, Inches(7.0), Inches(1.7), Inches(5.0), Inches(0.4), "Axes d'amélioration", size=16, color=TAUPE, bold=True)
improves = [
    "Anticiper le 'Bus Factor' (départ membres)",
    "Documenter les ADR plus tôt (Architecture Decision Records)",
    "Formaliser des cérémonies de l'équipe (rituels Agile)"
]
for i, item in enumerate(improves):
    y = Inches(2.2 + i * 0.8)
    add_circle(slide, Inches(7.2), y + Inches(0.05), Inches(0.2), TAUPE)
    txt(slide, Inches(7.6), y, Inches(4.5), Inches(0.7), item, size=13, color=TEXT_DARK)

add_logo(slide)
add_notes(slide, "D'un point de vue organisationnel, nous avons réussi à palier un départ sans déborder, mais nous devons formaliser nos documentations d'architecture (ADR) plus tôt.")

# =====================================================================
# SLIDE 12 : CONCLUSION
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "11. Conclusion : BricoLoc demain", "Un SI prêt pour l'international et la Marque Blanche")

conclusions = [
    ("Une Architecture Maîtrisée", "Pensée pour l'équipe (5 devs)\nÉvite la suringénierie (pas de Kubernetes)", TERRACOTTA, WHITE_BG),
    ("Le Core Restauré (Stocks)", "Outil asynchrone pour des stocks en temps réel\nStoppe la fuite de clients", TAUPE, WHITE_BG),
    ("L'Ouverture vers l'Europe", "Cloud OVHcloud réplicable à Bruxelles\nStratégie B2B SaaS prête grâce aux APIs", BLUSH, TEXT_DARK),
]
for i, (title, desc, shade, txt_color) in enumerate(conclusions):
    x = Inches(0.5 + i * 4.1)
    # Background and card setup
    add_box(slide, x, Inches(1.5), Inches(3.8), Inches(3.0), shade, BORDER, Pt(1))
    txt(slide, x + Inches(0.2), Inches(1.7), Inches(3.4), Inches(0.8), title, size=18, color=txt_color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.3), Inches(2.6), Inches(3.2), Inches(1.6), desc, size=14, color=txt_color, align=PP_ALIGN.CENTER)

add_rect(slide, Inches(0.5), Inches(5.5), Inches(12.3), Inches(0.04), SAND_LIGHT)
txt(slide, Inches(0.5), Inches(5.8), Inches(12.3), Inches(0.5), "Le BricoLoc de demain n'est plus une 'grande boule de boue', mais un moteur d'innovation serein.", size=16, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)

add_logo(slide)

# =====================================================================
# SLIDE 13 : Q&A
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)

add_rect(slide, Inches(5), Inches(3.4), Inches(3.333), Inches(0.04), TERRACOTTA)
txt(slide, Inches(1), Inches(2.0), Inches(11.333), Inches(1.2), "Merci de votre attention", size=48, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(3.8), Inches(11.333), Inches(0.8), "Des questions sur l'architecture ?", size=32, color=TERRACOTTA, align=PP_ALIGN.CENTER)

add_rect(slide, Inches(5.5), Inches(4.8), Inches(2.333), Inches(0.025), SAND_LIGHT)
txt(slide, Inches(1), Inches(5.1), Inches(11.333), Inches(0.5), "Romain  ·  Maël  ·  Loris", size=22, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)

add_logo(slide)

# =====================================================================
# GLOBAL DECORATIONS
# =====================================================================
total_slides = len(prs.slides)
for idx, slide in enumerate(prs.slides):
    trans = etree.SubElement(slide._element, qn('p:transition'))
    trans.set('spd', 'med')
    etree.SubElement(trans, qn('p:fade'))

    num_box = txt(slide, Inches(12.0), Inches(7.1), Inches(1.0), Inches(0.3), f"{idx + 1} / {total_slides}", size=9, color=TEXT_LIGHT, align=PP_ALIGN.RIGHT)
    
    progress_w = int(prs.slide_width * ((idx + 1) / total_slides))
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, prs.slide_height - Inches(0.04), progress_w, Inches(0.04))
    bar.fill.solid()
    bar.fill.fore_color.rgb = TERRACOTTA
    bar.line.fill.background()
    bar.shadow.inherit = False

prs.save(OUTPUT)
print(f"DONE: {OUTPUT}")
print(f"Total slides: {total_slides}")
