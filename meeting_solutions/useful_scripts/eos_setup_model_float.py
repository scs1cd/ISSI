'''Custom function to set model parameters based on the EOS provided by Atillio.
Can be imported and called in place of thermal_history.model.setup_model. Avoids needing to copy
and paste this code anytime we setup a model with the EOS parameters.'''

from scipy.integrate import trapezoid
import numpy as np

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
        properties = eos.liquidCore(prm.conc_l[0], P_av/1e9, T_av)
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

    
    propertiesSolidFeS=eos.FeSV(P_av/1e9, T_av)
    prm.core_solid_density_params  = [propertiesSolidFeS['rho']]
    #Set change in entropy on melting used for latent heat
    prm.entropy_melting_params = [eos.deltaSFeS(P_av/1e9, T_av)/prm.Na * prm.mm[0]/(prm.mm[0]+prm.mm[1])]
    prm.alpha_c = [properties['alphaC']]
    prm.core_conductivity_params = [eos.kFeSPommier(prm.conc_l[0], T_av)]
    
    if prm.core_melting_params[0] == 'AL':
         model.critical_failure_reason = True
         model.critical_failure_reason = 'Cannot use this expression for dS with Alfe Melting curve!'

    #Setup and return final model
    return th.model.setup_model(prm, core_method=core_method, stable_layer_method=stable_layer_method, verbose=verbose)