from tkinter import *
from tkinter import Tk, ttk
import tkinter

#instalando/importanto pillow
from PIL import Image, ImageTk
# cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" # - Profit
co6 = "#038cfc" # Azul
co7 = "#3fbfb9" # Verde
co8 = "#263238" # + Verde
co9 = "#e9edf5" # + Verde
co10 = "#6e8faf" # 
co11 = "#f2f4f2"

#Criando Janela
janela = Tk()
janela.title("") 
janela.geometry('250x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)   
style.theme_use('clam')

# Quadrados 

frameCima = Frame(janela, width=300, height=60, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)
frameMeio = Frame(janela, width=300, height=90, bg=co1, relief="flat")
frameMeio.grid(row=1, column=0)
frameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frameBaixo.grid(row=2, column=0)

# Logo do app --------------

app_ = Label(frameCima, text='Financeiro', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Roboto 20'), bg=co1, fg=co4)
app_.place(x=0, y=0)

# Abrindo Imagem do App
app_img = Image.open('./icone.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Roboto'), bg=co1, fg=co4)
app_logo.place(x=160, y=0)

app_linha = Label(frameCima, width=295, relief=FLAT, anchor=NW, font=('Roboto 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=45)

# Função Calcular 
def calcular():
    # Obtendo o valor total
    Renda_mensal = float(e_valor.get())

    # obtendo as porcentagens
    obter_50_porcento = (50 / 100) * Renda_mensal
    obter_30_porcento = (30 / 100) * Renda_mensal
    obter_20_porcento = (20 / 100) * Renda_mensal

    l_necessidades['text'] = ('R${:,.2f}'.format(obter_50_porcento))
    l_gastos['text'] = ('R${:,.2f}'.format(obter_30_porcento))
    l_poupança['text'] = ('R${:,.2f}'.format(obter_20_porcento))




# Freme Meio --------------

app_ = Label(frameMeio, text='Insira sua renda mesal:', relief=FLAT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
app_.place(x=7, y=15)

e_valor = Entry(frameMeio, width=10, font=('Ivy 14'), justify='center', relief='solid')
e_valor.place(x=10, y=40)

b_calcular= Button(frameMeio, command=calcular, text='Calcular'.upper(), relief=RIDGE, anchor=NW, font=('Ivy 9'), bg=co1, fg=co0)
b_calcular.place(x=150, y=40)

# Freme Baixo --------------

app_ = Label(frameBaixo, text='Seus valore de 50% 30% 20%', relief=FLAT, width=35, anchor=NW, font=('Roboto 11'), bg=co4, fg=co1)
app_.place(x=0, y=0)

# Total necessidades

l_total_necessidades = Label(frameBaixo, text='Necessidades ', relief=FLAT, width=22, anchor=NW, font=('Roboto 12'), bg=co1, fg=co4)
l_total_necessidades.place(x=10, y=40)

l_necessidades = Label(frameBaixo, relief=FLAT, width=35, anchor=NW, font=('Roboto 11'), bg=co9, fg=co0)
l_necessidades.place(x=10, y=75)

# Total Gastos

l_total_gastos = Label(frameBaixo, text='Gastos ', relief=FLAT, width=22, anchor=NW, font=('Roboto 12'), bg=co1, fg=co4)
l_total_gastos.place(x=10, y=115)

l_gastos = Label(frameBaixo, relief=FLAT, width=35, anchor=NW, font=('Roboto 11'), bg=co9, fg=co0)
l_gastos.place(x=10, y=145)

# Total Poupança

l_poupança = Label(frameBaixo, text='Poupança', relief=FLAT, width=22, anchor=NW, font=('Roboto 12'), bg=co1, fg=co4)
l_poupança.place(x=10, y=185)

l_poupança = Label(frameBaixo, relief=FLAT, width=35, anchor=NW, font=('Roboto 11'), bg=co9, fg=co0)
l_poupança.place(x=10, y=215)






janela.mainloop()
