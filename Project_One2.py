import requests
import xmltodict
import pandas as pd
import streamlit as st
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/" \
      "getStockPriceInfo?" \
      "serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&" \
      "numOfRows=10000&" \
      "basDt=20221101" \

response = requests.get(url,verify=False)
response = response.content

xmlobject = xmltodict.parse(response)
dict_data = xmlobject['response']['body']['items']['item']

df = pd.DataFrame(dict_data)

menu = st.sidebar.selectbox('MENU', options=['현재가','로그인','회원가입','정보수정'])

if menu == '현재가':
      주식 = df[df['itmsNm'] == 'SK하이닉스']
      주식 = 주식.astype({'clpr': 'int'})
      가격 = 주식['clpr']

      st.write(주식)
      st.write(가격)



