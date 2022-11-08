import requests
import xmltodict
import pandas as pd
import streamlit as st
import urllib3
import matplotlib.pyplot as plt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #오류코드 삭제

url = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/" \
      "getStockPriceInfo?" \
      "serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&" \
      "numOfRows=10000&" \
      "pageNo=1&" \
      f"beginBasDt=20221001&" \
      "itmsNm=삼성전자"

response = requests.get(url,verify=False)
response = response.content

xmlobject = xmltodict.parse(response)
dict_data = xmlobject['response']['body']['items']['item']

df = pd.DataFrame(dict_data)

df.drop(['isinCd'], axis=1, inplace=True)
df.drop(['mkp'], axis=1, inplace=True)
df.drop(['trPrc'], axis=1, inplace=True)
df.drop(['lstgStCnt'], axis=1, inplace=True)
df.drop(['mrktTotAmt'], axis=1, inplace=True)

df = df.sort_index(ascending=False)
df = df.reset_index(drop=True)


if 'count' not in st.session_state:
      st.session_state.count = 0

def increment_counter(increment_value=0):
      st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
      st.session_state.count -= decrement_value


menu = st.sidebar.selectbox('MENU', options=['현재가','로그인','회원가입','정보수정'])

if menu == '현재가':
      st.button('다음날짜', on_click=increment_counter,
                kwargs=dict(increment_value=1))

      st.button('이전날짜', on_click=decrement_counter,
                kwargs=dict(decrement_value=1))

      st.write('현재 인덱스 = ', st.session_state.count)
      주식 = df.loc[st.session_state.count]
      # 주식 = 주식.astype({'fltRt': 'float'})
      전일대비등락률 = 주식['fltRt']
      고가 = 주식['hipr']
      저가 = 주식['lopr']
      전일대비등락 = 주식['vs']
      현재가 = 주식['clpr']
      현재날짜 = 주식['basDt']
      차트주식 = df.astype({'basDt': 'int'})
      차트주식 = df.astype({'clpr': 'int'})
      차트주식['price'] = 차트주식['clpr']



      if 전일대비등락률[0] == '.':
            st.metric(label="현재가", value=현재가 + "원", delta='0'+전일대비등락률 + "%")
            st.write('전일대비등락률은 :', '0'+전일대비등락률)
      elif 전일대비등락률[0:2] == '-.':
            전일대비등락률 = 전일대비등락률.replace('-','')
            st.metric(label="현재가", value=현재가 + "원", delta='-0' + 전일대비등락률 + "%")
            st.write('전일대비등락률은 :', '-0' + 전일대비등락률)
      else:
            st.metric(label="현재가", value=현재가 + "원", delta=전일대비등락률 + "%")
            st.write('전일대비등락률은 :', 전일대비등락률)
      st.write('저가는 :', 저가)
      st.write('고가는 :', 고가)
      st.write('전일대비등락은 :', 전일대비등락)
      st.write('현재날자는 :', 현재날짜)
      st.write('현재가격은 :', 현재가)
      plt.rc('font', family='Malgun Gothic')
      plt.title('삼성전자')
      plt.plot(차트주식.loc[:st.session_state.count, 'basDt'], 차트주식.loc[:st.session_state.count, 'price'],'.-', color='black',)
      plt.grid(True, linestyle='--', color='#DDDDDD')
      plt.set_loglevel('WARNING') # 오류코드 삭제
      st.pyplot(plt)


df.to_csv('D:/newworkspace/first/df.csv')



