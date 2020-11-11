import time
import matplotlib as mpl
import warnings
from planet import Planet
from system import System

mpl.use('Agg')
warnings.filterwarnings("ignore")

start = time.time()
p1 = Planet(e=0.0, a=8, omega=0, Omega=0, i=89, r_p=0.1, first_periastron=0.03)
p2 = Planet(e=0.0, a=4, omega=0, Omega=0, i=89, r_p=0.07, first_periastron=0.52)
p3 = Planet(e=0.0, a=2, omega=0, Omega=0, i=87, r_p=0.05, first_periastron=0.0)
sys = System(star_prop={'Mass': 4}, planet_list=[p1, p3, p2], sort=True, model='Quadratic')
end = time.time()
print("Initialize - {:.3f}s".format(end - start))

start = time.time()
sys.plot(normalise=True)
end = time.time()
print("Plot Transit curve - {:.3f}s".format(end - start))

start = time.time()
sys.visualize(time=0.26)
end = time.time()
print("Visualize - {:.3f}s".format(end - start))

start = time.time()
sys.visualize(time=0.27)
end = time.time()
print("Visualize - {:.3f}s".format(end - start))

start = time.time()
sys.visualize(time=0.28)
end = time.time()
print("Visualize - {:.3f}s".format(end - start))
