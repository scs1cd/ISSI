#Automatically generated parameters file for the following methods:
#core: leeds

# All in SI units
#Constants
ys = 60*60*24*365     #Seconds in a year
ev = 1.602e-19        #Electron volt
kb = 1.3806485e-23    #Boltzmanns constant
G  = 6.67e-11         #Gravitational Constant
Na = 6.022140857e23   #Avogadros Constant
Rg = 8.31446261815324 #Gas constant

core = True  #True/False. Include core in solution
stable_layer = False #True/False. Include stable layer in solution
mantle = False #True/False. Include mantle in solution

#core: leeds parameters

T_cmb                      =  2400 # Initial temperature of the CMB. Can
                                   # specify Tcen (temperature at the center of the core) instead. Float.
conc_l                     =  [0.106108] # Initial light element mass fraction of
                                      # the core. Preserve order consistency with all other light element property lists. List(float).
core_solid_density_params  =  [7211] # Inner core density polynomials
                                     # (radial). List(float)
core_liquid_density_params =  [7211] # Outer core density polynomials
                                     # (radial). List(float)
ri                         = 0  # Initial inner core radius. Float
r_cmb                      = 1627e3  # CMB radius. Float
core_alpha_T_params        = [1e-5]  # Core thermal expansivity pressure
                                     # polynomial coefficients. List(Float)
core_cp_params             = [780]  # Core specific heat capacity pressure
                                    # polynomial coefficients. List(Float)
core_conductivity_params   = ['r', 40]  # List, first element is a string
                                        # followed by the core thermal conductivity polynomial coefficients. The string (either 'r'/'T'/'P') indicates if the polynomials are radial, temperature, or pressire coefficients. List(string, Float, Float...)
core_melting_params        = ['WN', 1990.48621274289, 1, -0.00218881211768781/1e9, 3.77133942042793e-07/1e18]  # List, first element is a string
                               #  followed by the constants used for the melting temperature parameterisation. The string element indicates the parameterisation to be used, if no string is given, 'AL' (method of Alfe et al. 2002) is assumed. See melting_curve() in ./routines/chemistry.py for possible options.
entropy_melting_params     =  [kb*1.99731, kb*-0.0082/1e9] # Change of entropy on freezing pressure
                                                           # polynomial coefficients. List(Float).
mm                         = [56, 32]  # Molar masses (g/mol) of Iron followed
                                       #  by alloying light elements. List(float)
alpha_c                    = [0.64]  # Chemical expansivity of alloying light
                                     # elements. List(float)
diffusivity_c              = [5e-9]  # Chemical diffusivities of alloying
                                     # light elements.  List(float)
use_partition_coeff        = True  # Boolean dictating if constant partition
                                   # coefficients shoulf be used (True) or if partitioning based on chemical equilibrium should be used (False)
core_h0                    = 0  # Present day radiogenic heating per unit
                                # mass in the core
half_life                  = 0  # Half life of radioactive isotope in the
                                #  core.
partition_coeff            = [0]  # Partition coefficients (x_i/x_o) for
                                  # mass fraction for each light element. Defined as the ratio of inner core concentration over outer core. List(float)
lambda_sol                 = [0]  # Linear corrections to chemical
                                  # potentials (solid phase). List(float)
lambda_liq                 = [0]  # Linear corrections to chemical
                                  # potentials (liquid phase). List(float)
dmu                        = [0]  # Change in chemical potential between
                                  # solid and liquid. List(float)
n_profiles                 = 3000  # Number of nodes used in radial profiles
                                  # for core properties. Float
P_cmb                      = 21e9 # CMB pressure. Float
precip_temp                = 1e4  # Temperature below which precipitation
                                  # of MgO begins. Float
Cm_mgo                     = 0    # mass fraction of MgO in the core
alpha_c_mgo                = 0    # MgO chemical expansivity


#Optional parameters that if not specified take their default values

#core: leeds optional parameters

#include_baro_diffusion =   # (Default: True) Boolean, if True,
                            # barodiffusion will be included for both the entropy budget and also chemical gradients in any chemcially stratified layer.
core_adiabat_params    =  [1, -2.88429493500129e-12/1e3, -7.60393797523802e-08/1e6] # (Default: None) None or List(float).
                            # Radial polynomial coefficients for the core adiabat normalised to T(r=0). If left as None, these will be calculated by fitting to a numerically integrated adiabatic gradient using given alpha/cp/g profiles.
#set_cooling_rate       =   # (Default: False) Boolean, if True, the
                            # core cooling rate is set to the parameter core_dTa_dt and the CMB heat flow is overwritten with the required value. Only used if no stable layer is included
#core_dTa_dt            =   # (Default: 0) Float, the cooling rate of
                            # the core if set_cooling_rate is True
iron_snow              = True  # (Default False) Boolean, if True, an top
                            # down core crystallisation rather than bottom up is assumed
#Ej_fixed               =   # (Default None) None or Float, if set to a
                            # value, Ej will be fixed to this value at all times. Q_cmb will be altered to ensure this condition
#Ej_lower_bound         =   # (Default None) None or Float, if set to a
                            # value, Ej will be limited to this value if it were to fall below it. Q_cmb will be altered to ensure this condition
#Ej_fixed_pre_ic        =   # (Default False). Boolean, when dt<0 and if
                            # true, Ej is fixed prior to ICN to the value immedietly post ICN. Q_cmb will be altered to ensure this condition.
#core_latent_heat       =   # (Default None). Latent heat is calculated
                            # using the change of entropy on melting unless this is set to a fixed number (J/kg). None or Float
#mf_l                   =   # (Default None) Starting mole fraction of
                            # light element in the core. If specified it will overrule conc_l.
#Tcen                  =   # (Default None) Initial temperature at the
                            # center of the core. If specified it will overrule T_cmb (but may still be overrulled by contraint of T=Tm at ri.)


