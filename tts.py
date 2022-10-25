from gtts import gTTS
import streamlit as st
from playsound import playsound

# text = '안녕하세요'
# with open('sample.txt', 'r', encoding ='utf8') as f:
# text = f.read()


txt = st.text_input('들으실 내용을 입력하라')
btn = st.button('실행')

if btn:
    file_name = 'sample.mp3'
    tts_en = gTTS(text=txt, lang='ko')
    tts_en.save(file_name)
    playsound(file_name)


