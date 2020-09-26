import sys

import math
import matplotlib.patches as patch
import matplotlib.pyplot as plt
import numpy as np


def coord_wrt_alpha(a, e, i, w):
    if a * (1 - e) <= 1.0:
        raise NameError('The planet enter the star, check the params!')

    w *= np.pi / 180
    i *= np.pi / 180

    def xy(alpha):
        nonlocal a, e, i, w
        angle = alpha + w
        r = a * (1 - e**2) / (1 + e * np.cos(alpha))
        x = r * np.cos(angle)
        y = r * np.sin(angle) * np.cos(i)
        return x, y

    def xyz(alpha):
        nonlocal a, e, i, w
        angle = alpha + w
        r = a * (1 - e**2) / (1 + e * np.cos(alpha))
        x = r * np.cos(angle)
        y = r * np.sin(angle) * np.cos(i)
        z = r * np.sin(angle) * np.sin(i)
        return x, y, z

    return xy, xyz


if __name__ == '__main__':
    a = 4.0  # in terms of Rs
    e = 0.4
    i = 0  # deg
    w = 0  # deg
    if len(sys.argv) == 2:
        a = float(sys.argv[1])
    elif len(sys.argv) == 3:
        a, e = float(sys.argv[1]), float(sys.argv[2])
    elif len(sys.argv) == 4:
        a, e, i = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    elif len(sys.argv) == 5:
        a, e, i, w = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])

    loc_2d, loc_3d = coord_wrt_alpha(a, e, i, w)

    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(111)
    # ax2 = fig.add_subplot(122, projection='3d')

    for x in range(360):
        alpha = x * (np.pi / 180)
        x, y, z = loc_3d(alpha)
        if x**2 + y**2 < 1.0:
            if z > 0:
                ax1.scatter(x, y, c='g', s=1, zorder=15)
            else:
                ax1.scatter(x, y, c='g', s=1, zorder=5)
        else:
            ax1.scatter(x, y, c='k', s=1, zorder=15)

    ylim = ax1.get_ylim()
    xlim = ax1.get_xlim()
    lim = max(abs(xlim[0]), abs(ylim[0]), abs(xlim[1]), abs(ylim[1]))
    ax1.set_xlim(-lim, lim)
    ax1.set_ylim(-lim, lim)
    ax1.set_xlabel(r'$x$')
    ax1.set_ylabel(r'$y$')
    ax1.set_xticks(np.arange(-math.ceil(lim), math.ceil(lim) + 1, 1.0))
    ax1.set_yticks(np.arange(-math.ceil(lim), math.ceil(lim) + 1, 1.0))

    c = patch.Circle((0, 0), 1.0, zorder=10, color='r', fill=True)
    ax1.add_patch(c)

    # for x in range(360):
    #     alpha = x * (np.pi / 180)
    #     x, y, z = loc_3d(alpha)
    #     ax2.scatter(x, y, z, s=1, c='k')
    #
    # ax2.set_xlim(-2 * a, 2 * a)
    # ax2.set_ylim(-2 * a, 2 * a)
    # ax2.set_zlim(-2 * a, 2 * a)
    # ax2.view_init(45, 45)

    ax1.set_title(r'$a={},\ e={},\ i={},\ w={}$'.format(a, e, i, w))
    ax1.grid(True)

    plt.show()
