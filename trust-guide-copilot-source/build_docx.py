import sys, re
from bs4 import BeautifulSoup, NavigableString, Tag
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_BREAK, WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HTML, LOGO, OUT = sys.argv[1:4]
NAVY, CORAL, TEAL, ORANGE = '0A2044', 'BA4D45', '0D7C7D', 'AB5836'
TEXT2, MUTED, LINE = '374151', '4B5563', 'E5E7EB'
TINT = {'teal': 'F0FAF9', 'coral': 'FFF5F4', 'gold': 'FFFBF0', 'gray': 'F5F7FB'}
BAR = {'teal': TEAL, 'coral': CORAL, 'gold': ORANGE, 'gray': NAVY}
TAGC = {'g': TEAL, 'y': ORANGE, 'r': CORAL}
rgb = RGBColor.from_string

soup = BeautifulSoup(open(HTML, encoding='utf-8').read(), 'html.parser')
d = Document()
sec = d.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.left_margin = sec.right_margin = Inches(0.8)
sec.top_margin, sec.bottom_margin = Inches(0.7), Inches(0.7)
st = d.styles['Normal']
st.font.name = 'Montserrat'; st.font.size = Pt(9.5); st.font.color.rgb = rgb(TEXT2)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Montserrat')
st.paragraph_format.space_after = Pt(5); st.paragraph_format.line_spacing = 1.12
for name in ('List Bullet',):
    d.styles[name].font.name = 'Montserrat'

def shade(cell, hexv):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:fill'), hexv); tcPr.append(sh)

def borders(tbl, inside=None):
    tblPr = tbl._tbl.tblPr; b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        x = OxmlElement('w:' + e)
        if inside and e == 'insideH':
            x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '4'); x.set(qn('w:color'), inside)
        elif inside and e == 'bottom':
            x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '4'); x.set(qn('w:color'), inside)
        else:
            x.set(qn('w:val'), 'nil')
        b.append(x)
    tblPr.append(b)

def cell_borders(cell, left=None, gap=False):
    tcPr = cell._tc.get_or_add_tcPr(); b = OxmlElement('w:tcBorders')
    if left:
        x = OxmlElement('w:left'); x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '24'); x.set(qn('w:color'), left); b.append(x)
    if gap:
        x = OxmlElement('w:right'); x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '36'); x.set(qn('w:color'), 'FFFFFF'); b.append(x)
    tcPr.append(b)

def cell_margins(tbl, top=70, side=110):
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn('w:tblW')): tblPr.remove(old)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), '5000'); w.set(qn('w:type'), 'pct'); tblPr.append(w)
    m = OxmlElement('w:tblCellMar')
    for e, v in (('top', top), ('bottom', top), ('left', side), ('right', side)):
        x = OxmlElement('w:' + e); x.set(qn('w:w'), str(v)); x.set(qn('w:type'), 'dxa'); m.append(x)
    tblPr.append(m)

def keep_row(row):
    trPr = row._tr.get_or_add_trPr(); x = OxmlElement('w:cantSplit'); trPr.append(x)

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr(); x = OxmlElement('w:tblHeader'); trPr.append(x)

def hyperlink(p, url, text, size):
    r_id = p.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), r_id)
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), TEAL); rPr.append(c)
    s = OxmlElement('w:sz'); s.set(qn('w:val'), str(int(size * 2))); rPr.append(s)
    f = OxmlElement('w:rFonts'); f.set(qn('w:ascii'), 'Montserrat'); f.set(qn('w:hAnsi'), 'Montserrat'); rPr.append(f)
    r.append(rPr); t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h)

