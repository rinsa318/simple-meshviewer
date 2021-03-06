"""
 ----------------------------------------------------
  @Author: tsukasa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-06-03 15:17:55
  @Last Modified by:   Tsukasa Nozawa
  @Last Modified time: 2019-08-02 20:19:41
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




def compute_normal(vertices, indices):
  '''
  Compute vertex normal: Nelson Max's method
  see here: "Weights for Computing Vertex Normals from Facet Normals"
  '''
  eps = 1e-10
  fn = np.zeros(indices.shape, dtype=np.float32)
  vn = np.zeros(vertices.shape, dtype=np.float32)
  v = [vertices[indices[:, 0], :],
       vertices[indices[:, 1], :],
       vertices[indices[:, 2], :]]

  ## loop for adjacent vertices
  ## this code assume triangle mesh
  ## f(v0, v1, v2)
  for i in range(3):
    v0 = v[i]
    v1 = v[(i + 1) % 3]
    v2 = v[(i + 2) % 3]
    e1 = v1 - v0
    e2 = v2 - v0
    e1_len = np.linalg.norm(e1, axis=-1)
    e2_len = np.linalg.norm(e2, axis=-1)
    side_a = e1 / (np.reshape(e1_len, (-1, 1)) + eps)
    side_b = e2 / (np.reshape(e2_len, (-1, 1)) + eps)


    ## compute face normal
    if(i == 0):
      fn = np.cross(side_a, side_b)
      print(fn)
      fn = fn / (np.reshape(np.linalg.norm(fn, axis=-1), (-1, 1)) + eps)
      # fn = n


    ## comput angle between 2 edge
    angle = np.where(np.sum(side_b *side_a, axis=-1) < 0,
                    np.pi - 2.0 * np.arcsin(0.5 * np.linalg.norm(side_a + side_b, axis=-1)),
                    2.0 * np.arcsin(0.5 * np.linalg.norm(side_a - side_b, axis=-1)))
    sin_angle = np.sin(angle)


    ## compute weight, and re-compute normal
    contrib = fn * np.reshape(sin_angle / ((e1_len * e2_len) + eps), (-1, 1))
    index = indices[:, i]

    ## add as vertex normal
    for i in range(index.shape[0]):
      vn[index[i], :] += contrib[i, :]


  ## normalize
  vn = vn / (np.reshape(np.linalg.norm(vn, axis=-1), (-1, 1)) + eps)

  return fn, vn



def calc_vertex_normal(ver, tri):


  fn = np.zeros(tri.shape, dtype=np.float32)
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


    fn[i] = face_normal / norm
   
    # add to vn array
    vn[id0] += fn[i]
    vn[id1] += fn[i]
    vn[id2] += fn[i]

  vn /= np.sqrt(np.sum(vn ** 2, axis=-1))[:, None]

  return fn, vn



def loadfp(path):
  fp = []
  
  with open(path, 'r') as f:
    for line in f:
      fp.append(line)
      
  return np.array(fp, dtype=np.int32)