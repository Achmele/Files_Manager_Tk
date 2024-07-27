"""
    import threading
import tkinter
from tkinter.constants import *
from functools import partial
def ok(n):
    for n in range(0,int(n)):
        print("ok")
    

tk = tkinter.Tk()
tk.geometry("400x400")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=32)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
put=tkinter.Entry()
put.pack()
#part=partial(ok,put.get())
#label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Midnight",command=lambda:ok(put.get()))
button.pack(side=BOTTOM)
tk.mainloop()

    
def ok(n):
    print(str(n))
    return n+1

a=lambda:ok(30)
print(a())
"""
#a=0
#print("1") if a else print("ooo")
#import gc

# Collecte manuelle des déchets
#gc.collect()

# Afficher les objets non accessibles
#print(gc.garbage)
"""
import keyboard

# Capturer une seule touche
event = keyboard.read_event()
print(event.name)  # Nom de la touche

# Capturer toutes les touches en boucle
while True:
    event = keyboard.read_event()
    print(event.name)  # Nom de la touche
    if event.name == 'esc':
        break  # Sortir de la boucle si la touche 'esc' est pressée
import keyboard

# Simuler une pression de touche
keyboard.press('ctrl')
keyboard.press('c')

# Simuler une combinaison de touches
keyboard.send('ctrl+shift+esc')
import keyboard

# Vérifier si une touche est enfoncée
if keyboard.is_pressed('shift'):
    print('La touche Shift est enfoncée.')
import keyboard

def on_hotkey():
    print('Combinaison de touches détectée!')

# Enregistrer une combinaison de touches
keyboard.add_hotkey('ctrl+shift+a', on_hotkey)

# Démarrer l'écoute des combinaisons de touches
keyboard.wait('esc')  # Attendre que la touche 'esc' soit pressée pour terminer


import pyautogui

# Obtenir les coordonnées x, y de la position actuelle de la souris
x, y = pyautogui.position()
print(f"Position actuelle de la souris : x = {x}, y = {y}")

import pyautogui

# Déplacer la souris à une position spécifique (par exemple, x=100, y=100)
pyautogui.moveTo(100, 100)

# Déplacer la souris de manière relative par rapport à sa position actuelle
pyautogui.move(50, 0)  # Déplace de 50 pixels vers la droite

import pyautogui

# Cliquer avec le bouton gauche de la souris à la position actuelle
pyautogui.click()

# Cliquer à une position spécifique (par exemple, x=200, y=200) avec un clic droit
pyautogui.click(200, 200, button='right')

import pyautogui

# Faire défiler la souris vers le haut de 100 pixels
pyautogui.scroll(100)

# Faire défiler la souris vers le bas de 50 pixels
pyautogui.scroll(-50)

import pyautogui

# Prendre une capture d'écran et l'enregistrer dans un fichier
screenshot = pyautogui.screenshot('capture.png')

import pyautogui

# Vérifier si le pixel à la position (100, 200) est de la couleur spécifiée (ici, blanc)
pixel_color = pyautogui.pixel(100, 200)
if pixel_color == (255, 255, 255):
    print("Le pixel est blanc.")

"""
a=[2,]
b=a
b[0]=22
print(a)