import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid
import sys

sys.path.append('/Users/tilio/ownCloud/python/thermal_history-current/thermal_history/useful_scripts') #Make useful scripts directory visible to import our custom setup_model

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

def TmC(x,p):
    return -973.1949862972292 - 159.45023271197547*p - 2.649550966097275*p**2 + 64212.43996334035*x + 1271.4356827385757*p*x - 222434.25817139592*x**2


model = th.model.setup_model(prm, core_method='solid_FeS',stable_layer_method=None, verbose=False)


#Tmx=list(map(lambda p: TmC(0.07,p*1e-9)-20, model.core.profiles["P"]))

# plt.figure()
# plt.plot(1e-3*model.core.profiles["r"], 1e-9*model.core.profiles["P"])
# plt.figure()
# plt.plot(1e-3*model.core.profiles["r"], model.core.profiles["T"])
# plt.plot(1e-3*model.core.profiles["r"], model.core.profiles["Tm"])
# plt.figure()
# plt.plot(1e-9*model.core.profiles["P"], model.core.profiles["Tm"])
# plt.plot(1e-9*model.core.profiles["P"], Tmx)
# plt.show()
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

data = model.save_dict_to_numpy_array()
core = data['core']

core = data['core']
time = core['time']/(1e6*prm.ys)
plt.figure()

plt.plot(time, 100*core['conc_l'])
plt.ylabel('C [wt%]')
plt.xlabel('time [Myrs]')

plt.figure()
plt.plot(time, 1e-9*core['Qs'])
plt.ylabel('Qs [GW]')
plt.xlabel('time [Myrs]')

plt.figure()
plt.plot(time, 1e-6*core['Ej'])
plt.ylabel('Ej [MW/K]')
plt.xlabel('time [Myrs]')

plt.figure()
plt.plot(time, 1e-3*core['r_snow'])
plt.ylabel('r_snow [km]')
plt.xlabel('time [Myrs]')

plt.figure()
plt.plot(time, core['T_upper'])
plt.ylabel('T [K]')
plt.xlabel('time [Myrs]')

plt.figure()
r = model.core.profiles['r']/1e3
T = model.core.profiles['T']
Tm = model.core.profiles['Tm']
plt.plot(r, T, label='T')
plt.plot(r, Tm, label='Tm')
plt.xlabel('Radius [km]')
plt.ylabel('T[r]')


plt.show()