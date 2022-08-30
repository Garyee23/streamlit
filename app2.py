import streamlit as st
import sqlite3
import pandas as pd

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pwd):
    cur.execute(f"SELECT * FROM users  WHERE id='{id}' and pw ='{pwd}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('MENU', options=['회원가입','로그인','회원목록','정보수정'])

if menu == '회원가입':
    with st.form('my_form', clear_on_submit=True):
        st.subheader('1. 아이디')
        id = st.text_input('아이디')

        st.subheader('2. 비밀번호')
        pw = st.text_input('비밀번호', type='password')

        st.subheader('3. 비밀번호 확인')
        pw_ck = st.text_input('비밀번호 확인', type='password')


        name = st.text_input('이름')

        st.subheader('4. 나이')
        age = st.text_input('나이')

        st.subheader('4. 성별')
        gender = st.radio(
            '셩별이 무엇인가요?', ('남자', '여자'), horizontal= True
        )

        st.subheader('5. 전화번호')
        number = st.text_input('잔화번호')
        register = st.form_submit_button('회원가입')

        if register:
            if pw == pw_ck:
                cur.execute(f"INSERT INTO users(id, pw, name, age, gender, number) "
                            f"VALUES('{id}','{pw}','{name}',{age},'{gender}','{number}')")
                st.success('회원가입이 완료되었습니다.')
            else:
                st.warning('비밀번호가 다릅니다.')

            con.commit()

if menu == '로그인':
    login_id = st.sidebar.text_input('아이디')
    login_pw = st.sidebar.text_input('비밀번호', type='password')
    login_btn = st.sidebar.button('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        if user_info:
            st.header(user_info[2] + '님 환영합니다.')
            st.sidebar.image('./img/'+user_info[0]+'.jpg')
        else:
            st.header('다시 입력하세요.')


if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql("SELECT name, age, gender FROM users", con)
    st.dataframe(df)
    
if menu == '정보수정':
    st.subheader('정보수정')