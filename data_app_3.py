import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('data.csv',encoding='cp949',index_col=0, thousands=',')
df_area = df[df.index.str.contains('산격')]

df_area = df_area.sum()
df_area = pd.DataFrame(df_area, columns=['산격동'])
df_area = df_area.drop(df_area.index[0])
df_area = df_area.drop(df_area.index[0])

age = [i for i in range(0,101)]
person = [i for i in df_area['산격동']]

menu = st.sidebar.selectbox('MENU', options=['Line Graph'])

if menu == 'Line Graph':
    plt.rc('font', family='Malgun Gothic')
    plt.title('산격동 인구 현황')
    plt.plot(age, person, '.-', color='pink', label='산격동')
    plt.grid(True, linestyle='--', color='#DDDDDD')
    plt.ylim(0, 1000)
    st.pyplot(plt)