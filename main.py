"""
 ----------------------------------------------------
  @Author: rinsa318
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-05 02:45:31
  @Last Modified by:   rinsa318
  @Last Modified time: 2019-06-05 03:53:34
 ----------------------------------------------------

  Usage:
   python main.py argvs[1] argvs[2] argvs[3]

   argvs[1]  :  .obj file
   argvs[2]  :  width of screen
   argvs[3]  :  height of screen

"""


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


## my function
from obj_functions import *
from viewer import Viewer
from material import *

argvs = sys.argv



def main():

  ##### load obj
  vertex, face = loadobj(argvs[1])


  #### window info
  width = int(argvs[2])
  height = int(argvs[3])


  #### light info
  light_ambient = [0.25, 0.25, 0.25]
  light_diffuse = [1.0, 1.0, 1.0]
  light_specular = [1.0, 1.0, 1.0]
  light_position = [0, 0, 1, 1]
  light = [light_ambient, light_diffuse, light_specular, light_position]


  ##### material info
  mat_list = get_mat_list()
  print_mat_list()
  material = set_parameter(mat_list[int(argvs[4])])


  #### start OpenGL loop
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
  glutInitWindowSize(width, height)
  glutCreateWindow("PyOpenGL Simple Viewer")
  Viewer(vertex, face, material, light)
  glutMainLoop()


if __name__ == '__main__':
  main()