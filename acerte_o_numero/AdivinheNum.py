from tkinter import *
from random import randint


def criaLayoutInicial():
    lb_adivinhe.place(x=100, y=30, anchor="center")
    bt_tente.place(x=105, y=50)    
    bt_quit.place(x=45, y=50)
    bt_tente["command"] = criaLayoutAdivinha

def criaLayoutAdivinha():
    numPc = randint(1, 100)
    lb_adivinhe["text"] = "Adivinhe qual é!"
    bt_tente["text"] = "CHUTE"
    bt_tente["command"] = adivinha
    lb_pensei.place(x=100, y=40, anchor="center")
    lb_adivinhe.place(x=100, y=60, anchor="center")
    entrada.place(x=100, y=100, anchor="center")
    entrada.focus()
    bt_tente.place(x=105, y=140)    
    bt_quit.place(x=45, y=140)
    

def adivinha():
    num = entrada.getint()
    
    

def validar_numero(texto):
    return texto.isdigit() or texto == ""  # Permite apenas números

    

janelaPrincipal = Tk()

vcmd = janelaPrincipal.register(validar_numero)  # Registra a função de validação

entrada = Entry(janelaPrincipal, width=3, validate="key", validatecommand=(vcmd, "%P"))
lb_adivinhe = Label(janelaPrincipal, text="Adivinhe o número!")
lb_pensei = Label(janelaPrincipal, text="Pensei em um número")
bt_tente = Button(janelaPrincipal, text="VAMOS", width=6, height=1)
bt_quit = Button(janelaPrincipal, text="QUIT", command=janelaPrincipal.destroy, width=6, height=1)


criaLayoutInicial()

janelaPrincipal.geometry("200x200+300+300")
janelaPrincipal.mainloop()