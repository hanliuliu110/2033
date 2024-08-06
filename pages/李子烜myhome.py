from PIL import Image
'''我的主页'''

#表情链接：
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

#streamlit==1.28.2

print('python -m ')

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
    st.write('图片小程序')
    uploadeb_file = st.file_uploader('上传图片')
    if uploadeb_file:
        file_name = uploadeb_file.name
        file_type = uploadeb_file.type
        file_size = uploadeb_file.size

        img = Image.open( uploadeb_file)
        st.image(img)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def page_3():
    '''我的留言'''
     st.write('坤坤，:red[I是你真爱粉！！！]')

def img_change(img, rc, gc, bc):
    '''我的图片'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
         for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '兴趣':
    page_1()
elif page == '图片':
    page_2()
elif page == '留言':
    page_3()
