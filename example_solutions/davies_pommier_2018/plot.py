import matplotlib.pyplot as plt
import numpy as np
import pickle

#Load in data
data = pickle.load(open('davies_pommier_2018.pik','rb'))

core = data['core']

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

time = core['time']/(60*60*24*365*1e6)


#Fortran results plotted as dots, python results as lines.

filename='./fortran_results/'
fortran_energy = np.genfromtxt(filename+'OUT_forw_energy',skip_header=1)/1e12
columns=[6,5,8,9]
fig, axes = plt.subplots(2,2,figsize=(9,8),sharex=True)

skip = 20 #Plot every 'skip' points
t = fortran_energy[:,0]*1e12
mine = [Qa,Q_cmb,Ql_s,Ql_l]
labels = ['Qa','Qcmb','Ql_s', 'Ql_l']
colors = ['c','b','m','g']
for i in range(len(columns)):
   axes[0,0].plot(t[::skip], fortran_energy[:,columns[i]][::skip],'o', color=colors[i],label=labels[i])
   axes[0,0].plot(time,mine[i])

axes[0,0].legend(loc=0)



columns=[7,10,11]
mine = [Ql_b,Qg_s,Qg_l]
labels = ['Ql_b','Qg_s','Qg_l']
colors = ['r','y','g']
for i in range(len(columns)):
   axes[1,0].plot(t[::skip], fortran_energy[:,columns[i]][::skip], 'o', color=colors[i],label=labels[i])
   axes[1,0].plot(time,mine[i])

axes[1,0].legend(loc=0)



fortran_entropy = np.genfromtxt(filename+'OUT_forw_entropy',skip_header=1)/1e6

columns = [6,5,10,11]
mine = [Ea,Ej,El_s,El_l]
labels = ['Ea','Ej','El_s','El_l']
colors = ['c','b','m','g']
for i in range(len(columns)):
   axes[0,1].plot(t[::skip], fortran_entropy[:,columns[i]][::skip],'o', color=colors[i],label=labels[i])
   axes[0,1].plot(time,mine[i])

axes[0,1].legend(loc=0)



columns = [9,12,13]
mine = [El_b,Eg_s,Eg_l]
labels = ['El_b','Eg_s','Eg_l']
colors = ['r','y','g']
for i in range(len(columns)):
   axes[1,1].plot(t[::skip], fortran_entropy[:,columns[i]][::skip],'o', color=colors[i],label=labels[i])
   axes[1,1].plot(time,mine[i])

axes[1,1].legend(loc=0)

axes[0,0].set_ylabel('TW')
axes[0,0].set_title('Energies')

axes[1,0].set_xlabel('time [Myrs]')
axes[1,0].set_ylabel('TW')

axes[0,1].set_ylabel('MW/K')
axes[0,1].set_title('Entropies')

axes[1,1].set_xlabel('time [Myrs]')
axes[1,1].set_ylabel('MW/K')

plt.show()






r_snow = core['r_snow']/1000
rs = np.genfromtxt(filename+'OUT_forw_diagnostics',skip_header=1)[:,4]/1000

plt.plot(t[::skip],rs[::skip], 'o')
plt.plot(time,r_snow)
plt.xlabel('time [Myrs]')
plt.title('Snow zone radius [km]')
plt.show()


fortran_conc = np.genfromtxt(filename+'OUT_forw_conc',skip_header=1)

plt.plot(t[::skip], 100*fortran_conc[:,3][::skip],'o')
conc_l = core['conc_l']*100
plt.plot(time, conc_l)
plt.xlabel('time [Myrs]')
plt.title('Sulphur concentration [wt%]')
plt.show()











