# import PyPDF2
# pdfFileObj = open('encrypted.pdf','rb')    # Zaczytujemy plik pdf w trybie odczytu binarnego
# pdfReader = PyPDF2.PdfReader(pdfFileObj)        # Zeby otrzymac obiekt pdfreader używamy metody PdfReader
# print(pdfReader.is_encrypted)
# pdfReader.decrypt('rosebud')
# pageObj = pdfReader.pages[0]
# print(pageObj.extract_text())
# print(len(pdfReader.pages))                     # Wyswietlamy ilość stron w pdfie
# pageObj = pdfReader.pages[1]                    # Zawartość strony 1 przekazujemy do obiektu pageObj
# print(pageObj.extract_text())                   # Wyswietlamy tekst za pomocą metody extract_text()

# import PyPDF2
# pdf1File = open('meetingminutes.pdf','rb')
# pdf2File = open('meetingminutes2.pdf','rb')
#
# pdf1Reader = PyPDF2.PdfReader(pdf1File)
# pdf2Reader = PyPDF2.PdfReader(pdf2File)
# pdfWriter = PyPDF2.PdfWriter()
# for pageNum in range(len(pdf1Reader.pages)):
#     pageObj = pdf1Reader.pages[pageNum]
#     pdfWriter.add_page(pageObj)
# for pageNum in range(len(pdf2Reader.pages)):
#     pageObj = pdf2Reader.pages[pageNum]
#     pdfWriter.add_page(pageObj)
# pdfOutputFile = open('combinedminutes_2.pdf','wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()

# import PyPDF2
# pdf1File = open('meetingminutes.pdf','rb')
# pdf1Reader = PyPDF2.PdfReader(pdf1File)
# page = pdf1Reader.pages[0]
# page.rotate(90)
# pdfWrite = PyPDF2.PdfWriter()
# pdfWrite.add_page(page)
# resultPdfFile = open('rotatedPage.pdf','wb')
# pdfWrite.write(resultPdfFile)
# resultPdfFile.close()
# pdf1File.close()

# import PyPDF2
# minutetFile = open('meetingminutes.pdf','rb')
# pdfReader = PyPDF2.PdfReader(minutetFile)
# minutesFirstPage = pdfReader.pages[0]
# pdfWatermarkReader = PyPDF2.PdfReader(open('watermark.pdf','rb'))
# minutesFirstPage.merge_page(pdfWatermarkReader.pages[0])
# pdfWriter = PyPDF2.PdfWriter()
# pdfWriter.add_page(minutesFirstPage)
#
# for pageNum in range(1,len(pdfReader.pages)):
#     pageObj = pdfReader.pages[pageNum]
#     pdfWriter.add_page(pageObj)
# resultPdfFile = open('watemarkedCover.pdf','wb')
# pdfWriter.write(resultPdfFile)
# minutetFile.close()
# resultPdfFile.close()
# import PyPDF2
#
# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfReader(pdfFile)
# pdfWriter = PyPDF2.PdfWriter()
# for pageNum in range(len(pdfReader.pages)):
#     pdfWriter.add_page(pdfReader.pages[pageNum])
# pdfWriter.encrypt('swordfish')
# resultPdf = open('encryptedminutes.pdf','wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()

# import PyPDF2,os
# pdfFiles = []
# for filename in os.listdir('.'):
#     if filename.endswith('.pdf'):
#         pdfFiles.append(filename)
# pdfFiles.sort(key=str.lower)
# pdfWriter = PyPDF2.PdfWriter()
# for filename in pdfFiles:
#     pdfFileObj = open(filename,'rb')
#     pdfReader = PyPDF2.PdfReader(pdfFileObj)
#     for pageNum in range(1, len(pdfReader.pages)):
#         pageObj = pdfReader.pages[pageNum]
#         pdfWriter.add_page(pageObj)
# pdfOutput = open('allminutes.pdf','wb')
# pdfWriter.write(pdfOutput)
# pdfOutput.close()
