from tkinter import *
from tkinter import messagebox

janela = Tk()


  
w1 = PanedWindow()  
w1.pack(expand=1)

contador = Label(w1, text="0",bd = 5)  
w1.add(contador)  
contadordata = 0

def funcVermelho():
    janela.after(2500, janela.destroy)
    messagebox.showwarning("Vermelho pressionado", "TOCOU NO VERMELHO COMEÇANDO AUTO-DESTRUIÇÃO")
def funcAzul():
    messagebox.showerror("Azul pressionado", "Vc não vai virar um avatar")
def funcMenos():
    a=1
    global contadordata
    contadordata -= a
    contador.config(text=str(contadordata))
    messagebox.askokcancel("Botão preto pressionado", "Perdeu um ponto man")
def funcMais():
    a=1
    global contadordata
    contadordata += a
    contador.config(text=str(contadordata))
    messagebox.showinfo("Botão amarelo pressionado", "RECEBA um ponto")

janela.geometry("500x300")
botaovermelho = Button(janela, text="ver meio", fg="blue", bg="red", width="20", height="3", command=funcVermelho)
botaovermelho.pack(side=TOP)
botaoazul = Button(janela, text="azu",fg="red", bg="blue", width="20", height="3", command=funcAzul)
botaoazul.pack(side=BOTTOM)
botaopreto = Button(janela, text="negro", fg="yellow", bg="black", width="20", height="3", command=funcMenos)
botaopreto.pack(side=LEFT)
botaoamarelo = Button(janela, text="marelo",fg="black", bg="yellow", width="20", height="3", command=funcMais)
botaoamarelo.pack(side=RIGHT)


janela.mainloop()