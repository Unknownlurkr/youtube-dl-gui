import tkinter as tk
from pytube import YouTube

#3)CREATE FUNCTION TO START DOWNLOADING
#bg setrs the background colour
#command is used to call the function
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    #video.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    video.download()
    #print("Video Title: " , video.title)
    tk.Label(root, text='your video has been downloaded', font='arial 15',fg="black").place(x=180,y=210)

#1) CREATE DISPLAY WINDOW
#initialize tkinter to create display window
root = tk.Tk()
#geometry() sets windows width and height
root.geometry('500x300')
#resizeable(0,0) set the fix size of the window
root.resizable(0,0)
#title() gives the title of the window
root.title('Youtube Downloader')
#Label() widget used to display text users can modify
#root-name of the window, text display the title of the label, font in which the text is written, pack prganized widget in block
tk.Label(root, text='Youtube video downloader',font='arial 20 bold').pack()

#2) CREATE FIELD TO ENTER LINK
#link-string variable that stores yt video link the user enters
#Entry()- widget used when we want to create an input text field and width sets width of the entry widget
#textvariable-used to retrive the value of current text variable to the Entry() widget
#place()-used to place widget into specific postion
#link = StringVar()
link = tk.StringVar()
#yt = YouTube(link)
tk.Label(root, text='Copy the link and paste it here:',font='arial 15 bold').place(x=160,y=60)
link_enter = tk.Entry(root, width=70,textvariable=link ,bg='lightgreen').place(x=32,y=90)
#Button() widget used to display button on the window
tk.Button(root, text='DOWNLOAD',font='arial 15 bold', bg='purple',padx=2,command=Downloader).place(x=180,y=150)

#root.mainloop()-method that executes when we run the program
root.mainloop()

#add file patth location 