def inline(p, node, size=9.5, color=TEXT2, bold=False):
    """Write a node's inline content into paragraph p."""
    for ch in node.children:
        if isinstance(ch, NavigableString):
            txt = re.sub(r'\s+', ' ', str(ch))
            if not txt.strip() and not p.runs:
                continue
            r = p.add_run(txt); r.font.size = Pt(size); r.font.color.rgb = rgb(color); r.bold = bold
        elif ch.name == 'br':
            if p.runs: p.runs[-1].add_break()
        elif ch.name in ('b', 'strong'):
            inline(p, ch, size, NAVY if color == TEXT2 else color, True)
        elif ch.name == 'a':
            hyperlink(p, ch['href'], ch.get_text(), size)
        elif ch.name == 'span' and 'tag' in ch.get('class', []):
            k = [c for c in ch['class'] if c in TAGC][0]
            r = p.add_run(ch.get_text() + '  '); r.bold = True; r.font.size = Pt(size - 1.5); r.font.color.rgb = rgb(TAGC[k])
        elif ch.name == 'h4':
            continue
        else:
            inline(p, ch, size, color, bold)

def strip_lead_space(p):
    ts = p._p.findall('.//' + qn('w:t'))
    if ts:
        ts[0].text = (ts[0].text or '').lstrip()
        ts[-1].text = (ts[-1].text or '').rstrip()

def para(node=None, text=None, size=9.5, color=TEXT2, bold=False, after=5, before=0, container=None, align=None):
    p = (container.add_paragraph() if container is not None else d.add_paragraph())
    p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(before)
    if align: p.alignment = align
    if text is not None:
        r = p.add_run(text); r.font.size = Pt(size); r.font.color.rgb = rgb(color); r.bold = bold
    elif node is not None:
        inline(p, node, size, color, bold); strip_lead_space(p)
    return p

def first_par(cell):
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(2); return p

def callout(div):
    kind = next((c for c in ('coral', 'gold', 'gray') if c in div['class']), 'teal')
    t = d.add_table(rows=1, cols=1); borders(t); cell_margins(t, 90, 160)
    c = t.rows[0].cells[0]; shade(c, TINT[kind]); cell_borders(c, BAR[kind]); keep_row(t.rows[0])
    k = div.find('b', class_='k')
    p = first_par(c)
    if k:
        r = p.add_run(k.get_text().strip()); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = rgb(NAVY)
        k.extract()
        body = div.find('p')
        if body:
            q = c.add_paragraph(); q.paragraph_format.space_after = Pt(1); inline(q, body, 9); strip_lead_space(q)
    else:
        inline(p, div, 9); strip_lead_space(p)
    d.add_paragraph().paragraph_format.space_after = Pt(2)

def cards(div):
    cs = div.find_all('div', class_='card', recursive=False)
    t = d.add_table(rows=1, cols=len(cs)); borders(t); cell_margins(t, 80, 120); keep_row(t.rows[0])
    for i, cd in enumerate(cs):
        kind = next((c for c in ('teal', 'coral', 'gold') if c in cd['class']), 'gray')
        c = t.rows[0].cells[i]; shade(c, TINT[kind]); cell_borders(c, BAR[kind], gap=i < len(cs) - 1)
        h = cd.find('h4'); p = first_par(c)
        if h:
            inline(p, h, 9, NAVY, True); strip_lead_space(p)
            h.extract(); q = c.add_paragraph(); q.paragraph_format.space_after = Pt(1)
            inline(q, cd, 8.5); strip_lead_space(q)
        else:
            inline(p, cd, 8.5); strip_lead_space(p)
    d.add_paragraph().paragraph_format.space_after = Pt(2)

def chips(div):
    items = div.find_all('div', recursive=False)
    t = d.add_table(rows=1, cols=len(items)); borders(t); cell_margins(t, 80, 100)
    for i, it in enumerate(items):
        c = t.rows[0].cells[i]; shade(c, TINT['gray']); cell_borders(c, CORAL, gap=i < len(items) - 1)
        p = first_par(c); r = p.add_run(it.find('b').get_text()); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = rgb(CORAL)
        q = c.add_paragraph(); r = q.add_run(it.get_text().replace(it.find('b').get_text(), '', 1).strip()); r.bold = True; r.font.size = Pt(8); r.font.color.rgb = rgb(NAVY)

