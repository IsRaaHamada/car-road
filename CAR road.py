from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, .1, 100)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0, .7, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward
    global z
    global a
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glColor3f(.1, .3, 0)
    glVertex3d(60, 4, 1)
    glVertex3d(-22, 4, 1)
    glVertex3d(-22, -4, 2)
    glVertex3d(60, -4, 2)
    glEnd()
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(2+x, -2.5 * .4, 1 * .6+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-1.5+x, -2.5 * .4, 2 * .6+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2+x, -2.5 * .5, -2.5 * .6+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-2+x, -2.5 * .5, -(2.5 * .6)+z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)

    glColor3f(1, 0, 0)
    glTranslate(x, 0, z)
    glScale(1, .25, .5)
    glutSolidCube(5)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x, 5*.25, z)
    glScale(.5, .25, .5)
    glutSolidCube(4)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)

    glColor3f(.9, 1, 0)
    glTranslate(2.5+x, 0, 1+z)
    glutSolidSphere(.4, 10, 10)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5 + x, 0, -1 + z)
    glutSolidSphere(.4, 10, 10)
    glLoadIdentity()
    glRotate(90, 0, -1, 0)
    glTranslate(2.5 + x, 0, -1 + z)
    glutSolidSphere(1, 11, 12)

    if forward:
        angle -= .1
        x += .005
        if x > 6:
            forward = False
    else:
        x -= .005
        angle += .1

        if x < -11:
            forward = True
    glutSwapBuffers()


z = 0
a = 1


def ArrowHandeler(key, x, y):
    global z
    global a
    if key == GLUT_KEY_RIGHT:
        z += a
    elif key == GLUT_KEY_LEFT:
        z -= a
    draw()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"car_road")
glutDisplayFunc(draw)
glutIdleFunc(draw)   #rotaion
myinit()
glutSpecialFunc(ArrowHandeler)
glutMainLoop()
