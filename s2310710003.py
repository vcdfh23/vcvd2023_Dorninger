#Run script with F5 for default values from json file
#Individual parameters example:
# & C:/Users/geral/AppData/Local/Programs/Python/Python310/python.exe 
# c:/Users/geral/VCVD/vcvd2023_Dorninger/s2310710003.py --mass="1000" --inclination="-5" 28 concrete dry

#import Libraries
import argparse
import sys
from scipy.constants import g
import numpy as np
#own modules
from examples.plot_example import plot_calculation

#Fricition coefficents from Powerpoint (constants)
concrete_dry = 0.5
concrete_wet = 0.35
ice_dry = 0.15
ice_wet = 0.08
gravel_dry = 0.35
sand_dry = 0.3

### parameter parser for: mass, velocity, road type, wet&dry, inclination
parameter_parser = argparse.ArgumentParser(description='Variance Parameter for calculation')
parameter_parser.add_argument('--mass',type=str,help='Mass of the vehicle.')
parameter_parser.add_argument('velocity',type=str, help='Velocity of the vehicle.')
parameter_parser.add_argument('road_type',type=str,help='Road type') #,choices = ['concrete','ice','gravel','sand'],
parameter_parser.add_argument('road_condition',type=str,help='Road condition wet or dry.')#choices = ['dry','wet'],
parameter_parser.add_argument('--inclination',type=str,help='Road inclination optional.')
param_pars_args = parameter_parser.parse_args() 
print(param_pars_args)

# If optional parameters are None -> assign standard values
if param_pars_args.mass is None:
  param_pars_args.mass = 1000
if param_pars_args.inclination is None:
  param_pars_args.inclination = 0

# Rule of Thumb Calculation:
# Calculate time for sstop and sstop_danger
def rule_of_thumb(velocity= float(param_pars_args.velocity)):
  kmh_to_ms = 3.6
  velocity = velocity*kmh_to_ms # conversion from m/s in km/h needed for RoT
  snormal = (velocity/10)**2
  sdanger = snormal*0.5
  sreaction = (velocity/10)*3
  sstop = snormal + sreaction
  sstop_danger = sdanger + sreaction
  sstop_vector = np.arange(0,sstop+0.1,0.1)
  sstop_danger_vector = np.arange(0,sstop_danger+0.1,0.1)
  
  #Time calculation and vector-generation
  t_sstop_danger = (sstop_danger_vector / (velocity/kmh_to_ms))
  t_sstop = (sstop_vector / (velocity/kmh_to_ms))
  
  return(sstop_vector,sstop_danger_vector,t_sstop,t_sstop_danger)

#Precise Calculation of breaking distance:
def calc_decelleration(mass=float(param_pars_args.mass), velocity=float(param_pars_args.velocity), road_type=param_pars_args.road_type
                       , road_condition=param_pars_args.road_condition, inclination=float(param_pars_args.inclination)):
  
  #Calculate degrees in radians:
  #from https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html
  inclination = np.deg2rad(inclination)

  if road_type == 'concrete' and 'dry':
    road_µ = concrete_dry
  elif road_type == 'concrete' and 'wet':
    road_µ = concrete_wet
  elif road_type == 'ice' and 'dry':
    road_µ = ice_dry
  elif road_type == 'ice' and 'wet':
    road_µ = ice_wet
  elif road_type == 'gravel' and 'dry':
    road_µ = gravel_dry
  elif road_type == 'sand' and 'dry':
    road_µ = sand_dry
  else: 
    print("Wrong input!")

  if inclination == 0:
    accel = g*road_μ
  else:
    #calculation with inclination:
    accel = g*road_μ*np.cos(inclination)+g*np.sin(inclination)
    
  #Calculation of timevector with a=g*µ and t = v/a
  stop_time = velocity/accel
  time_vector = np.arange(0,stop_time+0.1,0.1) #from https://numpy.org/doc/stable/reference/generated/numpy.arange.html
  calc_vel_array = []
  calc_s_stop_array = []

  #Calculation of distance and velocity vector!
  for t in time_vector:
    calc_vel = velocity-accel*t
    calc_s_stop = calc_vel*t+0.5*accel*t**2

    #Store all values in arrays:
    calc_vel_array.append(calc_vel)
    calc_s_stop_array.append(calc_s_stop)
  
  return (calc_vel_array,calc_s_stop_array,time_vector)


#===============
# a method
def main_method():
  sstop_vector,sstop_danger_vector,t_sstop,t_sstop_danger = rule_of_thumb()
  calc_v, calc_s,t_vector = calc_decelleration()
  plot_calculation(calc_v, calc_s,t_vector,sstop_vector,sstop_danger_vector,t_sstop,t_sstop_danger)
  
#===============
# do work and call a methode
main_method()
#terminate program
sys.exit()
