# import csv
# exampleFile = open('example.csv',encoding='UTF-8')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Wiersz #' +str(exampleReader.line_num) + ' ' +str(row))
#     for items in row:
#         print('           ' + str(items))

# import csv
# outputFile = open('output.csv','w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['Witaj Świecie','bacon','eggs','ham'])
# outputWriter.writerow([1,2,3.141523,4])


# import csv
# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
# csvWriter.writerow(['jabłka','pomarańcze','winogrono'])
# csvWriter.writerow(['eggs','bacon','ham'])
# csvWriter.writerow(['spam','spam','spam','spam','spam','spam'])
# csvFile.close()


import os, csv

newDirectory = os.makedirs(r'C:\pycharm_projects\z gita\hello-world\cvs_files\removeCsvHeader\removed_first_line',exist_ok=True)
os.chdir(r'C:\pycharm_projects\z gita\hello-world\cvs_files\removeCsvHeader')
for file in os.listdir('.'):
    if not file.endswith('.csv'):
        continue
    print('Removing the header of the file %s' % file)
    csvFile = open(file, encoding='UTF-8')
    csfReader = csv.reader(csvFile)
    copiedRow = []
    for rows in csfReader:
        if csfReader.line_num == 1:
            continue
        copiedRow.append(rows)
    csvFile.close()
    csvFileObj = open(os.path.join('removed_first_line',file),'w',newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in copiedRow:
        csvWriter.writerow(row)
    csvFileObj.close()

