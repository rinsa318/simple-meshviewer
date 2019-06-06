"""
 ----------------------------------------------------
  @Author: rinsa318
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-05 02:45:31
  @Last Modified by:   Tsukasa Nozawa
  @Last Modified time: 2019-06-06 10:28:22
 ----------------------------------------------------

  Usage:
   python main.py argvs[1]

    argvs[1]  :  path to .obj file
   
  (option) --> default is 'gold'
    argvs[2]  :  material index 

                0 : 'emerald'
                1 : 'jade'
                2 : 'obsidian'
                3 : 'pearl'
                4 : 'ruby'
                5 : 'turquoise'
                6 : 'brass'
                7 : 'bronze'
                8 : 'chrome'
                9 : 'copper'
               10 : 'gold'
               11 : 'silver'
               12 : 'black-plastic'
               13 : 'cyan-plastic'
               14 : 'green-plastic'
               15 : 'red-plastic'
               16 : 'white-plastic'
               17 : 'yellow-plastic'
               18 : 'black-rubber'
               19 : 'cyan-rubber'
               20 : 'green-rubber'
               21 : 'red-rubber'
               22 : 'white-rubber'
               23 : 'yellow-rubber'

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
  if(len(argvs)>=3):
    material_index = int(argvs[2])
  else:
    ## set defaul material as "gold"
    material_index = 10


  #### load obj
  vertex, face = loadobj(meshpath)


  #### light parameter
  light = get_light()


  ##### material parameter
  name, material = set_parameter(material_index)


  #### start OpenGL loop
  print("\nstart rendering!")
  print("Input: {}".format(meshpath))
  print("Selecrt material is: {}\n".format(name))
  Viewer(vertex, face, material, light)
  # Viewer(vertex, face, material, light, 1200, 900)


if __name__ == '__main__':
  main()