import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 3*159
screen_height = 3*181

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Challenge 01")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 181, 159, 0)


def draw_star(px: int, py: int, intensity: int) -> None:
    glPointSize(intensity)
    glBegin(GL_POINTS)
    glVertex2i(px, py)
    glEnd()


stars = [
    (15, 118, 10),
    (49, 78, 5),
    (50, 100, 5),
    (110, 65, 7),
    (110, 45, 5),
    (130, 20, 7),
    (135, 70, 5),
    (148, 30, 5),
    (137, 100, 10)
]

done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    for star in stars:
        draw_star(*star)

    pygame.display.flip()  # flips between the two screen buffers
    pygame.time.wait(100)

pygame.quit()
