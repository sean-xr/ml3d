"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    # TODO: Implement
    areas = []  #create an empty list to hold the areas
    sampled_points = []
    # for every face, calculate the area of that face:
    for face in faces:
        [p_1, p_2, p_3] = vertices[face]
        vector_1 = p_2 - p_1
        vector_2 = p_3 - p_1
        area = 0.5 * np.linalg.norm(np.cross(vector_1, vector_2), ord=1)
        areas.append(area)
    # areas is a list f scalars, we should convert it into np.array
    areas = np.array(areas)
    # normalization to 1 ==> each element of areas become possibilities
    prob = areas / areas.sum(axis=0)
    # randomly pick n_points with prob. of p with the index
    weighted_index = np.random.choice(range(len(areas)), p=prob, size=n_points) #这里是weighted sampling
    for sampled_face_index in weighted_index:
        #usbstracting the vertex of each face
        [A, B, C] = vertices[faces[sampled_face_index]]
        # using the equation given in ipynb
        r_1 = np.random.rand()
        r_2 = np.random.rand()
        u = 1 - np.sqrt(r_1)
        v = np.sqrt(r_1) * (1 - r_2)
        w = np.sqrt(r_1) * r_2
        sampled_point = u * A + v * B + w * C
        sampled_points.append(sampled_point)
    sampled_points = np.asarray(sampled_points)
    return sampled_points
    raise NotImplementedError
    # ###############
