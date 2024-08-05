'''我的主页'''

#表情链接：
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

#streamlit==1.28.2

#python -m 

import streamlit as st
page = st.sidebar.radio('我的首页', ['兴趣','图片','留言'])

def page_1():
    '''我的兴趣'''
    st.write("人生就俩字！俩字")
    st.write("我喜欢:orange[橙色]:sunglasses:")
    st.write("喜欢看:red[快手]，玩游戏（蛋仔派对，逃跑吧少年，和平精英，太空杀，迷你世界），但不喜欢上课，不喜欢钉钉:sunglasses:")
    st.write("最喜欢玩梗:sunglasses:")
    st.write('还有就是......')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write("我班的:orange[男娃娃]都很:red[帅]:sunglasses:")
    #st.image("111.png")
    #with open('霞光.mp3', 'rb') as f:
        #mymp3 = f.read()
    #st.audio(mymp3, format='audio/mp3', start_time=0)

def page_2():
    '''我的图片'''
def page_3():
    '''我的留言'''



if page == '兴趣':
    page_1()
elif page == '图片':
    page_2()
elif page == '留言':
    page_3()
