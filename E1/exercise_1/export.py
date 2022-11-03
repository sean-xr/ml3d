"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """
    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    # TODO: Implement
    with open(path, 'w') as f:
        for vertex in vertices:
            line = ("v %.1f %.1f %.1f\n" % (vertex[0], vertex[1], vertex[2]))
            f.write(line)
        for face in faces:
            line = ("f %d %d %d\n" % (face[0] + 1, face[1] + 1, face[2] + 1))
            f.write(line)
    #raise NotImplementedError
    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    # TODO: Implement
    with open(path, 'w') as f:
        for sampled_point in pointcloud:
            line = ("v %.1f %.1f %.1f\n" % (sampled_point[0], sampled_point[1], sampled_point[2]))
            f.write(line)
    #raise NotImplementedError
    # ###############
