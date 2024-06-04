from tkinter import*
from PIL import Image, ImageTk
import random

#-------------------------------------------------------------------------

co0 = "#f0f3f5"  # cizenta / grey
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor
co4 = "#403d3d"  # preta / black

janela = Tk()
janela.title ("Jogo acenda a luz - Willian Sozz")
janela.geometry('400x260')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


#-------------------------------------------------------------------------

frame_cima = Frame(janela, width=500, height=50, bg=co1)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

l_app = Label(frame_cima, text='Acenda as lâmpadas!',anchor=NE, font=('Fantasy 20 bold'), bg=co1, fg=co4)
l_app.place(x=60, y=5)

#-------------------------------------------------------------------------

frame_baixo = Frame(janela, width=500, height=210, bg=co4)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

img_2 = Image.open('2.png')
img_2 = img_2.resize((40,40))
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open('3.png')
img_3 = img_3.resize((40,40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('4.png')
img_4 = img_4.resize((40,40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('5.png')
img_5 = img_5.resize((40,40))
img_5 = ImageTk.PhotoImage(img_5)

l_img = Label(frame_baixo, image=img_2, bg=co4)
l_img.place(x=100, y=10)

l_estado = Label(frame_baixo, text='Estou com medo!',anchor=NW, font=('Fantasy 11 bold'), bg=co4, fg=co1)
l_estado.place(x=150, y=20)

#-------------------------------------------------------------------------

global control

def ligar_lampada(i):

    global control

    lista = i

    if lista[1] == 'interruptor - 1' :
        b_interruptor1['state'] = 'disable'
    elif lista[1] == 'interruptor - 2' :
        b_interruptor2['state'] = 'disable'
    elif lista[1] == 'interruptor - 3' :
        b_interruptor3['state'] = 'disable'
    elif lista[1] == 'interruptor - 4' :
        b_interruptor4['state'] = 'disable'
    else:
        b_interruptor5['state'] = 'disable'

    def substituir_valor(i):
        global control
        nova_lista = []

        for string in control:
            novo_valor = string.replace(i[0],i[1])
            nova_lista.append(novo_valor)
            
        control = nova_lista

    valor_selecionado = random.sample(lista[0],1)[0]
    
    if int(valor_selecionado) == 1:
        
        if control[0] == 'lampada_1':
            l_img_1['image'] = img_lampada_on
            l_img['image'] = img_3
            l_estado['text'] = 'Ainda esta escuro!'
            substituir_valor(['lampada_1',str(1)])
            
        else: 
            if control[1] == 'lampada_2':
                l_img_2['image'] = img_lampada_on
                l_img['image'] = img_4
                l_estado['text'] = 'Acenda so mais uma!'
                substituir_valor(['lampada_2',str(2)])
                
            else:
                if control[2] == 'lampada_3':
                    l_img_3['image'] = img_lampada_on
                    l_img['image'] = img_5
                    l_estado['text'] = 'Obrigado, você é 10!'
                    substituir_valor(['lampada_3',str(3)])
                
        
                    
#-------------------------------------------------------------------------

control = ['lampada_1','lampada_2','lampada_3']

img_lampada_off = Image.open('0.png')
img_lampada_off = img_lampada_off.resize((110,110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

l_img_1 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_img_1.place(x=5, y=70)

l_img_2 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_img_2.place(x=98, y=70)

l_img_3 = Label(frame_baixo, image=img_lampada_off, bg=co4)
l_img_3.place(x=190, y=70)


img_lampada_on = Image.open('1.png')
img_lampada_on = img_lampada_on.resize((110,110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

#-------------------------------------------------------------------------

lista = [0, 1, 1, 1, 0]

b_interruptor1 = Button(frame_baixo,command=lambda i=[lista, 'interruptor - 1']:ligar_lampada(i),text='Interruptor',anchor=NW, font=('Fantasy 9 bold'),relief=RAISED,
                         overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor1.place(x=310, y=50)

b_interruptor2 = Button(frame_baixo,command=lambda i =[lista,'interruptor - 2']:ligar_lampada(i), text='Interruptor',anchor=NW, font=('Fantasy 9 bold'),relief=RAISED,
                         overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor2.place(x=310, y=80)

b_interruptor3 = Button(frame_baixo,command=lambda i =[lista,'interruptor - 3']:ligar_lampada(i), text='Interruptor',anchor=NW, font=('Fantasy 9 bold'),relief=RAISED,
                         overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor3.place(x=310, y=110)

b_interruptor4 = Button(frame_baixo,command=lambda i =[lista,'interruptor - 4']:ligar_lampada(i), text='Interruptor',anchor=NW, font=('Fantasy 9 bold'),relief=RAISED,
                         overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor4.place(x=310, y=140)

b_interruptor5 = Button(frame_baixo,command=lambda i =[lista,'interruptor - 5']:ligar_lampada(i), text='Interruptor',anchor=NW, font=('Fantasy 9 bold'),relief=RAISED,
                         overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor5.place(x=310, y=170)

#-------------------------------------------------------------------------

janela.mainloop()
