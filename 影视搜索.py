#1.bilibili
#2.腾讯视频
#3.爱奇艺
from bs4 import BeautifulSoup
import requests
import tkinter
#腾讯视频的请求头
qqheaders = {
    'cookie':'RK=j70QURoBEk; ptcz=6ffaf62f483af6ba826e850e3ee03ba0659257d4f5af844f46eaa728e8029157; pgv_pvid=8343282850; pac_uid=0_a17f1bd708d8e; tvfe_boss_uuid=12a3cff58ddcefdd; sd_userid=59611662982552807; fqm_pvqid=1923d981-1987-4446-8282-fa201d2854a8; iip=0; _tc_unionid=c2e56cfb-bdc7-435b-bd21-8f60b816f514; eas_sid=P1y6Y6k7G5Z4h5Q7U3q7O5j9i3; ptui_loginuin=1214857227; video_platform=2; pgv_info=ssid=s5398108480',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
}

Video_source = ['https://v.qq.com/x/search/?q=']
headers = [qqheaders]


#开始搜索
def search_video(ViedoInput):
    for i in range(Video_source):
        data = requests.get(Video_source[i] + ViedoInput,headers=qqheaders)
        print(Video_source[i] + ViedoInput)
        data.encoding='utf-8'
        print(data.text)




#获取输入框中的影视名
def getVideoTextInput():
    ViedoInput = tkinter.Entry.get(video_text)
    search_video(ViedoInput)


#初始化图形界面
top = tkinter.Tk()
top.title('影视搜索')

#提供输入影视名的输入框
video_text = tkinter.Entry(top, text='影视名:')
video_text.pack(side='left')

#搜索按钮
search_button = tkinter.Button(top,command=getVideoTextInput,text='搜索')
search_button.pack(side='right')

top.mainloop()