#Author:15061077 Felix

import math
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 
from math import sin,cos,pi
import time
vertexs=[(1,-0.5,-1),(-1,-0.5,-1),(-1,0.5,-1),(1,0.5,-1),
         (1,-0.5,1),(-1,-0.5,1),(-1,0.5,1),(1,0.5,1)]
indices=[4,5,6,7,1,2,6,5,2,3,7,6,0,4,7,3,0,3,2,1,0,1,5,4]
speed=2*pi/60
last_time=0
def rotate(vec,ang,origin=(0.0,0.0)):
    vec=np.array(vec)
    origin=np.array(origin)
    mat=np.array([[cos(ang),sin(ang)],[-sin(ang),cos(ang)]])
    return (vec-origin).dot(mat)+origin
def init():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(250,250)
    glutInitWindowPosition(100,100)
    #sq=Square((0.5,0.5),0.25)
    glutCreateWindow("Star!")
    
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3,GL_FLOAT,0,vertexs)
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,1,0,1,-1,1)

'''
def update():
    global heart,star
    global last_time
    delta=time.time()-last_time
    last_time=last_time+delta

    for i in range(5):
        heart[i]=rotate(np.array(heart[i]),speed*delta,star[0])
        star[i]=rotate(np.array(star[i]),speed*delta,star[0])
    glutPostRedisplay()
''' 
def display():
    #glColor(0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(255,0,0)
    glEnable(GL_POINT_SMOOTH);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDrawElements(GL_QUADS,24,GL_UNSIGNED_BYTE,indices)
    glFlush()

def reshape(w,h):
   # glViewport(0,0,int(w),int(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,int(w),0,int(h),-1,1)


def mouse(button,state,x,y):
    global speed
    if button==GLUT_LEFT_BUTTON:
        speed=speed*2
    elif button==GLUT_RIGHT_BUTTON:
        speed=speed/2

last_time=time.time()
init()
glutMouseFunc(mouse)
glutDisplayFunc(display)
#glutReshapeFunc(reshape)
#glutIdleFunc(update)
glutMainLoop()