import pandas as pd
import requests
import xmltodict
import requests
import pandas as pd

# url = 'http://apis.data.go.kr/1360000/AmmIwxxmService/getMetar?' \
#       'serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&' \
#       'numOfRows=10&' \
#       '&pageNo=1' \
#       'icao=RKSI';

url = 'http://apis.data.go.kr/1360000/AmmIwxxmService/getMetar?serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&pageNo=1&numOfRows=10&dataType=XML&icao=RKSS'

response = requests.get(url)
response = response.content
xmlobject = xmltodict.parse(response)
dict_data = xmlobject['response']['body']['items']['item']['metarMsg']['iwxxm:METAR']
df = pd.DataFrame(dict_data)
print(df.columns)

print(df['iwxxm:extension'])