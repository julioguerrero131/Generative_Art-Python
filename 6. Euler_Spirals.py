from turtle import *
from theme import set_theme
import random as rd

def euler_curve(step_size, angle_step, n_steps):
    '''Crea las espirales de euler

    Args:
        step_size (int): Cuanto avanza la tortuga
        angle_step (int): Cuanto cambia el angulo
        n_steps (int): numero de pasos al avanzar
    '''

    angle = 0
    for i in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step

'''
set_theme(tracer_value=1, hide_turtle=False)
euler_curve(10, 1.00, 500)
'''
'''
set_theme(canvas_heigth=600,
          canvas_width=1000
          , tracer_value=100)
euler_curve(5, 0.66, 10000)
'''
'''
set_theme(canvas_heigth=600,
          canvas_width=1000
          , tracer_value=100)
euler_curve(2, 1.01, 100000)
'''

set_theme(canvas_heigth=600,
          canvas_width=1000
          , tracer_value=100)
euler_curve(3, 1.99, 100000)

tracer(True)
exitonclick()