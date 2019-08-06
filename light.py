"""
 ----------------------------------------------------
  @Author: Tsukasa Nozawa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-05 11:24:23
  @Last Modified by:   rinsa318
  @Last Modified time: 2019-08-05 17:40:23
 ----------------------------------------------------

"""



def get_light():

  '''
  function for get light parameter
  '''

  light_ambient = [0.25, 0.25, 0.25]
  light_diffuse = [1.0, 1.0, 1.0]
  light_specular = [1.0, 1.0, 1.0]
  light_position = [0, 0, 1, 1]
  light = [light_ambient, light_diffuse, light_specular, light_position]


  return light