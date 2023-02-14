import openpyxl,pprint
print('Otwieranie skoroszytu...')
# import census2010
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active
countyData={}

print('Odczyt wierszy...')
for row in range(2,sheet.max_row+1):
    state  = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop    = sheet['D'+str(row)].value
    #Upewniamy się że istnieje klucz dla danego stanu
    countyData.setdefault(state,{})     # Metoda setdefault nie wywołuje żadnych działań jeśli klucz istnieje, wiec mozna ja wywoływać podczas każdej iteracji
    #Upewniamy się że istnieje klucz dla danego hrabstwa w tym stanie
    countyData[state].setdefault(county,{'tracts':0,'pop':0})  # Nie wywołuje żadnych działań jeśli klucz istnieje, wiec mozna ja wywoływać podczas każdej iteracji
    #Kazdy wiersz przedstawia jeden obszar geograficzny wiec przeprowadzamy inkrementacje o 1
    countyData[state][county]['tracts']+=1
    #Populację hrabstwa zwiększamy o populację w tym obszarze geograficznym
    countyData[state][county]['pop']+=int(pop)
print('Zapis wyników...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Gotowe')
#
# print(census2010.allData['AK']['Anchorage'])
# anchoragePop = census2010.allData['AK']['Anchorage']['pop']
# print('Populacja Anchorage w 2010 roku wynosiła ' + str(anchoragePop))