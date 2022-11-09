import requests
import xmltodict
import pandas as pd
import streamlit as st

# url = 'http://apis.data.go.kr/1360000/AmmIwxxmService/getMetar?' \
#       'serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&' \
#       'numOfRows=10&' \
#       '&pageNo=1' \
#       'icao=RKSI';

# url = 'http://apis.data.go.kr/1360000/AmmService/getMetar?' \
#       'serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&' \
#       'numOfRows=10&' \
#       'pageNo=1&' \
#       'icao=RKSI'

# response = requests.get(url)
# response = response.content

# xmlobject = xmltodict.parse(response)
# dict_data = xmlobject['response']['body']['items']['item']['metarMsg']

menu = st.sidebar.selectbox('MENU', options=['실시간 공항별 METAR 정보','실시간 위성영상'])

if menu == '실시간 공항별 METAR정보':
      airport = st.selectbox('공항 선택', options=['RKSS','RKSI', 'RKSS'])

      url = 'http://apis.data.go.kr/1360000/AmmService/getMetar?' \
            'serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&' \
            'numOfRows=10&' \
            'pageNo=1&' \
            'icao='+ airport;

      response = requests.get(url)
      response = response.content

      xmlobject = xmltodict.parse(response)
      dict_data = xmlobject['response']['body']['items']['item']

      df = pd.DataFrame(dict_data)







