__doc__ = "sample file for a main methode"

#import system libs
import argparse
import sys
from scipy.constants import g
import numpy as np

#own modules
from examples.plot_example import exec_sample_plot_

#Fricition coefficents from Powerpoint (constants)
concrete_dry = 0.5
concrete_wet = 0.35
ice_dry = 0.15
ice_wet = 0.08
gravel_dry = 0.35
sand_dry = 0.3

#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("pdf_file_out", type=str, help="filename to plot")
cmd_call_args_ = arg_parser_.parse_args()
print (cmd_call_args_.pdf_file_out)


### parameter parser for: mass, velocity, road type, wet&dry, inclination
parameter_parser = argparse.ArgumentParser(description='Variance Parameter for calculation')
parameter_parser.add_argument('mass',type=float,default=0,help='Mass of the vehicle.')
parameter_parser.add_argument('velocity',type=float,default=28,help='Velocity of the vehicle.')
parameter_parser.add_argument('road_type',type=str,default='concrete',choices = ['concrete','ice','gravel','sand'],help='Road type')
parameter_parser.add_argument('road_condition',type=str,default='dry',choices = ['dry','wet'],help='Road condition wet or dry.')
parameter_parser.add_argument('inclination',type=int,default=0,help='Road inclination optional.')
#param_pars_args = parameter_parser.parse_args() # ERROR in this line!

#ToDO: Fix param_pars_args and change function values in method calc_decelleration
def calc_decelleration(mass=10, velocity=28, road_type='concrete', road_condition='dry', inclination=0):
  
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

  #if inclination == 0:
  
  #Calculation of timevector with a=g*µ and t = v/a
  accel = g*road_μ
  stop_time = velocity/accel
  time_vector = np.arange(0,stop_time+0.1,0.1) #from https://numpy.org/doc/stable/reference/generated/numpy.arange.html
  
  #Calculation of distance and velocity vector!
  for i in time_vector:
    calc_vel = velocity-accel*i
    calc_s_stop = calc_vel*i+0.5*accel*i**2
    print(calc_vel)


#===============
# a method
def main_method():
  
  calc_decelleration()
  ###
  ### Code from Prof. Altinger
  main_method.__doc__ = "sample main method"
  exec_sample_plot_(cmd_call_args_.pdf_file_out)

#===============
# do work and call a methode
main_method()
#terminate program
sys.exit()
