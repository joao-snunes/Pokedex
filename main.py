from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from data import *
#cores ------------------------------------
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1,ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")	

# Criando frame principal (onde estará o avatar completo)
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    # i = nome
    global imagem, poke_img
    # trocando cor do frame
    frame_pokemon['bg'] = pokemon[i]['Tipo'][3]
    
    # tipo do pokemon
    poke_nome['text'] = i
    poke_nome['bg'] = pokemon[i]['Tipo'][3]
    poke_tipo['text'] = pokemon[i]['Tipo'][1]
    poke_tipo['bg'] = pokemon[i]['Tipo'][3]
    poke_id['text'] = pokemon[i]['Tipo'][0]
    poke_id['bg'] = pokemon[i]['Tipo'][3]
    
    # Status
    poke_hp['text'] = pokemon[i]['Status'][0]
    poke_atk['text'] = pokemon[i]['Status'][1]
    poke_dfs['text'] = pokemon[i]['Status'][2]
    poke_vel['text'] = pokemon[i]['Status'][3]
    poke_total['text'] = pokemon[i]['Status'][4]
    
    # Habilidades
    poke_hb1['text'] = pokemon[i]['Habilidades'][0]
    poke_hb2['text'] = pokemon[i]['Habilidades'][1]
    
    # Pegando imagem Pokemon
    imagem = Image.open(pokemon[i]['Tipo'][2])
    imagem = imagem.resize((238, 238))
    imagem = ImageTk.PhotoImage(imagem)
    # Adicionando imagem ao label
    poke_img = Label(frame_pokemon, image=imagem, relief='flat', bg=pokemon[i]['Tipo'][3], fg=co1)
    poke_img.place(x=60, y=50)
    # Posicionando abaixo do texto
    poke_tipo.lift(poke_img)
    

# Nome do Pokemon
poke_nome= Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('fixedsys 20'), fg=co1)
poke_nome.place(x=12, y=15)

# Tipo do Pokemon
poke_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('ivy 10 bold'), fg=co0)
poke_tipo.place(x=12, y=50)

# Id do Pokemon
poke_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('ivy 10 bold'), fg=co0)
poke_id.place(x=12, y=75)



#----------------------------------

# Status
poke_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status.place(x=15, y=303)

# hp
poke_hp = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hp.place(x=15, y=350)

# efesa
poke_atk = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_atk.place(x=15, y=370)

# Defesa
poke_dfs = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_dfs.place(x=15, y=390)

# Velocidade
poke_vel = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_vel.place(x=15, y=410)

# Total
poke_total = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_total.place(x=15, y=430)

#----------------------------------
# Habilidades
poke_habilidade = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_habilidade.place(x=180, y=303)

poke_hb1 = Label(janela, text='Folha Navalha', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hb1.place(x=180, y=350)

poke_hb2 = Label(janela, text='Raio Solar', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hb2.place(x=180, y=370)

#-----------------------------------
# botao bulbasaur
img_p1 = Image.open('images/cabeca-bulbasaur.png')
img_p1 = img_p1.resize((40, 40))
img_p1 = ImageTk.PhotoImage(img_p1)

btn_p1 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'),image=img_p1, text=('Bulbasaur'),width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,  font=('Verdana 12'), bg=co1, fg=co0)
btn_p1.place(x=375, y=10)

# botao Charmander
img_p2 = Image.open('images/cabeca-charmander.png')
img_p2 = img_p2.resize((40, 40))
img_p2 = ImageTk.PhotoImage(img_p2)

btn_p2 = Button(janela,command=lambda:trocar_pokemon('Charmander') ,image=img_p2, text=('Charmander'),width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,  font=('Verdana 12'), bg=co1, fg=co0)
btn_p2.place(x=375, y=65)

# botao dragonite
img_p3 = Image.open('images/cabeca-dragonite.png')
img_p3 = img_p3.resize((40, 40))
img_p3 = ImageTk.PhotoImage(img_p3)

btn_p3 = Button(janela,command=lambda:trocar_pokemon('Dragonite') ,image=img_p3, text=('Dragonite'),width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,  font=('Verdana 12'), bg=co1, fg=co0)
btn_p3.place(x=375, y=120)

# botao gengar
img_p4 = Image.open('images/cabeca-gengar.png')
img_p4 = img_p4.resize((40, 40))
img_p4 = ImageTk.PhotoImage(img_p4)

btn_p4 = Button(janela,command=lambda:trocar_pokemon('Gengar') ,image=img_p4, text=('Gengar'),width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,  font=('Verdana 12'), bg=co1, fg=co0)
btn_p4.place(x=375, y=175)

# botao pikachu
img_p5 = Image.open('images/cabeca-pikachu.png')
img_p5 = img_p5.resize((40, 40))
img_p5 = ImageTk.PhotoImage(img_p5)

btn_p5 = Button(janela,command=lambda:trocar_pokemon('Pikachu') ,image=img_p5, text=('Pikachu'),width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,  font=('Verdana 12'), bg=co1, fg=co0)
btn_p5.place(x=375, y=230)

# botao gyarados
img_p6 = Image.open('images/cabeca-gyarados.png')
img_p6 = img_p6.resize((40, 40))
img_p6 = ImageTk.PhotoImage(img_p6)

btn_p6 = Button(janela,command=lambda:trocar_pokemon('Gyarados') ,image=img_p6, text=('Gyarados'),width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5,  font=('Verdana 12'), bg=co1, fg=co0)
btn_p6.place(x=375, y=285)

janela.mainloop()