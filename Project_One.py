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

stock = df.loc[st.session_state.count] #현재 선택된 주식

vsper = stock['fltRt'] #전일대비등락률

high = stock['hipr'] #고가

low = stock['lopr'] #저가

vsnum = stock['vs']

cur = stock['clpr']

tod = stock['basDt']

chstock = df.astype({'basDt': 'int'})
chstock = df.astype({'clpr': 'int'})
chstock['price'] = chstock['clpr']

total = 1000000

plt.rc('font', family='Malgun Gothic') # 차트 글꼴

# menu = st.sidebar.selectbox('MENU', options=['현재가','로그인','회원가입','정보수정'])
# if menu == '현재가':

st.button('다음날짜', on_click=increment_counter,
          kwargs=dict(increment_value=1))

st.button('이전날짜', on_click=decrement_counter,
          kwargs=dict(decrement_value=1))

st.write('현재 인덱스 = ', st.session_state.count)




if vsper[0] == '.':
      st.metric(label="현재가", value=cur + "원", delta='0'+vsper + "%")
      st.write('전일대비등락률은 :', '0'+vsper)
elif vsper[0:2] == '-.':
      vsper = vsper.replace('-','')
      st.metric(label="현재가", value=cur + "원", delta='-0' + vsper + "%")
      st.write('전일대비등락률은 :', '-0' + vsper)
else:
      st.metric(label="현재가", value=cur + "원", delta=vsper + "%")
      st.write('전일대비등락률은 :', vsper)

st.write('저가는 :', low)
st.write('고가는 :', high)
st.write('전일대비등락은 :', vsnum)
st.write('현재날자는 :', tod)
st.write('현재가격은 :', cur)

plt.title('삼성전자')
plt.plot(chstock.loc[:st.session_state.count, 'basDt'], chstock.loc[:st.session_state.count, 'price'],'.-', color='black',)
plt.grid(True, linestyle='--', color='#DDDDDD')
plt.set_loglevel('WARNING') # 오류코드 삭제
st.pyplot(plt)


df.to_csv('D:/newworkspace/first/df.csv')



