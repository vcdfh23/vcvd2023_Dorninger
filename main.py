__doc__ = "sample file for a main methode"

#import system libs
import argparse
import sys
#from scipy import constants



#own modules
from examples.plot_example import exec_sample_plot_

#Fricition coefficents
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
parameter_parser.add('mass',type=int,help='Mass of the vehicle.')
parameter_parser.add('velocity',type=int,help='Velocity of the vehicle.')
parameter_parser.add('road_type',type=str,help='Road type')
parameter_parser.add('road_condition',type=str,help='Road condition wet or dry.')
parameter_parser.add('inclination',type=int,help='Road inclination (optional).')
param_pars_args = parameter_parser.parse_args()





#===============
# a method
def main_method():
  

  ###
  ### Code from Prof. Altinger
  main_method.__doc__ = "sample main method"
  exec_sample_plot_(cmd_call_args_.pdf_file_out)

#===============
# do work and call a methode
main_method()

#terminate program
sys.exit()
