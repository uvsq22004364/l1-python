def restart():
    global a, b
    canvas.delete('all')
    a = 200
    b = 400
    ligne1 = canvas.create_line((a, 0), (a, 600), fill="red")
    ligne2 = canvas.create_line((b, 0), (b, 600), fill="blue")


def choix(event):
    global a, b
    x = event.x
    y = event.y
    canvas.delete('all')
    if x-200 <= 0:
        a -= 10
        b -= 10

        ligne1 = canvas.create_line((a, 0), (a, 600), fill="red")
        ligne2 = canvas.create_line((b, 0), (b, 600), fill="blue")

    elif x - 400 <= 0:
        a += 10
        b -= 10
        ligne1 = canvas.create_line((a, 0), (a, 600), fill="red")
        ligne2 = canvas.create_line((b, 0), (b, 600), fill="blue")
    else:
        a += 10
        b += 10
        ligne1 = canvas.create_line((a, 0), (a, 600), fill="red")
        ligne2 = canvas.create_line((b, 0), (b, 600), fill="blue")

#--------ligne1--------------
a = 200
#--------ligne2--------------
b = 400
#----------------------------

import tkinter as tk

racine = tk.Tk()


canvas = tk.Canvas(racine, bg = "black", width = 600 , height = 600 )
canvas.grid(column=0, row=0)

ligne1 = canvas.create_line( (a,0) , (a,600), fill = "red" )
ligne2 = canvas.create_line( (b,0) , (b,600), fill = "blue" )

canvas.bind("<Button-1>" , choix)

button = tk.Button(racine, text="recommencer", command = restart)
button.grid(column=0, row=1)

racine.mainloop()
