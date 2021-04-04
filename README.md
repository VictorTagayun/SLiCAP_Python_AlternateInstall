# Alternate Option to install SLiCAP for Python using Python Portable

SLiCAP is **open source** and can be viewed fom https://www.analog-electronics.eu/slicap/slicap.html

## What it is
- SLiCAP is an acronym for: **S** ymbolic **Li** near **C** ircuit **A** nalysis **P** rogram
- SliCAP is a tool for **algorithm-based analog design automation**
- SLiCAP is intended for setting up and solving **design equations** of electronic circuits
- SLiCAP is a an **open source** application written in Python and maxima CAS
- SLiCAP is part of the tool set for teaching 'Structured Electronic Design' at the Delft University of Technology

## Setting up SLiCAP
To set up SLiCAP, the following components are required:
- (Step 3) A Python 3 (portable) install -  Dependencies of packages is found in requirements.txt
- (Step 2) Maxima CAS
- (Step 1) SLiCAP can generate netlists from schematics made with:
  - LTspice
  - gschem
  - lepton-eda

The dependencies are listed in the 'requirements.txt' file.
When installing SLiCAP on an Anaconda distribution, it requires installing the 'in-place' module, which can be installed using the 'python -m pip install in-place'.
SLiCAP can be installed by running 'python setup.py install' or 'python setup.py install --user'. 


### Step 1 - Download and Install LTspice

- Go to https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html and install LTSpice


### Step 2 - Download and Install Maxima CAS

1. Go to https://sourceforge.net/projects/maxima/files/Maxima-Windows/  
2. Choose **"5.44.0-Windows"**
3. Install, by default it will be at **"C:\maxima-5.44.0"**


### Step 3 - Download SLiCAP

1. Download SLiCAP from github https://github.com/Lenty/SLiCAP_python and click the download button  
![download](https://github.com/VictorTagayun/SLiCAP_Python_AlternateInstall/blob/main/images/download.png)  
2. Unzip to your preferred location and preferrable rename the unzippped folder from _SLiCAP_python-master_ to **SLiCAP_python**


### Step 4 - Download Python Portable

1. Go to https://winpython.github.io/
2. Download your preferred version but include the version with **Spyder**, i.e. **WinPython64-3.9.2.0, WinPython64-3.9.2.0cod or WinPython64-3.8.8.0**.
3. After download, right click the exe file and choose unzip.


### Step 5 - Instal SliCAP

1. Before you install **SliCAP**, download **_in_place_** module first
2. Go to https://raw.githubusercontent.com/jwodder/inplace/master/src/in_place.py and save the file inside SliCAP folder where **"setup.py"** is located, it should be inside "SLiCAP\SLiCAP_python". Make sure **"setup.py"** and **"in_place.py"** are in the same folder. Make sure the file is not **"in_place.py.txt"**, if so, just rename to **"in_place.py"**.
3. In your PC, go to where the Python portable is located **"..\Winpython64-3.9.2.0cod\WPy64-3920"**. Run **"WinPython Command Prompt.exe"**, a commmand prompt will show.
4. In the command prompt, go to the folder where "downloaded" SLiCAP is located, you may need to issue a comand **"cd"** to change directory.
5. Run this command  

	```
	python setup.py install --user  
	```
	
6. When asked for the location of **Maxima CAS** bat file, type _"C:\maxima-5.44.0\bin\maxima.bat"_.
7. It should find LTSpice after, just press enter to accept the default answer.
8. By this time, SLiCAP should be already installed in **"C:\Users\\<user name>\SLiCAP"**.
9. You may now exit this command prompt by typing **"exit"**.


### Step 6 - Run Examples

1. In your PC, go to where the Python is located, **"..\Winpython64-3.9.2.0cod\WPy64-3920"**.
2. Run **"Spyder.exe"**.
3. Locate where the examples are **"C:\Users\"username"\SLiCAP\examples"**.
4. Run and display the plot


## Simulation Results

- You can go to [Simulation Result/s](https://victortagayun.github.io/SLiCAP_Python_AlternateInstall/) to see some results

[Disclaimer](https://github.com/VictorTagayun/GlobalDisclaimer)