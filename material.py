"""
 ----------------------------------------------------
  @Author: rinsa318
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-05 02:56:40
  @Last Modified by:   Tsukasa Nozawa
  @Last Modified time: 2019-06-05 12:31:04
 ----------------------------------------------------

  <material index>

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


def get_mat_list():
  mat_list = ["emerald", 
              "jade", 
              "obsidian", 
              "pearl", 
              "ruby", 
              "turquoise", 
              "brass", 
              "bronze", 
              "chrome", 
              "copper", 
              "gold", 
              "silver", 
              "black-plastic", 
              "cyan-plastic", 
              "green-plastic", 
              "red-plastic", 
              "white-plastic", 
              "yellow-plastic", 
              "black-rubber", 
              "cyan-rubber", 
              "green-rubber", 
              "red-rubber", 
              "white-rubber", 
              "yellow-rubber"]
  return mat_list




def set_parameter(index=10):
  '''
  function for select material.
  all parameter came from
  --> http://devernay.free.fr/cours/opengl/materials.html

  '''


  list = get_mat_list()
  name = list[index]
  material = []

  if(name == "emerald"):
    ambient   = [0.0215 , 0.1745,   0.0215]
    diffuse   = [0.07568, 0.61424,  0.07568]
    specular  = [0.633,   0.727811, 0.633 ]
    shininess = 128 * 0.6
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "jade"):
    ambient   = [0.135   ,0.2225  ,0.1575]
    diffuse   = [0.54  ,0.89  ,0.63]
    specular  = [0.316228  ,0.316228  ,0.316228]
    shininess = 128 * 0.1
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "obsidian"):
    ambient   = [0.05375   ,0.05  ,0.06625]
    diffuse   = [0.18275   ,0.17  ,0.22525]
    specular  = [0.332741  ,0.328634  ,0.346435]
    shininess = 128 * 0.3
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "pearl"):
    ambient   = [0.25  ,0.20725   ,0.20725]
    diffuse   = [1   ,0.829   ,0.829]
    specular  = [0.296648  ,0.296648  ,0.296648]
    shininess = 128 * 0.088
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "ruby"):
    ambient   = [0.1745  ,0.01175   ,0.01175]
    diffuse   = [0.61424   ,0.04136   ,0.04136]
    specular  = [0.727811  ,0.626959  ,0.626959]
    shininess = 128 * 0.6
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "turquoise"):
    ambient   = [0.1   ,0.18725   ,0.1745]
    diffuse   = [0.396   ,0.74151   ,0.691026]
    specular  = [0.297254  ,0.30829   ,0.306678]
    shininess = 128 * 0.1
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "brass"):
    ambient   = [0.329412, 0.223529, 0.027451]
    diffuse   = [0.780392, 0.568627, 0.113725]
    specular  = [0.992157, 0.941176, 0.807843]
    shininess = 128 * 0.21794872
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "bronze"):
    ambient   = [0.2125  ,0.1275  ,0.054]
    diffuse   = [0.714   ,0.4284  ,0.18144]
    specular  = [0.393548  ,0.271906  ,0.166721]
    shininess = 128 * 0.2
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "chrome"):
    ambient   = [0.25, 0.25, 0.25]
    diffuse   = [0.4, 0.4, 0.4]
    specular  = [0.774597, 0.774597, 0.774597]
    shininess = 128 * 0.6
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "copper"):
    ambient   = [0.19125   ,0.0735  ,0.0225]
    diffuse   = [0.7038  ,0.27048   ,0.0828]
    specular  = [0.256777  ,0.137622  ,0.086014]
    shininess = 128 * 0.1
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "gold"):
    ambient   = [0.24725   ,0.1995  ,0.0745]
    diffuse   = [0.75164   ,0.60648   ,0.22648]
    specular  = [0.628281  ,0.555802  ,0.366065]
    shininess = 128 * 0.4
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "silver"):
    ambient   = [0.19225   ,0.19225   ,0.19225]
    diffuse   = [0.50754   ,0.50754   ,0.50754]
    specular  = [0.508273  ,0.508273  ,0.508273]
    shininess = 128 * 0.4
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "black-plastic"):
    ambient   = [0.0   ,0.0   ,0.0]
    diffuse   = [0.01   ,0.01   ,0.01]
    specular  = [0.50   ,0.50   ,0.50]
    shininess = 128 * 0.25
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "cyan-plastic"):
    ambient   = [0.0   ,0.1   ,0.06]
    diffuse   = [0.0   ,0.50980392  ,0.50980392]
    specular  = [0.50196078  ,0.50196078  ,0.50196078]
    shininess = 128 * 0.25
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "green-plastic"):
    ambient   = [0.0   ,0.0   ,0.0]
    diffuse   = [0.1   ,0.35   ,0.1]
    specular  = [0.45   ,0.55   ,0.45]
    shininess = 128 * 0.25
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "red-plastic"):
    ambient   = [0.0   ,0.0   ,0.0]
    diffuse   = [0.5   ,0.0   ,0.0]
    specular  = [0.70   ,0.60   ,0.60]
    shininess = 128 * 0.25
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "white-plastic"):
    ambient   = [0.0   ,0.0   ,0.0]
    diffuse   = [0.55   ,0.55   ,0.55]
    specular  = [0.70   ,0.70   ,0.70]
    shininess = 128 * 0.25
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "yellow-plastic"):
    ambient   = [0.0   ,0.0   ,0.0]
    diffuse   = [0.5   ,0.5   ,0.0]
    specular  = [0.60   ,0.60   ,0.50]
    shininess = 128 * 0.25
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "black-rubber"):
    ambient   = [0.02   ,0.02   ,0.02]
    diffuse   = [0.01   ,0.01   ,0.01]
    specular  = [0.40   ,0.40   ,0.40]
    shininess = 128 * 0.078125
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "cyan-rubber"):
    ambient   = [0.0   ,0.05   ,0.05]
    diffuse   = [0.0   ,0.4  ,0.52]
    specular  = [0.04  ,0.7  ,0.7]
    shininess = 128 * 0.078125
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "green-rubber"):
    ambient   = [0.0   ,0.05   ,0.0]
    diffuse   = [0.4   ,0.5   ,0.4]
    specular  = [0.04   ,0.7   ,0.04]
    shininess = 128 * 0.078125
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "red-rubber"):
    ambient   = [0.05   ,0.0   ,0.0]
    diffuse   = [0.5   ,0.4   ,0.4]
    specular  = [0.70   ,0.04   ,0.04]
    shininess = 128 * 0.078125
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "white-rubber"):
    ambient   = [0.05   ,0.05   ,0.05]
    diffuse   = [0.5   ,0.5   ,0.5]
    specular  = [0.70   ,0.70   ,0.70]
    shininess = 128 * 0.078125
    material  = [ambient, diffuse, specular, shininess]

  elif(name == "yellow-rubber"):
    ambient   = [0.05   ,0.05   ,0.0]
    diffuse   = [0.5   ,0.5   ,0.4]
    specular  = [0.70   ,0.7   ,0.04]
    shininess = 128 * 0.078125
    material  = [ambient, diffuse, specular, shininess]



  else:
    print("wrong name.")
    return None

  return name, material