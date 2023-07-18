import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

msg_box = messagebox.showwarning("TOMO PAPUDO", "VOCÊ FOI HACKEADA")

if msg_box:
    msg_box = messagebox.showwarning("PERAI AI!", "PARA SER DESHACKEADA PRECISO QUE ME RESPONDA UMA PERGUNTA:")

if msg_box:
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA CASAR COMIGO?")

count = 1
while msg_box == 'no':
    count += 1
    if count == 6:
        msg_box = messagebox.showerror("TO INDO AI!", "SE VAI APANHAR FEIO")
        break
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA CASAR COMIGO?")

if msg_box == 'yes':
    msg_box = messagebox.showinfo("Boa!", "SABIA ESCOLHA!")
