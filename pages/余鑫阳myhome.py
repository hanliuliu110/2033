'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '图片处理工具', '数据收集', '工具分享', '留言区',])

def page_1():
    '''我的兴趣推荐'''
    st.write(":red_circle:听歌是我的兴趣之一，听的大多是一些老点的歌，我多用的是“网易云音乐”在听，虽然说是老歌:red_circle:，其实更多是一些红歌，“:red[永远也不会嫌腻]”的那种，你们喜欢听音乐吗?可以分享你们喜欢听的一:red_circle:些音乐啦！:wink:")

def page_2():
    '''图片处理工具'''
    st.write("这个可以简单地处理图片（滤镜效果）:face_with_hand_over_mouth:操作如下:arrow_down:")
    st.write(":one:点击右侧“Browesfiles”按钮，上传图片；上传图片后点击上方选项查看")
    st.write("注：作者把自己壁纸（图片示例）放在在同一文件目录下了，可以先试试:wink:")
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])

    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2)) 
        
    
def page_3():
    '''数据收集'''
    pass

def page_4():
    '''工具分享'''
    #第一个
    st.write(":one:")
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])

    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
    
def page_5():
    '''留言区'''
    pass


def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if page == '我的兴趣推荐':
    page_1()
if page == '图片处理工具':
    page_2()
elif page == '数据收集':
    page_3()
elif page == '工具分享':
    page_4()
elif page == '留言区':
    page_5()

