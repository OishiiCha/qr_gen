from tkinter import *
import qrcode
import pyperclip as pc
from PIL import ImageTk, Image

height = 250
width = 350
bgc = 'grey12'

row1 = (height/12)*1
row2 = (height/12)*2+10
row3 = (height/12)*4+5
row4 = (height/12)*5+15
row5 = (height/12)*9
row6 = (height/12)*11

enfont = ('calibri', 14)
lfont = ('calibri', 16)
clrfont = ('calibri', 14)
pastefont = ('calibri', 20)

root = Tk()
root.geometry("300x500")
root.title("QR Generator")
root.resizable(width=False, height=False)
root.configure(bg=bgc)
root.geometry(str(width) + "x" + str(height))
root.iconbitmap('data/logo.ico')

# images
gen_p = Image.open('data/images/genbutton.png') # 1200x300
gen_r = gen_p.resize((180, 45), Image.ANTIALIAS)
gen_i = ImageTk.PhotoImage(gen_r)

clr_p = Image.open('data/images/clrbutton.png') # 500x300
clr_r = clr_p.resize((75, 45), Image.ANTIALIAS)
clr_i = ImageTk.PhotoImage(clr_r)


def go_button():
    myurl = str(url_ent.get())
    filename = str(file_ent.get())
    img = qrcode.make(myurl)
    type(img)
    img.save('export/' + filename + '.png')

def delete_text():
    file_ent.delete(0, END)
    url_ent.delete(0, END)

def url_paste():
    pasted = pc.paste()
    url_ent.delete(0, END)
    url_ent.insert(0, pasted)

url_label = Label(root, font=lfont, bg=bgc, fg='white', text='Enter URL')
url_label.place(x=int(width/2), y=row1, anchor='center')
url_ent = Entry(root, font=enfont, justify="center", width=20)
url_ent.place(x=int(width/2), y=row2, anchor='center')
url_p_b = Button(root, font=pastefont, justify="center", fg='white', bg=bgc, height=0, text='⬅', borderwidth=0, highlightthickness=0, activebackground=bgc, command=url_paste)
url_p_b.place(x=int(width/10*9), y=row2, anchor='center')
file_label = Label(root, font=lfont, bg=bgc, fg='white', text='Enter File Name')
file_label.place(x=int(width/2), y=row3, anchor='center')
file_ent = Entry(root, font=enfont, justify="center", width=20)
file_ent.place(x=int(width/2), y=row4, anchor='center')
go_b = Button(root, font=lfont, justify="center", height=0, image=gen_i, borderwidth=0, highlightthickness=0, activebackground=bgc, bg=bgc, width=190, command=go_button)
go_b.place(x=int(width/3), y=row5, anchor='center')
clr_b = Button(root, font=clrfont, justify="center", height=0, image=clr_i, borderwidth=0, highlightthickness=0, activebackground=bgc, bg=bgc, width=85, command=delete_text)
clr_b.place(x=int(width/4*3)+20, y=row5, anchor='center')

if __name__ == '__main__':
    root.mainloop()
