import sys
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# random_color_r = random.uniform(0, 1.0)
# random_color_g = random.uniform(0, 1.0)
# random_color_b = random.uniform(0, 1.0)

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
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio, 1.0, -1.0)

    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_square(x, y, a, b, d=0.0):
    glVertex2f(x, y)
    glVertex2f(x + a * d, y)
    glVertex2f(x + a * d, y + b * d)

    glVertex2f(x, y + b * d)
    glVertex2f(x, y)
    glVertex2f(x + a * d, y + b * d)

    # glColor3f(random_color_r, random_color_g, random_color_b)
    # glVertex2f(x, y)
    # glVertex2f(x + a * d, y)
    # glVertex2f(x + a * d, y + b * d)
    #
    # glColor3f(random_color_r, random_color_g, random_color_b)
    # glVertex2f(x, y + b * d)
    # glVertex2f(x, y)
    # glVertex2f(x + a * d, y + b * d)

# def draw_square(x, y, size):
#     glVertex2f(x, y)
#     glVertex2f(x + size, y)
#     glVertex2f(x + size, y + size)
#     glVertex2f(x, y + size)

def sierpinski(x, y, a, b, depth, d=1.0):
    if depth == 0:
        draw_square(x, y, a, b, d)
    else:
        new_a = a / 3 #nowa szerokosc jednego prostokata z trzech
        new_b = b / 3 #nowa wysokosc jednego prostokata z trzech
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1: #pomijanie srodkowego prostokata
                    continue
                sierpinski(x + i * new_a, y + j * new_b, new_a, new_b, depth - 1, d)

def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    update_viewport(None, 400, 400)

def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    sierpinski(-50, -30, 100.0, 50.0, 4, 1)
    glEnd()
    glFlush()

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


