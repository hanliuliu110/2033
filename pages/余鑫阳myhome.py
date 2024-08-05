'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '图片处理工具', '数据收集', '工具分享', '留言区',])

def page_1():
    '''我的兴趣推荐'''
    st.write(":red_circle:听歌是我的兴趣之一，听的大多是一些老点的歌，我多用的是“网易云音乐”在听，虽然说是老歌:red_circle:，其实更多是一些红歌，“:red[永远也不会嫌腻]”的那种，你们喜欢听音乐吗?可以分享你们喜欢听的一:red_circle:些音乐啦！:wink:")

def page_2():
    '''图片处理工具'''
    pass
    
def page_3():
    '''数据收集'''
    pass

def page_4():
    '''工具分享'''
    pass

def page_5():
    '''留言区'''
    pass

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

