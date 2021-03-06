"""
 ----------------------------------------------------
  @Author: rinsa318
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-05 02:42:21
  @Last Modified by:   Tsukasa Nozawa
  @Last Modified time: 2019-08-02 20:19:08
 ----------------------------------------------------

  Usage:
   python viewer.py argvs[1]

   argvs[1]  :  .obj file

"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
from datetime import datetime
import sys


## my function
from obj_functions import *
argvs = sys.argv


class Viewer:
  def __init__(self, ver, tri, material, light, width=800, height=800):
    '''
    set variable, and run OpenGl init()
    '''  

    ## variable for mouse motion
    self.__mouseX = 0.0
    self.__mouseY = 0.0
    self.__rotX = 0.0
    self.__rotY = 0.0
    self.__rotZ = 0.0
    self.__transY = 0.0
    self.__transX = 0.0
    self.__zoom =  45.0
    self.__flag = None  

    ## flag for render
    self.__axis = False
    self.__wire = False
    self.__shading = False  

    ## variable for object
    self.__ver = ver
    self.__tri = tri
    self.__fn, self.__vn = compute_normal(ver, tri) 
    # self.__fn, self.__vn = calc_vertex_normal(ver, tri)  
  

    ## variable for screen
    # self.__width = glutGet(GLUT_WINDOW_WIDTH)
    # self.__height = glutGet(GLUT_WINDOW_HEIGHT)
    self.__width = width 
    self.__height = height


    ## variable for shading
    self.__ambient = material[0]
    self.__diffuse = material[1]
    self.__specular = material[2]
    self.__shininess = material[3]
    self.__light_ambient = light[0]
    self.__light_diffuse = light[1]
    self.__light_specular = light[2]
    self.__light_position = light[3]  


    ## OpenGL init()
    self._manual()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(self.__width, self.__height)
    glutCreateWindow("PyOpenGL Simple Viewer")
    glutDisplayFunc(self._draw)
    glutMouseFunc(self._mousePressed)
    glutMotionFunc(self._mouseDragged) 
    glutReshapeFunc(self._reshape)
    glutKeyboardFunc(self._keyboard)
    glClearColor(0.3, 0.3, 0.5, 1.0)
    self._setLight()
    glutMainLoop()
  


  def _manual(self):
    '''
    print manual
    '''

    manual = "\n*/----------------------------- manual -----------------------------/*\n\n\n"
    manual += " Drag with Left Mousebutton    :  move eye position\n"
    manual += " Drag with right Mousebutton   :  move down/up to zoom in/out\n"
    manual += " Drag with middle Mousebutton  :  move vertical/horizontal to\n"
    manual += "                                  translate the screen along y/x axis\n"
    manual += "           a / A               :  type a/A to turn on/off axis \n"
    manual += "           w / W               :  type w/W to turn on/off wireframe \n"
    manual += "           s / S               :  type s/S to change Smooth/Flat shading\n"
    manual += "             r                 :  reset viewport \n"
    manual += "             p                 :  take a screenshot as .png \n"
    manual += "             q                 :  quit the program\n"
    manual += "\n\n*/------------------------------------------------------------------/*\n"
    print(manual)




  def _setLight(self):
    '''
    function for setting shading
    '''  

    ## turn on shading
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)


    ## set lighting information
    glLightfv(GL_LIGHT0, GL_AMBIENT, self.__light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, self.__light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, self.__light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, self.__light_position)
    glEnable(GL_DEPTH_TEST)               
  
  

  def _draw_obj(self):
    '''
    function for render input objects
    with material
    '''  


    ## apply shading
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  
    if(self.__shading):
      glShadeModel(GL_SMOOTH)
    else:
      glShadeModel(GL_FLAT)

    ## set material information
    glMaterialfv(GL_FRONT, GL_AMBIENT, self.__ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, self.__diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, self.__specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, self.__shininess)  
  

    ## render objects
    glBegin(GL_TRIANGLES)
    for i in range(self.__tri.shape[0]):  

      ## index
      id0 = self.__tri[i][0]
      id1 = self.__tri[i][1]
      id2 = self.__tri[i][2]  

      ## set vertex and normal
      ## v1
      # glNormal3f(self.__fn[i][0], self.__fn[i][1], self.__fn[i][2])
      glNormal3f(self.__vn[id0][0], self.__vn[id0][1], self.__vn[id0][2])
      glVertex3f(self.__ver[id0][0], self.__ver[id0][1], self.__ver[id0][2])
      ## v2
      # glNormal3f(self.__fn[i][0], self.__fn[i][1], self.__fn[i][2])
      glNormal3f(self.__vn[id1][0], self.__vn[id1][1], self.__vn[id1][2])
      glVertex3f(self.__ver[id1][0], self.__ver[id1][1], self.__ver[id1][2])
      ## v3
      # glNormal3f(self.__fn[i][0], self.__fn[i][1], self.__fn[i][2])
      glNormal3f(self.__vn[id2][0], self.__vn[id2][1], self.__vn[id2][2])
      glVertex3f(self.__ver[id2][0], self.__ver[id2][1], self.__ver[id2][2]) 

    glEnd()  
  
  

  def _draw_wireframe(self):
    '''
    function for render wireframe
    '''  

    ## shading off
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)  
  

    ## render wireframe
    glLineWidth(2)
    glColor3f(0.0, 0.0, 0.0)
    for i in range(self.__tri.shape[0]):
      glBegin(GL_LINE_LOOP)
      
      # index
      id0 = self.__tri[i][0]
      id1 = self.__tri[i][1]
      id2 = self.__tri[i][2]  

      ## set vertex
      ## v1
      glVertex3f(self.__ver[id0][0], self.__ver[id0][1], self.__ver[id0][2])        
      ## v2
      glVertex3f(self.__ver[id1][0], self.__ver[id1][1], self.__ver[id1][2])        
      ## v3
      glVertex3f(self.__ver[id2][0], self.__ver[id2][1], self.__ver[id2][2])  

      glEnd()  
  
  

  def _draw_axis(self):
    '''
    function for render axis
    '''  

    ## shading off
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)  
  

    ## reder axis
    glLineWidth(3)
    glBegin(GL_LINES);  

    ## x
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1000, 0.0, 0.0)  

    ## y
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1000, 0.0)  

    ## z
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1000)
    glEnd()  

        
  

  def _draw(self):
    '''
    function for draw object
    '''  

    ## set screen info
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(self.__zoom, float(self.__width) / float(self.__height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)  
  

    ## modeling transform
    glRotatef(self.__rotX, 1.0, 0.0, 0.0)
    glRotatef(self.__rotY, 0.0, 1.0, 0.0)
    glRotatef(self.__rotZ, 0.0, 0.0, 1.0)
    glTranslatef(self.__transY/100.0, 0.0, 0.0)
    glTranslatef(0.0, -self.__transX/100.0, 0.0)
  

    ## render object with material
    self._draw_obj()  
  

    ## overlay wireframe to objects
    if(self.__wire):
        self._draw_wireframe()  
  

    ## show axis
    if(self.__axis):
      self._draw_axis()  

          
    glutSwapBuffers()
        
  

  def _mousePressed(self, button, state, x, y):
    '''
    Get bottun infomation.
    Then edit self.__flag for _mouseDragged()
    '''  

    ## add flag for move eye position
    if(button == GLUT_LEFT_BUTTON):
      self.__flag = "left"  
  

    ## add flag for zoom in/out
    elif(button == GLUT_RIGHT_BUTTON):
      self.__flag = "right"  
  

    ## add flag for translation
    elif(button==GLUT_MIDDLE_BUTTON):
      self.__flag = "middle"

    else:
      glutIdleFunc(0)
    self.__mouseX = x
    self.__mouseY = y  
  
  
  

  def _mouseDragged(self, x, y):
    '''
    Apply move eye position, translation, zoom in/out.  

    '''  

    ## mouse move with left click 
    ##  --> mouse based move eye position
    if(self.__flag == "left"):
      self.__rotX += y - self.__mouseY
      self.__rotY += x - self.__mouseX  
  

    ## mouse move with right click 
    ##  --> mouse based zoom in/out
    elif(self.__flag=="right"):
      self.__zoom -= y - self.__mouseY  

      ## apply cliping by using th
      th_max = 150.0
      th_min = 1.1
      if self.__zoom > th_max:
        self.__zoom = th_max
      elif self.__zoom < th_min:
        self.__zoom = th_min  
  

    ## mouse move with middle click 
    ##  --> mouse based translation
    elif(self.__flag=="middle"):
      self.__transY += y - self.__mouseY
      self.__transX += x - self.__mouseX
        


    self.__mouseX = x
    self.__mouseY = y
    glutPostRedisplay()  
  
  

  def _reshape(self, width, height):
    '''
    change viewport
    '''  

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(self.__zoom, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)  
  
  

  def _keyboard(self, bkey, x, y):
    '''
    set keyboard callback
    '''  

    key = bkey.decode("utf-8")  

    ## reset
    if(key=='r'): 
      self._reset()  

    ## turn on axis
    elif(key=='a'): 
      self.__axis = True  

    ## turn off axis
    elif(key=='A'): 
      self.__axis = False  

    ## turn on wireframe
    elif(key=='w'): 
      self.__wire = True  

    ## turn off wireframe
    elif(key=='W'): 
      self.__wire = False  

    ## turn on smooth-shading
    elif(key=='s'): 
      self.__shading = True

    ## turn off smooth-shading
    elif(key=='S'): 
      self.__shading = False

    ## take a screenshot
    elif(key=='p'): 
      self._screenshot()  

    ## quit a program
    elif(key=='q'): 
      sys.exit(0)  

    glutPostRedisplay()  
  
  

  def _screenshot(self):
    '''
    Save a screenshot as "current time info".png
    It will be save at ./screenshots directly.  

    If ./screenshots is not exist, 
    new directly will create automatically.  

    '''  

    ## create image from screen
    pixels = glReadPixels(0, 0, self.__width, self.__height, GL_RGB, GL_UNSIGNED_BYTE)
    img = Image.frombytes("RGB", (self.__width, self.__height), pixels)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  

    ## get current time stamp and create outpath
    now = datetime.now()
    outdir = "./screenshots"
    if(not(os.path.exists(outdir))):
      os.mkdir(outdir)
    outpath = os.path.join(outdir, str(now) + ".png")
    
    ## save screenshot
    img.save(outpath)
    print("save screenshot as:  {}".format(outpath))  
  
  
  

  def _reset(self):
    '''
    re-set viewer informaiton
    '''  

    self.__mouseX = 0.0
    self.__mouseY = 0.0
    self.__rotX = 0.0
    self.__rotY = 0.0
    self.__rotZ = 0.0
    self.__transY = 0.0
    self.__transX = 0.0
    self.__zoom = 45.0
    self.__flag = None 
    self.__axis = False
    self.__wire = False 
    self.__shading = False 
    glutPostRedisplay()



def main():

  #### window info
  width = 800
  height = 800


  #### light info
  light_ambient = [0.25, 0.25, 0.25]
  light_diffuse = [1.0, 1.0, 1.0]
  light_specular = [1.0, 1.0, 1.0]
  light_position = [0, 0, 1, 1]
  light = [light_ambient, light_diffuse, light_specular, light_position]

  ##### material info
  ## brass
  ambient = [0.329412, 0.223529, 0.027451]
  diffuse = [0.780392, 0.568627, 0.113725]
  specular = [0.992157, 0.941176, 0.807843]
  shininess = 128 * 0.21794872
  material = [ambient, diffuse, specular, shininess]

  # ## chrom
  # ambient = [0.25, 0.25, 0.25]
  # diffuse = [0.4, 0.4, 0.4]
  # specular = [0.774597, 0.774597, 0.774597]
  # shininess = 128 * 0.6
  # material = [ambient, diffuse, specular, shininess]


  ##### load obj
  vertex, face = loadobj(argvs[1])



  #### start OpenGL loop
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
  glutInitWindowSize(width, height)
  glutCreateWindow("PyOpenGL Simple Viewer")
  Viewer(vertex, face, material, light)
  glutMainLoop()


if __name__ == '__main__':
  main()