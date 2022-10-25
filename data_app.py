import streamlit as st
import matplotlib.pyplot as plt

menu = st.sidebar.selectbox('MENU', options=['Line Graph', 'Bar Graph','Mixed Graph','Pie Graph'])


if menu == 'Line Graph':
    x = ['09.07','09.08','09.09','09.10','09.11','09.12','09.13']
    #사망자
    y1 = [56,64,68,48,47,22,35]
    #신규입원
    y2 = [303,281,301,189,149,161,158	]

    plt.rc('font', family='Malgun Gothic')
    plt.title('코로나 바이러스19 현황')
    plt.plot(x,y1,'.-', color='pink',label='사망 현황(단위:명)')
    plt.plot(x,y2,'.-', color='skyblue',label='신규입원 현황(단위:명)')
    plt.legend()
    plt.grid(True, linestyle='--', color='#DDDDDD')
    plt.ylim(0, 400)
    st.pyplot(plt)

if menu == 'Bar Graph':
    x = ['서울우유','남양유업','매일유업','부산우유','연세우유']
    y = [6152,2077,1936,972,2020]

    plt.title('유제품 회사 매출')
    plt.bar(x, y, color = 'pink', edgecolor='black', width=0.4)
    plt.xlabel('회사명')
    plt.ylabel('매출액')

    plt.ylim(0,7000)
    st.pyplot(plt)

if menu == 'Mixed Graph':
    x = ['3월','4월','5월','6월','7월']
    # 기온
    y1 = [10,16,19,21,28]
    # 강수량
    y2 = [10,20,15,50,100]

    fig, ax1 = plt.subplots()
    ax1.bar(x,y1,color='pink')


    ax2 = ax1.twinx()
    ax2.plot(x,y2,color='skyblue')

    st.title('기상현상')
    st.pyplot(plt)

if menu == 'Pie Graph':
    subject = ['물리학','화학','생명과학','지구과학','프로그래밍']
    students = [56,22,35,12,18]
    colorList = ['#EEF1FF','#D2DAFF','#AAC4FF','#B1B2FF', '#CDF0EA']

    plt.pie(students, labels=subject, autopct='%.1f%%', colors = colorList)
    st.pyplot(plt)