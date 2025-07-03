import sys
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

N = 20
tab = np.zeros((N, N, 3))
u_values = np.linspace(0.0, 1.0, N)
v_values = np.linspace(0.0, 1.0, N)
colors = np.zeros((N, N, 3))

def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width =  1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspectRatio, 7.5 / aspectRatio, 1.0, -1.0)

    else:
        glOrtho(-7.5 * aspectRatio, 7.5 * aspectRatio, -7.5, 7.5, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def generate_egg_model():
    for i, u in enumerate(u_values):
        for j, v in enumerate(v_values):
            x = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.cos(np.pi * v)
            y = 160 * u ** 4 - 320 * u ** 3 + 160 * u ** 2 - 5
            z = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * np.sin(np.pi * v)
            tab[i][j] = [x, y, z]

            colors[i][j] = [random.random(), random.random(), random.random()] # <-- Do zad. 3

def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    update_viewport(None, 400, 400)
    glEnable(GL_DEPTH_TEST)

def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPointSize(2.0)
    #spin(time * 180 / 3.1415) Funkcja spin działa poprawnie
    axes()

    #Zad. 1
    glBegin(GL_LINE_STRIP)
    for i in range(N - 1):
        for j in range(N - 1):
            glVertex3fv(tab[i][j])
    generate_egg_model()
    glEnd()

    #Zad. 2
    # glBegin(GL_LINE_STRIP) #Uzylem GL_LINE_STRIP zamiast GL_LINES, poniewaz GL_LINES nie laczy punktow z jakiegos powodu
    # for i in range(N - 1):
    #     for j in range(N - 1):
    #         glVertex3fv(tab[i][j])
    #         glVertex3fv(tab[i + 1][j])
    #
    #         glVertex3fv(tab[i][j])
    #         glVertex3fv(tab[i][j + 1])
    #
    # for i in range(N - 1):
    #     glVertex3fv(tab[i][N - 1])
    #     glVertex3fv(tab[i + 1][N - 1])
    #
    # for j in range(N - 1):
    #     glVertex3fv(tab[N - 1][j])
    #     glVertex3fv(tab[N - 1][j + 1])
    # generate_egg_model()
    #glEnd()

    #Zad. 3
    # for i in range(N - 1):
    #     for j in range(N - 1):
    #         glBegin(GL_TRIANGLE_STRIP)
    #
    #         glColor3fv(colors[i][j])
    #         glVertex3fv(tab[i][j])
    #
    #         glColor3fv(colors[i + 1][j])
    #         glVertex3fv(tab[i + 1][j])
    #
    #         glColor3fv(colors[i][j + 1])
    #         glVertex3fv(tab[i][j + 1])
    #
    #         glColor3fv(colors[i + 1][j])
    #         glVertex3fv(tab[i + 1][j])
    #
    #         glColor3fv(colors[i + 1][j + 1])
    #         glVertex3fv(tab[i + 1][j + 1])
    #
    #         glColor3fv(colors[i][j + 1])
    #         glVertex3fv(tab[i][j + 1])
    #         generate_egg_model()
    #         glEnd()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwWaitEvents()
    shutdown()

    glfwTerminate()

if __name__ == '__main__':
    main()


