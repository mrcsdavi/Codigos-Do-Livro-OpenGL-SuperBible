import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

GL_PI = 3.14159

def init():
    
    glClearColor(0,0,0,1)
    glColor3f(0,1,0)
    glShadeModel(GL_FLAT)
   

def render():
    
    iPivot = 1
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if True: # back-face culling
        glEnable(GL_CULL_FACE)
    else:
        glDisable(GL_CULL_FACE)

    if True: # depth testing
        glEnable(GL_DEPTH_TEST)
    else:
        glDisable(GL_DEPTH_TEST)

    if True: # bOutline
        glPolygonMode(GL_BACK, GL_LINE)
    else:
        glPolygonMode(GL_BACK, GL_FILL)
    
    glPushMatrix()
    glRotatef(900, -0.5, 1.0, 0.0)
    glRotatef(-80, 0.0, 1.0, 0.0)

    # 1

    glFrontFace(GL_CW) #clockwise
    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(0.0, 0.0, 0.75); 

     # alterar o angulo
    angle = -1.0
    while angle < (2.0*GL_PI):

        x = 0.50*sin(angle)
        y = 0.50*cos(angle)

        if (iPivot % 2) == 0:
            glColor3f(1.0, 0.0, 0.0)
        else:
            glColor3f(0.0, 1.0, 0.0)
        iPivot += 1 # ?

        glVertex2f(x, y)
        
        angle += (GL_PI/8.0)
        
    glEnd()

    # 2
    glFrontFace(GL_CCW) # correção do culling - counter-clockwise
    glBegin(GL_TRIANGLE_FAN)#
    
    glVertex2f(0.0, 0.0); 

    # alterar o angulo
    angle = -1.0
    while angle < (2.0*GL_PI):

        x = 0.50*sin(angle)
        y = 0.50*cos(angle)

        if (iPivot % 2) == 0:
            glColor3f(1.0, 0.0, 0.0)
        else:
            glColor3f(0.0, 1.0, 0.0)
        iPivot += 1 # ?

        glVertex2f(x, y)

        angle += (GL_PI/8.0)

    glEnd()
    glPopMatrix()
    
    

def main():
    glfw.init()

    glfw.window_hint(glfw.DEPTH_BITS, 24)

    window = glfw.create_window(800, 600, "Janela", None, None)
    if window == None:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    glViewport(0,0,800,600)
    
    init()
    # renderizar tudo na janela do gflw
    while not glfw.window_should_close(window): 
        render()
        glfw.swap_buffers(window)
        glfw.poll_events() 
    glfw.terminate() # encerra a janela do glfw

if __name__ == '__main__':
    main()