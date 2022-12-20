# 1.bilibili（划掉）
# 2.腾讯视频
# 3.爱奇艺
from bs4 import BeautifulSoup
import requests
import tkinter
import webbrowser
from tkinter import ttk
import messagebox

# 腾讯视频的请求头
headers = {
    'cookie': '',  # 只加个cookie空就能过
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
}

Video_source = ['https://v.qq.com/x/search/?q=']


def gotoz(url):
    webbrowser.open_new_tab(url=url)


def gotofree(url):
    webbrowser.open_new_tab(url="https://bd.jx.cn/?url=" + url)


# 得到初始数据
def search_video(ViedoInput):
    for i in Video_source:
        print(type(i))
        data = requests.get(i + ViedoInput, headers=headers)
        data.encoding = 'utf-8'
        Processing_data(data.text, ViedoInput=ViedoInput)


# 对初始数据开始筛选信息
def Processing_data(data, ViedoInput):
    soup = BeautifulSoup(data, 'html.parser')
    for u in soup.find_all(name='a', href=True, _stat='video:poster_tle'):  # 查找影视的url
        Video_url = u['href']  # 获取'href'
        print(Video_url)
    name = soup.find(name='em', class_='hl').text  # 显示影视name
    try:
        detailed = soup.find_all(name='span', class_='sub')[0].text
        search_result(name=name, detailed=detailed, Video_url=Video_url, ViedoInput=ViedoInput)
    except IndexError:
        messagebox.showwarning('警告', '未找到相关匹配内容')


# 创建一个新窗口来显示搜索信息
def search_result(name, detailed, Video_url, ViedoInput):
    result = tkinter.Tk()
    result.geometry("600x500+200+20")
    result.title(ViedoInput + '的搜索结果')
    result.iconbitmap('icon.ico')
    tree = ttk.Treeview(result)
    tree["columns"] = ("影视名", "基本信息", "网址")
    tree.heading("影视名", text="影视名")  # #设置显示的表头名
    tree.heading("基本信息", text="基本信息")
    tree.heading("网址", text="网址")
    tree.column("影视名", width=100, minwidth=100)  # #设置列
    tree.column("基本信息", width=100, minwidth=100)
    tree.column("网址", width=100, minwidth=100)
    tree.insert("", 0, values=(name, detailed, Video_url))  # #给第0行添加数据，索引值可重复
    tree.pack(pady=20)
    z = tkinter.Button(result, command=lambda: gotoz(url=Video_url), text="带我去官网访问")
    z.pack()
    f = tkinter.Button(result, command=lambda: gotofree(url=Video_url), text="让我白嫖")
    f.pack()
    result.mainloop()


# 获取输入框中的影视名
def getVideoTextInput():
    ViedoInput = tkinter.Entry.get(video_text)
    search_video(ViedoInput)


# 初始化图形界面
top = tkinter.Tk()
top.title('影视搜索')
# top.iconbitmap('icon.ico')

# 提供输入影视名的输入框
video_text = tkinter.Entry(top)
video_text.pack(side='left')

# 搜索按钮
search_button = tkinter.Button(top, command=getVideoTextInput, text='搜索')
search_button.pack(side='right')

top.mainloop()
