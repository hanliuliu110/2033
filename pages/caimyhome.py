import streamlit as st
from PIL import Image
from pydub import AudioSegment

page = st.sidebar.radio("首页",["兴趣推荐","工具","排行","留言区"])


def page_1():
    '兴趣推荐'

    st.title("每日纪念")
    st.write(':red[牢大想你了]:cry::cry::cry::cry::cry:')
    st.image("KoBeicetea.jpg")
    with open('seeyouaginx3.mp4', 'rb') as f:
        mymp4 = f.read()
    st.video(mymp4, format='video/mp4', start_time=0)

def page_2():
    '''工具'''
    tab_photo,tab_music,tab_video = st.tabs(["图片工具","音频工具","视频工具"])
    with tab_photo:
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
    with tab_music:
        st.write(":sunglasses:音频格式小程序:sunglasses:")
        uploaded_file = st.file_uploader("选择音乐文件", type=['wav'])
        if uploaded_file is not None:
            # 显示文件名称和格式
            st.write("上传曲目: ", uploaded_file.name)
        
            # 因为 streamlit 的上传文件是一个 BytesIO 对象，我们可以直接读取它
            audio = AudioSegment.from_file(uploaded_file, format=uploaded_file.name.split('.')[-1])
        
            # 允许用户选择目标格式
            formats = ['mp3', 'wav', 'ogg', 'flac']
            target_format = st.selectbox("需要转换格式", formats)
        
            if st.button("开始"):
                try:
                    # 将文件转化为用户选择的格式
                    audio_buffer = audio.export(format=target_format)
    
                    # 读取导出的音频文件的二进制数据
                    audio_data = audio_buffer.read()
                    
                    # 提供下载
                    st.download_button(
                        label=f"下载 {target_format.upper()} 文件",
                        data=audio_data,
                        file_name=f"{uploaded_file.name.split('.')[0]}.{target_format}",
                        mime=f"audio/{target_format}")
                except Exception as e:
                    st.warning("该音频文件似乎不支持这样转换，请尝试选择其他格式进行转换或更换音频文件")
                    
            
    #     st.audio(uploaded_file, format='audio/mp3', start_time=0)
    # uploaded_file = st.file_uploader("选择视频文件")
    # if uploaded_file is not None:
    #     st.write("视频名:", uploaded_file.name)
    #     st.video(uploaded_file, start_time=0)

def page_3():
    '排行'
    pass

def page_4():
    '留言区'
    pass

def img_change(img, rc, gc, bc):
    '图片处理'
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img



if (page == '兴趣推荐'):
    page_1()
elif (page == '工具') :
    page_2()
elif (page == '排行') :
    page_3()
elif (page == '留言区') :
    page_4()
else :
    pass
