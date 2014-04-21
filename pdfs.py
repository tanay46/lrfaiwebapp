from xhtml2pdf import pisa
from cStringIO import StringIO

def create_pdf(html):
	from xhtml2pdf import pisa
	from cStringIO import StringIO
	pdf = StringIO()
	pisa.CreatePDF(StringIO(html.encode('utf-8')), pdf)
	resp = pdf.getvalue()
	print "HIIII"
	pdf.close()
	return resp