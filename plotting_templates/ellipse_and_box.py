from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = x_limits[1] - x_limits[0]; x_mean = np.mean(x_limits)
    y_range = y_limits[1] - y_limits[0]; y_mean = np.mean(y_limits)
    z_range = z_limits[1] - z_limits[0]; z_mean = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_mean - plot_radius, x_mean + plot_radius])
    ax.set_ylim3d([y_mean - plot_radius, y_mean + plot_radius])
    ax.set_zlim3d([z_mean - plot_radius, z_mean + plot_radius])

# Ellipsoid
def ellipsoid(rad_x=10, rad_y=10, rad_z=10):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = rad_x * np.outer(np.cos(u), np.sin(v))
    y = rad_y * np.outer(np.sin(u), np.sin(v))
    z = rad_z * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

def cylinder(rad=1, length=4):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = rad * np.outer(np.cos(u), np.sin(v))
    y = rad * np.outer(np.sin(u), np.sin(v))
    z = length * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

# Box
def box(length=1, width=1, height=1):
    u = np.linspace(0, 1, 2)
    x, y = np.meshgrid(u, u)
    x *= length
    y *= width

    ax.plot_surface(x, y, 0*x + height,  rstride=4, cstride=4, color='b')
    ax.plot_surface(x*0 + height, y, x,  rstride=4, cstride=4, color='b')
    ax.plot_surface(x, 0*y + height, y * height / width,  rstride=4, cstride=4, color='b')
    ax.plot_surface(x, y, 0*x,  rstride=4, cstride=4, color='b')
    ax.plot_surface(0*x, y, x * height / length,  rstride=4, cstride=4, color='b')
    ax.plot_surface(x, 0*x, y * height / width,  rstride=4, cstride=4, color='b')

#ellipsoid(10,20,10)
cylinder()
#box(5,10,5)
ax.set_aspect('equal')
set_axes_equal(ax)
ax.set_axis_off()
plt.show()
