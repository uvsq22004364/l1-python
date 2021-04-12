import tkinter as tk

def get_color(r=0, v=0, b=0):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, v, b)

def afficher_couleur():
    while True:
        r = int(input("Teinte de rouge? "))
        v = int(input("Teinte de vert? "))
        b = int(input("Teinte de bleu? "))
        if 0 <= r <= 255 and 0 <= v <= 255 and 0 <= b <= 255:
            break
    canvas.config(bg=get_color(r, v, b))                

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, width=400, height=400, bg="white")
canvas.grid(row=0)
bouton = tk.Button(racine, text="Choisir couleur", font=("Helvetica", "30"), command=afficher_couleur)
bouton.grid(row=1)

racine.mainloop() # Lancement de la boucle principale