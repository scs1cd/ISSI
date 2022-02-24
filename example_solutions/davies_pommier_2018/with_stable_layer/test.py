#Automatically generated parameters file for the following methods:
#core: leeds
#stable_layer: leeds_thermal

# All in SI units
#Constants
ys = 60*60*24*365     #Seconds in a year
ev = 1.602e-19        #Electron volt
kb = 1.3806485e-23    #Boltzmanns constant
G  = 6.67e-11         #Gravitational Constant
Na = 6.022140857e23   #Avogadros Constant
Rg = 8.31446261815324 #Gas constant

core         = True  #True/False. Include core in solution
stable_layer = True  #True/False. Include stable layer in solution
mantle       = False #True/False. Include mantle in solution

#core: leeds parameters

T_cmb                      =   # Initial temperature of the CMB. Can
                               #  specify Tcen (temperature at the center of the core) instead. Float.
conc_l                     =   # Initial light element mass fraction of
                               #  the core. Preserve order consistency with all other light element property lists. List(float).
core_solid_density_params  =   # Inner core density polynomials
                               #  (radial). List(float)
core_liquid_density_params =   # Outer core density polynomials
                               #  (radial). List(float)
ri                         =   # Initial inner core radius. Float
r_cmb                      =   # CMB radius. Float
core_alpha_T_params        =   # Core thermal expansivity pressure
                               #  polynomial coefficients. List(Float)
core_cp_params             =   # Core specific heat capacity pressure
                               #  polynomial coefficients. List(Float)
core_conductivity_params   =   # List, first element is a string
                               #  followed by the core thermal conductivity polynomial coefficients. The string (either 'r'/'T'/'P') indicates if the polynomials are radial, temperature, or pressire coefficients. List(string, Float, Float...)
core_melting_params        =   # List, first element is a string
                               #  followed by the constants used for the melting temperature parameterisation. The string element indicates the parameterisation to be used, if no string is given, 'AL' (method of Alfe et al. 2002) is assumed. See melting_curve() in ./routines/chemistry.py for possible options.
entropy_melting_params     =   # Change of entropy on freezing pressure
                               #  polynomial coefficients. List(Float).
mm                         =   # Molar masses (g/mol) of Iron followed
                               #  by alloying light elements. List(float)
alpha_c                    =   # Chemical expansivity of alloying light
                               #  elements. List(float)
diffusivity_c              =   # Chemical diffusivities of alloying
                               #  light elements.  List(float)
use_partition_coeff        =   # Boolean dictating if constant partition
                               #  coefficients shoulf be used (True) or if partitioning based on chemical equilibrium should be used (False)
core_h0                    =   # Present day radiogenic heating per unit
                               #  mass in the core
half_life                  =   # Half life of radioactive isotope in the
                               #  core.
partition_coeff            =   # Partition coefficients (x_i/x_o) for
                               #  mass fraction for each light element. Defined as the ratio of inner core concentration over outer core. List(float)
lambda_sol                 =   # Linear corrections to chemical
                               #  potentials (solid phase). List(float)
lambda_liq                 =   # Linear corrections to chemical
                               #  potentials (liquid phase). List(float)
dmu                        =   # Change in chemical potential between
                               #  solid and liquid. List(float)
n_profiles                 =   # Number of nodes used in radial profiles
                               #  for core properties. Float
P_cmb                      =   # CMB pressure. Float
precip_temp                =   # Temperature below which precipitation
                               #  of MgO begins. Float
Cm_mgo                     =   # mass fraction of MgO in the core
alpha_c_mgo                =   # MgO chemical expansivity


#stable_layer: leeds_thermal parameters

layer_thickness            =   # Initial stable layer thickness. Float.
entrainment_T              =   # Entrainment coefficient on thermal
                               #  stratification (assumed 0). Float

#Following are required but are already defined above:
# core_liquid_density_params
# r_cmb
# core_alpha_T_params
# core_cp_params
# core_conductivity_params
# P_cmb


#Optional parameters that if not specified take their default values

#core: leeds optional parameters

#include_baro_diffusion =   # (Default: True) Boolean, if True,
                            # barodiffusion will be included for both the entropy budget and also chemical gradients in any chemcially stratified layer.
#core_adiabat_params    =   # (Default: None) None or List(float).
                            # Radial polynomial coefficients for the core adiabat normalised to T(r=0). If left as None, these will be calculated by fitting to a numerically integrated adiabatic gradient using given alpha/cp/g profiles.
#set_cooling_rate       =   # (Default: False) Boolean, if True, the
                            # core cooling rate is set to the parameter core_dTa_dt and the CMB heat flow is overwritten with the required value. Only used if no stable layer is included
#core_dTa_dt            =   # (Default: 0) Float, the cooling rate of
                            # the core if set_cooling_rate is True
#iron_snow              =   # (Default False) Boolean, if True, an top
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
#Tcen                   =   # (Default None) Initial temperature at the
                            # center of the core. If specified it will overrule T_cmb (but may still be overrulled by contraint of T=Tm at ri.)
#use_new_Cr             =   # (Default False) Use new Cr factor that
                            # takes into account depression of Tm with changing LE concentration


#stable_layer: leeds_thermal optional parameters

#entrainment_T           =   # (Default: 0) Float in the range 0 <= x <
                             # 1. Entrainment coefficient, modifies the adiabatic heat flow out the convecting region by the factor (1-x) to represent entrainment of stable fluid at the base of the stratified layer.
#max_resolution          =   # (Default: 100) Maximum number of nodes in
                             # grid. Int
#min_resolution          =   # (Default: 10) Minumum number of nodes in
                             # grid. Int
#resolution              =   # (Default: 1/1000) Target number of nodes
                             # per meter when constructing the grid. Float.
#depth_tolerance         =   # (Default: 1000) Layer size below which
                             # the layer is assumed full eroded. Note this default value will be halved when considering chemically stable layers fot stability. Float
#init_size               =   # (Default: 5000) Size the stable layer
                             # should be initialised if conditions promote layer growth and a layer does not yet exist. Note this default value will be halved when considering chemically stable layers fot stability. Float
#mix_layer               =   # (Default: False) Boolean, if True, uses
                             # an experimental function to calculate the T/c profile of a layer that has the top portion mixed.
#thermal_stratification  =   # (Default: True). Boolean, internal flag
                             # to tell the code that thermal stratification is being used
#chemical_stratification =   # (Default: False). Boolean, internal flag
                             # to tell the code that chemical stratification is not being used


