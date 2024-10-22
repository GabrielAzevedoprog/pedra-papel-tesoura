import tkinter 
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image
import random

# Cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
bg_main = "#3b3b3b"


# Var Global --------------------------------
global player
global computer
global rounds
global pontos_player
global pontos_computer

rounds = 5
pontos_player = 0
pontos_computer = 0

janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=bg_main)

# Frame Header --------------------------------
frame_header = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_header.grid(row=0, column=0, sticky=NW)

l_linha0 = Label(frame_header, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0).place(x=0,y=0)
l_player0 = Label(frame_header, text='You', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0).place(x=25,y=70)
l_placar0 = Label(frame_header,  command= lambda: play_game('')text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0).place(x=60,y=20)

l_pontos = Label(frame_header, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0).place(x=125,y=20)

l_linhaempate = Label(frame_header, text='', width=254, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0).place(x=6,y=95)


l_linha1 = Label(frame_header, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0).place(x=255,y=0)
l_player1 = Label(frame_header, text='Computer', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0).place(x=170,y=70)
l_placar1 = Label(frame_header, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0).place(x=180,y=20)

# Função logica do jogo --------------------------------

def jogar(i):
    global rounds
    global pontos_player
    global pontos_computer

    if rounds > 0:
        print(rounds)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        computer = random.choice(opcoes)
        player = i

        if player == computer:

    else:
        fim()

# Função iniciar do jogo --------------------------------

def iniciar():
    global img_pedra
    global img_papel
    global img_tesoura
    
    img_pedra = Image.open('public/pedra.png')
    img_papel = Image.open('public/papel.png')
    img_tesoura = Image.open('public/tesoura.png')

    img_pedra = ImageTk.PhotoImage(img_pedra)
    img_papel = ImageTk.PhotoImage(img_papel)
    img_tesoura = ImageTk.PhotoImage(img_tesoura)

    l_img =Button(frame_body, command= lambda: jogar('Pedra'), image=img_pedra, compound=CENTER, bg=co0, fg=co0, anchor='center', relief=FLAT)
    l_img.place(x=15, y=60)

    l_img =Button(frame_body, command= lambda: jogar('Papel'), image=img_papel, compound=CENTER, bg=co0, fg=co0, anchor='center', relief=FLAT)
    l_img.place(x=95, y=60)

    l_img =Button(frame_body, command= lambda: jogar('Tesoura'), image=img_tesoura, compound=CENTER, bg=co0, fg=co0, anchor='center', relief=FLAT)
    l_img.place(x=180, y=60)


# Função terminar o jogo --------------------------------

def fim():
    global rounds
    global pontos_player
    global pontos_computer
pass












# Frame Body --------------------------------
frame_body = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_body.grid(row=1, column=0, sticky=NW)

l_img =Button(frame_body, width=15, command=play_game, text='Jogar', compound=CENTER, bg=bg_main, fg=co0, anchor='center', relief=RAISED, overrelief=RIDGE)
l_img.place(x=75, y=145)
# Style --------------------------------
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# MainLoop --------------------------------
janela.mainloop()