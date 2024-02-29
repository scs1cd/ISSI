import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid
import sys

sys.path.append('../useful_scripts')#Make useful scripts directory visible to import our custom setup_model
sys.path.append('C:\\Users\\earcd\\Documents\\GitHub\\thermal_history')
import eos_setup_model_float as eos_setup_model

import thermal_history as th
from thermal_history.core_models.leeds.routines import rivoldini_eos as eos

#Include a stable layer?
stable_layer = False  #True or false

#Load parameters
prm = th.model.Parameters(('300_params.py',))
prm.core_melting_params = ['RU', 1265, 11.15e-9, 3e-9, 1500.5, 29.6e-9, 0.247e-18] # Needed for RHS of Eutectic


#Loop over different CMB heat fluxes, compositions
q_cmb_array = [1, 5, 10]        #mW/m^2
S_array     = [0.25, 0.3, 0.35]

#Different timesteps for different heat flows to speed up calculation (yrs).
timesteps   = [5e5, 1e5, 1e4]  

#Make directory to store output if not already.
dir = 'output_float'
if not os.path.isdir(dir):
   os.mkdir(dir)

#Begin loops
for S in S_array:
   prm.conc_l[0] = S  #Set composition

   for q_cmb, _dt in zip(q_cmb_array, timesteps):

      #Name format for output files
      name = f'./output_float/S={S*100:.0f}_q={q_cmb:.0f}'
      if not stable_layer:
         name += '_adiabatic' #Add adiabatic if not using a stable layer

      if stable_layer:
         stable_layer_method='leeds_thermal'
         prm.stable_layer = True
      else:
         stable_layer_method=None
         prm.stable_layer = False

      #Setup model
      print(f'\nIterating S={S*100:.0f}, q={q_cmb:.0f}')
      model = eos_setup_model.setup_model(prm, core_method='solid_FeS', stable_layer_method=stable_layer_method, verbose=False)

      model.mantle.Q_cmb = q_cmb*1e-3 * 4*np.pi*prm.r_cmb**2 #Set constant CMB heat flow

      #Run model, breaking when snow zone covers whole core or non top-down freezing occurs
      #either will cause model.critical_failure = True as it is not defined in the model
      #how proceed in these scenarios

      dt = _dt*prm.ys
      while not model.critical_failure and model.it < (4.5e9*prm.ys/dt):

         if model.it == 1: 
              model.write_profiles(name+f'_profiles_{model.it}', overwrite=True, verbose=False)

         model.evolve(dt, print_freq=100, verbose=True) #Evolve model 1 timestep, printing progress every 10 steps.

      #Reached maximum iterations allowed
      if model.it == (4.5e9*prm.ys/dt):
         model.critical_failure_reason = True
         model.critical_failure_reason = 'Reached maximum iteration (4.5 Gyrs time total)'

      # save model output
      model.save_dict['core']['critical_failure_reason'] = model.critical_failure_reason #Save the reason for critical failure.
      model.write_data(name, overwrite=True)








