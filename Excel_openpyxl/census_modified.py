import openpyxl,pprint
print('Otwieranie skoroszytu...')
# import census2010
wb = openpyxl.load_workbook('censuspopdata_modified.xlsx')
sheet = wb.active
countyData={}

print('Odczyt wierszy...')
for row in range(2,sheet.max_row+1):
    state  = sheet['B'+str(row)].value
    if state == None:
        print('Wiersz %s zawiera brakujace informacje na temat stanu' %row)
    county = sheet['C'+str(row)].value
    if county == None:
        print('Wiersz %s zawiera brakujace informacje na temat hrabstwa w stanie %s ' % (row,state))
    pop    = sheet['D'+str(row)].value

    #Upewniamy się że istnieje klucz dla danego stanu
    countyData.setdefault(state,{})     # Metoda setdefault nie wywołuje żadnych działań jeśli klucz istnieje, wiec mozna ja wywoływać podczas każdej iteracji
    #Upewniamy się że istnieje klucz dla danego hrabstwa w tym stanie
    countyData[state].setdefault(county,{'tracts':0,'pop':0})  # Nie wywołuje żadnych działań jeśli klucz istnieje, wiec mozna ja wywoływać podczas każdej iteracji
    #Kazdy wiersz przedstawia jeden obszar geograficzny wiec przeprowadzamy inkrementacje o 1
    countyData[state][county]['tracts']+=1
    #Populację hrabstwa zwiększamy o populację w tym obszarze geograficznym
    if pop == None:
        print('Wiersz %s zawiera brakujace informacje na temat ludności w stanie %s w hrabstwie %s ' % (row, state, county))
    else:
        countyData[state][county]['pop']+=int(pop)
print('Zapis wyników...')
resultFile = open('census2010_modified.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Gotowe')
#