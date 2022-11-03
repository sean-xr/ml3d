"""SDF to Occupancy Grid"""
import numpy as np


def occupancy_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An occupancy grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with value 0 outside the shape and 1 inside.
    """

    # ###############
    # TODO: Implement
    x_ = np.linspace(-0.50, 0.50, resolution).astype(np.float32)
    y_ = np.linspace(-0.50, 0.50, resolution).astype(np.float32)
    z_ = np.linspace(-0.50, 0.50, resolution).astype(np.float32)

    x, y, z = np.meshgrid(x_, y_, z_, indexing='ij')

    assert np.all(x[:, 0, 0] == x_)
    assert np.all(y[0, :, 0] == y_)
    assert np.all(z[0, 0, :] == z_)
    sdf_value = sdf_function(x.flatten(), y.flatten(), z.flatten())
    sdf_grid = sdf_value.reshape(resolution, resolution, resolution)
    #zero_grid = np.maximum(sdf_grid,0)
    occupancy_grid = np.where(sdf_grid > 0, 0, 1)
    return occupancy_grid
    raise NotImplementedError
    # ###############
