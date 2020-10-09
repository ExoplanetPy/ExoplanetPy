# import sys

# import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


class Planet:
    def __init__(self, e=0.0, a=0.0, omega=0.0, Omega=0.0, i=0.0, r_p=0.0, first_periastron=0):
        self.e = e  # eccentricity
        self.a = a  # semi major axis
        self.omega = omega  # argument of periapsis
        self.Omega = Omega  # longitude of ascending node
        self.i = i * (np.pi) / 180  # inclination
        self.r_p = r_p  # planet radius
        self.first_periastron = first_periastron  # time origin, perhaps keep as a datetime object?
        self.alphas = self.alpha_wrt_time(e=self.e, split=1000, first_periastron=self.first_periastron)

    def der_alpha(self, t, alpha, e):
        return (2 * np.pi / (1 - e * e)**1.5) * (1 + e * np.cos(alpha))**2

    def alpha_wrt_time(self, e=0.0, split=1000, first_periastron=0.0):
        split = int(split)
        t_span = (0.0, 1.0)
        t = np.linspace(0.0, 1.0, split + 1)
        y0 = np.array([0])
        sol = solve_ivp(self.der_alpha, t_span, y0, t_eval=t, args=(e,))
        alpha_array = sol.y[0]
        # return lambda time : alpha_array[int((time%1) * split)]

        def alphas(time):
            nonlocal split, alpha_array
            time = (time - first_periastron) % 1.0
            n = time * split
            if int(n) < split:
                return alpha_array[int(n)]

        return alphas

    def getOrbitalElements(self):  # returns dictionary of Kepler Orbital elements (everything above except radius and first_periastron)
        return {'Eccentricity': self.e,
                'Semi Major Axis': self.a,
                'Argument of Periapsis': self.omega,
                'Longitude of Ascending Node': self.Omega,
                'Inclination': self.i}

    def getNu_from_time(self, time):  # returns true anomaly when time is inputted
        # use solutions of differential equation
        return self.alphas(time)

    def getPosition_from_nu(self, nu):  # returns position when true anomaly is inputted
        # n_x = -np.cos(self.i) * np.cos(self.Omega) * np.sin(self.omega + nu) - np.sin(self.Omega) * np.cos(self.omega + nu)
        # n_y = np.cos(self.Omega) * np.cos(self.omega + nu) - np.cos(self.i) * np.sin(self.Omega) * np.sin(self.omega + nu)
        # n_z = np.sin(self.i) * np.sin(self.omega + nu)
        angle = nu + self.omega
        n_x = np.cos(angle)
        n_y = np.sin(angle) * np.cos(self.i)
        n_z = np.sin(angle) * np.sin(self.i)

        unit_vector = np.array([n_x, n_y, n_z])

        r = self.a * (1 - self.e**2) / (1 + self.e * np.cos(nu))

        position = np.array([r * unit_vector[0], r * unit_vector[1], r * unit_vector[2]])
        return position

    def getPosition(self, time):  # returns position when time is inputted (just combining the above two functions)
        return self.getPosition_from_nu(self.getNu_from_time(time))

    def setPeriod(self, period):
        self.period = period  # To be calculated in System

    def setSplit(self, split):
        self.alphas = self.alpha_wrt_time(e=self.e, split=split, first_periastron=self.first_periastron)
