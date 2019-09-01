from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import scrap
import re
import sys

data = scrap.scrapit(sys.argv[1])

#name the file from scrapped article
my_doc = SimpleDocTemplate(re.sub(re.compile(r'\[\w+\]'), '', data[0]).replace(" ", "_") + '.pdf')
stysheet = getSampleStyleSheet()

#collect flowables
flowables = []
for d in data:
    dtype = ''
    if '[p]' in d or '[ul]' in d:
        dtype = 'BodyText'
    else:
        dtype = 'Heading2'
    flowables.append(Paragraph(re.sub(re.compile(r'\[\w+\]'), '', d), stysheet[dtype]))

#build the doc
my_doc.build(flowables)