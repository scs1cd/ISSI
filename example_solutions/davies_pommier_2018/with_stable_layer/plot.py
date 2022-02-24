import matplotlib.pyplot as plt
import numpy as np
import pickle



data = pickle.load(open('../davies_pommier_2018.pik','rb'))
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


data_layer = pickle.load(open('davies_pommier_2018_with_layer.pik','rb'))
core2 = data_layer['core']
time2 = core2['time']/(1e6*data_layer['parameters']['ys'])


r_snow2 = core2['r_snow']/1000
conc_l2 = core2['conc_l']*100

Qa2 = core2['Qa']/1e12
Q_cmb2 = core2['Q_cmb']/1e12
Qs2 = core2['Qs']/1e12
Es2 = core2['Es']/1e6

Ql_b2 = core2['Ql_b']/1e12
Ql_l2 = core2['Ql_l']/1e12
Ql_s2 = core2['Ql_s']/1e12

El_l2 = core2['El_l']/1e6
El_s2 = core2['El_s']/1e6
El_b2 = core2['El_b']/1e6

Qg_b2 = core2['Qg_b']/1e12
Qg_l2 = core2['Qg_l']/1e12 + Qg_b2
Qg_s2 = core2['Qg_s']/1e12

Eg_b2 = core2['Eg_b']/1e6
Eg_l2 = core2['Eg_l']/1e6 + Eg_b2
Eg_s2 = core2['Eg_s']/1e6

Ej2 = core2['Ej']/1e6
Ea2 = core2['Ek']/1e6
Es2 = core2['Es']/1e6



fig, axes = plt.subplots(2,2,figsize=(9,8), sharex=True)


axes[0,0].plot(time,r_snow, linestyle='--')
axes[0,0].plot(time2,r_snow2)
axes[0,0].set_ylabel('r_snow [km]')
axes[0,0].set_title('Snow radius')

axes[0,1].plot(time,conc_l, linestyle='--')
axes[0,1].plot(time2,conc_l2)
axes[0,1].set_ylabel('S [wt%]')
axes[0,1].set_title('Sulphur composition in convecting region')


axes[1,0].plot(time2, Q_cmb2, linestyle='--')
axes[1,0].plot(time2, Ql_l2+Ql_s2, linestyle='--')
axes[1,0].plot(time2, Qg_l2+Qg_s2, linestyle='--')
axes[1,0].plot(time, Q_cmb, label=r'$Q_\mathrm{c}$')
axes[1,0].plot(time, Ql_l+Ql_s, label=r'$Q_\mathrm{l}$')
axes[1,0].plot(time, Qg_l+Qg_s, label=r'$Q_\mathrm{g}$')

axes[1,0].legend(loc=0)
axes[1,0].set_ylabel('TW')
axes[1,0].set_title('Energy terms')
axes[1,0].set_xlabel('time [Myrs]')


axes[1,1].plot(time, Ej, linestyle='--')
axes[1,1].plot(time, Ea, linestyle=':')
axes[1,1].plot(time, Es, linestyle='--')
axes[1,1].plot(time, El_l+El_s, linestyle='--')
axes[1,1].plot(time, Eg_l+Eg_s, linestyle='--')

axes[1,1].plot(time2, Ej2, label=r'$E_\mathrm{J}$')
axes[1,1].plot(time2, Ea2, label=r'$E_\mathrm{a}$', linestyle='--')
axes[1,1].plot(time2, Es2, label=r'$E_\mathrm{s}$')
axes[1,1].plot(time2, El_l2+El_s2, label=r'$E_\mathrm{l}$')
axes[1,1].plot(time2, Eg_l2+Eg_s2, label=r'$E_\mathrm{g}$')

axes[1,1].legend(loc=0)
axes[1,1].set_xlabel('time [Myrs]')
axes[1,1].set_ylabel('MW/K')
axes[1,1].set_title('Entropy terms')

plt.show()








