# *_*coding:utf-8 *_*
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory

from Img_Label import lance_label
from src.split_video import split_video


def quit(m):
    m.destroy()


def lancer_split(video_path, frames=10):
    root = os.getcwd()
    video_name = os.path.split(video_path)[-1].split('.')[0]
    dir_img = os.path.join(root, "img", video_name)
    if not os.path.isdir(dir_img):
        os.makedirs(dir_img)
    split_video(video_path, dir_img, frames)
    mes = Tk()
    mes.title('Message from split')
    center_window(mes, 200, 50)
    Label(mes, text="Split Fini!").pack()
    Button(mes, text="Fermer", command=mes.destroy).pack()
    mes.mainloop()


def selectPath(path):
    path_ = askopenfilename()
    path.set(path_)


def selectdir(path):
    path_ = askdirectory()
    path.set(path_)


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


if __name__ == "__main__":
    root = Tk()
    root.title('Image Label tool')
    center_window(root, 500, 300)
    frame0 = Frame()
    path_video = StringVar()
    path_video.set(os.getcwd().replace('\\', '/'))
    Label(frame0, text="-------------- split video --------------").grid(row=0, column=1)
    Label(frame0, text="Path de video:".rjust(25, " ")).grid(row=1, column=0)
    Entry(frame0, textvariable=path_video).grid(row=1, column=1)
    Button(frame0, text="explorer".center(25, ' '), command=lambda: selectPath(path_video)).grid(row=1, column=2)
    Button(frame0, text="lancer split", command=lambda: lancer_split(path_video.get())).grid(row=2, column=1)
    dir_img = StringVar()
    ser_type = StringVar()
    class_anno = StringVar()
    Label(frame0, text="----------------- Label -----------------").grid(row=3, column=1)
    Label(frame0, text="Path des images:".rjust(25, " ")).grid(row=4, column=0)
    Entry(frame0, textvariable=dir_img).grid(row=4, column=1)
    Label(frame0, text="type des seringes:".rjust(25, " ")).grid(row=5, column=0)
    Entry(frame0, textvariable=ser_type).grid(row=5, column=1)
    Label(frame0, text="class des annotation:".rjust(25, " ")).grid(row=6, column=0)
    Entry(frame0, textvariable=class_anno).grid(row=6, column=1)
    Button(frame0, text="explorer".center(25, ' '), command=lambda: selectdir(dir_img)).grid(row=4, column=2)
    Button(frame0, text="lancer labelling",
           command=lambda: lance_label(dir_img.get(), ser_type.get(), class_anno.get())).grid(row=7, column=1)
    frame0.pack()
    root.mainloop()
