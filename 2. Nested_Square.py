from turtle import *
import random as rd
from theme import set_theme

def draw_square(x,y,s):
    '''Dibujar un cuadrado desde el centro'''
    penup()
    goto(x-s/2,y-s/2)
    pendown()
    for i in range(4):
        forward(s) #sigue recto la cantidad indicada
        left(90) #giro a la izquierda 90 grados

# setup()
# width(2)
# hideturtle()
# tracer(False)

set_theme()

noise = 5
size = 100
shrink = 15 # disminuye el tamanio del cuadrado
# especificar los puntos centrales de cada cuadrado
# se especifica cada punto en x, asi como en y
# se dibuja primero el grid
for x in range(-250+size//2, 250, size):
    for y in range(-250+size//2, 250, size): 

        # dibujar la cuadricula (cuadrado exterior)
        draw_square(x,y,size)

        # determinar los offsets
        x_off = rd.uniform(-noise,noise)
        y_off = rd.uniform(-noise,noise)

        # dibujar los cuadrados internos
        for i in range(6):
            draw_square(x+i*x_off, y+i*y_off,size-i*shrink)

tracer(True)
exitonclick()