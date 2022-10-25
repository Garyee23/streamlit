import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', encoding='cp949', index_col=0, thousands=',')

df_area = df[df.index.str.contains('구암동')]

df_area2 = df[df.index.str.contains('관문동')]

df_area3 = df[df.index.str.contains('동천동')]

df_area4 = df[df.index.str.contains('노원동')]

#행렬 전환
df_area = df_area.transpose()
df_area.rename(columns=df.iloc[0], inplace=True)
df_area = df_area.drop(df_area.index[0])
df_area = df_area.drop(df_area.index[0])

df_area2 = df_area2.transpose()
df_area2.rename(columns=df.iloc[0], inplace=True)
df_area2 = df_area2.drop(df_area2.index[0])
df_area2 = df_area2.drop(df_area2.index[0])

df_area3 = df_area3.transpose()
df_area3.rename(columns=df.iloc[0], inplace=True)
df_area3 = df_area3.drop(df_area3.index[0])
df_area3 = df_area3.drop(df_area3.index[0])

df_area4 = df_area4.transpose()
df_area4.rename(columns=df.iloc[0], inplace=True)
df_area4 = df_area4.drop(df_area4.index[0])
df_area4 = df_area4.drop(df_area4.index[0])

age = [i for i in range(0,101)]
person = [i for i in df_area['대구광역시 북구 구암동(2723074500)']]
person2 = [i for i in df_area2['대구광역시 북구 관문동(2723071500)']]
person3 = [i for i in df_area3['대구광역시 북구 동천동(2723078000)']]
person4 = [i for i in df_area4['대구광역시 북구 노원동(2723079000)']]

menu = st.sidebar.selectbox('MENU', options=['Line Graph'])

if menu == 'Line Graph':
    plt.rc('font', family='Malgun Gothic')
    plt.title('구암동 인구 현황')
    plt.plot(age, person, '.-', color='pink', label='구암동')
    plt.plot(age, person2, '.-', color='skyblue', label='관문동')
    plt.plot(age, person3, '.-', color='orange', label='동천동')
    plt.plot(age, person4, '.-', color='green', label='노원동')
    plt.legend()
    plt.grid(True, linestyle='--', color='#DDDDDD')
    plt.ylim(0, 1000)
    st.pyplot(plt)
