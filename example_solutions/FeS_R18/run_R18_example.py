import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid
import sys

sys.path.append('C:\\Users\\earcd\\Documents\\GitHub\\ISSI\\meeting_solutions\\useful_scripts') #Make useful scripts directory visible to import our custom setup_model
sys.path.append('C:\\Users\\earcd\\Documents\\GitHub\\thermal_history')
import eos_setup_model

import thermal_history as th
from thermal_history.core_models.leeds.routines import rivoldini_eos as eos

#Include a stable layer?
stable_layer = False  #True or false

if stable_layer:
    stable_layer_method='leeds_thermal'
else:
    stable_layer_method=None

#Load parameters
prm = th.model.Parameters(('R18_params.py',))

#Ruckriemen melting parameters
prm.core_melting_params = np.array(['RU', 1265, 11.15e-9, 3e-9, 1500.5, 29.6e-9, 0.247e-18])

model = th.model.setup_model(prm, core_method='solid_FeS', verbose=False)
#model = th.model.setup_model(prm, core_method='solid_FeS', stable_layer_method=stable_layer_method, verbose=False)

#Run model, breaking when snow zone covers whole core or non top-down freezing occurs
#either will cause model.critical_failure = True as it is not defined in the model
#how proceed in these scenarios

dt = 1e6*prm.ys
for i in range(4500):

   t = model.time / (1e6*prm.ys)
   heat_flux = 3 + 40 * np.exp(-t/100)  #Approximate Tina's results (mW/m^2)
   model.mantle.Q_cmb = (heat_flux/1000) * 4*np.pi*prm.r_cmb**2
   

   model.evolve(dt, print_freq=100, verbose=True)

# save model output
model.write_data('output', overwrite=True)


