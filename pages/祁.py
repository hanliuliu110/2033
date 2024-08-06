'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页',['赤石视频','我の个人资料','评论区','兴趣推荐','阴乐','图片处理工具'])

def page_1():
    '''赤石视频'''
    st.write("父亲是矿工，儿子也会是...")
    with open('祁何立吊五.mp4', 'rb') as f:
        mymp4 = f.read()
    st.video(mymp4, format='video.mp4',start_time=0)
    
def page_2():
    '''我の个人资料'''
    st.write("爱玩：")
    st.write(":green[第五人格、co、原神、绝区零、崩铁]")
    st.write(":red[:exclamation:对了，你怎么知道我有：]")
    st.write("那维莱特")
    st.image("祁何立那维莱特.jpg")
    st.write("艾莲")
    st.image("祁何立艾莲.jpg")
    st.write("布洛妮娅")
    st.image("祁何立布洛妮娅.jpg")
    st.write("病患")
    st.image("祁何立病患.jpg")
    st.write("钻皮短剑")
    st.image("祁何立短剑.jpg")
    
    
def page_3():
    '''评论区'''
    st.write(":x:网络错误，请查看您的网络是否正常"":blue[(点击刷新)]")

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
    
def page_4():
    '''兴趣推荐'''
    st.write(":blue[:sparkles:猜你喜欢：]")
    st.write(":red[1.外国网友锐评：法国奥运会不如让芙宁娜去跳舞]")
    st.image("祁何立傻芙.jpg")
    st.write(":orange[2.AI深井图片大赏]")
    st.image("祁何立什静.jpg")
    st.write("3.精致女孩坐高铁")
    st.image("祁何立精致.jpg")
    st.write(":blue[:arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small:点击查看更多:arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small::arrow_down_small:]")
    
def page_5():
    '''阴乐'''
    st.write("Just Friends:musical_note:")
    with open('祁何立Justfriends.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write("童话镇:musical_note:")
    with open('祁何立童话镇.ogg', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/ogg', start_time=0)
    
def page_6():
    '''图片处理工具'''
    st.write("图片换色工具:badminton_racquet_and_shuttlecock:")
    uploaded_file = st.file_uploader("上传图片",type=["png",'jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))        
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))              

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
elif page == '图片处理工具':
    page_6()

#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/