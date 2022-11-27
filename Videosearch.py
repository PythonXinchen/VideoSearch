#1.bilibili
#2.腾讯视频
#3.爱奇艺
from bs4 import BeautifulSoup
import requests
import tkinter
#腾讯视频的请求头
qqheaders = {
    'cookie':'',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
}

Video_source = ['https://v.qq.com/x/search/?q=']
headers = [qqheaders]


#开始搜索
def search_video(ViedoInput):
    data = requests.get('https://v.qq.com/x/search/?q=' + ViedoInput,headers=qqheaders)
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
