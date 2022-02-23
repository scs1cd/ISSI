import matplotlib.pyplot as plt
import sys
sys.path.append('../../')
import numpy as np


import thermal_history as th

#th.utils.create_parameters_file('rc=100_params', core_method='development')

prm = th.model.Parameters(('rc=100_params.py',))

model = th.model.setup_model(prm, core_method='leeds')

dt = 1e4*prm.ys

for i in range(10000):

   if model.core.r_snow == 0:
      break

   model.mantle.Q_cmb = 1e9

   model.evolve(dt)

data = model.save_dict_to_numpy_array()
core = data['core']
time = core['time']/(1e6*prm.ys)
r_snow = core['r_snow']/1000
conc_l = core['conc_l']*100


plt.plot(time, prm.r_cmb/1000-r_snow)
plt.title('Snow zone thickness [km]')
plt.xlabel('time [Myrs]')
plt.show()


plt.plot(time, conc_l)
plt.title('Sulphur concentration [wt%]')
plt.xlabel('time [Myrs]')
plt.show()



