import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import trapezoid
import sys

sys.path.append('C:\\Users\\earcd\\Documents\\GitHub\\thermal_history')
sys.path.append('C:\\Users\\earcd\\Documents\\GitHub\\ISSI\\meeting_solutions\\useful_scripts')

import thermal_history as th
import rivoldini_eos as eos

def setup_model(prm, core_method=None, stable_layer_method=None, verbose=True):

    '''Set self-consistent model paramters using EOS and return model ready to run.'''

    #Calculate material properties from EOS for given composition at CMB. Start with initial guess of CMB P/T and
    #Iterate to self consistently find properties at volume average P/T

    P_av = prm.P_cmb
    T_av = prm.T_cmb

    #10 iteration seems plenty. Most converge after a couple.

    for i in range(10):

        properties = eos.liquidCoreFeCideal(prm.conc_l[0], P_av/1e9, T_av)
        prm.core_cp_params             = [1000*properties['Cp']/properties['M']]   #Specific heat
        prm.core_alpha_T_params        = [properties['alpha']]  #Thermal expansivity
        prm.core_liquid_density_params = [properties['rho']]   #Density of liquid.

        #Create model to get radial profiles and new average P/T

        model = th.model.setup_model(prm, core_method=core_method, stable_layer_method=stable_layer_method, verbose=False)

        r, T, P = model.core.profiles['r'], model.core.profiles['T'], model.core.profiles['P']

        P_av = trapezoid(P*r**2, x=r)/((1/3)*prm.r_cmb**3)

        T_av = trapezoid(T*r**2, x=r)/((1/3)*prm.r_cmb**3)

        #Force T_cmb to be at the melting temp so snow starts straight away.

        prm.T_cmb = model.core.profiles['Tm'][-1]

    

    graphite=eos.graphite(P_av/1e9, T_av)

    prm.core_solid_density_params  = [graphite['rho']]

    prm.entropy_melting_params = [17. / (prm.Na *1000/prm.mm[1])] # convert J/K/kg  J/K/atom

    prm.alpha_c = [properties['alphaC']]

    prm.core_conductivity_params = [eos.kFeCZhang(prm.conc_l[0], T_av)]

    prm.core_melting_params = ['XX', eos.pdFeC()]

    return th.model.setup_model(prm, core_method=core_method, stable_layer_method=stable_layer_method, verbose=verbose)



#Load parameters

prm = th.model.Parameters('graphite_params.py')

prm.core_melting_params = ['XX', eos.pdFeC()]

prm.conc_l[0] = 0.07

prm.P_cmb=3e9

prm.r_cmb=400e3

model = setup_model(prm, core_method='solid_FeS',stable_layer_method=None, verbose=False)



T0=model.core.profiles["T"]

Tm0=model.core.profiles["Tm"]





dt = 1e6*prm.ys

while not model.critical_failure and model.it < (4.5e9*prm.ys/dt):

    t = model.time / (1e6*prm.ys)

    heat_flux = 1 + 40 * np.exp(-t/100)

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

plt.ylabel('r_graphite [km]')

plt.xlabel('time [Myrs]')



plt.figure()

plt.plot(time, core['T_upper'])

plt.ylabel('T [K]')

plt.xlabel('time [Myrs]')



plt.figure()

p = model.core.profiles['P']/1e9

T = model.core.profiles['T']

Tm = model.core.profiles['Tm']

plt.plot(p, T0, label='T(t=0)')

plt.plot(p, T, label='T')

plt.plot(p, Tm0, label='Tm(t=0)')

plt.plot(p, Tm, label='Tm')

plt.xlabel('p [GPa]')

plt.ylabel('T[K]')

plt.legend()



plt.figure()

r = model.core.profiles['r']/1e3

T = model.core.profiles['T']



Tm = model.core.profiles['Tm']

plt.plot(r, T0, label='T(t=0)')

plt.plot(r, T, label='T')

plt.plot(r, Tm0, label='Tm(t=0) C='+str(round(100*core['conc_l'][0],2))+"wt%")

plt.plot(r, Tm, label='Tm C='+str(round(100*core['conc_l'][-1],2))+"wt%")

plt.xlabel('r [km]')

plt.ylabel('T[K]')

plt.legend()





plt.show()