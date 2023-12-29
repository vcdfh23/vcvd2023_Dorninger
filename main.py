__doc__ = "sample file for a main methode"

#import system libs
import argparse
import sys

#own modules
from examples.plot_example import exec_sample_plot_


#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("pdf_file_out", type=str, help="filename to plot")
cmd_call_args_ = arg_parser_.parse_args()
print (cmd_call_args_.pdf_file_out)

#===============
# a method
def main_method():
  main_method.__doc__ = "sample main method"
  exec_sample_plot_(cmd_call_args_.pdf_file_out)

#===============
# do work and call a methode
main_method()

#terminate program
sys.exit()
