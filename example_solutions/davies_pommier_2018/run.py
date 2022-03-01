import numpy as np
import matplotlib.pyplot as plt
from thermal_history.model import Parameters, setup_model

prm = Parameters('DP18_parameters.py')

model = setup_model(prm, core_method='leeds')

WN = np.genfromtxt('WN04-Qcmb', skip_header=1)

dt = 4.5e6*prm.ys
for i in range(1000):
    model.mantle.Q_cmb = np.interp(model.time/(1e9*prm.ys), WN[:,0], WN[:,1])*1e12
    model.evolve(dt)


core = model.save_dict['core']

model.write_data('davies_pommier_2018.pik')

