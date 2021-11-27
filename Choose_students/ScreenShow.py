###############################
#   HansLimon at 2021/09/21   #
#                             #
# Only for educational usage. #
#                             #
#     CopyLEFT Mongrokey®     #
###############################
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from win32api import GetSystemMetrics

userans = ["error_noresponse"]
def ScreenShow(heading, body, mode):
    Systemwidth = GetSystemMetrics(0)
    Systemheight = GetSystemMetrics(1)
    def passer(tkwindow, ans):
        print("ans is " + ans)
        tkwindow.destroy()
        userans[0] = ans
    def call(ans):
        print("ans is " + ans)
        userans[0] = ans
    if mode == "retrycancel":
        messagebox.askretrycancel(heading, body)
    elif mode == "choose":#body[0] is for the text and body[1+] are for texts in buttons
        window = Tk(baseName = "1", className = "1")
        window.geometry("+" + str(Systemwidth//3) + "+" + str(Systemheight//3))
        window.title(heading)
        label0 = Label(window, text = body[0], font = ('SimHei', 14), width = 30, height = 4)
        label0.grid(row = 0)
        Button(window, text = body[1], font = ("SimHei", 12), width = 20, command = lambda: {window.destroy(), call(body[1])}).grid \
            (row = 1//2 + 1%2, column = (1 - 1)%2, sticky = "w", padx = 15, pady = 10)
        Button(window, text = body[2], font = ("SimHei", 12), width = 20, command = lambda: {window.destroy(), call(body[2])}).grid \
            (row = 2//2 + 2%2, column = (2 - 1)%2, sticky = "w", padx = 15, pady = 10)
        #for line in range(1, len(body)):
        #    Button(window, text = body[line], font = ("SimHei", 12), width = 20, command = lambda: {window.destroy(), call(body[line])}).grid \
        #        (row = line//2 + line%2, column = (line - 1)%2, sticky = "w", padx = 15, pady = 10)
        window.mainloop()
        return userans[0]