import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid
import sys

sys.path.append('../')#Make directory above visible to import our custom setup_model
import eos_setup_model

import thermal_history as th
from thermal_history.core_models.leeds.routines import rivoldini_eos as eos

#Load parameters
prm = th.model.Parameters(('500_params.py',))

#Loop over different CMB heat fluxes, compositions
q_cmb_array = [1, 5, 10]        #mW/m^2
S_array     = [0.05, 0.1, 0.15]

#Make directory to store output if not already.
if not os.path.isdir('output'):
   os.mkdir('output')

#Begin loops
for S in S_array:
   prm.conc_l[0] = S  #Set composition

   for q_cmb in q_cmb_array:

      #Name format for output files
      name = f'./output/S={S*100:.0f}_q={q_cmb:.0f}'

      #Setup model
      model = eos_setup_model.setup_model(prm, verbose=True)

      model.mantle.Q_cmb = q_cmb*1e-3 * 4*np.pi*prm.r_cmb**2 #Set constant CMB heat flow

      #Run model, breaking when snow zone covers whole core or non top-down freezing occurs
      #either will cause model.critical_failure = True as it is not defined in the model
      #how proceed in these scenarios

      dt = 1e4*prm.ys
      while not model.critical_failure and model.it < 100000:

         #Write profiles
         model.write_profiles(name+f'_profiles_{model.it}', overwrite=True, verbose=False)

         model.evolve(dt, print_freq=100, verbose=True) #Evolve model 1 timestep, printing progress every 10 steps.

      if not model.critical_failure_reason == 'Snow zone covers whole core':
         name = name+'_FAILED'

      # save model output
      model.save_dict['core']['critical_failure_reason'] = model.critical_failure_reason #Save the reason for critical failure.
      model.write_data(name, overwrite=True)









