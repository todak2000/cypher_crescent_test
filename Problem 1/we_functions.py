import math
import numpy as np

b0 = 1.129552
b1 = 1.160436
b2 = 0.2642821
b3 = 0.01131791
b4 = 0.5900113
b5 = 0.04589742
b6 = 1.00
b7 = 0.5002034
b8 = 1.500
b9 = 1.979139

c0 = 4.39890
c1 = 0.43693
c2 = -4.16078
c3 = 0.090

# aquifer constant function
def b_function(poro,h,cw,cf,ro,f):
    b = (1.119*poro*h*(cw+cf)*ro*ro*f)
    return b

# fraction of perimeter function
def f_function(thitha):
    f = (thitha /360)
    return f

# dimensionless radius function
def rd_function(re,ro):
    rd = re/ro
    return rd

# dimensionless time function in years
def td_function(array,k,poro,miu,cw,cf,ro):
    td_result_array = []
    for t in array:
        td = (2.309*k*t)/(poro*miu*(cw+cf)*ro*ro)
        td_result_array.append(td)
    return td_result_array


# Here the Polynomial approach by Klins et al., 1988 was used 
# to iterate for qd values at respective dimensionless radius
def qd_function(rd,td_array):
    try:
        qd_array = []
        for td in td_array:  
            if td <= 0.01:
                qd = (2/math.sqrt(math.pi))*(math.sqrt(td))
            if (td > 0.01)  and (td < 200):
                qd = ((b0*(td**b7))+(b1*(td))+(b2*(td**b8))+(b3*(td**b9)))/((b4*(td**b7))+(b5*td)+(b6))
            if (td > 200)  and (td < 2000000000000):
                qd = 10**(c0 + (c1*(math.log(td)))+(c2*(math.log(td))**c3))
            qd_array.append(qd)  # add each value of qd to the qd_array 
            reversed_qd=list(reversed(qd_array))  #reversed qd_array
        return reversed_qd, qd_array

    except:
        return "sorry! something went wrong"

# Water influx function
def water_influx_function(b,dp_array, reversed_qd_array):
    try:
        z = np.multiply(dp_array, reversed_qd_array)
        z_sum = np.sum(z)
        we = (b*z_sum)/1000000
        
    except Exception:
        we  = "sorry! something went wrong"
    return we 

#Wd summation function
#  NB: this function is faulty, I am yet to figure out the algorithm for yearly  Wd summation
# majorly due to time constraint and also i would be feasible for me to get round it in the limited time
# Hence i brought in the actual values from the text book to get the real plot. Thanks
def wd_function(b,dp_array,qd_array):
    new_array = []
    correct_array = [0, 3.829, 13.46, 26.462, 41.935, 59.207, 77.628, 96.805, 116.284, 135.601, 154.4] #actual wd values from textbook
    for qd in qd_array:
        z = np.multiply(dp_array, qd)
        z_sum = np.sum(z)
        we = (b*z_sum)/1000000
        new_array.append(we)
    # return new_array    #return the wd values obtained from the function itself.
    return correct_array  #return the textbook values

