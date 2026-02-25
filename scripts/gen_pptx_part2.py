# -*- coding: utf-8 -*-
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn, nsmap
from lxml import etree
import os, math, random
import copy

OUTPUT = r"c:\Users\Loris\Documents\bricoloc\maelJtm\07-presentation\BricoLoc2_Presentation.pptx"
LOGO_PATH = r"c:\Users\Loris\Documents\bricoloc\maelJtm\assets\image.png"
ICON_DIR  = r"c:\Users\Loris\Documents\bricoloc\maelJtm\assets\icons2"
prs = Presentation(OUTPUT)

# ═══════════════════════════════════════
# DESIGN SYSTEM — Palette pastel cuivrée (identique part1)
# ═══════════════════════════════════════
CREAM        = RGBColor(0xE5, 0xE7, 0xE6)
SAND_LIGHT   = RGBColor(0xEE, 0xE6, 0xD8)
BLUSH        = RGBColor(0xDA, 0xAB, 0x3A)
TAUPE        = RGBColor(0xB6, 0x73, 0x32)
TERRACOTTA   = RGBColor(0x93, 0x44, 0x1A)

TEXT_DARK    = RGBColor(0x2E, 0x28, 0x22)
TEXT_MID     = RGBColor(0x5C, 0x50, 0x44)
TEXT_LIGHT   = RGBColor(0x82, 0x78, 0x6E)
WHITE_BG     = RGBColor(0xFF, 0xFF, 0xFF)
BORDER       = RGBColor(0xEE, 0xE6, 0xD8)

FONT_NAME = "Inter"

# ═══════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════

def set_slide_bg(slide, color=CREAM):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_logo(slide):
    logo_size = Inches(1.33)
    left = Inches(0.3)
    top = prs.slide_height - logo_size - Inches(0.2)
    slide.shapes.add_picture(LOGO_PATH, left, top, logo_size, logo_size)


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
    # Subtle drop shadow (L)
    spPr = shape._element.spPr
    effectLst = etree.SubElement(spPr, qn('a:effectLst'))
    outerShdw = etree.SubElement(effectLst, qn('a:outerShdw'))
    outerShdw.set('blurRad', '50800')
    outerShdw.set('dist', '25400')
    outerShdw.set('dir', '5400000')
    outerShdw.set('rotWithShape', '0')
    srgb = etree.SubElement(outerShdw, qn('a:srgbClr'))
    srgb.set('val', '000000')
    alpha = etree.SubElement(srgb, qn('a:alpha'))
    alpha.set('val', '18000')
    return shape


def add_rect(slide, left, top, width, height, fill_color, border_color=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def add_circle(slide, left, top, size, fill_color):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
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


def add_glitter(slide, count=60):
    """Add small star-like dots in the background (Galaxy Effect)."""
    for _ in range(count):
        size = Pt(random.uniform(1.5, 4.0))
        x = Inches(random.uniform(0, 13.333))
        y = Inches(random.uniform(0, 7.5))
        # Mostly white/cream, some terracotta sparks
        color = random.choice([WHITE_BG, SAND_LIGHT, BLUSH, TERRACOTTA])
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, size, size)
        dot.fill.solid()
        dot.fill.fore_color.rgb = color
        dot.line.fill.background()
        # Non-animated background
    return

def add_left_arrow(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.LEFT_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def add_chevron(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.CHEVRON, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def add_lucid_icon(slide, name, left, top, size, color):
    """Draws a 'Lucidchart-style' icon using native PPTX shapes."""
    if name == "database":
        # Cylinder
        return slide.shapes.add_shape(MSO_SHAPE.CAN, left, top, size * 0.8, size)
    elif name == "user":
        # Head + Shoulders
        head_s = size * 0.4
        h = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + (size-head_s)/2, top, head_s, head_s)
        h.fill.solid(); h.fill.fore_color.rgb = color; h.line.fill.background()
        b = slide.shapes.add_shape(MSO_SHAPE.CHORD, left, top + head_s, size, size * 0.6)
        b.rotation = 180; b.fill.solid(); b.fill.fore_color.rgb = color; b.line.fill.background()
        return h
    elif name == "cloud":
        return slide.shapes.add_shape(MSO_SHAPE.CLOUD, left, top, size * 1.2, size)
    elif name == "server":
        # Rect with 3 lines
        r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, size, size)
        r.fill.solid(); r.fill.fore_color.rgb = color; r.line.color.rgb = WHITE_BG
        for i in range(3):
            line_y = top + (i+1) * (size/4)
            l = slide.shapes.add_connector(1, left + size*0.2, line_y, left + size*0.8, line_y)
            l.line.color.rgb = WHITE_BG; l.line.width = Pt(1)
        return r
    elif name == "security":
        # Shield
        return slide.shapes.add_shape(MSO_SHAPE.SHIELD, left, top, size, size)
    elif name == "gear":
        # Hexagon/Sun looking thing
        return slide.shapes.add_shape(MSO_SHAPE.SUN, left, top, size, size)
    elif name == "message":
        # Rounded box + triangle
        return slide.shapes.add_shape(MSO_SHAPE.TEXT_BALLOON, left, top, size, size)
    elif name == "cart":
        # Simplified L shape
        return slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top + size*0.7, size, size * 0.1)
    elif name == "stock":
        # Cube
        return slide.shapes.add_shape(MSO_SHAPE.CUBE, left, top, size, size)
    elif name == "globe":
        # Oval with some lines
        g = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
        g.fill.solid(); g.fill.fore_color.rgb = color; g.line.color.rgb = WHITE_BG
        return g
    return None


def txt(slide, left, top, width, height, text, size=18, color=TEXT_DARK, bold=False, align=PP_ALIGN.LEFT):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = FONT_NAME
    p.alignment = align
    return txBox


def bullets(slide, left, top, width, height, items, size=14, color=TEXT_MID):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = item
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.name = FONT_NAME
        p.space_after = Pt(6)
    return txBox


def slide_header(slide, title, subtitle=None):
    txt(slide, Inches(0.8), Inches(0.4), Inches(10), Inches(0.7), title, size=32, color=TEXT_DARK, bold=True)
    add_rect(slide, Inches(0.8), Inches(1.05), Inches(2.5), Inches(0.035), TERRACOTTA)
    if subtitle:
        txt(slide, Inches(0.8), Inches(1.15), Inches(10), Inches(0.5), subtitle, size=14, color=TEXT_MID)


