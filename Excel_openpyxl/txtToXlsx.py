import openpyxl, os, re

fileList = os.listdir('C:\pycharm_projects\z gita\hello-world')
txtFileRegex = re.compile(r'''(^(.+)
                                (\.)
                                (txt)$)''', re.VERBOSE)
wb = openpyxl.Workbook()
sheet = wb.active
colNr = 1
for i in fileList:
    if txtFileRegex.search(i):
        file = open(os.path.join('C:\pycharm_projects\z gita\hello-world',i), encoding="utf8")
        fileLines = file.readlines()
        for j in range(len(fileLines)):
            sheet.cell(row=j+1 , column =colNr).value = fileLines[j]
        colNr+=1
wb.save('txt_to_xlsx.xlsx')


