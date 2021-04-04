# SLiCAP for Python Setup and instal

SLiCAP is **open source** and can be viewed fom https://www.analog-electronics.eu/slicap/slicap.html

## What it is
- SLiCAP is an acronym for: **S** ymbolic **Li** near **C** ircuit **A** nalysis **P** rogram
- SliCAP is a tool for **algorithm-based analog design automation**
- SLiCAP is intended for setting up and solving **design equations** of electronic circuits
- SLiCAP is a an **open source** application written in Python and maxima CAS
- SLiCAP is part of the tool set for teaching 'Structured Electronic Design' at the Delft University of Technology

## Setting up SLiCAP
To set up SLiCAP, the following components are required:
- A Python 3 install -  Dependencies of packages is found in requirements.txt
- Maxima CAS
- SLiCAP can generate netlists from schematics made with:
  - LTspice
  - gschem
  - lepton-eda

The dependencies are listed in the 'requirements.txt' file.
When installing SLiCAP on an Anaconda distribution, it requires installing the 'in-place' module, which can be installed using the 'python -m pip install in-place'.
SLiCAP can be installed by running 'python setup.py install' or 'python setup.py install --user'. 

## First Run
To verify setting up of SLiCAP has been done correctly, it is possible to run one of the example projects that are in the examples/ directory. 
Here either jupyter notebooks or the python file with the name of the example can be ran.
Please take care to verify that the paths in the SLiCAPconfig.py of the example project are set correctly.

## Full Documentation
The full documentation can be found in the doc/_build/ directory, this can be rebuilt with Sphinx given that all dependencies are installed (such as the sphinx-rtd-theme).
In addition to the reference of functions, the documentation also contains elaborate information on the syntax that is to be used including examples.

## Contributing
This github page is to be used for contributing to SLiCAP.

### Adding features
Features should be added through pull requests and pass all checks that have been set up on the github page.
These tests include:
* Functional python tests
* Style tests verified using a linter

### Bugs
In case bugs are found, please report them to the 'Issues' page where we can resolve the issues and keep track of any possible bugs.

[![Build Status](https://travis-ci.org/Lenty/SLiCAP_python.svg?branch=master)](https://travis-ci.org/Lenty/SLiCAP_python)
