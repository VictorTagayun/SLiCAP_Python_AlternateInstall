# Alternate Option to install SLiCAP for Python using WinPython. a portable Python

SLiCAP is **open source** and can be viewed fom https://www.analog-electronics.eu/slicap/slicap.html

## What it is
- SLiCAP is an acronym for: **S** ymbolic **Li** near **C** ircuit **A** nalysis **P** rogram
- SliCAP is a tool for **algorithm-based analog design automation**
- SLiCAP is intended for setting up and solving **design equations** of electronic circuits
- SLiCAP is a an **open source** application written in Python and maxima CAS
- SLiCAP is part of the tool set for teaching 'Structured Electronic Design' at the Delft University of Technology

## Setting up SLiCAP
To set up SLiCAP, the following components are required:
- (Steps 3 - 5) A Python 3 (portable) install -  Dependencies of packages is found in requirements.txt
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
2. Choose the latest version, at of this writing it is **"5.46.0-Windows"**
3. Install, by default it will be at **"C:\maxima-5.46.0"**


### Step 3 - Download SLiCAP

1. Download SLiCAP from github https://github.com/Lenty/SLiCAP_python and click the download button  
![download](https://github.com/VictorTagayun/SLiCAP_Python_AlternateInstall/blob/main/images/download.png)  
2. Unzip to your preferred location and preferrably rename the unzippped folder from _SLiCAP_python-master_ to **SLiCAP_python**


### Step 4 - Download Winpython, a Python portable

1. Go to https://winpython.github.io/
2. Download your preferred version but include the version with **Spyder**, i.e. **WinPython64-3.10.5.0, WinPython64-3.9.2.0, WinPython64-3.9.2.0cod or WinPython64-3.8.8.0**.
3. After download, right click the exe file and choose unzip.


### Step 5 - Instal SliCAP and its *dependencies*   

1. Before you install **SliCAP**, download **_in_place_** module first
2. Go to https://raw.githubusercontent.com/jwodder/inplace/master/src/in_place.py , right click the "In-place file processing" and choose "Save as". Save the file inside SLiCAP_python folder where **"setup.py"** is located, it should be inside "SLiCAP_python". Make sure **"setup.py"** and **"in_place.py"** are in the same folder. Make sure the file is not **"in_place.py.txt"**, if so, just rename to **"in_place.py"**.
3. In your PC, go to where the Python portable is located **"..\Winpython64-3.10.5.0\WPy64-31050\"**. Run **"WinPython Command Prompt.exe"**, a commmand prompt will show.
4. In the command prompt, go to the folder where "SLiCAP_python" is located, you may need to issue a comand **"cd (directory where SLiCAP_python is located)"** to change to that directory.
5. Install dependencies in **"requirements.txt"**, run this command   
	```
	pip install -r requirements.txt  
	```
5. Set-up and install **SliCAP**, run this command  

	```
	python setup.py install --user  
	```
	
6. When asked for the location of **Maxima CAS** bat file, type _"C:\maxima-5.46.0\bin\maxima.bat"_.
7. It should find LTSpice after, just press enter to accept the default answer.
8. It will ask you for the location of SliCAP install folder, you may press enter for the default location.
9. By this time, SLiCAP should be already installed in **"C:\Users\ (user name)\SLiCAP"**.
10. You may now exit this command prompt by typing **"exit"**.


### Step 6 - Run Examples

1. In your PC, go to where the Python is located, **"..\Winpython64-3.10.5.0\WPy64-31050"**.
2. Run **"Spyder.exe"**.
3. Locate where the examples are **"C:\Users\ (username)\SLiCAP\examples"**.
4. Run and display the plot


### Setup LTSpice

- Go to https://www.analog-electronics.eu/slicap/SLiCAP_python/docs/html/userguide/install.html#ltspice to setup LTSpice for SliCAP


## Simulation Results

- You can go to [Simulation Result/s](https://victortagayun.github.io/SLiCAP_Python_AlternateInstall/) to see some results

[Disclaimer](https://github.com/VictorTagayun/GlobalDisclaimer)
