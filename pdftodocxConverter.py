from pdf2docx import Converter
pdf_path = "\...\....pdf"
docx_path = "output1.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()
print("convert process is ended")