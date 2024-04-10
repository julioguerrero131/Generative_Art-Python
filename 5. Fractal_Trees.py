from turtle import *
from theme import set_theme
import random as rd

set_theme(canvas_width=1000,
          canvas_heigth=700,
          pen_color=(0.8, 0.32, 0.45),
          canvas_color=(0.23, 0.13, 0.46))

def grow(length, decrease, angle, noise=0):
    '''Crea las ramas del arbol de forma recursiva.

    Args:
        length (int): longitud de cada rama
        decrease (int): cuanto disminuye la rama en cada iteracion
        angle (int): angulo de las nuevas ramas
        noise (int): ruido
    '''

    if length > 10:

        width(length / 10)
        forward(length)
        

        new_length = length * decrease
        if noise > 0:
            new_length *= rd.uniform(0.9,1.1) 

        angle_l = angle + rd.gauss(0,noise)
        angle_r = angle + rd.gauss(0,noise)
        
        # crear ramas
        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        left(angle_r)

        backward(length)

penup()
goto(0,-330)
pendown()
left(90)
grow(120,0.81,18,6)


tracer(True)
exitonclick()