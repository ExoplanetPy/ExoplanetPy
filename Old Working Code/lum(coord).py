import copy
import random
import time

import matplotlib.pyplot as plt
import numpy as np


def limb_dark_two_params(cosine):
    u = [0.1, 0.2]
    return 1 - u[0] * (1 - cosine) - u[1] * ((1 - cosine)**2)


def initialize_star(limb_func, split=1000):
    star = np.zeros((2 * split + 1, 2 * split + 1))
    total = 0
    for i in range(-split, split + 1):
        rg_j = abs(int((split**2 - i**2)**0.5))
        for j in range(-rg_j, rg_j + 1):
            x = (i) / split
            y = (j) / split
            cosine = abs((1 - x**2 - y**2)**0.5)
            lum = limb_func(cosine)
            total += lum
            star[split + i][split + j] = lum

    return star, total


def lum_wrt_coord(img, tot):
    split = int((len(img) - 1) / 2)

    def shadow(coord_x, coord_y, R_p):
        nonlocal img, tot
        x, y, Rp = int(coord_x * split), int(coord_y * split), int(R_p * split)
        for i in range(-Rp, Rp + 1):
            if y - i >= -split and y - i <= split:
                rg_j = abs(int((Rp**2 - i**2)**0.5))
                for j in range(-rg_j, rg_j + 1):
                    if x + j >= -split and x + j <= split:
                        m = split - y + i
                        n = split + x + j
                        lum = img[m][n]
                        tot = tot - lum
                        img[m][n] = 0

    def lum():
        nonlocal tot
        return tot

    def star():
        nonlocal img
        return img

    return shadow, lum, star


if __name__ == '__main__':
    start = time.time()
    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Start'))
    split = 1000
    star, total = initialize_star(limb_dark_two_params, split)
    print(total)

    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Initialized Star'))
    fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(10, 20))
    fig.tight_layout(pad=5.0)
    update, get_total, get_star = lum_wrt_coord(copy.deepcopy(star), copy.deepcopy(total))

    for i in range(4):
        for j in range(4):
            x = random.randint(-99, 99)
            y = random.randint(-99, 99)
            Rp = random.randint(0, 20)

            update(x / 100, y / 100, Rp / 100)
            ax[i][j].imshow(get_star(), 'gray')
            ax[i][j].set_title('{}, {}, {} : {}'.format(x, y, Rp, get_total()))

    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Made the plots'))
    plt.show()

    start = time.time()
    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Start'))
    split = 1000
    star, total = initialize_star(limb_dark_two_params, split)
    print(total)

    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Initialized Star'))
    update, get_total, _ = lum_wrt_coord(copy.deepcopy(star), copy.deepcopy(total))

    for i in range(4):
        for j in range(4):
            x = random.randint(-99, 99)
            y = random.randint(-99, 99)
            Rp = random.randint(0, 20)

            update(x / 100, y / 100, Rp / 100)

    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Completed calculation'))
