from tkinter import *
import hashlib

s256 = hashlib.sha256()
md5 = hashlib.md5()
sh1 = hashlib.sha1()

def test():
    pwhData = entryW.get()
    if pwhData == "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4":
        labHash["text"] = "sha256"
        Opw["text"] = "1234"
    elif pwhData == "7110eda4d09e062aa5e4a390b0a572ac0d2c0220":
        labHash["text"] = "sha1"
        Opw["text"] = "1234"
    elif pwhData == "81dc9bdb52d04dc20036dbd8313ed055":
        labHash["text"] = "md5"
        Opw["text"] = "1234"
    elif pwhData == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8":
        labHash["text"] = "sha256"
        Opw["text"] = "password"
    elif pwhData == "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8":
        labHash["text"] = "sha1"
        Opw["text"] = "password"
    elif pwhData == "5f4dcc3b5aa765d61d8327deb882cf99":
        labHash["text"] = "md5"
        Opw["text"] = "password"
    elif pwhData == "bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721":
        labHash["text"] = "sha256"
        Opw["text"] = "abcdef"
    elif pwhData == "1f8ac10f23c5b5bc1167bda84b833e5c057a77d2":
        labHash["text"] = "sha1"
        Opw["text"] = "abcdef"
    elif pwhData == "e80b5017098950fc58aad83c8c14978e":
        labHash["text"] = "md5"
        Opw["text"] = "abcdef"
    elif pwhData == "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5":
        labHash["text"] = "sha256"
        Opw["text"] = "qwerty"
    elif pwhData == "b1b3773a05c0ed0176787a4f1574ff0075f7521e":
        labHash["text"] = "sha1"
        Opw["text"] = "qwerty"
    elif pwhData == "d8578edf8458ce06fbc5bb76a58c5ca4":
        labHash["text"] = "md5"
        Opw["text"] = "qwerty"
    elif pwhData == "":
        labHash["text"] = "None"
        Opw["text"] = "None"
    else:
        labHash["text"] = "I don't know"
        Opw["text"] = "I don't know"


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

root = Tk()
root.title("Test")
root.geometry("600x300+300+200")
labPWs = Label(root, text="PW hash code:", anchor=E, justify=RIGHT, font=("times",20))
lab1 = Label(root, text="Hashlib:", anchor=E, justify=RIGHT, font=("times",20))
labHash = Label(root, text="None", anchor=W, justify=RIGHT, font=("times",20))
Opww = Label(root, text="Password:", anchor=E, justify=RIGHT, font=("times",20))
Opw = Label(root, text="None", anchor=W, justify=RIGHT, font=("times",20))
entryW = Entry(root, width=70)
btnTest = Button(root, text="Test",font=("Helvetica", 30, "bold"), command=test)
labPWs.grid(row=0, column=0, sticky=EW)
entryW.grid(row=0, column=1, sticky=EW)
lab1.grid(row=1, column=0, sticky=EW)
labHash.grid(row=1, column=1, sticky=EW)
Opww.grid(row=2, column=0, sticky=EW)
Opw.grid(row=2, column=1, sticky=EW)
btnTest.grid(row=3, column=0, sticky=EW)

top = Toplevel(root)
labID = Label(top, text="ID", anchor=E, justify=RIGHT, font=("times",20))
labPW = Label(top, text="Password", anchor=E, justify=RIGHT, font=("times",20))
entryID = Entry(top)
entryPW = Entry(top, show="*")
btnLogin = Button(top, text="Login", command=login)
btnExit = Button(top, text="Exit", command=exitp)
labID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labPW.grid(row=1, column=0, sticky=NSEW)
entryPW.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnExit.grid(row=2, column=1, sticky=NSEW)

root.withdraw()
root.mainloop()