
# Water Influx history matching using the Van Everdingen - Hurst dimensionless variables for water encroachment
# Source: L.P Dake “Fundamentals of Reservoir Engineering” pp. 310 – 314, 1978.
# Author: Olagunju Daniel

# Problem

# A wedge-shaped reservoir is suspected of having a fair strong natural water drive. The geometry of
# the reservoir-aquifer system is shown below. The reservoir was at bubble point at the initial condition
# with no gas cap (m=0). Develop a computer program that will Perform history matching of the
# reservoir using the production and PVT data given below.

# Hint: Use Klins et al paper: “A Polynomial approach to the Van Everdingen - Hurst dimensionless
# variables for water encroachment”

# Other data given 

import matplotlib.pyplot as plt
from we_functions import (f_function,rd_function,b_function, qd_function, td_function, water_influx_function,wd_function)
from mb_functions import (mbf_function,mbe_function, feo_function, weo_function)

# Original Values
h = 100                     # Aquifer height (ft)
k = 200                     # Permeability (mD)
miu = 0.55                  # Viscosity of Water (cp)
poro = 0.25                 # Porosity 
cw = 0.000003               # water compressibility (1/psi)
cf = 0.000004               # fluid compressibility (1/psi) 
bw = 1.0                    # formation volume factor of water (stb/scf) 
n = 312000000               # Oil in place (stb) 
sw = 0.05                   # connate water saturation 
thita = 140                 # angle of encroachment 
re =   92000                # radius to perimeter of aquifer (ft)
ro = 9200                   # radius to perimeter of reservoir (ft)

dp_array = [120, 225, 196, 170, 146, 123, 105, 84, 64, 47, 0]   # change in pressure data (psia)
time_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                 #time (years)
Np_array = [0, 7.88, 18.42, 29.15, 40.69, 50.14, 58.42, 65.39, 70.74, 74.54, 77.43]                 #Cumulative Oil Produces (MMstb)
Rp_array = [650, 760, 845, 920, 975, 1025, 1065, 1095, 1120, 1145, 1160]                 #Rp (scf/stb)
Rs_array = [650, 592, 545, 507, 471, 442, 418, 398, 383, 381, 364]                 #Rs (scf/stb)
Bo_array = [1.404, 1.374, 1.349, 1.329, 1.316, 1.303, 1.294, 1.287, 1.280, 1.276, 1.273]                 #Bo (rb/stb)
Bg_array = [0.00093, 0.00098, 0.00107, 0.00117, 0.00128, 0.00139, 0.00150, 0.00160, 0.00170, 0.00176, 0.00182]                 #Bg (rb/scf)

# Step I
# Calculate the Water influx parameters  as follows
f = f_function(thita)           # fraction of perimeter of circle that orignal oil/water boundary constitutes
rd = rd_function(re,ro)         # dimensionless radius
b = b_function(poro,h,cw,cf,ro,f)  # aquifer constant (bbl/psi)

# Step 2
# Calculate for dimensionless water flow rate qd

td_result_array = td_function(time_array,k,poro,miu,cw,cf,ro)
reversed_qd, qd_array= qd_function(rd,td_result_array)


# Step 3
# Calculate the Cumulative Water Influx
We = water_influx_function(b,dp_array, reversed_qd)

# step 4
mbf = mbf_function(Np_array, Bo_array, Bg_array, Rp_array, Rs_array)

# step 5
mbe = mbe_function(Bo_array, Bg_array, Rs_array)

# step 6
wd_array = wd_function(b,dp_array,qd_array)
f_eo = feo_function(mbf, mbe)
w_eo = weo_function(wd_array, mbe)

# Step 7
# Plot of F/Eo against We/Eo
plt.plot(w_eo,f_eo)
plt.ylabel('F/Eo')
plt.xlabel('W/Eo')
plt.show()

# print("<----------------- INPUTS -------------------->")
# print("Height: "+str(h)+" ft")
# print("Permeability: "+str(k)+" mD")
# print("Porosity: "+str(poro))
# print("re: "+str(re)+" ft")
# print("ro: "+str(ro)+" ft")
# print("thita: "+str(thita)+" deg")
# print("<--------------------------------------------->")
# print("<----------------- OUTPUT -------------------->")
# print("<--------------------------------------------->")
# print("<--------------------------------------------->")
# print("dimensionless radius: "+str(rd))
# print("aquifer constant: "+str(b)+" bbl/psi")
# print("<-----------------Cummulative Water Influx after "+str(len(time_array)-1)+" Years-------------------->")
# print(str(We)+" MMbbls")
# print("<-----------------F/Eo-------------------->")
# print(str(We)+" MMbbls")




