import matplotlib.pyplot as plt
import random
import json

largeur = 200
hauteur = 200

# position de depart
y = round(hauteur/2)
x = round(largeur/2)
orientations = ["N","E","S","O"]
Ori = random.choice(orientations)

save_time = 0


Matrice = [[0 for i in range(largeur)] for i in range(hauteur)]

while True:
    if Ori =="N":
        x-=1
    if Ori =="S":
        x+=1
    if Ori =="E":
        y+=1
    if Ori =="O":
        y-=1

    if Matrice[x][y]==0:
        Matrice[x][y]=1
        try:
            Ori = orientations[orientations.index(Ori)-1]
        except:
            Ori = orientations[3]
    elif Matrice[x][y]==1:
        Matrice[x][y]=0
        try:
            Ori = orientations[orientations.index(Ori)+1]
        except:
            Ori = orientations[0]

    plt.imshow(Matrice)
    plt.pause(0.01)
    plt.clf()
