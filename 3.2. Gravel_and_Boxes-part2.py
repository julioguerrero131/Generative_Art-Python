from turtle import *
from theme import set_theme
import random as rd
import math

set_theme(canvas_heigth=600, canvas_width=1000, thickness=2)

size = 20 
noise = 0.0
max_distance = math.sqrt(250**2 + 450**2) # punto mas lejano

for y in range(250,-250,-size): 
    for x in range(-450,450,size):

        # moverse a la ubicacion
        penup()
        goto(x,y)
        pendown()

        # rotar
        distance = math.sqrt(x**2 + (7/4)**2 * y**2)
        noise = (max_distance - distance) / 13
        noise = noise if noise > 13 else 0
        angle = rd.uniform(-noise, noise)
        right(angle)

        # dibujar cuadrado
        for i in range(4):
            forward(size)
            right(90)

        #rotar de vuelta
        left(angle)

    # aniadir ruido 
    # noise += 4.0


tracer(True)
exitonclick()