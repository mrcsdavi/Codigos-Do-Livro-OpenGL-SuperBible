import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

triangulo = [
    [-0.1, -0.1, 0.0],  
    [ 0.1, -0.1, 0.0],  
    [ 0.0,  0.1, 0.0]  
]


def init():
    glClearColor(0,0,1,1)
    glEnable(GL_DEPTH_TEST)

def render():
    # Angulo da revolução ao redor do nucleo
    fElect1 = 0.0

    # Limpar a janela com a atual clearing color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reseta a modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Traduz toda a cena fora e dentro da view
    # Esse é a viewing transformation inicial
    glTranslatef(0,0,-0.100)

    # Nucleo vermelho
    glColor3ub(255,0,0)
    gluSphere(gluNewQuadric(), 0.10, 15, 15)

    # Eletrons amarelos
    glColor3ub(255,255,0)

    # Primeiro eletron a orbitar
    # Salvando a viewing transformation
    glPushMatrix()

    # Rotação pelos angulos da revolução 
    glRotatef(fElect1, 0.0, 1.0, 0.0)

    # Tradução da origem para distancia de orbita
    glTranslatef(0.90, 0.0, 0.0)

    # Desenha o eletron
    gluSphere(gluNewQuadric(), 0.10, 15, 15)

    # Restaura o viewing transformation
    glPopMatrix()

    # Orbita do segundo eletron
    glPushMatrix()
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glRotatef(fElect1, 0.0, 1.0, 0.0)
    glTranslatef(-0.70, 0.0, 0.0)
    gluSphere(gluNewQuadric(), 0.10, 15, 15)
    glPopMatrix()

    # Orbita do Terceiro eletron
    glPushMatrix()
    glRotatef(360, 0.0, 0.0, 1.0)
    glRotatef(fElect1, 0.0, 1.0, 0.0)
    glTranslatef(-0.60, 0.60, 0.60)
    gluSphere(gluNewQuadric(), 0.10, 15, 15)
    glPopMatrix()

    # Incremente o angulo da revolução 
    fElect1 += 10.0
    if fElect1 > 360.0:
        fElect1 = 0.0

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