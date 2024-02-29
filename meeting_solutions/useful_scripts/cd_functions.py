import numpy as np
import matplotlib.pyplot as plt

def plot_single_ts(data, name, field, figure=None, ax=None, ignore_last_datapoint=True):
    
    """ Plots field vs time and saves to file"""
    
    if figure == None:
        fig, ax = plt.subplots(figsize=(16,6))

    time   = data['core']['time'] / (1e6*data['parameters']['ys'])  #Convert time from seconds to Myrs.
    variable = data['core'][field]  

    if ignore_last_datapoint:
        idx = time.size-1
    else:
        idx = time.size

    ax.plot(time[:idx], variable[:idx], label=name.split('/')[-1])  #Remove any file paths from name
    ax.legend(bbox_to_anchor=(0.1, 1.05), ncol=5)
    ax.set_xlabel('time [Myrs]')
    ax.set_ylabel(field+'[km]')
    
    if figure == None:
        fig.savefig(name+"_"+field+".pdf", format='pdf',bbox_inches="tight")
        plt.close(fig)
        
def plot_Q(data, fields, name, ignore_last_datapoint=True):
    
    """ Plots power terms vs time for one case 
    if fields == 1 then all terms are plotted, else just the large terms are plotted"""
    
    fig, ax = plt.subplots(figsize=(16,6))
 
    time   = data['core']['time'] / (1e6*data['parameters']['ys'])  #Convert time from seconds to Myrs.

    Qs   = data['core']['Qs']/1e10
    Qcmb = data['core']['Q_cmb']/1e10
    Qls  = data['core']['Ql_s']/1e10
    Qll  = data['core']['Ql_l']/1e10
    Qlb  = data['core']['Ql_b']/1e10
    Qgb  = data['core']['Qg_b']/1e10
    Qgs  = data['core']['Qg_s']/1e10
    Qgl  = data['core']['Qg_l']/1e10   
    Qa   = data['core']['Qa']/1e10
  
    if ignore_last_datapoint:
        idx = time.size-1
    else:
        idx = time.size

    plt.plot(time[:idx], Qcmb[:idx], 'b-'   , label='Qcmb')
    plt.plot(time[:idx], Qa[:idx]  , 'b'    , label='Qa', linestyle="dashed")
    plt.plot(time[:idx], Qs[:idx]  , 'grey' , label='Qs')
    plt.plot(time[:idx], Qls[:idx] , 'black', label='Qls')
    plt.plot(time[:idx], Qll[:idx] , 'black', label='Qll', linestyle="dashed")
    plt.xlabel('time')
    plt.ylabel('Q ($\\times 10^{10}$ W)')
    #plt.xlim([0,5])
    #plt.ylim([0.9,1.2])

    if fields == 1: # plot the small terms
        plt.plot(time[:idx], Qlb[:idx] , 'black', label='Qlb', linestyle="dotted")
        plt.plot(time[:idx], Qgs[:idx] , 'red'  , label='Qgs')
        plt.plot(time[:idx], Qgl[:idx] , 'red'  , label='Qgl', linestyle="dashed") 
        plt.plot(time[:idx], Qgb[:idx] , 'red'  , label='Qgb', linestyle="dotted")
        plt.legend(loc=2, ncol=2, bbox_to_anchor=(0.7,0.8))
        fig.savefig(name+"_Q_all.pdf", format='pdf',bbox_inches="tight")
    else:
        if Qgs[idx-1] > Qgl[idx-1]:  #Index -2 since last value is when r_snow=0 and energies/entropies are not defined.
            plt.plot(time[:idx], Qgs[:idx], 'red', label='Qgs')
        else:
            plt.plot(time[:idx], Qgl[:idx], 'red', label='Qgl', linestyle="dashed")    
        plt.legend(loc=2, ncol=2, bbox_to_anchor=(0.7,0.8))
        fig.savefig(name+"_Q_red.pdf", format='pdf',bbox_inches="tight")
    
    plt.close(fig)
    
def plot_E(data, fields, name, ignore_last_datapoint=True):
 
    """ Plots Entropy terms vs time for one case 
    if fields == 1 then all terms are plotted, else just the large terms are plotted"""

    fig, ax = plt.subplots(figsize=(16,6))

    time   = data['core']['time'] / (1e6*data['parameters']['ys'])  #Convert time from seconds to Myrs.

    Es   = data['core']['Es']/1e6
    EJ   = data['core']['Ej']/1e6
    Ek   = data['core']['Ek']/1e6
    Els  = data['core']['El_s']/1e6
    Ell  = data['core']['El_l']/1e6
    Elb  = data['core']['El_b']/1e6
    Egs  = data['core']['Eg_s']/1e6
    Egl  = data['core']['Eg_l']/1e6
    Egb  = data['core']['Eg_b']/1e6

    if ignore_last_datapoint:
        idx = time.size-1
    else:
        idx = time.size
                  
    plt.plot(time[:idx], EJ[:idx]  , 'b-'  , label='EJ')
    plt.plot(time[:idx], Ek[:idx]  , 'b'   , label='Ek', linestyle="dashed")
    plt.plot(time[:idx], Es[:idx]  , 'grey', label='Es')
    plt.plot(time[:idx], Egs[:idx] , 'red' , label='Egs')
    plt.plot(time[:idx], Egl[:idx] , 'red' , label='Egl', linestyle="dashed")
    #plt.xlim([0,5])
    #plt.ylim([0.9,1.2])
    plt.xlabel('time')
    plt.ylabel('Entropy (MW / K)')

    if fields == 1: # plot the small terms
        plt.plot(time[:idx], Egb[:idx] , 'red'  , label='Egb', linestyle="dotted")
        plt.plot(time[:idx], Els[:idx] , 'black', label='Els')
        plt.plot(time[:idx], Ell[:idx] , 'black', label='Ell', linestyle="dashed")
        plt.plot(time[:idx], Elb[:idx] , 'black', label='Elb', linestyle="dotted")
        plt.legend(loc=2, ncol=2, bbox_to_anchor=(0.7,0.8))
        fig.savefig(name+"_E_all.pdf", format='pdf',bbox_inches="tight")
    else:
        if Els[idx-1] > Ell[idx-1]:  
            plt.plot(time[:idx], Els[:idx] , 'black', label='Els')
        else:
            plt.plot(time[:idx], Ell[:idx] , 'black', label='Ell', linestyle="dashed")
        plt.legend(loc=2, ncol=2, bbox_to_anchor=(0.7,0.8))
        fig.savefig(name+"_E_red.pdf", format='pdf',bbox_inches="tight")
    
    plt.close(fig)
    