'''Prints selected output from the .pik model files into an ASCII file for use outside of python
Set the filename to one of the .pik files and 3 .txt files will be generated. The first contains
selected outputs e.g. time, CMB temperature, snow zone radius etc. The second contains the input
parameters used to generate the .pik file. The final file contains the radial profiles for the
last iteration of the model ('present day').

the thermal_history python code is not needed for this script, just pickle (usually included with
all python distributions) and numpy.
'''

import pickle
import numpy as np

file = '../500km/output/S=10_q=10.pik'

#Read data
data = pickle.load(open(file,'rb'))

core = data['core']
prof = core['profiles']
prm  = data['parameters']


#Write output

#ALL SI UNITS
#model iteration, time , snow zone radius, mass fraction in the convecting region, CMB temperature,
#Temperature at r=0, cooling rate at r=0, stable layer radius, Ohmic dissipation, CMB heat flow, ratio of CMB heat flow/ adiabatic heat flow
keys = ['it', 'time', 'r_snow', 'conc_l', 'T_cmb', 'Tcen', 'dT_dt', 'rs', 'Ej', 'Q_cmb', 'ADR']

arrays = []
for key in keys:
    arrays.append(core[key])
arrays = tuple(arrays)

np.savetxt('output.txt', np.column_stack(arrays), delimiter='\t', header='\t'.join(keys), fmt='%.6e')


#Write parameters
with open('parameters.txt','w') as f:

    for key in prm.keys():
        f.write(f'{key} = {prm[key]}\n')


#Write profiles
arrays = []
for key in prof.keys():
    arrays.append(prof[key])
arrays = tuple(arrays)

np.savetxt('profiles.txt', np.column_stack(arrays), delimiter='\t', header='\t'.join(prof.keys()), fmt='%.6e')