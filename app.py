import streamlit as st
import pandas as pd
import hashlib
import folium
from streamlit_folium import st_folium
from PIL import Image
import time

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def new_window():
	url = 'https://t1.daumcdn.net/cfile/blog/99AB2B4B5D4057A52D'
	st.image(url)

def main():
	st.title("Dou - ME")
	menu = ["Dou-ME!","회원가입"]
	choice = st.sidebar.selectbox("메뉴",menu)
	

	if choice == "Dou-ME!":
		st.subheader("메인 화면")
		st.sidebar.subheader("로그인")
		username = st.sidebar.text_input("이름")
		password = st.sidebar.text_input("비밀번호",type='password')

		if st.sidebar.checkbox("로그인"):
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("{}님 로그인 되었습니다.".format(username))
				time.sleep(1)
				l1 = 35.92592905660903
				l2 = 128.5529675876424

				chk = st.checkbox("도움이 필요해요")

				# time.sleep(10)
				# chk = True

				if chk == True:
					time.sleep(1)
					l1 = 35.84506774086036
					l2 = 128.627121949104

					st.header("회원정보")

					col1, col2, col3 = st.columns(3)

					with col1:
						st.subheader("이름 : 박순자")

					with col2:
						st.subheader("나이 : 84세")

					with col3:
						st.subheader("성별 : 여")

					st.subheader("요청사항 : 귀가 잘 안들리니 이해해주세요.")


				m = folium.Map(location=[l1, l2], zoom_start=32)
				folium.Marker(
					[l1, l2],
					popup="여기요",
					tooltip="여기요"
				).add_to(m)
				st_data = st_folium(m, width=725)

			else:
				st.warning("Incorrect Username/Password")

	elif choice == "회원가입":
		st.subheader("새로운 계정 생성")

		new_user = st.text_input("이름")
		new_password = st.text_input("비밀번호",type='password')

		col1, col2, col3, col4 = st.columns(4)

		with col1:
			sex = st.radio("성별", ("남", "여"))

		with col2:
			age = st.text_input("생년월일",placeholder="050222")

		with col3:
			bf = st.text_input("참고사항",placeholder="소아마비, 고혈압")

		st.text_input("요청사항",placeholder =" 제가 과민성대장증후군이 있어서 가까이 오실때 소리는 울리지 말아주세요. 배가 아파져요ㅠㅠ")

		if st.button("회원가입"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("회원가입이 성공적으로 완료되었습니다.")

			st.info("Go to Login Menu to login")
if __name__ == '__main__':
	main()