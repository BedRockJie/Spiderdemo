from docx import Document
from docx.shared import Pt,RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT  #对其方式


doc = Document("demp.docx")

for paragraph in doc.paragraphs:
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    paragraph.paragraph_format.line_spacing = 2.0

    for run in paragraph.runs:
        run.font.bold = True
        run.font.italic = True
        run.font.underline = True
        run.font.strike = True
        run.font.shadow = True
        run.font.size = Pt(20)
        run.font.color.rgb = RGBColor(255,255,255)
        run.font.name = '微软雅黑'
        r = run._element.rPr.rFonts
        r.set(qn('w:easrAsia'),'微软雅黑')


doc.save('demp1.docx')