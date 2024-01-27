__doc__ = "sample file for ploting method \
           baed on \
           https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

#based on
#src: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

#required imports
import matplotlib.pyplot as plt

#Plot exact calculation and Rule of Thumb in one PDF-Document:
def plot_calculation(calc_v, calc_s,
                     t_vector,sstop_vector,
                     sstop_danger_vector,
                     t_sstop,t_sstop_danger):
  fig,ax = plt.subplots(1,4,figsize=(18,5))
  ax[0].plot(t_vector,calc_v)
  ax[0].set_xlabel("Time [s]")
  ax[0].set_ylabel("Velocity [m/s]")
  ax[0].set_title("Velocity reduction\n", fontweight ="bold")
  ax[0].grid(True)
  ax[1].plot(t_vector,calc_s)
  ax[1].set_xlabel("Time [s]")
  ax[1].set_ylabel("Distance [m]")
  ax[1].set_title("Distance \n", fontweight ="bold")
  ax[1].grid(True)
  ax[2].plot(t_sstop,sstop_vector)
  ax[2].set_xlabel("Time[s]")
  ax[2].set_ylabel("Distance [m] (sstop)")
  ax[2].set_title("sstop (Rule of thumb)\n", fontweight ="bold")
  ax[2].grid(True)
  ax[3].plot(t_sstop_danger,sstop_danger_vector)
  ax[3].set_xlabel("Time [s]")
  ax[3].set_ylabel("Distance [m] (sstop_danger)")
  ax[3].set_title("sstop_danger (Rule of thumb) \n", fontweight ="bold")
  ax[3].grid(True)
  plt.savefig("s2310710003.pdf")
  print("s2310710003.pdf has been built!")
