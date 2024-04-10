from turtle import *
import random as rd
from theme import *

# setup(700,700)
set_theme()

def tiling(x, y, s, l, mode="straight"):
    '''Usar recursion para crear un mosaico.

    Args:
        x (int): posicion en x
        y (int): posicion en y
        s (int): tamanio de la porcion
        l (int): nivel de recursion
    '''
    
    # Llegamos al nivel final de recursion
    # ahora dibujamos
    if l == 0:

        if mode == "straight":
            # vertical line
            if rd.random() < 0.5:
                penup()
                goto(x,y-s)
                pendown()
                goto(x,y+s)

            # horizontal line
            else:
                penup()
                goto(x-s,y)
                pendown()
                goto(x+s,y)

        elif mode == "diagonal":
            # top left to bottom right
            if rd.random() < 0.5:
                penup()
                goto(x-s,y+s)
                pendown()
                goto(x+s,y-s)

            # bottom left to top right
            else:
                penup()
                goto(x-s,y-s)
                pendown()
                goto(x+s,y+s)

    # divide la pantalla y va al siguiente nivel de recursion
    else:
        s /= 2
        l -= 1
        tiling(x-s,y+s,s,l,mode)
        tiling(x+s,y+s,s,l,mode)
        tiling(x-s,y-s,s,l,mode)
        tiling(x+s,y-s,s,l,mode)


# width(3) # anchura de las lineas

# hideturtle() # esconder puntero
# tracer(False) # para no mirar todo el proceso de dibujo
tiling(0,0,250,4,mode="diagonal")    
tracer(True) # debe volver o faltaran partes

exitonclick()
