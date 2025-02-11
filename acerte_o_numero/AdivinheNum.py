from tkinter import *
from random import randint

numPc = 0
tentativas = 0

def criaLayoutInicial():
    bt_tente.config(state="normal")
    lb_pensei.place_forget()
    entrada.place_forget()
    lb_adivinhe["text"] = "Adivinhe o número!"
    lb_adivinhe.place(x=100, y=30, anchor="center")
    bt_tente.place(x=105, y=50)    
    bt_quit.place(x=45, y=50)
    bt_quit["command"] = janelaPrincipal.destroy
    bt_tente["command"] = criaLayoutAdivinha
    bt_tente["text"] = "TENTE"
    bt_quit["text"] = "QUIT"
    lb_feedback.place_forget()
    entrada.delete(0, END)

def criaLayoutAdivinha():
    global numPc
    numPc = randint(1, 100)
    lb_pensei["text"] = "Pensei em um número"
    lb_adivinhe["text"] = "Adivinhe qual é!"
    bt_tente["text"] = "CHUTE"
    bt_tente["command"] = adivinha
    bt_quit["command"] = criaLayoutInicial
    bt_quit["text"] = "VOLTAR"
    lb_feedback["text"] = "Esperando"
    lb_pensei.place(x=100, y=40, anchor="center")
    lb_adivinhe.place(x=100, y=60, anchor="center")
    entrada.place(x=100, y=100, anchor="center")
    entrada.focus()
    lb_feedback.place(x=100, y=120, anchor="center")
    bt_tente.place(x=105, y=140)    
    bt_quit.place(x=45, y=140)
    

def adivinha():
    global tentativas
    tentativas+=1
    num = entrada.get()
    num = entrada.getint(num)
    entrada.select_range(0, END)
    if numPc == num:
        lb_feedback["text"] = "Acertou em " + str(tentativas) + " tentativas"
        bt_tente.config(state="disabled")
    elif numPc > num:
        lb_feedback["text"] = "O meu número é maior"
    else:
        lb_feedback["text"] = "O meu número é menor"
    
    

def validar_numero(texto):
    return texto.isdigit() or texto == ""  # Permite apenas números

    

janelaPrincipal = Tk()

vcmd = janelaPrincipal.register(validar_numero)  # Registra a função de validação

entrada = Entry(janelaPrincipal, width=3, validate="key", validatecommand=(vcmd, "%P"))
lb_adivinhe = Label(janelaPrincipal)
lb_pensei = Label(janelaPrincipal)
bt_tente = Button(janelaPrincipal, text="VAMOS", width=6, height=1)
bt_quit = Button(janelaPrincipal, text="QUIT", command=janelaPrincipal.destroy, width=6, height=1)
lb_feedback = Label(janelaPrincipal)

criaLayoutInicial()

janelaPrincipal.geometry("200x200+300+300")
janelaPrincipal.mainloop()