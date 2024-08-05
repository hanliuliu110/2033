import streamlit as st

page = st.sidebar.radio("首页",["兴趣推荐","数据","排行","留言区"])

def page_1():
    '兴趣推荐'
    st.title("每日纪念")
    st.write(':red[牢大想你了]:cry::cry::cry::cry::cry:')
    st.image("KoBeicetea.jpg")
    with open('seeyouaginx3.mp4', 'rb') as f:
        mymp4 = f.read()
    st.video(mymp4, format='video/mp4', start_time=0)
def page_2():
    '数据'
    pass

def page_3():
    '排行'
    pass

def page_4():
    '留言区'
    pass

if (page == '兴趣推荐'):
    page_1()
elif (page == '数据') :
    page_2()
elif (page == '排行') :
    page_3()
elif (page == '留言区') :
    page_4()
else :
    pass