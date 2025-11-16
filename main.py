# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:37:00 2021

@author: felipe feijoo
"""
#%%
#MAIN
###############################################################################
######################SENARIO NAME and single parameters#######################
###############################################################################

#SCENARIO DESIGN
scen = 'Base'
rps_inv          = True     # Options: True / False
carbonLimit      = True     # Options: True / False
res_inv          = True     # Options: True / False
ceep_limit       = True     # Options: True / False
ceep_penalty     = True     # Options: True / False
fossil_dispatch  = True
hydro_storage    = True     # Options: True / False
NoResToHeatInv   = False    # Options: True / False
save_csv         = True     # Options: True / False

periods = list(range(1,24*365))
years = list([2020,2025,2030,2035,2040,2045,2050])

#Policy Paramenters
rps              = list([0.4, 0.5, 0.60, 0.7, 0.8, 0.9, 1])
CO2_limit        = list([8261526*1,8261526*0.8,8261526*0.6,8261526*0.4,8261526*0.3,8261526*0.2,8261526*0.1])
carbon_price     = list([30, 50, 60, 70, 80, 90, 100])        # Carbon price in $/tCO2
ceep_parameter   = 0.1    # Note that H2RES takes 0.1 = 10% not as 0.1%.
ceep_value       = 450    # penalty for CEEP
LostLoad_Cost    = 1000   # Cost for Unserved demand (heat (dh, ind) and electricity) 

#General Paramenters
NPV              = list([1,0.78,0.61,0.48,0.38,0.3,0.23])   #IR 5%
TechChangeSolar  = list([1, 0.95, 0.9, 0.8, 0.7, 0.6, 0.5])
TechChangeWind   = list([1, 0.95, 0.9, 0.8, 0.7, 0.6, 0.5])
ThermalDecomInd  = list([1, 0.6, 0.3, 0, 0, 0, 0])
HeatPumpDecomInd = list([1, 0.6, 0.3, 0, 0, 0, 0])
ThermalDecomDH   = list([1, 0.6, 0.3, 0, 0, 0, 0])
StaStoDecomInd   = list([1, 0.6, 0.3, 0, 0, 0, 0])
Import_Price     = 45       # $/MWh
Imp_price_inc    = 0.05     # 5% increase in import price pear year. 


#### V2G
V2G_cost        = 25       # Vehicle to grid price $/MWh 
ev_Demand_year  = list([1, 1, 1, 1, 1, 1, 1])  # Total yearly demand per year (MWh)
ev_sto_min      = 0
ev_Grid_eff     = 0.9
number_of_veh   = 1670000   #Number of total vehicles
average_ch_rate = 7         #kW
average_bat     = 50        #kWh
charging_veh    = number_of_veh*average_ch_rate/1000    #MW
stor_veh        = number_of_veh*average_bat/1000        #MWh
ev_Grid_P       = list([0.075*charging_veh, 0.2*charging_veh, 0.4*charging_veh, 0.4*charging_veh, 0.4*charging_veh, 0.4*charging_veh, 0.4*charging_veh])
ev_stor         = list([0.075*stor_veh, 0.2*stor_veh, 0.4*stor_veh,0.4*stor_veh,0.4*stor_veh,0.4*stor_veh,0.4*stor_veh])

###############################################################################
### GENCO/Demand data (enter genco data file name with extension)##############
###############################################################################
genco_dat             = './data/1_genco_data_HR.csv'
demand_dat            = './data/2_demand_2020_2050.csv'
heat_demand_dat       = './data/3_heat_demand_2020_2050.csv'
cooling_demand_dat    = './data/4_cooling_demand_2020_2050.csv'
h2_demand_dat         = './data/5_demand_H2_2020_2050.csv'
fuel_price_dat        = './data/6_fuel_cost_2020_2050.csv'
avl_factor_plant_dat  = './data/7_ncre_aval_factor_2020_2050.csv'
inflows_dat           = './data/8_scaled_inflows_2020_2050.csv' 
import_export         = './data/9_import_export_2020_2050.csv' 
ev_transpload_dat     = './data/10_ev_transp_load.csv'
flex_tech_dat         = './data/11_flex_tech_2020_2050.xlsx'

###############################################################################
### GENCO/Demand data (enter genco data file name with extension)##############
###############################################################################
print('Reading and processing data')
exec(open("scripts/read_process_data.py").read())
print('Building and solve the model')
exec(open("scripts/Build_model.py").read())
print('Printing and ploting results')
exec(open("scripts/export_plot.py").read())
exec(open("scripts/combine_plot.py").read())
###############################################################################
###############################################################################



