# for windows
from tkinter import *
import tkinter
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import random

font1 = ("Arial bold", 15)
font2 = ("Arial", 14)
font3 = ("Arial", 13)

# random proxy creator
def randomProxy():
    listOfProxies = RequestProxy()
    myProxy = listOfProxies.get_proxy_list()
    return myProxy[0]

class youtubeViewerBot():
    def __init__(self, root):
        self.root = root
        self.menu()

    def menu(self):
        newFrame = Frame(self.root)
        newFrame.grid(row=0, column=0, sticky=N+S+E+W)
        programName = Label(newFrame, text='Youtube Viewer Bot', font = font1)
        programName.grid(row=0, column=0,padx=10, pady=30)

        myLink = Label(newFrame, text='Enter the link of the Youtube video:', font = font2)
        myLink.grid(row=1, column=0,padx=15, pady=15)
        link = tkinter.StringVar()
        entry = tkinter.Entry(newFrame, textvariable=link)
        link.set("")
        entry.grid(row=2, column=0,padx=10, pady=10)

        lblThis = Label(newFrame, text='Enter the number of views:', font = font2)
        lblThis.grid(row=3, column=0,padx=15, pady=15)
        lbl2 = tkinter.StringVar()
        entry2 = tkinter.Entry(newFrame, textvariable=lbl2)
        lbl2.set("")
        entry2.grid(row=4, column=0,padx=10, pady=10)

        lblThis2 = Label(newFrame, text='Enter the time for the viewing video(seconds):', font = font2)
        lblThis2.grid(row=5, column=0,padx=15, pady=15)
        lbl3 = tkinter.StringVar()
        entry3 = tkinter.Entry(newFrame, textvariable=lbl3)
        lbl3.set("")
        entry3.grid(row=6, column=0,padx=10, pady=10)

        downloadButton = Button(newFrame, text='Start',font = font2, fg="green", command=lambda link=link,lbl2=lbl2,lbl3=lbl3: self.viewer(link,lbl2,lbl3))
        downloadButton.grid(row=7, column=0)

        
    def viewer(self,link,number,length):
        viewCount = int(number.get())
        for i in range(viewCount):
            self.eachView(link,number,length)
        myBrowser.close()
        
    def eachView(self,link,number,length):
        myOption = Options()
        # each time assigning random proxy
        randomTaker = randomProxy()
        currentProxy = randomTaker.get_address()
        thisSetting = webdriver.DesiredCapabilities.CHROME.copy()
        thisSetting['proxy']={
        "httpProxy":currentProxy,
        "ftpProxy":currentProxy,
        "sslProxy":currentProxy,    
        "noProxy":None,
        "proxyType":"MANUAL",
        "class":"org.openqa.selenium.Proxy",
        "autodetect":False
        }
        #######################    CHANGE TO THE FOLLOWING LINE  #############################
        myBrowser = webdriver.Chrome(executable_path=r"C:\ChromeDriver", options=myOption)
        #######################################################################################
        viewLength = float(length.get())
        myBrowser.get(link.get())
        time.sleep(10)
        element = myBrowser.find_element_by_xpath("//*[@class='ytp-large-play-button ytp-button']")
        element.click()
        time.sleep(viewLength)
        


if __name__ == '__main__':
    root = Tk()
    root.geometry("430x450+600+200")
    youtubeViewerBot(root)
    root.mainloop()
