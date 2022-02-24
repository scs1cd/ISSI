import matplotlib.pyplot as plt
import numpy as np

import thermal_history as th

#Load parameters
prm = th.model.Parameters(('rc=307_params.py',))

#Setup model
model = th.model.setup_model(prm, core_method='leeds')

#Run model, breaking when snow zone covers whole core
dt = 1e4*prm.ys
for i in range(100000):

   if model.core.r_snow == 0 or model.core.conc_l[0] <= 0:
      break

   model.mantle.Q_cmb = 1e11 #Set CMB heat flow
   model.evolve(dt)

#save output
# model.write_data('rc=100.pik')

#load output
# import pickle
# data = pickle.load(open('rc=100.pik', 'rb'))

#Plot data
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




