import requests
import xmltodict
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


national1 = ['South Korea','Japan','China','United States of America',
            'United Kingdom','Italy', 'France','Germany']

color = ['red','orange','yellow','green',
            'skyblue','purple', 'pink']

# national1 = st.sidebar.selectbox('국가선택1' , options=national1, key = 1)
# national2 = st.sidebar.selectbox('국가선택2' , options=national2, key = 2)

selectNation = st.sidebar.multiselect('나라를 선택하세요',
                                      national1,
                                      ['South Korea', 'Japan']
                                      )

selectcolor = st.sidebar.multiselect('색깔을 선택하세요',
                                      color,
                                      ['red','orange']
                                      )

date1 = st.sidebar.text_input('시작 날짜', placeholder='20220222')
date2 = st.sidebar.text_input('종료 날짜', placeholder='20220302')

btn = st.sidebar.button('차트 그리기')

plt.rc('font', family='Malgun Gothic')
plt.title('세계 코로나 확진자 현황')

if btn:
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?' \
          'serviceKey=nwFe1iYXo5NL2z6yTKP2KjBGMP66OS5yhSLhL6P4Flb2k5bxzK%2F9cITnYVX%2BdHqysj8JUFZkZ6giylrVfeJ9eQ%3D%3D&' \
          'pageNo=1&numOfRows=10&' \
          'startCreateDt=' + date1 + '&' \
          'endCreateDt=' + date2;

    response = requests.get(url)
    response = response.content

    xmlobject = xmltodict.parse(response)
    dict_data = xmlobject['response']['body']['items']['item']

    df = pd.DataFrame(dict_data)

    for i in range(len(selectNation)):
            국가 = df[df['nationNmEn']== selectNation[i]]
            국가 = 국가.astype({'natDeathCnt': 'int', 'natDefCnt': 'int'})
            국가['date'] = pd.to_datetime(국가['createDt'])
            국가 = 국가[['date','natDeathCnt','natDefCnt','nationNmEn','stdDay']]
            국가 = 국가.sort_values(by='date')
            국가['daily_natDefCnt'] = 국가['natDefCnt'].diff()
            국가 = 국가[국가['daily_natDefCnt'] > 0]

            if len(selectNation) == len(selectcolor):
                plt.plot(국가['date'], 국가['daily_natDefCnt'], '.-', color=selectcolor[i], label=selectNation[i])
            else:
                if i < len(selectcolor):
                    plt.plot(국가['date'], 국가['daily_natDefCnt'], '.-', color=selectcolor[i], label=selectNation[i])
                else:
                    plt.plot(국가['date'], 국가['daily_natDefCnt'], '.-', label=selectNation[i])



    plt.grid(True, linestyle='--', color='#DDDDDD')
    plt.legend()
    st.pyplot(plt)


