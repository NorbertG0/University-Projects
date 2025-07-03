
#
# def main():
#     if not glfwInit():
#         sys.exit(-1)
#
#     window = glfwCreateWindow(400, 400, __file__, None, None)
#     if not window:
#         glfwTerminate()
#         sys.exit(-1)
#
#     glfwMakeContextCurrent(window)
#     glfwSetFramebufferSizeCallback(window, update_viewport)
#     glfwSetKeyCallback(window, keyboard_key_callback)
#     glfwSetCursorPosCallback(window, mouse_motion_callback)
#     glfwSetMouseButtonCallback(window, mouse_button_callback)
#     glfwSwapInterval(1)
#
#     startup()
#     while not glfwWindowShouldClose(window):
#         render(glfwGetTime())
#         glfwSwapBuffers(window)
#         glfwPollEvents()
#     shutdown()
#
#     glfwTerminate()
#
# if __name__ == '__main__':
#     main()

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math


viewer = [0.0, 0.0, 10.0]

xs, ys, zs = 0.0, 0.0, 10.0
phi, theta = 0.0, 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
delta_x = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [xs, ys, zs, 1.0]

light1_ambient = [0.0, 0.0, 0.1, 1.0]
light1_diffuse = [0.0, 0.0, 1.0, 1.0]
light1_specular = [0.5, 0.5, 0.5, 1.0]
light1_position = [0.0, 10.0, 0.0, 1.0]


att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001
current_component = 'ambient'
current_index = 0

print('\n\tParametry poczatkowe')
print('Ambient: ', light_ambient[:3])
print('Diffuse: ', light_diffuse[:3])
print('Specular: ', light_specular[:3])

def update_light_position():
    global xs, ys, zs
    xs = 10.0 * math.cos(phi) * math.cos(theta)
    ys = 10.0 * math.sin(phi)
    zs = 10.0 * math.cos(phi) * math.sin(theta)


def adjust_light(component, index, delta):
    if component == 'ambient':
        light_ambient[index] = light_ambient[index] + delta
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    elif component == "diffuse":
        light_diffuse[index] = light_diffuse[index] + delta
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    elif component == "specular":
        light_specular[index] = light_specular[index] + delta
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    if current_index == 0:
        print('------------V------------')
    elif current_index == 1:
        print('-----------------V-------')
    elif current_index == 2:
        print('----------------------V--')

    print('Ambient: ', light_ambient[:3])
    print('Diffuse: ', light_diffuse[:3])
    print('Specular: ', light_specular[:3])
    print('--------------------------')

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)
    glLightfv(GL_LIGHT1, GL_POSITION, light1_position)

    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)


def shutdown():
    pass


def render(time):
    global theta, light_position

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glTranslatef(xs, ys, zs)
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    gluSphere(quadric, 0.5, 6, 5)
    gluDeleteQuadric(quadric)
    glTranslatef(-xs, -ys, -zs)

    light_position = [xs, ys, zs, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)
    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global current_component, current_index
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)
    elif key == GLFW_KEY_A and action == GLFW_PRESS:
        current_component = 'ambient'
        print('\n-------------------------- \nWybrano skladowa Ambient\n--------------------------')
    elif key == GLFW_KEY_D and action == GLFW_PRESS:
        current_component = 'diffuse'
        print('\n-------------------------- \nWybrano skladowa Diffuse\n--------------------------')
    elif key == GLFW_KEY_S and action == GLFW_PRESS:
        current_component = 'specular'
        print('\n-------------------------- \nWybrano skladowa Specular\n--------------------------')
    elif key == GLFW_KEY_UP and action == GLFW_PRESS:
        print('\tZwiekszono parametr')
        adjust_light(current_component, current_index, 0.1)
    elif key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        print('\tZmniejszono parametr')
        adjust_light(current_component, current_index, -0.1)
    elif key == GLFW_KEY_RIGHT and action == GLFW_PRESS:
        current_index += 1
        if current_index > 2:
            current_index = 0
        print('Przesunieto indeks o 1 w prawo')
    elif key == GLFW_KEY_LEFT and action == GLFW_PRESS:
        current_index -= 1
        if current_index < 0:
            current_index = 2
        print('Przesunieto indeks o 1 w lewo')



def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x, delta_y, mouse_x_pos_old, mouse_y_pos_old, phi, theta
    delta_x = x_pos - mouse_x_pos_old
    delta_y = y_pos - mouse_y_pos_old

    mouse_x_pos_old = x_pos
    mouse_y_pos_old = y_pos

    theta += delta_x * pix2angle * 0.01
    phi += delta_y * pix2angle * 0.01

    if phi > 1.5:
        phi = 1.5
    elif phi < -1.5:
        phi = -1.5

    update_light_position()


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