def table(tb):
    rows = tb.find_all('tr')
    ncol = max(len(r.find_all(['th', 'td'])) for r in rows)
    t = d.add_table(rows=len(rows), cols=ncol); borders(t, inside=LINE); cell_margins(t, 60, 100)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    small = 'grid' in tb.get('class', []) or 'ladder' in tb.get('class', [])
    ths = rows[0].find_all('th')
    pcts = []
    for th in ths:
        m = re.search(r'width:(\d+)%', th.get('style', ''))
        pcts.append(float(m.group(1)) if m else None)
    if ths and 'check' not in tb.get('class', []) and any(pcts):
        known = sum(x for x in pcts if x); unknown = [x for x in pcts if not x]
        rest = (100 - known) / len(unknown) if unknown else 0
        pcts = [x if x else rest for x in pcts]
        widths = [6.9 * x / 100 for x in pcts]
        lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); t._tbl.tblPr.append(lay)
        for gc, w in zip(t._tbl.tblGrid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(w * 1440)))
        for r in t.rows:
            for ci, w in enumerate(widths):
                if ci < len(r.cells): r.cells[ci].width = Inches(w)
    if 'check' in tb.get('class', []):
        for ri in range(len(rows)):
            for ci, w in enumerate((0.35, 2.6, 3.95)): t.rows[ri].cells[ci].width = Inches(w)
        lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); t._tbl.tblPr.append(lay)
        for gc, w in zip(t._tbl.tblGrid.findall(qn('w:gridCol')), (0.35, 2.6, 3.95)): gc.set(qn('w:w'), str(int(w * 1440)))
    for ri, tr in enumerate(rows):
        keep_row(t.rows[ri])
        cells = tr.find_all(['th', 'td'])
        for ci, td in enumerate(cells):
            c = t.rows[ri].cells[ci]; p = first_par(c)
            if td.name == 'th':
                shade(c, NAVY); inline(p, td, 8, 'FFFFFF', True); strip_lead_space(p)
                if ri == 0: repeat_header(t.rows[ri])
            else:
                if 'h' in td.get('class', []): shade(c, TINT['gray'])
                inline(p, td, 8 if small else 8.6, TEXT2, 'h' in td.get('class', [])); strip_lead_space(p)
    d.add_paragraph().paragraph_format.space_after = Pt(2)

def qlist(qs):
    has_ms = qs[0].find('div', class_='ms') is not None
    t = d.add_table(rows=len(qs), cols=3 if has_ms else 2); borders(t, inside=LINE); cell_margins(t, 50 if not has_ms else 70, 90)
    widths = (Inches(0.45), Inches(3.2), Inches(3.25)) if has_ms else (Inches(0.45), Inches(6.45))
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); t._tbl.tblPr.append(lay)
    for gc, w in zip(t._tbl.tblGrid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(w.inches * 1440)))
    for i, q in enumerate(qs):
        keep_row(t.rows[i])
        for j, w in enumerate(widths): t.rows[i].cells[j].width = w
        n = q.find('span', class_='num').get_text()
        p = first_par(t.rows[i].cells[0]); r = p.add_run(n); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = rgb(CORAL)
        mid = q.find('div'); b = mid.find('b'); s = mid.find('span')
        p = first_par(t.rows[i].cells[1]); r = p.add_run(b.get_text()); r.bold = True; r.font.size = Pt(10); r.font.color.rgb = rgb(NAVY)
        p2 = t.rows[i].cells[1].add_paragraph(); r = p2.add_run(s.get_text()); r.font.size = Pt(8.6); r.font.color.rgb = rgb(TEXT2)
        ms = q.find('div', class_='ms')
        if ms:
            p = first_par(t.rows[i].cells[2]); p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r = p.add_run(ms.get_text()); r.bold = True; r.font.size = Pt(8.4); r.font.color.rgb = rgb(TEAL)
    d.add_paragraph().paragraph_format.space_after = Pt(2)

