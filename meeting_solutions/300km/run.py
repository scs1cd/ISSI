import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid

import thermal_history as th
from thermal_history.core_models.leeds.routines import rivoldini_eos as eos

#Load parameters
prm = th.model.Parameters(('300_params.py',))

#Loop over different CMB heat fluxes, compositions and thermal conductivities
k_array     = [5, 10, 15]
q_cmb_array = [1, 5, 10]        #mW/m^2
S_array     = [0.05, 0.1, 0.15]

#Make directory to store output if not already.
if not os.path.isdir('output'):
   os.mkdir('output')

#Begin loops
for k in k_array:
   prm.core_conductivity = [k] #Set conductivity

   for S in S_array:
      prm.conc_l[0] = S  #Set composition

      #Calculate material properties from EOS for given composition at CMB. Start with initial guess of CMB P/T and
      #Iterate to self consistently find properties at volume average P/T
      P_av = prm.P_cmb
      T_av = prm.T_cmb

      for it in range(10):
         properties = eos.liquidCore(S, P_av/1e9, T_av)
         prm.core_cp_params[0]             = 1000*properties['Cp']/properties['M']   #Specific heat
         prm.core_alpha_T_params[0]        = properties['alpha']  #Thermal expansivity
         prm.core_liquid_density_params[0] = properties['rho']    #Density of liquid.

         model = th.model.setup_model(prm, core_method='leeds', stable_layer_method='leeds_thermal', verbose=False)
         r, T, P = model.core.profiles['r'], model.core.profiles['T'], model.core.profiles['P']
         P_av = trapezoid(P*r**2, x=r)/((1/3)*trapezoid(r**2, x=r))
         T_av = trapezoid(T*r**2, x=r)/((1/3)*trapezoid(r**2, x=r))

         #Force T_cmb to be at the melting temp so snow starts straight away.
         prm.T_cmb = model.core.profiles['Tm'][-1]

      for q_cmb in q_cmb_array:

         #Setup model
         model = th.model.setup_model(prm, core_method='leeds', stable_layer_method='leeds_thermal')

         model.mantle.Q_cmb = q_cmb*1e-3 * 4*np.pi*prm.r_cmb**2 #Set constant CMB heat flow

         #Run model, breaking when snow zone covers whole core
         dt = 1e4*prm.ys
         for i in range(10000):

            if model.core.r_snow == 0:
               break

            #Save radial profiles at each time step
            name = f'./output/k={k:.0f}_S={S*100:.0f}_q={q_cmb:.0f}'

            #Write profiles
            # model.write_profiles(name+f'_profiles_{model.it}', overwrite=True, verbose=False)

            model.evolve(dt, print_freq=1) #Evolve model 1 timestep, printing progress every 10 steps.

         # save model output
         model.write_data(name, overwrite=True)




