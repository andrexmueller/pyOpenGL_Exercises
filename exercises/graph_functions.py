import sys
import os
import numpy as np
from math import *

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def print_help():
    os.system('')
    ajuda = """
        \t\x1b[4mPequeno Scritp para plotar funções matemáticas\x1b[0m\n
        \t\x1b[1mEscreve a definição de uma função de x uma equação, 
        \tSEM ESPAÇOS, utilizando a sintaxe padrão do Python. 
        \tOpcionalmente, poderá digitar duas tuplas contendo os limites 
        \tdo gráfico, para os eixos x e y.\x1b[0m
        
        \t\x1b[33mc:\> python grap_funcionts.py [equação] [(min_x, max_y)] [(min_y, max_y)]\x1b[0m 

        \tPor ex.:
        
        \t\x1b[32mpython grap_funcionts.py exp(-x)*cos(2*pi*x) (0,4) (-1,1)\x1b[0m

    """
    print(ajuda)


# Configs
screen_width = 640
screen_height = 480
point_size = 2
graph_color = (1.0,0.0,0.0)
min_x, max_x = -5, 5
min_y, max_y = -5, 5



def init_ortho(min_x, max_x, min_y, max_y):    
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(min_x, max_x, min_y, max_y)
        

def plot_graph(equation, x_0, x_f):
    glPointSize(2)
    glBegin(GL_POINTS)
    x: GL_DOUBLE
    y: GL_DOUBLE
    for x in np.arange(x_0, x_f, 0.001):
        y = eval(equation)
        glVertex2f(x, y)
    glEnd()


def plot_axes(min_x, max_x, min_y, max_y):
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_LINES)
    # center of plotting box
    glVertex2f(min_x, (min_y + max_y)/2)
    glVertex2f(max_x, (min_y + max_y)/2)
    glVertex2f((min_x + max_x)/2, min_y)
    glVertex2f((min_x + max_x)/2, max_y)
    glColor3f(0.8, 0.8, 0.8)
    # eixo x
    glVertex2f(-screen_width, 0)
    glVertex2f(screen_width, 0)
    # eixo y
    glVertex2f(0, -screen_height)
    glVertex2f(0, screen_height)
    glEnd()
    glColor3f(*graph_color)


def plot_point(x=0, y=0):
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()



if __name__ == "__main__":

    
    if len(sys.argv) >= 4:
        min_x, max_x = eval(sys.argv[2])
        min_y, max_y = eval(sys.argv[3])

    if len(sys.argv) == 1 or "-h" in sys.argv:
        print_help()
        sys.exit()

    # function to be plotted    
    equation = sys.argv[1]
    
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Graph your fun')


    done = False
    init_ortho(min_x, max_x, min_y, max_y)
    glPointSize(point_size)
    glColor3f(*graph_color)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #plot_point()
        plot_graph(equation, min_x, max_x)
        plot_axes(min_x, max_x, min_y, max_y)
        pygame.display.flip()
        
    pygame.quit()









    
    





