import time
from tkinter import *
from OpenGL import GL
from pyopengltk import OpenGLFrame

import sys, math, time
if sys.version_info[0] < 3:
    from Tkinter import Tk, YES, BOTH
else:
    from tkinter import Tk, YES, BOTH
from OpenGL import GL, GLU
from pyopengltk import OpenGLFrame

class AppOgl(OpenGLFrame):

    def initgl(self):
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glColor3f(1.0, 1.0, 1.0)
        GL.glPointSize(4.0)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(-5, 5, -5, 5)
        self.start = time.time()
        self.nframes = 0

    def redraw(self):
        """Render a single frame"""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex2f(10, 10)
        GL.glVertex2f(20, 20)
        GL.glEnd()
        GL.glFlush()
        
        
        self.nframes += 1
        tm = time.time() - self.start
        
        print("fps",self.nframes / tm, end="\r" )

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=750, height=400)
        label = Label(root, text="hello")
        label.pack()

if __name__ == '__main__':
    root = Tk()
    app = AppOgl(root, width=750, height=400)
    app.pack(fill=BOTH, expand=YES)
    ui = StartPage(root)
    app.animate = 1
    app.after(100, app.printContext)
    app.mainloop()
