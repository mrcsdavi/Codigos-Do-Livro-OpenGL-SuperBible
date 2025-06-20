import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

def init():
    pass

def render():
    x = 0.100
    y = 0.200
    rsize = 100
    
    dRadius = 0.1
    dAngle = 0.0

    # Limpa a cor da janela azul
    glClearColor(0, 0, 1, 0)

    # Usa 0 para limpar o stencil e ativa o stencil test
    glClearStencil(0)
    glEnable(GL_STENCIL_TEST)
  
    # Limpa a cor do buffer e o stencil buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
   
    # Todos os comandos de desenho falham o stencil test, e não são desenhados
    # mas incrementam o valor em um stencil buffer
    glStencilFunc(GL_NEVER, 0x0, 0x0)
    glStencilOp(GL_INCR, GL_INCR, GL_INCR)
   

    # Padrão de espiral cria um stencil pattern
    # Desenha o padrão de espiral com linhas brancas. 
    # As linhas brancas demonstram que a função stencil
    # previne elas de serem desenhadas
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    dAngle = 0.0
    while dAngle < 400.0:
        glVertex2d(dRadius * cos(dAngle), dRadius * sin(dAngle))
        dRadius *= 1.002

        dAngle += 0.1
    glEnd()


    # Agora, permitindo o desenho, exceto onde o stencil pattern é 0x1
    # e não faz nenhuma mudança a mais para o stencil buffer
    glStencilFunc(GL_NOTEQUAL, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
   
    # Agora desenha um quadrado vermelho
    glColor3f(1.0, 0.0, 0.0)
    glRectf(x, y, x + rsize, y - rsize) # x = 100 + rsize = 1000, y = 400 + rsize = 1000

   

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