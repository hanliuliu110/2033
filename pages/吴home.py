'''我的主页'''
import streamlit as st
page = st.sidebar.radio("我的首页", ["我的兴趣推荐", "我的图片处理工具", "我的智能词典", "我的留言区"])

def page_1():
    '''我的兴趣推荐'''
    st.write("地铁逃生专辑")
    st.image("1.jpg")
    st.image("2.jpg")
    st.image("3.jpg")
    st.image("4.jpg")
    st.image("5.jpg")
    st.image("6.jpg")
    st.image("7.jpg")
    st.image("8.jpg")

def page_2():
    '''我的图片处理工具'''
    pass

def page_3():
    '''我的智能词典'''
    pass
    
def page_4():
    '''我的留言区'''
    pass
    
if page == "我的兴趣推荐":
    page_1()
if page == "我的图片处理工具":
    page_2()
if page == "我的智能词典":
    page_3()
if page == "我的留言区":
    page_4()