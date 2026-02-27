
# =====================================================================
# SLIDE 5 : STRATÉGIE CLOUD — MATRICE DE CHOIX
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "4. Stratégie Cloud — Choix de l'Hébergeur", "Une matrice d'évaluation structurée selon nos contraintes européennes")

matrix_criteria = [
    ("Légal & Souveraineté (20%)", "Insensibilité au CLOUD Act américain, RGPD strict"),
    ("Sécurité & Confiance (25%)", "Certifications, SLAs, chiffrement"),
    ("Indépendance (25%)", "Réversibilité, limitation du vendor lock-in"),
    ("FinOps (20%)", "Prévisibilité des coûts réseau et de stockage"),
    ("Green IT (10%)", "Efficacité énergétique (PUE/WUE)"),
]

txt(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.4), "Critères d'évaluation pondérés", size=16, color=TERRACOTTA, bold=True)
anim_groups = []
for i, (title, desc) in enumerate(matrix_criteria):
    y = Inches(1.8 + i * 0.9)
    grp = []
    grp.append(add_box(slide, Inches(0.8), y, Inches(11.5), Inches(0.7), WHITE_BG, BORDER, Pt(1)))
    grp.append(add_circle(slide, Inches(1.0), y + Inches(0.15), Inches(0.4), SAND_LIGHT))
    grp.append(txt(slide, Inches(1.0), y + Inches(0.18), Inches(0.4), Inches(0.4), str(i + 1), size=12, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER))
    grp.append(txt(slide, Inches(1.6), y + Inches(0.18), Inches(3.5), Inches(0.4), title, size=14, color=TEXT_DARK, bold=True))
    grp.append(txt(slide, Inches(5.2), y + Inches(0.18), Inches(6.0), Inches(0.4), desc, size=12, color=TEXT_MID))
    anim_groups.append(grp)

add_logo(slide)
add_fade_on_click(slide, anim_groups)
add_notes(slide, "Nous avons évalué les offres selon 5 critères. La souveraineté et le FinOps ont été très discriminants face aux géants américains.")

# =====================================================================
# SLIDE 6 : JUSTIFICATION OVHCLOUD
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "5. Choix de l'Hébergeur : OVHcloud")

podium_w = Inches(3.2)
podium_base_y = Inches(6.8)
centers = [3.266, 6.666, 10.066]

cloud_data = [
    ("Scaleway", "4,40/5", "🥈 2ème", Inches(1.2), TAUPE, WHITE_BG, "server", "✓ Français très solide\n✓ RGPD\n✓ Facturation claire", "Briques cloud avancées parfois moins poussées"),
    ("OVHcloud", "4,50/5", "🥇 1er", TERRACOTTA, WHITE_BG, "cloud", "✓ Leader européen (100% RGPD)\n✓ Green IT (water-cooling)\n✓ Bande passante prévisible", "Moindre interopérabilité historique"),
    ("Microsoft Azure", "4,10/5", "🥉 3ème", SAND_LIGHT, TEXT_DARK, "globe", "✓ Intégration (Active Dir.)\n✓ Puissance technique", "Soumis au CLOUD Act américain\nCoûts difficiles à justifier")
]

anim_groups = []
def build_podium(i, name, score, medal, p_height, bg_col, txt_col, icon, strengths, weakness):
    cx = centers[i]
    x_left = Inches(cx) - podium_w/2
    y_top = podium_base_y - p_height
    grp = []
    border_col = BORDER if bg_col == SAND_LIGHT else bg_col
    grp.append(add_rect(slide, x_left, y_top, podium_w, p_height, bg_col, border_col))
    grp.append(txt(slide, x_left, y_top + Inches(0.08), podium_w, Inches(0.4), medal, size=18, color=txt_col, bold=True, align=PP_ALIGN.CENTER))
    grp.append(txt(slide, x_left, y_top + Inches(0.35), podium_w, Inches(0.4), score, size=20, color=txt_col, bold=True, align=PP_ALIGN.CENTER))
    
    card_h = Inches(3.2)
    card_y = y_top - card_h - Inches(0.15)
    grp.append(add_box(slide, x_left, card_y, podium_w, card_h, WHITE_BG, border_col, Pt(2)))
    grp.append(add_rect(slide, x_left, card_y, podium_w, Inches(0.08), bg_col))
    grp.append(txt(slide, x_left, card_y + Inches(0.15), podium_w, Inches(0.4), name, size=16, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER))
    grp.append(add_icon(slide, icon, x_left + podium_w/2 - Inches(0.2), card_y + Inches(0.55), Inches(0.4)))
    grp.append(txt(slide, x_left + Inches(0.15), card_y + Inches(1.15), podium_w - Inches(0.3), Inches(0.9), strengths, size=11, color=TEXT_DARK, align=PP_ALIGN.CENTER))
    grp.append(add_rect(slide, x_left + Inches(0.6), card_y + Inches(2.1), podium_w - Inches(1.2), Inches(0.01), SAND_LIGHT))
    grp.append(txt(slide, x_left + Inches(0.15), card_y + Inches(2.3), podium_w - Inches(0.3), Inches(0.7), weakness, size=10, color=TEXT_MID, align=PP_ALIGN.CENTER))
    return grp

