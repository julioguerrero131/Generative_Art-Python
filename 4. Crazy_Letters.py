from turtle import *
from theme import set_theme
import random as rd

set_theme(canvas_width=1000,
          canvas_heigth=600,
          thickness=3
          )

size = 70
n = 1 # puntos a conectarse en cada columna

for y in range(250,-250,-size): 
    for x in range(-400,400,size):

        # cambiar de pencolor en cada letra
        r = rd.random() 
        g = rd.random()
        b = rd.random()
        pencolor(r,g,b)

        # original point 
        px = x + rd.uniform(-size/4, size/4)
        py = y + rd.uniform(-size/4, size/4)

        # inicializar start point con original point
        px_start = px 
        py_start = py 

        # ir al start point
        penup()
        goto(px_start, py_start)
        pendown()

        # dibujar la figura
        for i in range(n):

            # random end point
            px_end = x + rd.uniform(-size/4, size/4)
            py_end = y + rd.uniform(-size/4, size/4) 

            # dibujar la linea conectora
            goto(px_end,py_end)
            
            # reiniciar start point
            px_start = px_end
            py_start = py_end

        # volver al punto inicial
        goto(px, py)

    # incrementar puntos 
    n += 1

tracer(True)
exitonclick()