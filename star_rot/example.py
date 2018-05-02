#Author:15061077 Felix

import math
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 
from math import sin,cos,pi
import time
star=[]
heart=[]
origin=[]
speed=2*pi/60
last_time=0
spin=0
def rotate(vec,ang,origin=(0.0,0.0)):
    vec=np.array(vec)
    origin=np.array(origin)
    mat=np.array([[cos(ang),sin(ang)],[-sin(ang),cos(ang)]])
    return (vec-origin).dot(mat)+origin
def init():
    global origin,heart,star
    star=[(0.5,0.8)]
    heart=[(0.5,0.3854)]
    origin=np.array((0.5,0.5))
    
    #init start data
    vec1=star[0]-origin
    vec2=heart[0]-origin
    for i in range(4):
         vec1=rotate(vec1,pi*2/5)
         vec2=rotate(vec2,pi*2/5)
         star.append(vec1+origin)
         heart.append(vec2+origin)

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(250,250)
    glutInitWindowPosition(100,100)
    #sq=Square((0.5,0.5),0.25)
    glutCreateWindow("Star!")

    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,1,0,1,-1,1)

def update():
    global  spin
    spin=spin+2
    if spin>360:
        spin=spin-360
    glutPostRedisplay()
def drawStar():
    global origin,heart,star
    glEnable(GL_POINT_SMOOTH);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glPointSize(5)
    glBegin(GL_POINTS)
    # draw points
    for point in star:
       # print point
        glVertex(point[0],point[1])
    glEnd()
    #draw lines
    glBegin(GL_LINE_LOOP)
    for i in range(0,5):
        glVertex(*star[i*2%5])
    glEnd()
    glColor(1,1,0)
    #draw heart 
    glBegin(GL_POLYGON)
    for point in heart:
       # print point
        glVertex(point[0],point[1])
    glEnd()
    glFlush()
def display():
    glColor(1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
   # glPushMatrix()
   # glRotate(spin,0,0,1)
    glColor(0,0,0)
    drawStar()
  #  glRectf(-0.5,-0.5,0.5,0.5)
  ##  glPopMatrix()
    glutSwapBuffers()
def reshape(w,h):
    glViewport(0,0,w,h)
   # glViewport(0,0,int(w),int(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,int(w),0,int(h),-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

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
glutIdleFunc(update)
glutReshapeFunc(reshape)
glutMainLoop()