'''我的主页'''
import streamlit as st
from PIL import Image
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
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2,tab3,tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
    uploaded_file = st.file_uploader("选择视频文件")
    if uploaded_file is not None:
        st.write("视频名:", uploaded_file.name)
        st.video(uploaded_file, start_time=0)

def page_3():
    '''我的智能词典'''
    pass
    
def page_4():
    '''我的留言区'''
    pass

def img_change(img, rc, gc, bc):
    '''图片管理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
    
if page == "我的兴趣推荐":
    page_1()
if page == "我的图片处理工具":
    page_2()
if page == "我的智能词典":
    page_3()
if page == "我的留言区":
    page_4()