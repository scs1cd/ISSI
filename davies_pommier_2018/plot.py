import matplotlib.pyplot as plt
import numpy as np
import pickle



data = pickle.load(open('davies_pommier_2018.pik','rb'))
core = data['core']
time = core['time']/(1e6*data['parameters']['ys'])


r_snow = core['r_snow']/1000
conc_l = core['conc_l']*100

Qa = core['Qa']/1e12
Q_cmb = core['Q_cmb']/1e12
Qs = core['Qs']/1e12
Es = core['Es']/1e6

Ql_b = core['Ql_b']/1e12
Ql_l = core['Ql_l']/1e12
Ql_s = core['Ql_s']/1e12

El_l = core['El_l']/1e6
El_s = core['El_s']/1e6
El_b = core['El_b']/1e6

Qg_b = core['Qg_b']/1e12
Qg_l = core['Qg_l']/1e12 + Qg_b
Qg_s = core['Qg_s']/1e12

Eg_b = core['Eg_b']/1e6
Eg_l = core['Eg_l']/1e6 + Eg_b
Eg_s = core['Eg_s']/1e6

Ej = core['Ej']/1e6
Ea = core['Ek']/1e6
Es = core['Es']/1e6



fig, axes = plt.subplots(2,2,figsize=(9,8), sharex=True)


axes[0,0].plot(time,r_snow)
axes[0,0].set_ylabel('r_snow [km]')
axes[0,0].set_title('Snow radius')

axes[0,1].plot(time,conc_l)
axes[0,1].set_ylabel('S [wt%]')
axes[0,1].set_title('Sulphur composition in convecting region')


axes[1,0].plot(time, Q_cmb, label=r'$Q_\mathrm{c}$')
axes[1,0].plot(time, Ql_l+Ql_s, label=r'$Q_\mathrm{l}$')
axes[1,0].plot(time, Qg_l+Qg_s, label=r'$Q_\mathrm{g}$')

axes[1,0].legend(loc=0)
axes[1,0].set_ylabel('TW')
axes[1,0].set_title('Energy terms')
axes[1,0].set_xlabel('time [Myrs]')


axes[1,1].plot(time, Ej, label=r'$E_\mathrm{J}$')
axes[1,1].plot(time, Ea, label=r'$E_\mathrm{a}$', linestyle='--')
axes[1,1].plot(time, Es, label=r'$E_\mathrm{s}$')
axes[1,1].plot(time, El_l+El_s, label=r'$E_\mathrm{l}$')
axes[1,1].plot(time, Eg_l+Eg_s, label=r'$E_\mathrm{g}$')

axes[1,1].legend(loc=0)
axes[1,1].set_xlabel('time [Myrs]')
axes[1,1].set_ylabel('MW/K')
axes[1,1].set_title('Entropy terms')

plt.show()








