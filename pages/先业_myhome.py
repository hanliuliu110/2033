'''我的主页'''
from PIL import Image

import streamlit as st
page = st.sidebar.radio("我的首页",["推荐","游戏分享","留言区","挑战"])
def page1():
    """推荐"""
    st.write("植物大战僵尸杂交版修改器个人认为:red[非常好用和有趣]:+1:夸克网盘https://pan.quark.cn/s/c73a972e2368")
    st.image("hxy修改器.png")
    st.image("hxy修改器1.png")
    st.image("hxy修改器2.png")
    st.image("hxy修改器3.png")
    st.image("hxy修改器4.png")
    st.image("hxy修改器5.png")
    st.image("hxy修改器6.png")
    st.write("求生之路2的萌新花费100小时打的成就:relieved:")
    st.image("hxy战绩.png")
    
def page2():
    """游戏分享"""
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
    uploaded_file = st.file_uploader("选择音乐文件")
    if uploaded_file is not None:
        st.write("歌曲名:", uploaded_file.name)
        st.audio(uploaded_file, format='audio/mp3', start_time=0)
    uploaded_file = st.file_uploader("选择视频文件")
    if uploaded_file is not None:
        st.write("视频名:", uploaded_file.name)
        st.video(uploaded_file, start_time=0)
def page3():
    """留言区"""
    pass
def page4():
    """挑战"""
    pass
def img_change(img,rc,gc,bc):
    """图片处理"""
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y]=(b,g,r)
    return img
if page =="推荐":
    page1()
elif page =="游戏分享":
    page2()
elif page =="留言区":
    page3()
elif page =="挑战":
    page4()