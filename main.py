"""
 ----------------------------------------------------
  @Author: rinsa318
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-05 02:45:31
  @Last Modified by:   Tsukasa Nozawa
  @Last Modified time: 2019-06-05 12:15:57
 ----------------------------------------------------

  Usage:
   python main.py argvs[1] argvs[2] argvs[3]

   argvs[1]  :  path to .obj file
   argvs[2]  :  material index

                  0 : 'emerald'
                  1 : 'jade'
                  2 : 'obsidian'
                  3 : 'pearl'
                  5 : 'ruby'
                  6 : 'turquoise'
                  7 : 'brass'
                  8 : 'bronze'
                  9 : 'chrome'
                 10 : 'copper'
                 11 : 'gold'
                 12 : 'silver'
                 13 : 'black-plastic'
                 14 : 'cyan-plastic'
                 15 : 'green-plastic'
                 16 : 'red-plastic'
                 17 : 'white-plastic'
                 18 : 'yellow-plastic'
                 19 : 'black-rubbe'
                 20 : 'cyan-rubbe'
                 21 : 'green-rubbe'
                 22 : 'red-rubbe'
                 23 : 'white-rubbe'
                 24 : 'yellow-rubbe'

"""



import sys

## my class and function
from obj_functions import *
from viewer import Viewer
from material import *
from light import *
argvs = sys.argv



def main():

  #### set config
  meshpath = argvs[1]
  material_index = int(argvs[2])


  #### load obj
  vertex, face = loadobj(meshpath)


  #### light parameter
  light = get_light()


  ##### material parameter
  name, material = set_parameter(material_index)


  #### start OpenGL loop
  print("start rendering!")
  print("Input: {}".format(meshpath))
  print("Selecrt material is: {}\n".format(name))
  # print("-----------------------------\n")
  Viewer(vertex, face, material, light)
  # Viewer(vertex, face, material, light, 1200, 900)


if __name__ == '__main__':
  main()