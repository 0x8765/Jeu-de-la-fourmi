# Jeu-de-la-fourmi  
'Langton's Ant' fait en cours.

## Principe

Le **Jeu de la fourmi** est un automate cellulaire imaginé par **Chris Langton** en 1986. Il se joue sur une grille composée de cases blanches et noires, avec une fourmi se déplaçant selon les 2 règles suivantes :

- Si la fourmi se trouve sur une case **blanche**, elle tourne à **droite**, change la case en **noire** et avance d'une case.  
- Si la fourmi se trouve sur une case **noire**, elle tourne à **gauche**, change la case en **blanche** et avance d'une case.

Après un certain temps on peut voir qu'elle finit par construire un **chemin répétitif** en forme de "route" infinie.

Dans mon programme, j'ai représenté la grille par une matrice de listes Python imbriquées qui contient des entiers 0 ou 1, **0** pour une case **blanche** et **1** pour une case **noire**. La position et la direction de la fourmi sont mises à jour à chaque étape en fonction des règles ci-dessus.

## Installation

Pour lancer ce programme sur votre ordinateur, il vous faudra **Python 3.7** et le module **matplotlib**. Voici la commande pour lancer le programme :

**macOS / Linux :**  
```
python3 fourmi.py
```

**Windows :**  
```
python fourmi.py
```