def card_with_accent_top(slide, left, top, width, height, accent_color):
    add_box(slide, left, top, width, height, WHITE_BG, BORDER, Pt(1))
    add_rect(slide, left, top, width, Inches(0.05), accent_color)

def add_section_slide(title, subtitle=None):
    """Creates a minimal section transition slide (J)."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(s, TERRACOTTA)
    txt(s, Inches(1), Inches(2.5), Inches(11.333), Inches(1.2),
        title, size=44, color=WHITE_BG, bold=True, align=PP_ALIGN.CENTER)
    if subtitle:
        add_rect(s, Inches(5.5), Inches(3.9), Inches(2.333), Inches(0.03), BLUSH)
        txt(s, Inches(1), Inches(4.2), Inches(11.333), Inches(0.6),
            subtitle, size=18, color=SAND_LIGHT, align=PP_ALIGN.CENTER)
    add_logo(s)
    return s


def add_notes(slide, text):
    """Add speaker notes to a slide (C)."""
    notes = slide.notes_slide
    notes.notes_text_frame.text = text


def add_icon(slide, name, left, top, size=Inches(0.32)):
    """Insert a PNG icon from assets/icons folder."""
    path = os.path.join(ICON_DIR, f"{name}.png")
    return slide.shapes.add_picture(path, left, top, size, size)


def add_fade_on_click(slide, shape_groups, fade_dur=500):
    """
    Add OOXML 'Fade' entrance animations to a slide.
    shape_groups: list of lists — each sub-list is a group of shapes
                  that appear together on one click.
    fade_dur: fade duration in ms (default 500 = smooth half-second).
    """
    # ── <p:timing> ──
    timing_el = etree.SubElement(slide._element, qn("p:timing"))
    tn_lst = etree.SubElement(timing_el, qn("p:tnLst"))

    # Root par (id=1, tmRoot)
    par_root = etree.SubElement(tn_lst, qn("p:par"))
    ctn_root = etree.SubElement(par_root, qn("p:cTn"))
    ctn_root.set("id", "1")
    ctn_root.set("dur", "indefinite")
    ctn_root.set("restart", "never")
    ctn_root.set("nodeType", "tmRoot")
    child_root = etree.SubElement(ctn_root, qn("p:childTnLst"))

    # Main sequence (id=2)
    seq_el = etree.SubElement(child_root, qn("p:seq"))
    seq_el.set("concurrent", "1")
    seq_el.set("nextAc", "seek")
    ctn_seq = etree.SubElement(seq_el, qn("p:cTn"))
    ctn_seq.set("id", "2")
    ctn_seq.set("dur", "indefinite")
    ctn_seq.set("nodeType", "mainSeq")
    child_seq = etree.SubElement(ctn_seq, qn("p:childTnLst"))

    # Prev / Next conditions
    for evt in ("onPrev", "onNext"):
        lst_tag = "p:prevCondLst" if evt == "onPrev" else "p:nextCondLst"
        lst = etree.SubElement(seq_el, qn(lst_tag))
        c = etree.SubElement(lst, qn("p:cond"))
        c.set("evt", evt); c.set("delay", "0")
        t = etree.SubElement(c, qn("p:tgtEl"))
        etree.SubElement(t, qn("p:sldTgt"))

    nid = 3  # next time-node id
    dur_str = str(fade_dur)

    for grp_idx, shapes in enumerate(shape_groups):
        # ── One click-step per group ──
        par1 = etree.SubElement(child_seq, qn("p:par"))
        ctn1 = etree.SubElement(par1, qn("p:cTn"))
        ctn1.set("id", str(nid)); nid += 1
        ctn1.set("fill", "hold")
        sc1 = etree.SubElement(ctn1, qn("p:stCondLst"))
        etree.SubElement(sc1, qn("p:cond")).set("delay", "0")
        ch1 = etree.SubElement(ctn1, qn("p:childTnLst"))

        # Inner grouping par
        par2 = etree.SubElement(ch1, qn("p:par"))
        ctn2 = etree.SubElement(par2, qn("p:cTn"))
        ctn2.set("id", str(nid)); nid += 1
        ctn2.set("fill", "hold")
        sc2 = etree.SubElement(ctn2, qn("p:stCondLst"))
        etree.SubElement(sc2, qn("p:cond")).set("delay", "0")
        ch2 = etree.SubElement(ctn2, qn("p:childTnLst"))

        for si, shape in enumerate(shapes):
            sp_id = str(shape.shape_id)

            par3 = etree.SubElement(ch2, qn("p:par"))
            ctn3 = etree.SubElement(par3, qn("p:cTn"))
            ctn3.set("id", str(nid)); nid += 1
            ctn3.set("presetID", "10")       # 10 = Fade
            ctn3.set("presetClass", "entr")
            ctn3.set("presetSubtype", "0")
            ctn3.set("fill", "hold")
            ctn3.set("grpId", "0")
            ctn3.set("nodeType", "clickEffect" if si == 0 else "withEffect")

            sc3 = etree.SubElement(ctn3, qn("p:stCondLst"))
            etree.SubElement(sc3, qn("p:cond")).set("delay", "0")
            ch3 = etree.SubElement(ctn3, qn("p:childTnLst"))

            # <p:set> — flip visibility to visible
            set_el = etree.SubElement(ch3, qn("p:set"))
            cBhvr_s = etree.SubElement(set_el, qn("p:cBhvr"))
            cTn_s = etree.SubElement(cBhvr_s, qn("p:cTn"))
            cTn_s.set("id", str(nid)); nid += 1
            cTn_s.set("dur", "1")
            cTn_s.set("fill", "hold")
            sc_s = etree.SubElement(cTn_s, qn("p:stCondLst"))
            etree.SubElement(sc_s, qn("p:cond")).set("delay", "0")
            tgt_s = etree.SubElement(cBhvr_s, qn("p:tgtEl"))
            etree.SubElement(tgt_s, qn("p:spTgt")).set("spid", sp_id)
            attr_s = etree.SubElement(cBhvr_s, qn("p:attrNameLst"))
            etree.SubElement(attr_s, qn("p:attrName")).text = "style.visibility"
            to_s = etree.SubElement(set_el, qn("p:to"))
            etree.SubElement(to_s, qn("p:strVal")).set("val", "visible")

            # <p:animEffect> — the actual fade
            anim_eff = etree.SubElement(ch3, qn("p:animEffect"))
            anim_eff.set("transition", "in")
            anim_eff.set("filter", "fade")
            cBhvr_f = etree.SubElement(anim_eff, qn("p:cBhvr"))
            cTn_f = etree.SubElement(cBhvr_f, qn("p:cTn"))
            cTn_f.set("id", str(nid)); nid += 1
            cTn_f.set("dur", dur_str)
            tgt_f = etree.SubElement(cBhvr_f, qn("p:tgtEl"))
            etree.SubElement(tgt_f, qn("p:spTgt")).set("spid", sp_id)

    # ── <p:bldLst> — shapes start hidden ──
    bld_lst = etree.SubElement(slide._element, qn("p:bldLst"))
    for shapes in shape_groups:
        for shape in shapes:
            b = etree.SubElement(bld_lst, qn("p:bldP"))
            b.set("spid", str(shape.shape_id))
            b.set("grpId", "0")
            b.set("animBg", "1")


# ═══════════════════════════════════════
# SLIDE 10 : COMPARAISON STYLES (barres horizontales + verdicts accessibles)
#             + animations fade-in au clic
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "7. Comparaison des approches possibles")

styles_data = [
    ("Application modulaire", 40, 55, "Adapté à notre équipe de 5", True),
    ("Messagerie temps réel", 40, 55, "Stocks toujours à jour", True),
    ("Microservices", 39, 55, "Trop complexe pour 5 personnes", False),
    ("Bus centralisé (SOA/ESB)", 33, 55, "Infrastructure surdimensionnée", False),
    ("Architecture actuelle", 23, 55, "Source des problèmes actuels", False),
]

# Bar chart
bar_area_x = Inches(4.5)
bar_max_w = Inches(6.5)
row_h_in = 0.8
row_gap_in = 0.15

slide10_groups = []  # one group per bar row

for i, (name, score, total, verdict, retained) in enumerate(styles_data):
    y = Inches(1.4 + i * (row_h_in + row_gap_in))
    row_shapes = []

    # Style name (left)
    row_shapes.append(txt(slide, Inches(0.5), y + Inches(0.05), Inches(3.8), Inches(0.35),
        name, size=14, color=TEXT_DARK, bold=True))
    row_shapes.append(txt(slide, Inches(0.5), y + Inches(0.4), Inches(3.8), Inches(0.3),
        verdict, size=11, color=TEXT_MID))

    # Bar background
    row_shapes.append(add_rect(slide, bar_area_x, y + Inches(0.15), bar_max_w, Inches(0.45), SAND_LIGHT))

    # Filled bar
    filled_w = int(bar_max_w * (score / total))
    bar_color = BLUSH if retained else TAUPE
    row_shapes.append(add_rect(slide, bar_area_x, y + Inches(0.15), filled_w, Inches(0.45), bar_color))

    # Score label inside bar
    row_shapes.append(txt(slide, bar_area_x + Inches(0.1), y + Inches(0.18), Inches(1.5), Inches(0.4),
        f"{score}/{total}", size=13, color=WHITE_BG if retained else TEXT_DARK, bold=True))

    # Retained indicator
    if retained:
        row_shapes.append(add_circle(slide, Inches(11.5), y + Inches(0.2), Inches(0.35), BLUSH))
        row_shapes.append(txt(slide, Inches(11.5), y + Inches(0.26), Inches(0.35), Inches(0.25),
            "\u2713", size=12, color=WHITE_BG, bold=True, align=PP_ALIGN.CENTER))

    slide10_groups.append(row_shapes)

# Recommendation card at bottom (appears with last bar)
reco_shapes = []
reco_shapes.append(add_box(slide, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.9), WHITE_BG, BLUSH, Pt(2)))
reco_shapes.append(add_rect(slide, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.05), BLUSH))
reco_shapes.append(txt(slide, Inches(0.8), Inches(6.1), Inches(11.5), Inches(0.35),
    "Notre choix", size=14, color=TERRACOTTA, bold=True))
reco_shapes.append(txt(slide, Inches(0.8), Inches(6.45), Inches(11.5), Inches(0.4),
    "Combiner les deux meilleures approches : une application bien organisée + une messagerie temps réel pour les stocks",
    size=13, color=TEXT_DARK, bold=True))
slide10_groups.append(reco_shapes)

add_logo(slide)
add_fade_on_click(slide, slide10_groups)
add_notes(slide, "Nous avons comparé 5 approches avec notre matrice multicritères. Les deux meilleures sont l'application modulaire et la messagerie temps réel. C'est la combinaison des deux que nous avons retenue.")

# ═══════════════════════════════════════
# SLIDE 11 : STYLES RETENUS (cards, langage accessible)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "8. Styles retenus & justification")

retained = [
    ("Monolithe modulaire", "Coeur de l'application",
     "Une seule application bien organisée\nen 9 briques indépendantes.\nRéalisable par notre équipe de 5.\nMigration progressive possible.",
     TERRACOTTA),
    ("Événementiel ciblé", "Stocks & alertes en temps réel",
     "Les informations circulent instantanément\nentre les briques via des messages.\nFini le fichier CSV quotidien.\nSi une brique tombe, les autres continuent.",
     TAUPE),
    ("APIs REST", "Ouverture aux partenaires",
     "Des points d'accès documentés\npour les partenaires et outils externes.\nIntégration simple et autonome.\nPas de serveur intermédiaire coûteux.",
     BLUSH),
]
for i, (title, scope, desc, color) in enumerate(retained):
    x = Inches(0.8 + i * 4.0)
    card_with_accent_top(slide, x, Inches(1.3), Inches(3.6), Inches(3.8), color)
    txt(slide, x + Inches(0.2), Inches(1.5), Inches(3.2), Inches(0.5),
        title, size=18, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)
    
    # PNG Icon for style
    style_icons = ["gear", "message", "globe"]
    add_icon(slide, style_icons[i], x + Inches(1.55), Inches(4.2), Inches(0.5))
    # Scope badge
    scope_w = Inches(2.8)
    add_box(slide, x + Inches(0.4), Inches(2.1), scope_w, Inches(0.4), color, border_color=None)
    txt(slide, x + Inches(0.4), Inches(2.13), scope_w, Inches(0.35),
        scope, size=12, color=WHITE_BG, align=PP_ALIGN.CENTER)

    txt(slide, x + Inches(0.2), Inches(2.7), Inches(3.2), Inches(2.2), desc, size=13, color=TEXT_MID, align=PP_ALIGN.CENTER)

# Rejected styles bar
add_box(slide, Inches(0.8), Inches(5.5), Inches(11.5), Inches(1.2), SAND_LIGHT, BORDER, Pt(1))
txt(slide, Inches(1.0), Inches(5.55), Inches(11), Inches(0.4),
    "Approches écartées", size=14, color=TERRACOTTA, bold=True)
txt(slide, Inches(1.0), Inches(5.95), Inches(11), Inches(0.6),
    "Microservices (trop complexe pour 5 personnes)  ·  SOA/ESB (infrastructure surdimensionnée)  ·  Architecture actuelle (source des problèmes)  ·  Serverless (inadapté)",
    size=13, color=TEXT_MID)

add_logo(slide)
add_notes(slide, "3 styles architecturaux combinés : le monolithe modulaire donne la structure, l'événementiel gère les stocks en temps réel, et les APIs REST ouvrent aux partenaires. C'est pragmatique pour une équipe de 5.")

# ═══════════════════════════════════════
# SLIDE 12 : CHOIX TECHNOLOGIQUES (cards + language accessible)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "9. Choix technologiques")

tech_choices = [
    ("Moteur applicatif", "Spring Boot 3", "4,90/5",
     "Déjà maîtrisé par l'équipe\nMigration progressive depuis l'existant\nGratuit et open-source", TERRACOTTA),
    ("Base de données", "PostgreSQL 16", "4,60/5",
     "Gratuit, remplacement d'Oracle\nUtilisé par les plus grands acteurs\nCompatible avec le cloud", TAUPE),
    ("Messagerie", "RabbitMQ", "4,55/5",
     "Simple à mettre en place\nStocks mis à jour instantanément\nAdapté à la taille de BricoLoc", BLUSH),
    ("Hébergement cloud", "Microsoft Azure", "4,75/5",
     "Compatible avec nos outils existants\nOffice 365, Power BI, Active Directory\nBase de données gérée incluse", TERRACOTTA),
]
for i, (decision, tech, score, justif, color) in enumerate(tech_choices):
    x = Inches(0.6 + (i % 2) * 6.2)
    y = Inches(1.3 + (i // 2) * 3.0)
    card_with_accent_top(slide, x, y, Inches(5.8), Inches(2.5), color)

    txt(slide, x + Inches(0.2), y + Inches(0.15), Inches(3.5), Inches(0.4),
        decision, size=13, color=TEXT_LIGHT)
    txt(slide, x + Inches(0.2), y + Inches(0.5), Inches(3.5), Inches(0.5),
        tech, size=22, color=TEXT_DARK, bold=True)

    # Score circle
    score_s = Inches(0.7)
    add_circle(slide, x + Inches(4.5), y + Inches(0.25), score_s, color)
    
    # PNG Icon for tech
    tech_icons = ["gear", "database", "message", "cloud"]
    add_icon(slide, tech_icons[i], x + Inches(5.1), y + Inches(1.8), Inches(0.4))
    txt(slide, x + Inches(4.5), y + Inches(0.38), score_s, score_s,
        score, size=11, color=WHITE_BG, bold=True, align=PP_ALIGN.CENTER)

    txt(slide, x + Inches(0.2), y + Inches(1.15), Inches(5.2), Inches(1.2),
        justif, size=12, color=TEXT_MID)

add_logo(slide)
add_notes(slide, "Technologies choisies via matrice multicritères. Spring Boot car maîtrisé par l'équipe. PostgreSQL car gratuit et performant. RabbitMQ car simple à opérer. Azure car compatible Microsoft et cohérent avec nos compétences.")

# ═══════════════════════════════════════
# SLIDE DE TRANSITION : CONCEPTION
# ═══════════════════════════════════════
add_section_slide("Architecture & Conception", "Du diagnostic aux solutions")

# ═══════════════════════════════════════
# SLIDE 13 : ARCHITECTURE LOGIQUE — VUE D'ENSEMBLE (simplifiée)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "10. Architecture logique — Vue d'ensemble")

# 5 couches empilées, largeur centrée, labels clairs et gros
layer_x = Inches(2.0)
layer_w = Inches(9.3)
layer_h = Inches(0.9)

layers = [
    ("Utilisateurs", "Web · Mobile · Partenaires · Salariés", SAND_LIGHT, TAUPE, TEXT_DARK),
    ("Point d'entrée sécurisé", "Authentification · Protection · Routage", WHITE_BG, BLUSH, TEXT_DARK),
    ("Application BricoLoc 2.0", "9 modules métier indépendants", WHITE_BG, TERRACOTTA, TERRACOTTA),
    ("Messagerie temps réel", "Communication instantanée entre modules", WHITE_BG, BLUSH, TEXT_DARK),
    ("Stockage des données", "Base de données · Cache · Fichiers", SAND_LIGHT, TAUPE, TEXT_DARK),
]

_layer_icons = ["user", "shield", "gear", "message", "database"]
for i, (name, sub, bg, border_c, txt_c) in enumerate(layers):
    y = Inches(1.3) + i * (layer_h + Inches(0.15))
    add_box(slide, layer_x, y, layer_w, layer_h, bg, border_c, Pt(2))
    txt(slide, layer_x + Inches(0.3), y + Inches(0.08), Inches(8.5), Inches(0.45),
        name, size=18, color=txt_c, bold=True)
    txt(slide, layer_x + Inches(0.3), y + Inches(0.5), Inches(8.5), Inches(0.35),
        sub, size=13, color=TEXT_MID)
    # PNG icon at right of each layer
    add_icon(slide, _layer_icons[i], layer_x + layer_w - Inches(0.48), y + Inches(0.25), Inches(0.4))

    # Arrow between layers (except after last)
    if i < len(layers) - 1:
        arrow_y = y + layer_h + Inches(0.01)
        add_down_arrow(slide, Inches(6.5), arrow_y, Inches(0.3), Inches(0.13), border_c)

# --- Application layer: 9 mini-modules inside layer 3 ---
y_app = Inches(1.3) + 2 * (layer_h + Inches(0.15))
mods = ["Catalogue", "Réservation", "Stocks", "Paiement", "Utilisateurs",
        "Notifications", "Admin", "Marque Blanche", "Intégration"]
for mi, mod in enumerate(mods):
    mx = layer_x + Inches(5.0 + (mi % 3) * 1.4)
    my = y_app + Inches(0.08 + (mi // 3) * 0.26)
    add_circle(slide, mx - Inches(0.15), my + Inches(0.04), Inches(0.1), TERRACOTTA)
    txt(slide, mx, my, Inches(1.3), Inches(0.25), mod, size=8, color=TEXT_MID)

# --- SYSTÈMES TIERS (côté gauche) ---
add_box(slide, Inches(0.2), Inches(2.5), Inches(1.6), Inches(3.5), SAND_LIGHT, TERRACOTTA, Pt(2))
txt(slide, Inches(0.25), Inches(2.55), Inches(1.5), Inches(0.35),
    "Partenaires", size=12, color=TERRACOTTA, bold=True, align=PP_ALIGN.CENTER)
bullets(slide, Inches(0.3), Inches(2.9), Inches(1.4), Inches(2.8), [
    "SAP", "  Stocks & compta", "",
    "Stripe", "  Paiements", "",
    "Power BI", "  Analyse",
], size=9, color=TEXT_MID)

# Arrows Tiers <> App
add_arrow(slide, Inches(1.82), Inches(3.5), Inches(0.4), Inches(0.2), TERRACOTTA)
add_left_arrow(slide, Inches(1.82), Inches(4.0), Inches(0.4), Inches(0.2), TERRACOTTA)

add_logo(slide)
add_notes(slide, "Vue d'ensemble en 5 couches. De haut en bas : présentation (ce que voit l'utilisateur), contrôleurs (qui reçoivent les requêtes), services métier (la logique), messagerie (communication entre modules), infrastructure (base de données et cloud).")

# ═══════════════════════════════════════
# SLIDE 14 : MODULES — Cercle Vertueux
#             + animations fade-in au clic
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "10b. Les 9 modules de BricoLoc 2.0", subtitle="Un écosystème modulaire interdépendant")

# Central hub
cx, cy = Inches(6.666), Inches(4.3)
sun_s = Inches(1.8)
add_circle(slide, cx - sun_s/2, cy - sun_s/2, sun_s, TERRACOTTA)
txt(slide, cx - sun_s/2, cy - Inches(0.3), sun_s, Inches(0.35),
    "BricoLoc", size=18, color=WHITE_BG, bold=True, align=PP_ALIGN.CENTER)
txt(slide, cx - sun_s/2, cy + Inches(0.05), sun_s, Inches(0.3),
    "2.0", size=16, color=WHITE_BG, align=PP_ALIGN.CENTER)

# Connecting ring
ring_s = Inches(5.6)
ring = slide.shapes.add_shape(MSO_SHAPE.OVAL, cx - ring_s/2, cy - ring_s/2, ring_s, ring_s)
ring.fill.background()
ring.line.color.rgb = SAND_LIGHT
ring.line.width = Pt(1.5)
ring.line.dash_style = 2 
ring.shadow.inherit = False

# Modules classification
mods_data = [
    # CORE
    ("Catalogue", "Outils & recherche", "cart", TERRACOTTA),
    ("Réservation", "Locations & calendrier", "message", TERRACOTTA),
    ("Stocks", "Temps réel", "stock", TERRACOTTA),
    # SUPPORT
    ("Paiement", "Transactions", "cart", TAUPE),
    ("Utilisateurs", "Comptes & accès", "user", TAUPE),
    ("Notifications", "Alertes", "message", TAUPE),
    # PERIPHERAL
    ("Admin", "Back-office", "gear", BLUSH),
    ("Marque Blanche", "SaaS", "globe", BLUSH),
    ("Intégration", "SAP/Stripe", "server", BLUSH),
]

radius = Inches(2.8)
mod_w, mod_h = Inches(2.2), Inches(1.2)
animation_groups = []

for i, (name, sub, icon, color) in enumerate(mods_data):
    angle = -math.pi/2 + (i * (2 * math.pi / len(mods_data)))
    mx = cx + radius * math.cos(angle)
    my = cy + radius * math.sin(angle)
    
    left = mx - mod_w/2
    top = my - mod_h/2
    
    current_group_shapes = []
    
    # Card
    current_group_shapes.append(add_box(slide, left, top, mod_w, mod_h, WHITE_BG, BORDER, Pt(1)))
    
    # Accent top
    current_group_shapes.append(add_rect(slide, left, top, mod_w, Inches(0.05), color))
    
    # Icon
    ic = add_icon(slide, icon, left + mod_w/2 - Inches(0.18), top + Inches(0.1), Inches(0.36))
    current_group_shapes.append(ic)
    
    # Text
    t1 = txt(slide, left + Inches(0.1), top + Inches(0.5), mod_w - Inches(0.2), Inches(0.3),
        name, size=11, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)
    t2 = txt(slide, left + Inches(0.1), top + Inches(0.8), mod_w - Inches(0.2), Inches(0.3),
        sub, size=9, color=TEXT_MID, align=PP_ALIGN.CENTER)
    
    current_group_shapes.extend([t1, t2])
    animation_groups.append(current_group_shapes)

# Conclusion label
txt(slide, Inches(0.5), Inches(7.1), Inches(12.3), Inches(0.3),
    "Une architecture modulaire : chaque brique remplit une mission précise au sein du système",
    size=12, color=TEXT_LIGHT, align=PP_ALIGN.CENTER)

add_logo(slide)
add_fade_on_click(slide, animation_groups)
add_notes(slide, "Visualisation des 9 modules en cercle vertueux. Au centre, le moteur BricoLoc 2.0. Chaque module est indépendant mais parfaitement intégré à l'écosystème.")

# ═══════════════════════════════════════
# SLIDE DE TRANSITION : DEPLOIEMENT
# ═══════════════════════════════════════
add_section_slide("Mise en \u0153uvre", "De la conception au terrain")

# ═══════════════════════════════════════
# SLIDE 15 : MIGRATION (chevrons + descriptions accessibles)
#             + animations fade-in au clic
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "11. Plan de migration en 7 étapes")

phases = [
    ("0", "2-3 mois", "Fondations", "Mettre en place les\noutils de développement\net la nouvelle base"),
    ("1", "3-4 mois", "Stocks", "Remplacer le fichier\nCSV par des mises à jour\nen temps réel"),
    ("2", "2-3 mois", "Comptes", "Nouveau système\nde connexion sécurisé\net gestion des accès"),
    ("3", "4-6 mois", "Catalogue", "Refonte du catalogue\net du système de\nréservation"),
    ("4", "2-3 mois", "Paiement", "Paiement en ligne\nsécurisé et alertes\nautomatiques"),
    ("5", "3-4 mois", "Partenaires", "Ouverture aux\npartenaires et\nexpansion européenne"),
    ("6", "1-2 mois", "Fin legacy", "Extinction définitive\nde l'ancien système"),
]

# Chevron flow
chevron_h = Inches(1.3)
chevron_w = Inches(1.65)
gap = Inches(0.05)
y_flow = Inches(1.4)

shades = [TERRACOTTA, TAUPE, BLUSH, SAND_LIGHT, TERRACOTTA, TAUPE, BLUSH]
txt_c = [WHITE_BG, WHITE_BG, TEXT_DARK, TEXT_DARK, WHITE_BG, WHITE_BG, TEXT_DARK]

# Build chevrons — collect shapes per phase for animation
slide15_chevrons = []
for i, (num, duration, label, desc) in enumerate(phases):
    x = Inches(0.5) + i * (chevron_w + gap)
    phase_shapes = []
    phase_shapes.append(add_chevron(slide, x, y_flow, chevron_w, chevron_h, shades[i]))
    phase_shapes.append(txt(slide, x + Inches(0.35), y_flow + Inches(0.1), Inches(0.9), Inches(0.35),
        num, size=22, color=txt_c[i], bold=True, align=PP_ALIGN.CENTER))
    phase_shapes.append(txt(slide, x + Inches(0.1), y_flow + Inches(0.5), Inches(1.45), Inches(0.7),
        label, size=10, color=txt_c[i], bold=True, align=PP_ALIGN.CENTER))
    slide15_chevrons.append(phase_shapes)

# Detail cards below each chevron — add to same phase group
for i, (num, duration, label, desc) in enumerate(phases):
    x = Inches(0.5) + i * (chevron_w + gap)
    y_card = Inches(3.0)
    slide15_chevrons[i].append(add_box(slide, x, y_card, chevron_w, Inches(2.5), WHITE_BG, BORDER, Pt(1)))
    slide15_chevrons[i].append(add_rect(slide, x, y_card, chevron_w, Inches(0.05), shades[i]))
    slide15_chevrons[i].append(txt(slide, x + Inches(0.05), y_card + Inches(0.15), chevron_w - Inches(0.1), Inches(0.35),
        duration, size=12, color=TERRACOTTA, bold=True, align=PP_ALIGN.CENTER))
    slide15_chevrons[i].append(txt(slide, x + Inches(0.05), y_card + Inches(0.55), chevron_w - Inches(0.1), Inches(1.8),
        desc, size=10, color=TEXT_MID, align=PP_ALIGN.CENTER))

# Timeline bar at bottom (always visible, not animated)
add_rect(slide, Inches(0.5), Inches(5.8), Inches(12.3), Inches(0.04), TERRACOTTA)
txt(slide, Inches(0.5), Inches(5.95), Inches(12.3), Inches(0.4),
    "L'ancien et le nouveau système coexistent — aucune interruption de service",
    size=13, color=TEXT_DARK, align=PP_ALIGN.CENTER)

# Timeline markers
for i in range(7):
    x_mark = Inches(0.5 + 0.8) + i * (chevron_w + gap)
    add_circle(slide, x_mark, Inches(5.72), Inches(0.18), TERRACOTTA)

add_logo(slide)
add_fade_on_click(slide, slide15_chevrons)
add_notes(slide, "7 étapes de migration progressive. L'ancien système coexiste avec le nouveau — zéro interruption de service. Durée totale estimée : 18 à 24 mois.")

# ═══════════════════════════════════════
# SLIDE 16 : REGLES D'ARCHITECTURE (grille de cards par catégorie)
#             + animations fade-in au clic
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "Règles d'architecture (garde-fous)")

rules_cards = [
    ("Isolation", "R01", "Chaque module a ses\npropres données. Pas\nd'accès croisés.", TERRACOTTA),
    ("Simplicité", "R02", "La logique métier reste\ndans le code, jamais\ndans la base de données.", TAUPE),
    ("Passerelle unique", "R03", "Un seul point de contact\navec les systèmes\nexternes (SAP, Stripe...).", BLUSH),
    ("Sécurité", "R04", "Toute requête extérieure\nest vérifiée et\nauthentifiée.", TERRACOTTA),
    ("Données bancaires", "R05", "Aucune donnée de carte\nbancaire ne passe par\nnos serveurs.", TAUPE),
    ("Organisation", "R06", "Chaque module possède\nson propre espace\nde stockage dédié.", BLUSH),
    ("Traçabilité", "R07", "Chaque message échangé\nentre modules est\nversionné et traçable.", TERRACOTTA),
    ("Déploiement", "R08", "Tout le code est versionné\nsur Git. Aucun envoi\nmanuel autorisé.", TAUPE),
]

card_w = Inches(2.7)
card_h = Inches(2.4)

slide16_groups = []

for i, (category, rid, desc, color) in enumerate(rules_cards):
    col = i % 4
    row = i // 4
    x = Inches(0.5) + col * (card_w + Inches(0.2))
    y = Inches(1.25) + row * (card_h + Inches(0.2))

    card_shapes = []

    # Card background
    card_shapes.append(add_box(slide, x, y, card_w, card_h, WHITE_BG, BORDER, Pt(1)))

    # Category circle at top
    circle_s = Inches(0.55)
    card_shapes.append(add_circle(slide, x + card_w / 2 - circle_s / 2, y + Inches(0.15), circle_s, color))
    txt_color = WHITE_BG if color in [TERRACOTTA, TAUPE] else TEXT_DARK
    card_shapes.append(txt(slide, x + card_w / 2 - circle_s / 2, y + Inches(0.28), circle_s, circle_s,
        rid, size=11, color=txt_color, bold=True, align=PP_ALIGN.CENTER))

    # Category name
    card_shapes.append(txt(slide, x + Inches(0.1), y + Inches(0.8), card_w - Inches(0.2), Inches(0.35),
        category, size=14, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER))

    # Description
    card_shapes.append(txt(slide, x + Inches(0.1), y + Inches(1.2), card_w - Inches(0.2), Inches(1.1),
        desc, size=11, color=TEXT_MID, align=PP_ALIGN.CENTER))
    # PNG icon bottom-right of rule card
    _rule_icons = ["database", "gear", "globe", "shield", "shield", "stock", "message", "server"]
    ic = add_icon(slide, _rule_icons[i], x + card_w - Inches(0.36), y + card_h - Inches(0.36), Inches(0.28))
    card_shapes.append(ic)

    slide16_groups.append(card_shapes)

# Bottom note (always visible)
txt(slide, Inches(0.5), Inches(6.2), Inches(12.3), Inches(0.35),
    "Ces garde-fous évitent de reproduire les problèmes du système actuel",
    size=13, color=TEXT_LIGHT, align=PP_ALIGN.CENTER)

add_logo(slide)
add_fade_on_click(slide, slide16_groups)
add_notes(slide, "8 garde-fous pour éviter de reproduire les erreurs du système actuel. Chaque règle est tracée vers un point faible identifié.")

# ═══════════════════════════════════════
# SLIDE 17 : EQUIPE DEV (avatars + périmètre clair)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "Répartition de l'équipe de développement")

devs = [
    ("Marion H.", "MH", "Développement Java", "Réservations\nGestion des stocks"),
    ("Piotr S.", "PS", "Développement complet", "Catalogue d'outils\nInterface admin"),
    ("Thibaut E.", "TE", "Développement Java", "Comptes utilisateurs\nEspace partenaires"),
    ("Hervé D.", "HD", "Développement mixte", "Paiements en ligne\nConnexions externes"),
    ("Isabelle A.", "IA", "Données & analyse", "Tableaux de bord\nTests & qualité"),
]

dev_shades = [TERRACOTTA, TAUPE, BLUSH, TERRACOTTA, TAUPE]
dev_txt_c = [WHITE_BG, WHITE_BG, TEXT_DARK, WHITE_BG, WHITE_BG]

for i, (name, initials, role, scope) in enumerate(devs):
    x = Inches(0.5 + i * 2.5)

    # Card
    card_with_accent_top(slide, x, Inches(1.4), Inches(2.3), Inches(4.5), dev_shades[i])

    # Avatar circle with initials
    avatar_s = Inches(0.9)
    add_circle(slide, x + Inches(0.7), Inches(1.6), avatar_s, dev_shades[i])
    txt(slide, x + Inches(0.7), Inches(1.78), avatar_s, Inches(0.4),
        initials, size=18, color=dev_txt_c[i], bold=True, align=PP_ALIGN.CENTER)

    # Name
    txt(slide, x + Inches(0.1), Inches(2.6), Inches(2.1), Inches(0.4),
        name, size=15, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)

    # Role subtitle
    txt(slide, x + Inches(0.1), Inches(3.0), Inches(2.1), Inches(0.35),
        role, size=11, color=TEXT_LIGHT, align=PP_ALIGN.CENTER)

    # Divider
    add_rect(slide, x + Inches(0.5), Inches(3.4), Inches(1.3), Inches(0.02), SAND_LIGHT)

    # Scope
    txt(slide, x + Inches(0.1), Inches(3.55), Inches(2.1), Inches(1.5),
        scope, size=12, color=TEXT_MID, align=PP_ALIGN.CENTER)

# Bottom insight
add_box(slide, Inches(0.5), Inches(6.2), Inches(12.3), Inches(0.6), SAND_LIGHT, BORDER, Pt(1))
txt(slide, Inches(0.8), Inches(6.28), Inches(11.7), Inches(0.45),
    "Chaque développeur a un périmètre défini pour éviter les conflits et répartir la charge de travail",
    size=13, color=TEXT_DARK, align=PP_ALIGN.CENTER)

add_logo(slide)
add_notes(slide, "Chaque développeur a un périmètre défini et une spécialité. Pas de conflit, charge répartie équitablement. Les 8 000 lignes de code estimées sont réalistes pour 3 personnes en 24 mois.")

# ═══════════════════════════════════════
# SLIDE 18 : CONCLUSION (résumé accessible + perspectives)
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)
slide_header(slide, "12. Conclusion & perspectives")

# Summary: 3 large cards instead of 5 small ones
conclusions = [
    ("Une architecture\nadaptée", "Pensée pour une équipe de 5,\navec des technologies\nque nous maîtrisons déjà.", TERRACOTTA, WHITE_BG),
    ("Une migration\nsans risque", "7 étapes progressives,\nl'ancien et le nouveau\ncoexistent en parallèle.", TAUPE, WHITE_BG),
    ("Tous les problèmes\nadressés", "Chaque point faible\nest couvert, avec des\ngardes-fous pour éviter\nles mêmes erreurs.", BLUSH, TEXT_DARK),
]

for i, (title, desc, shade, txt_color) in enumerate(conclusions):
    x = Inches(0.5 + i * 4.1)
    add_box(slide, x, Inches(1.3), Inches(3.8), Inches(2.8), shade, BORDER, Pt(1))
    txt(slide, x + Inches(0.2), Inches(1.45), Inches(3.4), Inches(0.8),
        title, size=18, color=txt_color, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, x + Inches(0.2), Inches(2.3), Inches(3.4), Inches(1.6),
        desc, size=13, color=txt_color, align=PP_ALIGN.CENTER)

# Perspectives section
add_box(slide, Inches(0.5), Inches(4.5), Inches(12.3), Inches(2.0), WHITE_BG, BORDER, Pt(1))
add_rect(slide, Inches(0.5), Inches(4.5), Inches(12.3), Inches(0.05), BLUSH)
txt(slide, Inches(0.8), Inches(4.6), Inches(11), Inches(0.5),
    "Et après ?", size=18, color=TERRACOTTA, bold=True)

perspectives = [
    ("Expansion européenne", "Ouverture vers Bruxelles, Lausanne et Francfort en multilingue"),
    ("Évolution future", "Si l'équipe grandit, on peut découper davantage l'application"),
    ("Application mobile", "Une application mobile pour les clients, grâce aux APIs déjà prêtes"),
]
persp_icons = ["globe", "gear", "cart"]
for i, (title, desc) in enumerate(perspectives):
    y = Inches(5.1 + i * 0.45)
    add_icon(slide, persp_icons[i], Inches(0.75), y, Inches(0.3))
    txt(slide, Inches(1.2), y, Inches(2.5), Inches(0.4), title, size=13, color=TEXT_DARK, bold=True)
    txt(slide, Inches(3.7), y, Inches(8.5), Inches(0.4), desc, size=12, color=TEXT_MID)

add_logo(slide)
add_notes(slide, "3 points clés à retenir : architecture adaptée à l'équipe, migration progressive sans coupure, et tous les problèmes actuels sont adressés. Les perspectives incluent l'expansion européenne et une application mobile.")

# ═══════════════════════════════════════
# SLIDE 19 : MERCI
# ═══════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide)

# Accent line
add_rect(slide, Inches(5), Inches(3.4), Inches(3.333), Inches(0.04), TERRACOTTA)

txt(slide, Inches(1), Inches(2.0), Inches(11.333), Inches(1.2),
    "Merci pour votre attention", size=48, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(3.8), Inches(11.333), Inches(0.8),
    "Questions ?", size=32, color=TERRACOTTA, align=PP_ALIGN.CENTER)

# Divider
add_rect(slide, Inches(5.5), Inches(4.8), Inches(2.333), Inches(0.025), SAND_LIGHT)

txt(slide, Inches(1), Inches(5.1), Inches(11.333), Inches(0.5),
    "Romain  ·  Maëlle  ·  Loris", size=22, color=TEXT_DARK, bold=True, align=PP_ALIGN.CENTER)
txt(slide, Inches(1), Inches(5.6), Inches(11.333), Inches(0.5),
    "Master 1 Architecte d'Application — CESI", size=16, color=TEXT_LIGHT, align=PP_ALIGN.CENTER)

add_logo(slide)

# ═══════════════════════════════════════
# GLOBAL DECORATIONS (applied to ALL slides)
# ═══════════════════════════════════════
total_slides = len(prs.slides)

for idx, slide in enumerate(prs.slides):
    # (A) Fade transition between slides
    trans = etree.SubElement(slide._element, qn('p:transition'))
    trans.set('spd', 'med')
    etree.SubElement(trans, qn('p:fade'))

    # (B) Slide number "X / N" bottom-right
    num_box = txt(slide, Inches(12.0), Inches(7.1), Inches(1.0), Inches(0.3),
        f"{idx + 1} / {total_slides}", size=9, color=TEXT_LIGHT, align=PP_ALIGN.RIGHT)

    # (H) Progress bar at very bottom
    progress_w = int(prs.slide_width * ((idx + 1) / total_slides))
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, prs.slide_height - Inches(0.04), progress_w, Inches(0.04))
    bar.fill.solid()
    bar.fill.fore_color.rgb = TERRACOTTA
    bar.line.fill.background()
    bar.shadow.inherit = False

# (D) Sommaire hyperlinks — add clickable overlay shapes on slide 2 (index 1)
from pptx.opc.constants import RELATIONSHIP_TYPE as RT

sommaire_slide = prs.slides[1]
# Map each sommaire item to its target slide index
# Part1: 0=Titre, 1=Sommaire, 2=Orga, 3=Contexte, 4=Démarche, 5=TransitionAnalyse
# Part1: 6=SI, 7=PF, 8=ENF, 9=Axes
# Part2: 10=Comparaison, 11=Styles, 12=ChoixTech, 13=TransitionConception
# Part2: 14=ArchiLogique, 15=Modules, 16=TransitionDeploiement
# Part2: 17=Migration, 18=Règles, 19=Equipe, 20=Conclusion, 21=Merci
sommaire_targets = [
    2,   # Organisation du groupe
    3,   # Contexte & objectifs
    4,   # Démarche
    6,   # SI existant (after transition slide)
    7,   # Points faibles
    8,   # ENF
    9,   # Axes d'amélioration
    10,  # Comparaison
    11,  # Styles retenus
    12,  # Choix technologiques
    14,  # Architecture logique (after transition slide)
    17,  # Migration (after transition slides)
]

for i, target_idx in enumerate(sommaire_targets):
    if target_idx >= total_slides:
        continue
    col = 0 if i < 6 else 1
    row = i if i < 6 else i - 6
    x_base = Inches(1.0 + col * 6.0)
    y = Inches(1.6 + row * 0.85)

    # Add transparent clickable area
    link_shape = sommaire_slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, x_base, y, Inches(5.5), Inches(0.75))
    link_shape.fill.background()
    link_shape.line.fill.background()
    link_shape.shadow.inherit = False

    # Add hyperlink via OOXML
    target_slide_obj = prs.slides[target_idx]
    rId = sommaire_slide.part.relate_to(target_slide_obj.part, RT.SLIDE)
    cNvPr = link_shape._element.nvSpPr.cNvPr
    hlink = etree.SubElement(cNvPr, qn('a:hlinkClick'))
    hlink.set(qn('r:id'), rId)
    hlink.set('action', 'ppaction://hlinksldjump')

# ═══════════════════════════════════════
# SAVE
# ═══════════════════════════════════════
prs.save(OUTPUT)
print(f"DONE: {OUTPUT}")
print(f"Total slides: {total_slides}")
