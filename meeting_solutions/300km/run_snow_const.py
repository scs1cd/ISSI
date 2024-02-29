import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid
import sys

sys.path.append('C:\\Users\\earcd\\Documents\\GitHub\\thermal_history')
sys.path.append('../useful_scripts')#Make useful scripts directory visible to import our custom setup_model
import eos_setup_model_snow as eos_setup_model
import thermal_history as th

#Include a stable layer?
stable_layer = False  #True or false

#Load parameters
prm = th.model.Parameters(('300_params.py',))

#Loop over different CMB heat fluxes, compositions
q_cmb_array = [1, 5, 10]        #mW/m^2
S_array     = [0.05, 0.1, 0.15]

#Different timesteps for different heat flows to speed up calculation (yrs).
timesteps = [5e5, 1e5, 1e4]  

#Make directory to store output if not already.
if not os.path.isdir('output_snow_const'):
   os.mkdir('output_snow_const')

#Begin loops
for S in S_array:
   prm.conc_l[0] = S  #Set composition

   for q_cmb, _dt in zip(q_cmb_array, timesteps):

      #Name format for output files
      name = f'./output_snow_const/S={S*100:.0f}_q={q_cmb:.0f}'
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
      model = eos_setup_model.setup_model(prm, core_method='leeds', stable_layer_method=stable_layer_method, verbose=False)
      
      # From C:\Users\earcd\Documents\GitHub\ISSI\meeting_solutions\plots\scaling_plots_snow_adiabatic\300km
      prm.core_cp_params             = [752.30301587]
      prm.core_alpha_T_params        = [7.00227877e-05]
      prm.core_liquid_density_params = [6832.773584]
      prm.entropy_melting_params     = [1.46785937514748E-23]
      prm.core_solid_density_params  = [7688.779267]
      prm.alpha_c                    = [1.42076925625963]
      prm.core_conductivity_params   = [28.5765653922255]
      
      model = th.model.setup_model(prm, core_method='leeds', stable_layer_method=stable_layer_method, verbose=False)

      model.mantle.Q_cmb = q_cmb*1e-3 * 4*np.pi*prm.r_cmb**2 #Set constant CMB heat flow
      
      # CD NEED TO CHECK QCMB > QA!!!

      #Run model, breaking when snow zone covers whole core or non top-down freezing occurs
      #either will cause model.critical_failure = True as it is not defined in the model
      #how proceed in these scenarios

      dt = _dt*prm.ys
      while not model.critical_failure and model.it < (4.5e9*prm.ys/dt):

         #Write profiles Takes up lots of space! lots of files!
         #if np.mod(model.it, 10) == 0:
         #    model.write_profiles(name+f'_profiles_{model.it}', overwrite=True, verbose=False)

         model.evolve(dt, print_freq=100, verbose=True) #Evolve model 1 timestep, printing progress every 10 steps.
         
      #Reached maximum iterations allowed      
      if model.it == (4.5e9*prm.ys/dt):
         model.critical_failure_reason = True
         model.critical_failure_reason = 'Reached maximum iteration (4.5 Gyrs time total)'

      # save model output
      model.save_dict['core']['critical_failure_reason'] = model.critical_failure_reason #Save the reason for critical failure.
      model.write_data(name, overwrite=True)








