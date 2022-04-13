from scipy.integrate import trapezoid
import numpy as np

import thermal_history as th
import thermal_history.core_models.leeds.routines.rivoldini_eos as eos


def setup_model(prm, verbose=True):
    '''Set self-consistent model paramters using EOS and return model ready to run.'''

    #Calculate material properties from EOS for given composition at CMB. Start with initial guess of CMB P/T and
    #Iterate to self consistently find properties at volume average P/T
    P_av = prm.P_cmb
    T_av = prm.T_cmb

    #10 iteration seems plenty. Most converge after a couple.
    for i in range(10):
        properties = eos.liquidCore(prm.conc_l[0], P_av/1e9, T_av)
        prm.core_cp_params             = [1000*properties['Cp']/properties['M']]   #Specific heat
        prm.core_alpha_T_params        = [properties['alpha']]  #Thermal expansivity
        prm.core_liquid_density_params = [properties['rho']]   #Density of liquid.

        #Create model to get radial profiles and new average P/T
        model = th.model.setup_model(prm, core_method='leeds', stable_layer_method='leeds_thermal', verbose=False)
        r, T, P = model.core.profiles['r'], model.core.profiles['T'], model.core.profiles['P']
        P_av = trapezoid(P*r**2, x=r)/((1/3)*prm.r_cmb**3)
        T_av = trapezoid(T*r**2, x=r)/((1/3)*prm.r_cmb**3)

        #Force T_cmb to be at the melting temp so snow starts straight away.
        prm.T_cmb = model.core.profiles['Tm'][-1]

    #Set change in entropy on melting used for latent heat
    s_solid = eos.fccFe(P_av/1e9, T_av)['S']
    s_liq   = eos.liquidFe(P_av/1e9, T_av)['S']
    delta_s = (s_liq-s_solid)/prm.Na  #J/K/atom. 
    prm.entropy_melting_params = [delta_s]
    
    #Finite difference to approximate alpha_c
    S = prm.conc_l[0]
    drho_dc = (eos.liquidCore(S+0.001, P_av/1e9, T_av)['rho'] - eos.liquidCore(S-0.001, P_av/1e9, T_av)['rho'])/0.002
    prm.alpha_c = [-1/properties['rho'] * drho_dc]

    #Set core conductivity:
    def kFeS(x,T):
        return (2.445*T)/(92.71381967698574 + 1189.0330473455936*x + 2404.678175564527*x**2)
    
    prm.core_conductivity_params = [kFeS(S, T_av)]

    #Setup and return final model
    return th.model.setup_model(prm, core_method='leeds', stable_layer_method='leeds_thermal', verbose=verbose)
