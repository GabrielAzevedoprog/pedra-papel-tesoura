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
global rounds
global player, computer
global pontos_player, pontos_computer

rounds = 5
pontos_player = 0
pontos_computer = 0

# Style --------------------------------
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=bg_main)

# Style --------------------------------
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Frame Header --------------------------------
frame_header = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_header.grid(row=0, column=0, sticky=NW)

l_linha0 = Label(frame_header, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
l_linha0.place(x=0,y=0)
l_player0 = Label(frame_header, text='You', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
l_player0.place(x=25,y=70)
l_placar0 = Label(frame_header,text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
l_placar0.place(x=60,y=20)

l_pontos = Label(frame_header, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0).place(x=125,y=20)

l_linhaempate = Label(frame_header, text='', width=254, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
l_linhaempate.place(x=6,y=95)

l_linha1 = Label(frame_header, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
l_linha1.place(x=255,y=0)
l_player1 = Label(frame_header, text='Computer', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
l_player1.place(x=170,y=70)
l_placar1 = Label(frame_header, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
l_placar1.place(x=180,y=20)

# Função logica do jogo --------------------------------
def jogar(i):
    global rounds, pontos_computer, pontos_player

    if rounds > 0:
        print(rounds)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        computer = random.choice(opcoes)
        player = i
        print(player, computer)
        
        if player == 'Pedra' and computer == 'Pedra' or player == 'Papel' and computer == 'Papel' or player == 'Tesoura' and computer == 'Tesoura':
            print('Empate')
            l_linha0['bg']= co1
            l_linha1['bg']= co1
            l_linhaempate['bg']= co3
        elif player == 'Pedra' and computer == 'Tesoura':
            print('You Win')
            pontos_player += 1
            l_linha0['bg']= co4
            l_linha1['bg']= co1
            l_linhaempate['bg']= co1
            rounds -= 1
        elif player == 'Tesoura' and computer == 'Pedra':
            print('Computer Win')
            pontos_computer +=1
            l_linha0['bg']= co1
            l_linha1['bg']= co4
            l_linhaempate['bg']= co1
            rounds -= 1
        elif player == 'Tesoura' and computer == 'Papel':
            print('You Win')
            pontos_player += 1
            l_linha0['bg']= co4
            l_linha1['bg']= co1
            l_linhaempate['bg']= co1
            rounds -= 1
        elif player == 'Papel' and computer == 'Tesoura':
            print('Computer Win')
            pontos_computer +=1
            l_linha0['bg']= co1
            l_linha1['bg']= co4
            l_linhaempate['bg']= co1
            rounds -= 1
        elif player == 'Papel' and computer == 'Pedra':
            print('You Win')
            pontos_player += 1
            l_linha0['bg']= co4
            l_linha1['bg']= co1
            l_linhaempate['bg']= co1
            rounds -= 1
        elif player == 'Pedra' and computer == 'Papel':
            print('Computer Win')
            pontos_computer +=1
            l_linha0['bg']= co1
            l_linha1['bg']= co4
            l_linhaempate['bg']= co1
            rounds -= 1
        l_placar0['text'] = pontos_player
        l_placar1['text'] = pontos_computer
    else:
        fim()

# Função iniciar do jogo --------------------------------
def iniciar():
    global img_pedra
    global img_papel
    global img_tesoura
    global l_img1, l_img2, l_img3

    l_iniciar.destroy()
    
    img_pedra = Image.open('public/pedra.png')
    img_papel = Image.open('public/papel.png')
    img_tesoura = Image.open('public/tesoura.png')

    img_pedra = ImageTk.PhotoImage(img_pedra)
    img_papel = ImageTk.PhotoImage(img_papel)
    img_tesoura = ImageTk.PhotoImage(img_tesoura)

    l_img1 =Button(frame_body, command= lambda: jogar('Pedra'), image=img_pedra, compound=CENTER, bg=co0, fg=co0, anchor='center', relief=FLAT)
    l_img1.place(x=15, y=60)

    l_img2 =Button(frame_body, command= lambda: jogar('Papel'), image=img_papel, compound=CENTER, bg=co0, fg=co0, anchor='center', relief=FLAT)
    l_img2.place(x=95, y=60)

    l_img3 =Button(frame_body, command= lambda: jogar('Tesoura'), image=img_tesoura, compound=CENTER, bg=co0, fg=co0, anchor='center', relief=FLAT)
    l_img3.place(x=180, y=60)

# Função terminar o jogo --------------------------------
def fim():
    global rounds
    global pontos_player
    global pontos_computer
    
    l_img1.destroy()
    l_img2.destroy()
    l_img3.destroy()

    def jogar_denovo():
        l_resta.destroy()
        l_res.destroy()
        l_iniciar0.destroy()
        l_placar0['text'] = pontos_player
        l_placar1['text'] = pontos_computer
        iniciar()

    if pontos_player > pontos_computer:
        print('Parabens você ganhou do computador!!')
        l_res = Label(frame_body, text='Parabens você ganhou do computador!!', height=1, anchor='center', font=('Ivy 8 bold'), bg=co0, fg=co1)
        l_res.place(x=25, y=60)
    elif pontos_computer > pontos_player:
        print('Você perdeu para o computador!!')
        l_res = Label(frame_body, text='Você perdeu para o computador!!', height=1, anchor='center', font=('Ivy 8 bold'), bg=co0, fg=co1)
        l_res.place(x=35, y=60)

    l_resta = Label(frame_body, text='Deseja jogar novamente?', height=1, anchor='center', font=('Ivy 8 bold'), bg=co0, fg=co1)
    l_resta.place(x=60, y=80)
    l_iniciar0 =Button(frame_body, width=15, command=jogar_denovo, text='Sim', compound=CENTER, bg=bg_main, fg=co0, anchor='center', relief=RAISED, overrelief=RIDGE)
    l_iniciar0.place(x=75, y=110)

    rounds = 5
    pontos_player = 0
    pontos_computer = 0

# Frame Body --------------------------------
frame_body = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_body.grid(row=1, column=0, sticky=NW)

l_iniciar =Button(frame_body, width=15, command=iniciar, text='Jogar', compound=CENTER, bg=bg_main, fg=co0, anchor='center', relief=RAISED, overrelief=RIDGE)
l_iniciar.place(x=75, y=145)

# MainLoop --------------------------------
janela.mainloop()