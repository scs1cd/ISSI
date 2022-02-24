import matplotlib.pyplot as plt
import numpy as np

import thermal_history as th

#th.utils.create_parameters_file('ref_case_params.py', core_method='development')

prm = th.model.Parameters(('ref_case_params.py',))
prm.core_adiabat_params[1] = -0.19314243E-04/0.19314243E+04 #Match adiabatic gradient in Chris' code

model = th.model.setup_model(prm, core_method='leeds')


dt = 1e5*prm.ys
for i in range(1900):

   #Stop when snow zone covers whole core
   if model.core.r_snow == 0:
      break

   model.mantle.Q_cmb = 1e12
   model.evolve(dt)

# model.write_data('ref_case.pik')
# import pickle
# data = pickle.load(open('ref_case.pik', 'rb'))

data = model.save_dict_to_numpy_array()
core = data['core']
time = core['time']/(1e6*prm.ys)
r_snow = core['r_snow']/1000
conc_l = core['conc_l']*100


fortran_data = np.genfromtxt('OUT_forw_snow', skip_header=1)

time_f = fortran_data[:,0]
snow_f = fortran_data[:,1]/1000

plt.plot(time_f, snow_f, 'o', label='fortran')
plt.plot(time, prm.r_cmb/1000-r_snow, 'k-', label='thermal_history')
plt.title('Snow zone thickness [km]')
plt.xlabel('time [Myrs]')
plt.legend(loc=0)
plt.show()


fortran_data = np.genfromtxt('OUT_forw_conc', skip_header=1)

time_f = fortran_data[:,0]
conc_f = fortran_data[:,3]*100

plt.plot(time_f, conc_f, 'o', label='fortran')
plt.plot(time, conc_l, 'k-', label='thermal_history')
plt.title('Sulphur concentration [wt%]')
plt.xlabel('time [Myrs]')
plt.legend(loc=0)
plt.show()



