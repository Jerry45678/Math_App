from tkinter import *
import hashlib

s256 = hashlib.sha256()

def login():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0:
        s256.update(pwData.encode("utf-8"))
        pwHash = s256.hexdigest()
        #h3041723
        if idData == "csie" and pwHash == "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
            root.deiconify()
            top.destroy()
        else:
            entryID.delete(0, "end")
            entryPW.delete(0, "end")
    else:
            entryID.delete(0, "end")
            entryPW.delete(0, "end")

def exitp():
    top.destroy()
    root.destroy()

def setBtnText(num):
    global count
    count+=1
    if count % 2 != 0:
        sign = "O"
    else:
        sign = "X"
    btn0
    if num == 0 and btn0.cget('text')==" ":
        btn0.config(text=sign, background="black")
    elif num == 1 and btn1.cget('text')==" ":
        btn1.config(text=sign)
    elif num == 2 and btn2.cget('text')==" ":
        btn2.config(text=sign)
    elif num == 3 and btn3.cget('text')==" ":
        btn3.config(text=sign)
    elif num == 4 and btn4.cget('text')==" ":
        btn4.config(text=sign)
    elif num == 5 and btn5.cget('text')==" ":
        btn5.config(text=sign)
    elif num == 6 and btn6.cget('text')==" ":
        btn6.config(text=sign)
    elif num == 7 and btn7.cget('text')==" ":
        btn7.config(text=sign)
    elif num == 8 and btn8.cget('text')==" ":
        btn8.config(text=sign)

    if btn0.cget('text') == btn1.cget('text') and btn0.cget('text') == btn2.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1(O) win")
        elif btn0.cget('text') == "X":
            print("Player2(X) win")
    if btn3.cget('text') == btn4.cget('text') and btn3.cget('text') == btn5.cget('text'):
        if btn3.cget('text') == "O":
            print("Player1(O) win")
        elif btn3.cget('text') == "X":
            print("Player2(X) win")
    if btn6.cget('text') == btn7.cget('text') and btn6.cget('text') == btn8.cget('text'):
        if btn6.cget('text') == "O":
            print("Player1(O) win")
        elif btn6.cget('text') == "X":
            print("Player2(X) win")
    if btn0.cget('text') == btn3.cget('text') and btn0.cget('text') == btn6.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1(O) win")
        elif btn0.cget('text') == "X":
            print("Player2(X) win")
    if btn1.cget('text') == btn4.cget('text') and btn1.cget('text') == btn7.cget('text'):
        if btn1.cget('text') == "O":
            print("Player1(O) win")
        elif btn1.cget('text') == "X":
            print("Player2(X) win")
    if btn2.cget('text') == btn5.cget('text') and btn2.cget('text') == btn8.cget('text'):
        if btn2.cget('text') == "O":
            print("Player1(O) win")
        elif btn2.cget('text') == "X":
            print("Player2(X) win")
    if btn0.cget('text') == btn4.cget('text') and btn0.cget('text') == btn8.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1(O) win")
        elif btn0.cget('text') == "X":
            print("Player2(X) win")
    if btn2.cget('text') == btn4.cget('text') and btn2.cget('text') == btn6.cget('text'):
        if btn2.cget('text') == "O":
            print("Player1(O) win")
        elif btn2.cget('text') == "X":
            print("Player2(X) win")

count = 0

root = Tk()
root.title("Game")
root.geometry("600x600+460+200")
root.config(bg="White")
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

top = Toplevel(root)
labID = Label(top, text="ID", anchor=E, justify=RIGHT, font=("times",20))
labPW = Label(top, text="Password", anchor=E, justify=RIGHT, font=("times",20))
entryID = Entry(top)
entryPW = Entry(top, show="*")
btnLogin = Button(top, text="Login", command=login)
btnExit = Button(top, text="Exit", command=exitp)
labID.grid(row=0, column=0 ,sticky=NSEW)
entryID.grid(row=0, column=1 ,sticky=NSEW)
labPW.grid(row=1, column=0 ,sticky=NSEW)
entryPW.grid(row=1, column=1 ,sticky=NSEW)
btnLogin.grid(row=2, column=0 ,sticky=NSEW)
btnExit.grid(row=2, column=1 ,sticky=NSEW)


btn0 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(0))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(root, text=" ",font=("Helvetica", 30, "bold"), command=lambda:setBtnText(8))
btn8.grid(row=2, column=2, sticky=NSEW)

root.withdraw()
root.mainloop()