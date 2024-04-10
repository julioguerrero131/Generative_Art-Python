from turtle import *

def set_theme(canvas_width =500,
              canvas_heigth = 500,
              canvas_color = (232/255, 210/255, 210/255),
              pen_color = (94/255, 71/255, 69/255),
              thickness = 2,
              speed_value = 0, 
              tracer_value = False,
              hide_turtle = True
              ):
    ''' Para no repetir todos los valores iniciales para crear el canvas '''

    setup(canvas_width, canvas_heigth)
    bgcolor(canvas_color)
    color(pen_color)
    width(thickness)
    speed(speed_value)
    tracer(tracer_value)
    if hide_turtle:
        hideturtle()