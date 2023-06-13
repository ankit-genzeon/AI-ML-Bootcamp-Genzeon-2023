from pdf2docx import Converter
pdf_file = ''
docx_file = ''
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()