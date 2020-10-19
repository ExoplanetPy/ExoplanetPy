from planet import Planet
from system import System

p1 = Planet(e=0.0, a=8, omega=0, Omega=0, i=89, r_p=0.1, first_periastron=0.03)
p2 = Planet(e=0.0, a=4, omega=0, Omega=0, i=89, r_p=0.07, first_periastron=0.52)
p3 = Planet(e=0.0, a=2, omega=0, Omega=0, i=87, r_p=0.05, first_periastron=0.0)
sys = System(star_prop={'Mass': 4}, planet_list=[p1, p3, p2], sort=True)
sys.plot(model='Quadratic', normalise=True)
sys.visualize(time=0.26, model='Quadratic')
sys.visualize(time=0.27, model='Quadratic')
sys.visualize(time=0.28, model='Quadratic')
