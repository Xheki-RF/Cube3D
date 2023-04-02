import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

print("Введите длину стороны куба: ")
a = int(input())

vertices = (
    (a, -a, -a),
    (a, a, -a),
    (-a, a, -a),
    (-a, -a, -a),
    (a, -a, a),
    (a, a, a),
    (-a, -a, a),
    (-a, a, a)
    )
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
    )
colors = (
    (0, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 0, 0),

    (0, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 0, 0),
)
color_y = (
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 1)
)


def Cube():                                 # Drawing cube
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        y = 0
        for vertex in edge:
            y += 1
            glColor3fv(color_y[y])
            glVertex3fv(vertices[vertex])
    glEnd()


def main():                                 # Creating window and main loop
    pygame.init()
    display = (1024, 720)
    pygame.display.set_caption("CUBE")
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 1.0, 250.0)
    glTranslatef(0.0, 0.0, -50)
    x = 1
    y = 0
    z = 1
    v = 10
    while True:                             # Keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if v/10 >= -4:
                    v -= 0.5
                else:
                    v -= 0
            if event.key == pygame.K_RIGHT:
                if v/10 <= 4:
                    v += 0.5
                else:
                    v += 0

        glRotatef(v/10, x, y, z)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x = 1
                y = 0
                z = 1
            if event.key == pygame.K_DOWN:
                x = 0
                y = 1
                z = 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()