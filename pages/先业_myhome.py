'''我的主页'''
import streamlit as st
page = st.sidebar.radio("我的首页",["推荐","游戏分享","留言区","挑战"])
def page1():
    """推荐"""
    st.write("植物大战僵尸杂交版修改器https://pan.quark.cn/s/c73a972e2368夸克网盘")
    st.image("修改器.png")
def page2():
    """游戏分享"""
    pass
def page3():
    """留言区"""
    pass
def page4():
    """挑战"""
    pass
if page =="推荐":
    page1()
elif page =="游戏分享":
    page2()
elif page =="留言区":
    page3()
elif page =="挑战":
    page4()