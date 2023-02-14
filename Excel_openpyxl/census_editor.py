import census2010
print(census2010.allData['AK']['Anchorage'])
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('Populacja Anchorage w 2010 roku wynosiła ' + str(anchoragePop))