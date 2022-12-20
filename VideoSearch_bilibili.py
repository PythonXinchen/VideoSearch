from bs4 import BeautifulSoup
import requests
import tkinter
import webbrowser
from tkinter import ttk
import messagebox


def init():
    top = tkinter.Tk()  # 图形化
    top.geometry('500*400')  # 设置分辨率
    top.title('BilibiliSearch')  # 设置标题
    video_text = tkinter.Entry(top)
    video_text.pack(side='left')
    top.mainloop()
    return video_text

def get_text():
    viedoinput = tkinter.Entry.get(init())
    get_data()


class Search:
    def __init__(self, search, data, url):
        self.search = search
        self.data = data
        self.url = url

def get_data(url):
