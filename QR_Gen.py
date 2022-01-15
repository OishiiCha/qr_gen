from tkinter import *
import qrcode

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

root = Tk()
root.geometry("300x500")
root.title("QR Generator")
root.resizable(width=False, height=False)
root.configure(bg=bgc)
root.geometry(str(width) + "x" + str(height))
root.iconbitmap('data/logo.ico')

def go_button():
    myurl = str(url_ent.get())
    filename = str(file_ent.get())
    img = qrcode.make(myurl)
    type(img)
    img.save('export/' + filename + '.png')

def delete_text():
    file_ent.delete(0, END)
    url_ent.delete(0, END)

url_label = Label(root, font=lfont, bg=bgc, fg='white', text='Enter URL')
url_label.place(x=int(width/2), y=row1, anchor='center')
url_ent = Entry(root, font=enfont, justify="center", width=20)
url_ent.place(x=int(width/2), y=row2, anchor='center')
file_label = Label(root, font=lfont, bg=bgc, fg='white', text='Enter File Name')
file_label.place(x=int(width/2), y=row3, anchor='center')
file_ent = Entry(root, font=enfont, justify="center", width=20)
file_ent.place(x=int(width/2), y=row4, anchor='center')
go_b = Button(root, font=lfont, justify="center", height=0, text='Generate and Save', command=go_button)
go_b.place(x=int(width/3), y=row5, anchor='center')
clr_b = Button(root, font=clrfont, justify="center", height=0, text='Clear', command=delete_text)
clr_b.place(x=int(width/4*3), y=row5, anchor='center')

if __name__ == '__main__':
    root.mainloop()
