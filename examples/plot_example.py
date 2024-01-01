__doc__ = "sample file for ploting method \
           baed on \
           https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

#based on
#source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

#required imports
import matplotlib.pyplot as plt
import numpy as np


def plot_correct_calc(calc_v, calc_s,t_vector):
  fig,ax = plt.subplots(1,2,figsize=(10,5))

  ax[0].plot(t_vector,calc_v)
  ax[0].set_xlabel("time")
  ax[0].set_ylabel("velocity [m/s]")
  ax[0].set_title("Velocity reduction\n\n", fontweight ="bold")

  ax[1].plot(t_vector,calc_s)
  ax[1].set_xlabel("time")
  ax[1].set_ylabel("Distance [m]")
  ax[1].set_title("Distance \n\n", fontweight ="bold")

  plt.savefig("test.pdf")

  """ fig1 = plt.figure()
  #add one plot
  ax1 = fig1.add_subplot(111)
  
  #define plots
  ax1.plot(t_vector,calc_v,color ="green", lw = 2)

  #add axis label
  ax1.set_xlabel("time")
  ax1.set_ylabel("velocity [m/s]")

  #add plot label
  fig1.suptitle("Velocity reduction\n\n", fontweight ="bold")  
  plt.savefig('Velocity_red.png')

  fig2 = plt.figure()
  #add one plot
  ax2 = fig2.add_subplot(111)
  
  #define plots
  ax2.plot(t_vector,calc_s,color ="green", lw = 2)

  #add axis label
  ax2.set_xlabel("time")
  ax2.set_ylabel("distance [m]")

  #add plot label
  fig2.suptitle("Breaking distance\n\n", fontweight ="bold")  
  plt.savefig('breaking_distance.png')

 """


  #fig.hold()
#================================================
def exec_sample_plot_(file_name_out):
  exec_sample_plot_.__doc__ = "sample call to mathplotlib"

  #define figure
  fig = plt.figure()
  #add one plot
  ax1 = fig.add_subplot(111)

  #data
  t = np.arange(0.0, 1.0, 0.01)
  s = np.sin(2 * np.pi * t)
  #define plots
  ax1.plot(t, s, color ="green", lw = 2)

  #add axis label
  ax1.set_xlabel("time")
  ax1.set_ylabel("sin (2 pi t)")

  #add plot label
  fig.suptitle("Plot Sample\n\n", fontweight ="bold")

  #export as PDF
  plt.savefig(file_name_out)
  