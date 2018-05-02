import math
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 
star=[(0.5,0.8)]
heart=[(0.5,0.3854)]
origin=np.array((0.5,0.5))

def init():
    global origin,heart,star
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,1,0,1,-1,1)
    #init start data
    vec1=star[0]-origin
    vec2=heart[0]-origin
    ang=np.array([[0.309,0.951],[-0.951,0.309]])
    for i in range(4):
         vec1=vec1.dot(ang)
         vec2=vec2.dot(ang)
         star.append(vec1+origin)
         heart.append(vec2+origin)
def display():
    #glColor(0,0,0)
    global origin,heart,star
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0,0,0)
    glEnable(GL_POINT_SMOOTH);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glPointSize(5)
    glBegin(GL_POINTS)
    for point in star:
       # print point
        glVertex(point[0],point[1])
    #glVertex(0.25,0.25,0)
    #glVertex(0.75,0.25,0)
    #glVertex(0.75,0.75,0)
    #glVertex(0.25,0.75,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex(star[0])
    glVertex(star[2])
    glVertex(star[4])
    glVertex(star[1])
    glVertex(star[3])
    glEnd()
    glColor(1,1,0)
    glBegin(GL_POLYGON)
    for point in heart:
       # print point
        glVertex(point[0],point[1])
    glEnd()
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(250,250)
glutInitWindowPosition(100,100)
#sq=Square((0.5,0.5),0.25)
glutCreateWindow("Star!-  Author:15061077 Felix")
init()
glutDisplayFunc(display)
glutMainLoop()