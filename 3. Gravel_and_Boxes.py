from turtle import *
from theme import set_theme
import random as rd

set_theme(canvas_heigth=600, canvas_width=400)

size = 30 # tamanio del cuadrado
noise = 0.0

for y in range(250,-250,-size): 
    for x in range(-150,150,size):

        # moverse a la ubicacion
        penup()
        goto(x,y)
        pendown()

        # rotar
        angle = rd.uniform(-noise, noise)
        right(angle) # no importa si es right o left

        # dibujar cuadrado
        for i in range(4):
            forward(size)
            right(90)

        #rotar de vuelta
        left(angle)

    # aniadir ruido 
    noise += 4.0


tracer(True)
exitonclick()