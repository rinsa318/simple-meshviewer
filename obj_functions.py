"""
 ----------------------------------------------------
  @Author: tsukasa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-03 15:17:55
  @Last Modified by:   rinsa318
  @Last Modified time: 2019-06-05 02:28:08
 ----------------------------------------------------


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




def calc_vertex_normal(ver, tri):

  vn = np.zeros(ver.shape, dtype=np.float32)
  for i in range(tri.shape[0]):
    # index
    id0 = tri[i][0]
    id1 = tri[i][1]
    id2 = tri[i][2]

    # face normal
    ab = ver[id1] - ver[id0]
    ac = ver[id2] - ver[id0]
    face_normal = np.cross(ab, ac)
    # norm = np.sqrt(np.sum(face_normal ** 2, axis=-1))
    norm = np.linalg.norm(face_normal, axis=-1)
    # norm = np.linalg.norm(face_normal)
    # print(norm)
    # print(np.linalg.norm(np.array(face_normal)))
    # print(np.sqrt(np.sum(face_normal ** 2, axis=-1)))


    fn = face_normal / norm
   
    # add to vn array
    vn[id0] += fn
    vn[id1] += fn
    vn[id2] += fn

  vn /= np.sqrt(np.sum(vn ** 2, axis=-1))[:, None]

  return np.array(vn, dtype=np.float32)