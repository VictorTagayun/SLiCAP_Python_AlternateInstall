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
- (Step 3) A Python 3 install -  Dependencies of packages is found in requirements.txt
- (Step 2) Maxima CAS
- (Step 1) SLiCAP can generate netlists from schematics made with:
  - LTspice
  - gschem
  - lepton-eda

The dependencies are listed in the 'requirements.txt' file.
When installing SLiCAP on an Anaconda distribution, it requires installing the 'in-place' module, which can be installed using the 'python -m pip install in-place'.
SLiCAP can be installed by running 'python setup.py install' or 'python setup.py install --user'. 

### Step 1 - Download and Install LTspice

Go to https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html and install LTSpice


### Step 2 - Download and Install Maxima CAS

Go to https://sourceforge.net/projects/maxima/files/Maxima-Windows/  

Choose "5.44.0-Windows"

Install, by default it will be **C:\maxima-5.44.0**

