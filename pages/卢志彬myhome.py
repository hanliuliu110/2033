'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页',['歌曲推荐室','评论室','我的收藏夹','我的分享','音频格式处理'])

def page_1():
    pass
    
def page_2():
    pass
    
def page_3():
    pass
    
def page_4():
    pass
    
def page_5():
    pass


if page == '歌曲推荐室':
    page_1()
elif page == '评论室':
    page_2()
elif page == '我的收藏夹':
    page_3()
elif page == '我的分享':
    page_4()
elif page == '音频格式处理':
    page_5()