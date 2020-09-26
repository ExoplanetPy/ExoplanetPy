import copy
import os
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import scipy
import yaml

dir = os.path.dirname(__file__)

alpha_wrt_time = __import__('alpha(time)').alpha_wrt_time
coord_wrt_alpha = __import__('coord(alpha)').coord_wrt_alpha
initialize_star = __import__('lum(coord)').initialize_star
lum_wrt_coord = __import__('lum(coord)').lum_wrt_coord


class system(object):
    def __init__(self, file_name, time_split=100, img_split=100, n=1.0):
        try:
            params_file = os.path.join(os.path.dirname(__file__), 'params', file_name)
            with open(params_file, 'r') as stream:
                data = yaml.safe_load(stream)
            self.time_split = time_split
            self.img_split = img_split
            self.planets = data['planets']
            self.star_radius = data['star_radius']
            self.star_mass = data['star_mass']
            self.u = data['u']
            period_constant = (2 * np.pi) / ((scipy.constants.G * self.star_mass * 1.989e30)**0.5)
            for planet in self.planets:
                planet['period'] = period_constant * ((planet['semi-major'] * 6.96e8)**1.5) / (36 * 24)  # days
            self.total_time = max([planet['period'] for planet in self.planets])
        except Exception as e:
            raise NameError('Check the params!')

        count = 0
        for planet in self.planets:
            planet['index'] = count
            split = self.time_split * planet['period'] / self.total_time
            planet['alphas'] = alpha_wrt_time(e=planet['eccentricity'], split=int(split),
                                              first_periastron=planet['first_periastron'])
            planet['coord_2d'], planet['coord_3d'] = coord_wrt_alpha(a=planet['semi-major'], e=planet['eccentricity'],
                                                                     i=planet['inclination'], w=planet['periastron_angle'])
            count += 1

        self.star, self.total = initialize_star(limb_func=self.limb_dark, split=img_split)
        self.timespan = np.linspace(0, int(n) * self.total_time, int(n) * self.time_split + 1)

    def output(self):
        lum = []
        for timing in self.timespan:
            update, get_lum, get_star = lum_wrt_coord(copy.deepcopy(self.star), copy.deepcopy(self.total))
            for planet in self.planets:
                x, y = planet['coord_2d'](planet['alphas'](timing / planet['period']))
                if y * (planet['inclination'] - (np.pi / 2)) > 0:  # Only the part of orbit which is away from us
                    continue
                if x**2 + y**2 > 2 * ((1 + planet['planet_radius'])**2):
                    continue

                update(x, y, planet['planet_radius'])
            lum.append(get_lum())
        lum = np.array(lum)
        return lum / max(lum)

    def coords(self):
        time_coord = []
        for timing in self.timespan:
            locs = []
            for planet in self.planets:
                locs.append(planet['coord_3d'](planet['alphas'](timing / planet['period'])))
            time_coord.append(locs)
        return time_coord

    def limb_dark(self, cosine):
        if len(self.u) == 2:
            return 1 - self.u[0] * (1 - cosine) - self.u[1] * ((1 - cosine)**2)
        else:
            raise NameError('Check the u values')


if __name__ == '__main__':
    start = time.time()
    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Start'))

    params_file = '1.yaml'
    if len(sys.argv) > 1:
        params_file = sys.argv[1]

    n = 2.0
    exoplanets = system(params_file, time_split=10000, img_split=100, n=n)
    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Initialized the Exoplanets system'))
    lum = exoplanets.output()

    fig = plt.figure(figsize=(20, 12))
    ax = fig.add_subplot(111)
    ax.scatter(exoplanets.timespan / 100, lum, s=1, c='b')
    ax.set_xlim(0, max(exoplanets.timespan) / 100)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xlabel('Time in days', fontsize=18)
    ax.set_ylabel('Relative luminosity', fontsize=18)
    ax.set_title('Multiple Exoplanets - {} Planet system'.format(len(exoplanets.planets)), fontsize=22)
    ax.grid(True)

    plt.show()
    print('Time : {} seconds; {}'.format(round(time.time() - start, 2), 'Made the plots'))
