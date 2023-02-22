# import docx
# doc = docx.Document('demo.docx')
# print(len(doc.paragraphs))
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[1].text)
# print(len(doc.paragraphs))
# print(doc.paragraphs[1].runs[0].text)
# print(doc.paragraphs[1].runs[1].text)
# print(doc.paragraphs[1].runs[2].text)
# print(doc.paragraphs[1].runs[3].text)
#
# def getText():
#     doc = docx.Document('demo.docx')
#     fullText =[]
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)
# print(getText())

# import docx
# doc = docx.Document('demo.docx')
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[0].style)
# doc.paragraphs[0].style = 'Normal'
# print(doc.paragraphs[0].style)
# print(doc.paragraphs[1].text)
# doc.paragraphs[1].runs[0].style = 'Quote Char'
# print(doc.paragraphs[1].runs[0].style)
# doc.paragraphs[1].runs[1].underline = True
# doc.paragraphs[1].runs[3].strike = True
# doc.save('restyled.docx')

# import docx
# doc = docx.Document()
# doc.add_heading('Witaj Świecie!',0)
# doc.add_heading('Witaj Świecie!',1)
# doc.add_heading('Witaj Świecie!',2)
# doc.add_heading('Witaj Świecie!',3)
# doc.add_heading('Witaj Świecie!',4)
# doc.save('helloworld.docx')

import os, PyPDF2
dir = 'C:\pycharm_projects\z gita\hello-world\pdf_operations'

for foldername, subfolders, filenames in os.walk(dir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFileReader = PyPDF2.PdfReader(os.path.join(foldername,filename))
            print(pdfFileReader)
            pdfFileWriter = PyPDF2.PdfWriter()
            for pageNum in range(len(pdfFileReader.pages)):
                pageObj = pdfFileReader.pages[pageNum]
                pdfFileWriter.add_page(pageObj)
            pdfFileWriter.encrypt('haslo')
            resultPdf = open(os.path.join(foldername, (filename.replace('.pdf', '')) + '_Encrypted.pdf'),'wb')
            pdfFileWriter.write(resultPdf)
            resultPdf.close()
            pdfFileR = PyPDF2.PdfReader(os.path.join(foldername, (filename.replace('.pdf', '')) + '_Encrypted.pdf'))
            if pdfFileR.is_encrypted:
                print('Usuwamy plik niezakodowany')
                os.remove(os.path.join(foldername,filename))


