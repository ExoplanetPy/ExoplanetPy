# ExoplanetPy 

ExoplanetPy is a python package for modelling the transit light curves of systems with multiple exoplanets orbiting around their host stars.
To obtain transit curves, set up the Keplerian orbital elements for each planet in the system.
![](https://raw.githubusercontent.com/ExoplanetPy/ExoplanetPy/master/images/logo_400.png "ExoplanetPy logo")

The `Planet()` class handles each planet's orbital elements, and the `System()` class can be used to plot the final transit curves.

The following orbital elements are set up:
- **e**: eccentricity 
- **a**: semi-major axis 
- **omega**: argument of periapsis (ω) 
- **Omega**: longitude of ascending node (Ω) 
- **i**: orbital inclination 
- **r_p**: planet:star radius 

Each `Planet()` can have different initial true anomaly (ν) values, varied by the `first_periastron` time argument.

## Installation
Installation is recommended via pip for Python 3.
```python
pip install exoplanetpy
```
The package can then be imported using:
```python
import ExoplanetPy
```

## Usage
Access the modules using the following statements.
```python
from ExoplanetPy import Planet
from ExoplanetPy import System
```
### Transit Curves
Define a single `Planet()` and input as `planet_list` argument in `System()`.  
Limb darkening models are chosen in the `plot()` method.
```python
p1 = Planet(e=0.0, a=8, omega=0, Omega=0, i=89.9, r_p=0.1, first_periastron=0.0)
sys = System(star_prop={'Mass': 4}, planet_list=[p1], sort=True)
sys.plot(model='Quadratic', normalise=True)
```
![](https://raw.githubusercontent.com/ExoplanetPy/ExoplanetPy/master/ExoplanetPy/test_plots/test_plot_1.png "Test Plot 1")

Additional `Planet()` objects are inputted as `planet_list` argument in `System()`.
```python
p1 = Planet(e=0.0, a=8, omega=0, Omega=0, i=89.9, r_p=0.1, first_periastron=0.0)
p2 = Planet(e=0.0, a=2, omega=0, Omega=0, i=89.9, r_p=0.05, first_periastron=0.0)
sys = System(star_prop={'Mass': 4}, planet_list=[p1,p2], sort=True)
sys.plot(model='Quadratic', normalise=True)
```
![](https://raw.githubusercontent.com/ExoplanetPy/ExoplanetPy/master/ExoplanetPy/test_plots/testv0_plot.png "Test Plot 2")

### Direct Imaging
Take the following planetary system:
```python
p1 = Planet(e=0.0, a=8, omega=0, Omega=0, i=89, r_p=0.1, first_periastron=0.03)
p2 = Planet(e=0.0, a=4, omega=0, Omega=0, i=89, r_p=0.07, first_periastron=0.52)
p3 = Planet(e=0.0, a=2, omega=0, Omega=0, i=87, r_p=0.05, first_periastron=0.0)
sys = System(star_prop={'Mass': 4}, planet_list=[p1, p3, p2], sort=True)
```
The `visualize()` method allows the user to obtain visual images of the actual transit.
```python
sys.visualize(time=0.26, model='Quadratic')
```
![](https://raw.githubusercontent.com/ExoplanetPy/ExoplanetPy/master/ExoplanetPy/test_plots/visualize-0.26.png ".visualize(0.26)")

Changing the fractional time parameter allows the user to obtain images at any point during transit. 
```python
sys.visualize(time=0.27, model='Quadratic')
```
![](https://raw.githubusercontent.com/ExoplanetPy/ExoplanetPy/master/ExoplanetPy/test_plots/visualize-0.27.png ".visualize(0.27)")

Similarly, for `time = 0.28`:
```python
sys.visualize(time=0.28, model='Quadratic')
```
![](https://raw.githubusercontent.com/ExoplanetPy/ExoplanetPy/master/ExoplanetPy/test_plots/visualize-0.28.png ".visualize(0.28)")

## Dependencies
ExoplanetPy has the following dependencies:
* [NumPy](https://numpy.org/)
* [SciPy](https://www.scipy.org/)
* [Matplotlib](https://matplotlib.org/)  (produce plots)
* [Seaborn](https://seaborn.pydata.org/) (stylize plots)

## License 
MIT License  
© 2020 ExoplanetPy
