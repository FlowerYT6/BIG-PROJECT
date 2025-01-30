import tkinter
import tkinter.messagebox


def msgbox(msg):
    window = tkinter.Tk()
    window.wm_withdraw()
    tkinter.messagebox.showinfo(title="Information", message=msg)
    window.destroy()
    return None