'''我的主页'''
import streamlit as st
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区'])
import streamlit as st 
import pandas as pd 


msg1 = '将要被打印的信息'

msg2=': orange ［将要被打印的信息］'

d ={
    '姓名':['阿短','编程猫','同学 A '],
    '学号':[1,2,3]
}

d = pd.DataFrame ( d )

number =12345

def page_1():
    '''我的兴趣推荐'''
    st.write (": orange ［我： sunglasses ：班的： sunglasses ：男娃： sunglasses ：娃都很帅： sunglasses :]")
    st.image ("111.png")
    #with open ('霞光．mp3', 'rb') as f :
	#mymp3= f.read ()
    #st.audio (mymp3, format =' audio /mp3', start_time =0)

def page_2():
    '''我的图片处理工具'''
    pass

     
def page_3():
    '''我的智能词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

 
if page == '我的兴趣推荐':
    page_1()
if page == '我的图片处理工具':
    page_2()
if page == '我的智能词典':
    page_3()
if page == '我的留言区':
    page_4()