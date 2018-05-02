from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
pos=0
spin=0
vertices=[1,-0.5,-1,-1,-0.5,-1,-1,0.5,-1,1,0.5,-1,
         1,-0.5,1,-1,-0.5,1,-1,0.5,1,1,0.5,1]
indices=[4,5,6,7,1,2,6,5,2,3,7,6,0,4,7,3,0,3,2,1,0,1,5,4]
color=[1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0]
def init():
    glClearColor(0,0,0,0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)
    glPolygonMode(GL_FRONT,GL_FILL)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glEnableClientState(GL_INDEX_ARRAY)
    glVertexPointer(3,GL_FLOAT,0,vertices)
    glIndexPointer(GL_FLOAT,0,indices)
    glColorPointer(3,GL_FLOAT,0,color)
def draw():
    glDrawElements(GL_QUADS,24,GL_UNSIGNED_BYTE,indices)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,1,1)
    glLoadIdentity()
    gluLookAt(0,0,5,0,0,-15,0,1,0)
    glTranslate(pos,0,0)
    glRotate(spin,1,1,1)
    draw()
    glFlush()
def update():
    global pos
    global spin
    #pos=pos+0.002
    if pos>5:
        pos=-5

    spin=spin+0.02
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
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Rotating Cube")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(update)
    glutMainLoop()

main()