from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
spin=0
def init():
    glClearColor(0,0,0,0)
    glShadeModel(GL_FLAT)
    glEnable(GL_CULL_FACE)

def draw():
    glutWireTeapot(1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,1,1)
    glLoadIdentity()
    gluLookAt(5,0,0,0,0,0,0,1,0)
    glRotate(spin,0,1,0)
    draw()
    glFlush()

def update():
    global spin
    spin+=0.002
    if spin>360:
        spin=0
    glutPostRedisplay()

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1,1,-1,1,1.5,20)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(400,400)
    glutCreateWindow("Rotating Teapot")
    init()
    glutIdleFunc(update)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()
main()