def render(node):
    kids = [k for k in node.children if isinstance(k, Tag)]
    i = 0
    while i < len(kids):
        k = kids[i]; cls = k.get('class', [])
        if 'foot' in cls: pass
        elif k.name == 'img':
            first = k.find_parent('section') is pages[0]
            w = 0.45 if 'width:0.6in' in k.get('style','') else (0.75 if first else 0.45)
            p = para(after=10 if first else 2); p.add_run().add_picture(LOGO, width=Inches(w))
        elif k.name == 'p' and 'eyebrow' in cls:
            para(text=k.get_text().upper(), size=8, color=CORAL, bold=True, after=4)
        elif k.name == 'h1':
            sz = 30 if 'font-size:34pt' in k.get('style', '') else 22
            p = para(text=k.get_text(' ').replace('  ', ' ').strip(), size=sz, color=NAVY, bold=True, after=8)
        elif k.name == 'h2':
            para(text=k.get_text().strip(), size=11.5, color=CORAL, bold=True, before=8, after=4)
        elif k.name == 'p':
            style = k.get('style', '')
            if 'color:var(--teal)' in style and 'font-size:17pt' in style:
                para(text=k.get_text(), size=16, color=TEAL, bold=True, after=10)
            elif 'color:var(--coral)' in style:
                para(node=k, size=12, color=CORAL, bold=True, after=8)
            elif 'srcline' in cls:
                para(node=k, size=7.5, color=MUTED, before=6, after=0)
            elif 'small' in cls:
                para(node=k, size=8, color=MUTED, after=6)
            elif 'lead' in cls:
                para(node=k, size=10, after=8)
            elif any(c in cls for c in ()) :
                pass
            elif k.find_parent('section') is not None and 'src2' in k.find_parent('section').get('class', []) and k.find('a'):
                para(node=k, size=8, after=4)
            elif 'color:var(--teal)' in style:
                para(node=k, size=9, color=TEAL, after=0)
            elif 'font-weight:700' in style:
                para(node=k, size=10, color=NAVY, bold=True, after=0)
            else:
                para(node=k, size=9.5, after=5)
        elif k.name == 'ul':
            for li in k.find_all('li', recursive=False):
                p = d.add_paragraph(style='List Bullet'); p.paragraph_format.space_after = Pt(3)
                inline(p, li, 9.2); strip_lead_space(p)
        elif k.name == 'table':
            table(k)
        elif k.name == 'div' and 'callout' in cls:
            callout(k)
        elif k.name == 'div' and 'chips' in cls:
            chips(k)
        elif k.name == 'div' and 'row' in cls and k.find('div', class_='card', recursive=False):
            cards(k)
        elif k.name == 'div' and 'q' in cls:
            group = []
            while i < len(kids) and 'q' in kids[i].get('class', []):
                group.append(kids[i]); i += 1
            qlist(group); continue
        elif k.name == 'div':
            if 'position:absolute' in k.get('style', ''):
                para(after=6)
            render(k)
        i += 1

pages = soup.find_all('section', class_='page')
for n, pg in enumerate(pages):
    before = len(d.element.body)
    render(pg)
    if n:
        for el in list(d.element.body)[before:]:
            if el.tag == qn('w:p'):
                pPr = el.get_or_add_pPr(); x = OxmlElement('w:pageBreakBefore'); pPr.insert(0, x); break

# footer with page number
fp = sec.footer.paragraphs[0]
r = fp.add_run('© 2026 Growth Partner Pros. All Rights Reserved.        '); r.font.size = Pt(7.5); r.font.color.rgb = rgb(MUTED)
r = fp.add_run(); r.font.size = Pt(7.5); r.font.color.rgb = rgb(MUTED)
for tag, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    if tag:
        f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), tag); r._r.append(f)
    else:
        it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = txt; r._r.append(it)
sec.different_first_page_header_footer = True
d.core_properties.title = soup.title.get_text() if soup.title else 'Growth Partner Pros'
d.core_properties.author = 'Caroline Hinton, Growth Partner Pros'
d.save(OUT); print('saved')
