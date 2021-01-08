
# Calculates the zFactor of a gas using the Hall & Yarborough method
# Source: Chi. U. Ikoku “Natural Gas Production Engineering” Wiley pp. 46 – 47, 1984.
# Author: Olagunju Daniel

# Problem

# For Natural gas with specific gravity of 0.7, at a pressure of 2000 psia and a temperature of 180 deg
# Fahrenheit, use the equations above to calculate the z-factor, considering the presence of the 
#  components: N2 = 0.5%, CO2 = 2% and H2S = 0.1%.

from functions import (temp_converter,percent_converter, pseudo_pressure, pseudo_temp, pseudo_pressure_prime, 
                        pseudo_temp_prime, reduced_temp, reduced_pressure, reciprocal_temp, y_function, z_fac)

# Original Values
g = 0.7         # Specific Gravity 
p = 2000        # Gas Pressure in Psia
t = 180         # Temperature in degree fahrenheit
yn = 0.5        # Mole fraction of Nitrogen gas
yc = 2          # Mole fraction of Carbon (IV) oxide gas
yh = 0.1          # Mole fraction of Hydrogen Sulphide 

# Test values
# g = 0.665         # Specific Gravity 
# p = 3250        # Gas Pressure in Psia
# t = 213         # Temperature in degree fahrenheit
# yn = 2.07        # Mole fraction of Nitrogen gas
# yc = 0.1          # Mole fraction of Carbon (IV) oxide gas
# yh = 0.0          # Mole fraction of Hydrogen Sulphide 


temperature = temp_converter(t)     # convert temperature from celcius to rankine
n2_mol = percent_converter(yn)      # convert nitrogen  fraction into percentage
co2_mol = percent_converter(yc)     # convert co2  fraction into percentage
h2S_mol = percent_converter(yh)     # convert h2s  fraction into percentage

# Step I
# Calculate the PSeudo Critical Pressure and Temperature 
# as a function of the Specific Gravity
ppc = pseudo_pressure(g)
tpc = pseudo_temp(g)

# Step 2
# Calculate the PSeudo Critical Pressure and Temperature 
# taking CO2, H2S and N2 into consideration 
ppc_prime = pseudo_pressure_prime(ppc,co2_mol,h2S_mol,n2_mol)
tpc_prime = pseudo_temp_prime(tpc,co2_mol,h2S_mol,n2_mol)

# Step 3
# Calculate the Pseudo Reduced Pressure and Temperature 
ppr = reduced_pressure(p,ppc_prime)
tpr = reduced_temp(temperature,tpc_prime)

# Step 4
# Calculate the reciprocal (t) of reduced Temperature 
tr = reciprocal_temp(tpr)


# Step 5
# Calculate the y value where f(y) is zero
y_value = y_function(ppr,tr)


# Step 6
# Calculate the z factor using the return y_value obtained
z_factor = z_fac(ppr,tr, y_value)
print("<----------------- INPUTS -------------------->")
print("Pressure: "+str(p)+" psia")
print("Temperature: "+str(t)+" deg F")
print("Specific Gravity: "+str(g))
print("Mol fraction of N2: "+str(yn)+" %")
print("Mol fraction of H2S: "+str(yh)+" %")
print("Mol fraction of CO2: "+str(yc)+" %")
print("<----------------- OUTPUT -------------------->")
print("z-factor: "+str(z_factor))




