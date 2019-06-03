"""
 ----------------------------------------------------
  @Author: tsukasa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-03 15:17:55
  @Last Modified by:   tsukasa
  @Last Modified time: 2019-06-03 15:18:28
 ----------------------------------------------------

  Usage:
   python <file_name>.py argvs[1] argvs[2] argvs[3]...
  
   argvs[1]  :  ??????????   -->   !!!!!!!!!!
   argvs[2]  :  ??????????   -->   !!!!!!!!!!
   argvs[3]  :  ??????????   -->   !!!!!!!!!!
 
  Options:
   xxx       :  ??????????   -->   !!!!!!!!!!



"""


import numpy as np



def loadobj(path):
  vertices = []
  #texcoords = []
  triangles = []
  normals = []

  with open(path, 'r') as f:
    for line in f:
      if line[0] == '#':
        continue

      pieces = line.split(' ')

      if pieces[0] == 'v':
        vertices.append([float(x) for x in pieces[1:4]])      
      # elif pieces[0] == 'vt':
      #   texcoords.append([float(x) for x in pieces[1:]])
      elif pieces[0] == 'f':
        if pieces[1] == '':
            triangles.append([int(x.split('/')[0]) - 1 for x in pieces[2:]])
        else: 
            triangles.append([int(x.split('/')[0]) - 1 for x in pieces[1:]])
      elif pieces[0] == 'vn':
        normals.append([float(x) for x in pieces[1:]])
      else:
        pass

  return (np.array(vertices, dtype=np.float32),
            #np.array(texcoords, dtype=np.float32),
            np.array(triangles, dtype=np.int32))#,
            # np.array(normals, dtype=np.float32))




def writeobj(filepath, vertices, triangles):
  with open(filepath, "w") as f:
    for i in range(vertices.shape[0]):
      f.write("v {} {} {}\n".format(vertices[i, 0], vertices[i, 1], vertices[i, 2]))
    for i in range(triangles.shape[0]):
      f.write("f {} {} {}\n".format(triangles[i, 0] + 1, triangles[i, 1] + 1, triangles[i, 2] + 1))