"""
 ----------------------------------------------------
  @Author: tsukasa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-03 23:07:50
  @Last Modified by:   Tsukasa Nozawa
  @Last Modified time: 2019-06-04 00:19:49
 ----------------------------------------------------

  Usage:
   python <file_name>.py argvs[1] argvs[2] argvs[3]...
  
   argvs[1]  :  ??????????   -->   !!!!!!!!!!
   argvs[2]  :  ??????????   -->   !!!!!!!!!!
   argvs[3]  :  ??????????   -->   !!!!!!!!!!
 

"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from utils.obj_functions import *

argvs = sys.argv




##### global #####

## light color and position
light_ambient = [0.25, 0.25, 0.25]
light_diffuse = [1.0, 1.0, 1.0]
light_specular = [1.0, 1.0, 1.0]
light_position = [0, 0, 2, 1]


## material 1
ambient = [0.25, 0.25, 0.25]
diffuse = [ 174.0/255.0, 214.0/255.0, 241.0/255.0 ]
# specular = [1.0, 1.0, 1.0]
# shininess = 32.0

## material 2
ambient2 = [0.25, 0.25, 0.25]
diffuse2 = [250.0/255.0, 215.0/255.0, 160.0/255.0]
# specular2 = [1.0, 1.0, 1.0]
# shininess2 = 32.0


def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
  glutInitWindowSize(600, 600)
  glutInitWindowPosition(0, 0)
  glutCreateWindow("mesh viewer")
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  init(600, 600)
  glutMainLoop()



def init(width, height):
  glClearColor(0.3, 0.3, 0.5, 1.0)
  glEnable(GL_DEPTH_TEST)

  ## setting for lighting
  glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
  glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
  glLightfv(GL_LIGHT0, GL_POSITION, light_position)
  glEnable(GL_LIGHTING)  # turn on lighting
  glEnable(GL_LIGHT0)# turn on GL_LIGHT0 which defined above

  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)



def calcu_vertex_normqal(ver, tri):

  vn = np.zeros(ver.shape, dtype=np.float32)
  for i in range(tri.shape[0]):
  # index
  id0 = tri[i][0]
  id1 = tri[i][1]
  id2 = tri[i][2]

  # face normal
  ab = ver[id1] - ver[id0]
  ac = ver[id2] - ver[id0]
  fn = np.cross(ab, ac)
  fn = fn / np.linalg.norm(fn)
 
  # add to vn array
  vn[id0] += fn
  vn[id1] += fn
  vn[id2] += fn

  vn /= np.sqrt(np.sum(vn ** 2, axis=-1))[:, None]

  return np.array(vn, dtype=np.float32)



def draw_obj():

  for i in range(tri.shape[0]):
  glBegin(GL_TRIANGLES)

  # index
  id0 = tri[i][0]
  id1 = tri[i][1]
  id2 = tri[i][2]

  ver0 = ver[id0] #* scale
  ver1 = ver[id1] #* scale
  ver2 = ver[id2] #* scale

  # glNormal3f(fn[i][0], fn[i][1], fn[i][2])
  glNormal3f(vn[id0][0], vn[id0][1], vn[id0][2])
  glVertex3f(ver0[0],ver0[1],ver0[2])
  glNormal3f(vn[id1][0], vn[id1][1], vn[id1][2])
  glVertex3f(ver1[0],ver1[1],ver1[2])
  glNormal3f(vn[id2][0], vn[id2][1], vn[id2][2])
  glVertex3f(ver2[0],ver2[1],ver2[2])

  glEnd()



def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  gluLookAt(0.0, 0.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

  # # set material
  # glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
  # glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
  # # glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
  # # glMaterialfv(GL_FRONT, GL_SHININESS, shininess)
  # glutSolidTeapot(1.0) # render teapot

  # set material
  glMaterialfv(GL_FRONT, GL_AMBIENT, ambient2)
  glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse2)
  # glMaterialfv(GL_FRONT, GL_SPECULAR, specular2)
  # glMaterialfv(GL_FRONT, GL_SHININESS, shininess2)
  draw_obj()

  glutSwapBuffers()


def reshape(width, height):
  glViewport(0, 0, width, height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)



if __name__ == "__main__":
  ver, tri = loadobj(argvs[1])
  vn = calcu_vertex_normqal(ver, tri)
  main()