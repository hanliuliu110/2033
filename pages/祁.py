'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页',['赤石视频','我の个人资料','评论区','兴趣推荐','阴乐'])

def page_1():
    '''赤石视频'''
    pass
def page_2():
    '''我の个人资料'''
    pass
def page_3():
    '''评论区'''
    pass
def page_4():
    '''兴趣推荐'''
    st.write(":blue[:sparkles:猜你喜欢：]")
    st.write(":red[1.外国网友锐评：法国奥运会不如让芙宁娜去跳舞]")
    st.image("傻芙.jpg")
    st.write(":orange[2.AI深井图片大赏]")
    st.image("什静.jpg")
    st.write("3.精致女孩坐高铁")
    st.image("精致.jpg")
    
def page_5():
    '''阴乐'''
    st.write("Just Friends")
    with open('1outa - Just Friends  (铃声).mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write("童话镇")
    with open('卿听盲盒 - 《童话镇》萧忆情Alex：总有一条，蜿蜒在童话镇里七彩的河 (长音频).ogg', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/ogg', start_time=0)
    

if page == '赤石视频':
    page_1()
elif page == '我の个人资料':
    page_2()
elif page == '评论区':
    page_3()
elif page == '兴趣推荐':
    page_4()
elif page == '阴乐':
    page_5()

#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/