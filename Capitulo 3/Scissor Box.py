import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

def init():
    pass

def render():
    glClearColor(0,0,1,0)
    glClear(GL_COLOR_BUFFER_BIT)

    glClearColor(1,0,0,0)
    glScissor(100, 100, 600, 400)
    glEnable(GL_SCISSOR_TEST)
    glClear(GL_COLOR_BUFFER_BIT)

    glClearColor(0, 1, 0, 0)
    glScissor(200, 200, 400, 200)
    glClear(GL_COLOR_BUFFER_BIT)

    glDisable(GL_SCISSOR_TEST)
    

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