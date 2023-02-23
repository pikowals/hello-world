# import json
# stringOfJsonData = '{"name": "Zophie","isCat":"True","miceCaught":0,"felineIQ":null}'
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

# import json
# pythonValue = {'name': 'Zophie','isCat':'True','miceCaught':0,'felineIQ':None}
# stringOfJsonData = json.dumps(pythonValue)
# print(stringOfJsonData)

import json, requests, pprint
url = 'https://api.open-meteo.com/v1/forecast?latitude=51.40&longitude=21.15&hourly=temperature_2m'
response = requests.get(url)
response.raise_for_status()
weather_data = json.loads(response.text)
pprint.pprint(weather_data)