import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def der_alpha(t, alpha, e):
    return (2 * np.pi / (1 - e * e)**1.5) * (1 + e * np.cos(alpha))**2


def alpha_wrt_time(e=0.0, split=1000, first_periastron=0.0):
    t_span = (0.0, 1.0)
    t = np.linspace(0.0, 1.0, split + 1)
    y0 = np.array([0])
    sol = solve_ivp(der_alpha, t_span, y0, t_eval=t, args=(e,))
    alpha_array = sol.y[0]

    # return lambda time : alpha_array[int((time%1) * split)]
    def alphas(time):
        nonlocal split, alpha_array
        time = (time - first_periastron) % 1.0
        n = time * split
        if int(n) < split:
            return alpha_array[int(n)]

    return alphas


if __name__ == '__main__':
    try:
        e = 0.0  # eccentricity
        first_periastron = 0.0  # t/P where t is the time at first periastron
        split = 1000  # time split
        if len(sys.argv) == 2:
            e = float(sys.argv[1])
        elif len(sys.argv) == 3:
            e, first_periastron = float(sys.argv[1]), float(sys.argv[2])
        elif len(sys.argv) == 4:
            e, first_periastron, split = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
        func = alpha_wrt_time(e, split, first_periastron)
    except Exception as e:
        raise NameError('Check the params again!')

    t = np.linspace(0, 1, split + 1)
    alphas = [func(time) for time in t]

    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax1.scatter(t, alphas, s=1)
    ax1.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax1.set_yticks([0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2])
    ax1.set_yticklabels([r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    ax1.set_xlabel(r'$t$')
    ax1.set_ylabel(r'$\alpha$')
    ax1.grid(True)

    ax2.scatter(t, np.sin(alphas), s=1)
    ax2.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax2.set_xlabel(r'$t$')
    ax2.set_ylabel(r'$sin(\alpha)$')
    ax2.grid(True)

    plt.show()
