#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:28:17 2021

@author: anton
"""
from SLiCAP import *

fileName = 'ExNoiseFigureRp'
makeNetlist(fileName + '.asc', fileName)
i1 = instruction()
i1.setCircuit(fileName + '.cir')

# Create an HTML page will the circuit information

htmlPage('Circuit data')
head2html('Circuit diagram')
img2html(fileName + '.svg', 500)
netlist2html(fileName + '.cir')
elementData2html(i1.circuit)
params2html(i1.circuit)

# Define symbolic noise simulation

i1.setSimType('symbolic')
i1.setGainType('vi')
i1.setDataType('noise')

# Define source and detector

i1.setSource('V1')
i1.setDetector('V_out')

# Execute the instruction

result = i1.execute()

# Calculate the noise figure (from the detector-referred noise)

F_o = sp.simplify(result.onoise/result.onoiseTerms['V1'])

# Calculate the noise figure (from the source-referred noise)

F_i = sp.simplify(result.inoise/result.inoiseTerms['V1'])

# Create an HTML page with the results of the noise analysis

htmlPage('Symbolic noise analysis')
noise2html(result)
head2html('Noise figure')
text2html('The noise figure is obtained as')
eqn2html('F', F_o)
head2html('Detector referred noise spectrum')
text2html('The spectral density of the total output noise equals')
eqn2html('S_out', sp.together(result.onoise))