for i, cd in enumerate(cloud_data):
    anim_groups.append(build_podium(i, *cd))

grp_notes = []
grp_notes.append(txt(slide, Inches(0.5), Inches(7.0), Inches(11.0), Inches(0.3), "Note : Google Cloud et AWS ont été écartés car soumis au CLOUD Act.", size=10, color=TEXT_LIGHT, align=PP_ALIGN.CENTER))
anim_groups.append(grp_notes)

add_logo(slide)
add_fade_on_click(slide, anim_groups)
add_notes(slide, "Le choix s'est porté sur OVHcloud. Pourquoi ? Parce que l'intégration technologique ne fait pas tout : nous devons protéger légalement nos données (RGPD européen) et maîtriser notre budget avec certitude.")

# =====================================================================
# SLIDE 7 : CHOIX DES STYLES ARCHITECTURAUX
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "6. Styles Architecturaux Retenus", "Pourquoi n'avons nous pas choisi les microservices purs ?")

# Rejected
add_box(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.9), SAND_LIGHT, BORDER, Pt(1))
txt(slide, Inches(1.0), Inches(1.35), Inches(11), Inches(0.4), "Approches écartées", size=14, color=TERRACOTTA, bold=True)
txt(slide, Inches(1.0), Inches(1.75), Inches(11), Inches(0.4), "Microservices (trop complexe pour 5 développeurs) · SOA/ESB (usne à gaz injustifiée) · N-tiers legacy", size=13, color=TEXT_MID)

# Retained
retained = [
    ("Monolithe Modulaire", "Cœur de l'application", "Spring Boot 3 / Java 21\n9 modules Maven isolés (clean archi).\nTransactions ACID préservées pour les réservations.", TERRACOTTA),
    ("Événementiel Ciblé", "Découplage temporel", "RabbitMQ (AMQP)\nPour les retours de stocks et notifications.\nRemplace le batch CSV.", TAUPE),
    ("APIs REST", "Intégration et Marque Blanche", "API Gateway (JWT) / OpenAPI.\nContrats d'interface propres avec SAP, Stripe.\nBase pour le SaaS futur.", BLUSH)
]

anim_groups = []
for i, (title, scope, desc, color) in enumerate(retained):
    x = Inches(0.8 + i * 4.0)
    grp = []
    grp.append(card_with_accent_top(slide, x, Inches(2.5), Inches(3.6), Inches(4.2), color))
    grp.append(txt(slide, x + Inches(0.2), Inches(2.7), Inches(3.2), Inches(0.5), title, size=18, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER))
    
    style_icons = ["gear", "message", "globe"]
    grp.append(add_icon(slide, style_icons[i], x + Inches(1.55), Inches(5.6), Inches(0.5)))
    
    scope_w = Inches(2.8)
    grp.append(add_box(slide, x + Inches(0.4), Inches(3.3), scope_w, Inches(0.4), color, border_color=None))
    grp.append(txt(slide, x + Inches(0.4), Inches(3.33), scope_w, Inches(0.35), scope, size=12, color=WHITE_BG, align=PP_ALIGN.CENTER))
    grp.append(txt(slide, x + Inches(0.2), Inches(3.9), Inches(3.2), Inches(1.6), desc, size=13, color=TEXT_MID, align=PP_ALIGN.CENTER))
    anim_groups.append(grp)

add_logo(slide)
add_fade_on_click(slide, anim_groups)
add_notes(slide, "Une architecture hybride pragmatique : Le monolithe modulaire permet la rapidité de dev et la cohérence ACID, l'événementiel garantit la fraîcheur des stocks, les APIs permettent l'évolution B2B.")

# =====================================================================
# SLIDE 8 : SCHÉMA D'ARCHITECTURE CIBLE
# =====================================================================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "7. Architecture Cible — Logique & Réseau")

txt(slide, Inches(0.5), Inches(1.2), Inches(12.3), Inches(0.4), "Cible V4 OVHcloud (schema-infrastructure-cible-v4.drawio)", size=14, color=TEXT_MID, italic=True)

drawio_cible_png = os.path.join(os.path.dirname(__file__), "..", "05-architecture", "schema-infrastructure-cible-v4.png")
if os.path.exists(drawio_cible_png):
    slide.shapes.add_picture(drawio_cible_png, Inches(1), Inches(1.6), Inches(11.3), Inches(5.3))
else:
    ph_box = add_box(slide, Inches(1.0), Inches(1.8), Inches(11.333), Inches(5.0), WHITE_BG, BORDER, Pt(2))
    ph_box.shadow.inherit = False
    txt(slide, Inches(1.0), Inches(4.0), Inches(11.333), Inches(0.5), "[ Insérer Image schema-infrastructure-cible-v4.png ]", size=18, color=TEXT_LIGHT, align=PP_ALIGN.CENTER)

add_logo(slide)
add_notes(slide, "Au sein d'OVHcloud, nos modules sont derrière une API Gateway sécurisée et communiquent via un bus RabbitMQ pour les stocks.")

