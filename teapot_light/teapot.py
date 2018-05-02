from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
spin=0
x=0.52573
z=0.85065
vdata=[-x,0,z,x,0,z,-x,0,-z,x,0,-z,\
       0,z,x,0,z,-x,0,-z,x,0,-z,-x,\
       z,x,0,-z,x,0,z,-x,0,-z,-x,0]
tindices=[1,4,0,4,9,0,4,5,9,8,5,4,1,8,4,\
         1,10,8,10,3,8,8,3,5,3,2,5,3,7,2,\
         3,10,7,10,6,7,6,11,7,6,0,11,6,1,0,\
         10,1,6,11,0,9,2,11,9,5,2,9,11,2,7]
def init():
    glClearColor(0,0,0,0)
    glShadeModel(GL_SMOOTH)
    #glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
   # glPolygonMode(GL_BACK,GL_LINE)
   # glCullFace(GL_FRONT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_INDEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3,GL_FLOAT,0,vdata)
    glIndexPointer(GL_FLOAT,0,tindices)
    glNormalPointer(GL_FLOAT,0,vdata)
    
    mat_specular=[1,1,1,1]
    mat_shininess=[70]
    white_light_position=[-10,-5,0,1]
    red_light_position=[10,5,0,1]
    white_light=[1,1,1,1]
    red_light=[1,0,0,1]
    glMaterial(GL_FRONT,GL_SPECULAR,mat_specular)
    glMaterial(GL_FRONT,GL_SHININESS,mat_shininess)
    glLight(GL_LIGHT0,GL_POSITION,white_light_position)
    glLight(GL_LIGHT0,GL_DIFFUSE,white_light)
    glLight(GL_LIGHT0,GL_SPECULAR,white_light)
    glLight(GL_LIGHT1,GL_POSITION,red_light_position)
    glLight(GL_LIGHT1,GL_DIFFUSE,red_light)
    glLight(GL_LIGHT1,GL_SPECULAR,red_light)
    
def draw():
    glutSolidTeapot(1)
  #  glDrawElements(GL_TRIANGLES,60,GL_UNSIGNED_BYTE,tindices)
   # glutSolidSphere(1,20,16)
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor(1,1,1)
    glLoadIdentity()
    gluLookAt(0,0,5,0,0,0,0,1,0)
    glRotate(spin,0,1,0)
    draw()
    glFlush()

def update():
    global spin
    spin+=0.006
    if spin>360:
        spin=0
    glutPostRedisplay()

def reshape(w,h):
    if w>h:
        glViewport(0,0,h,h)
    else:
        glViewport(0,0,w,w)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1,1,-1,1,1.5,20)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE|GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow("Rotating Teapot")
    init()
    glutIdleFunc(update)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()
main()