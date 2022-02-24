import numpy as np
import matplotlib.pyplot as plt
from thermal_history.model import Parameters, setup_model

prm = Parameters('DP18_parameters_with_layer.py')

prm.T_cmb -= 100 #CMB 100 K colder initially to force snow zone to form

model = setup_model(prm, core_method='leeds', stable_layer_method='leeds_thermal')

WN = np.genfromtxt('../WN04-Qcmb', skip_header=1)

dt = 4.5e6*prm.ys
for i in range(1000):
    model.mantle.Q_cmb = np.interp(model.time/(1e9*prm.ys), WN[:,0], WN[:,1])*1e12
    model.evolve(dt)


r = model.core.profiles['r']/10000
T = model.core.profiles['T']
Tm = model.core.profiles['Tm']
plt.plot(r, T, label='T')
plt.plot(r, Tm, label='Tm')
plt.legend(loc=0)
plt.xlabel('Radius [km]')
plt.ylabel('K')
plt.show()


try:
    model.write_data('davies_pommier_2018_with_layer.pik')
except Exception as e:
    print(e)

breakpoint()
