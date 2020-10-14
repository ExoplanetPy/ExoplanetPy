from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ExoplanetPy',
    version='0.0.3',
    description='Package for Multiple exoplanet system modelling',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ExoplanetPy/ExoplanetPy',
    author='Arnav Das & Devansh Jain',
    author_email='arnav257@gmail.com',
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3 :: Only",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Scientific/Engineering :: Astronomy",
                 "Topic :: Scientific/Engineering :: Visualization"],
    keywords='exoplanets, orbits, visualize, astronomy',
    packages=['ExoplanetPy'],
    python_requires='>=3.5, <4',
    install_requires=['numpy', 'matplotlib', 'scipy', 'seaborn'],
)
