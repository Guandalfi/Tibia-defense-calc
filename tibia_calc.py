#r = redução de armadura mínima
#R = redução de armadura máxima
#t = armadura total
#d = dano (depois do escudo)
#p = porcentagem de redução do item
#h = hit inicial
#r = chao(t/2)
#R = (chao(t/2) * 2) - 1

#d = chao(((100-p)/100) * d)

import math
import os
import tkinter as tk


#Calcula reducao minima e maxima da armadura
def calcula_min_max(defesa):
    t = int(defesa)
    r = math.floor(t/2)
    R = (math.floor(t/2) * 2) - 1

    return r, R


#Reducao das porcentagem
def red_porcentagem(porcentagem, d):
    p = int(porcentagem)
    d_inicial = d
    d = math.floor(((100-p) / 100) * d)
    reducao = d_inicial - d
    print(f"dano reduzido: {reducao}")
    return reducao

def calcular():
    defesas = [int(e.get()) for e in entries_defesas]
    porcentagens = [int(p.get()) for p in entries_porcentagens]
    dano = int(entry_dano.get())
    print(defesas)
    print(porcentagens)
    print(dano)
    minimas_e_maximas = [calcula_min_max(defesa) if defesa >= 1 else (0, 0) for defesa in defesas]
    print(minimas_e_maximas)

os.system('cls')

#def_helmet = int(input("Digite a def do helmet: "))
#def_armadura = int(input("Digite a def da armadura: "))
#def_legs = int(input("Digite a def das legs: "))
#def_boots = int(input("Digite a def das boots: "))

#defesas = []
#defesas.append(def_helmet)
#defesas.append(def_armadura)
#defesas.append(def_legs)
#defesas.append(def_boots)

#minimas_e_maximas = []

#for defesa in defesas:
    #if defesa < 1:
        #pass
    #minimas_e_maximas.append(calcula_min_max(defesa))

#porc_helmet = int(input("Digite a porcentagem do helmet: "))
#porc_armadura = int(input("Digite a porcentagem da armadura: "))
#porc_legs = int(input("Digite a porcentagem das legs: "))
#porc_boots = int(input("Digite a porcentagem das boots: "))

#porcentagens = []
#porcentagens.append(porc_helmet)
#porcentagens.append(porc_armadura)
#porcentagens.append(porc_legs)
#porcentagens.append(porc_boots)

#d = int(input("Digite o dano tomado: "))

#reducoes = []

#for porcentagem in porcentagens:
    #if porcentagem < 1:
        #pass
    #reducoes.append(red_porcentagem(porcentagem, d))

#for reducao in reducoes:
    #d = d - reducao

#r = 0
#R = 0
#for i in minimas_e_maximas:
    #r += i[0]
    #R += i[1]

#d_max = d - r
#d_min = d - R

root = tk.Tk()
root.title("Cálculo de Redução de Dano")

frame_defesas = tk.Frame(root)
frame_defesas.pack()

labels_defesas = ["Helmet: ", "Armadura: ", "Legs: ", "Boots: "]
entries_defesas = []
for i, label_text in enumerate(labels_defesas):
    label = tk.Label(frame_defesas, text=label_text)
    label.grid(row=i, column=0)
    entry = tk.Entry(frame_defesas)
    entry.grid(row=i, column=1)
    entries_defesas.append(entry)

frame_porcentagens = tk.Frame(root)
frame_porcentagens.pack()

labels_porcentagens = ["Porc. Helmet: ", "Porc. Armadura: ", "Porc. Legs: ", "Porc. Boots: "]
entries_porcentagens = []
for i, label_text in enumerate(labels_porcentagens):
    label = tk.Label(frame_porcentagens, text=label_text)
    label.grid(row=i, column=0)
    entry = tk.Entry(frame_porcentagens)
    entry.grid(row=i, column=1)
    entries_porcentagens.append(entry)

frame_dano = tk.Frame(root)
frame_dano.pack()

label_dano = tk.Label(frame_dano, text="Dano Tomado:")
label_dano.grid(row=0, column=0)
entry_dano = tk.Entry(frame_dano)
entry_dano.grid(row=0, column=1)

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()
