"""
    PDF文档
"""
import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)  # 19 -->总页数
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()

# 解密PDF
import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

