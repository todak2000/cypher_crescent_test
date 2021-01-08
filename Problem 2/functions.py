import math

# convert temperature values from fahrenheit to rankine
def temp_converter(temperature):
    rankine = (temperature + 460)
    return rankine

# convert values in percentage to decimals
def percent_converter(value):
    result = (value /100)
    return result

# pseudo critical pressure function
def pseudo_pressure(sg):
    ppc = 667 + (15*sg) - (37.5*sg*sg)
    return ppc

# pseudo critical temperature function
def pseudo_temp(sg):
    tpc = 168 + (325*sg) - (12.5*sg*sg)
    return tpc

# pseudo critical pressure (non-HC components) function
def pseudo_pressure_prime(ppc,c,h,n):
    ppc_prime = ppc + (440*c) + (600*h)- (170*n)
    return ppc_prime

# pseudo critical temperature (non-HC components) function
def pseudo_temp_prime(tpc, c,h,n):
    tpc_prime =  tpc + (80*c) + (130*h)- (250*n)
    return tpc_prime

# pseudo reduced temperature function
def reduced_temp(temperature, tpc_prime):
    tpr = (temperature / tpc_prime)
    return tpr

# pseudo reduced pressure function
def reduced_pressure(pressure, ppc_prime):
    ppr = (pressure / ppc_prime)
    return ppr

# temperature reciprocal (t) function
def reciprocal_temp(tpr):
    rt = (1 / tpr)
    return rt

# The non-linear euation as proposed by Ikoku page 46
#  was splited into 4(a, c, d, and e) parts as seen below
# The function proper is represented as y_function
def a_function(t):
    a_result = (0.06125*t)*math.exp(-1.2*((1 - t)**2))
    # print("a-value:" +str(a_result))
    return round(a_result, 6)

def c_function(t):
    c_result = (14.76*t - 9.76*(t**2) + 4.58*(t**3))
    # print("c-value:" +str(c_result))
    return round(c_result, 6)

def d_function(t):
    d_result = (90.7*t - 242.2*(t**2) + 42.4*(t**3))
    # print("d-value:" +str(d_result))
    return round(d_result, 6) 

def e_function(t):
    e_result = 2.18 + 2.82*t
    # print("e-value:" +str(e_result))
    return round(e_result, 6) 

#Newton-Raphson iteration initiated here
def y_function(ppr,t):
    try:
        y = 0.01        
        y_array = []
        while y < 100:
            y_array.append(y)
            for i in y_array:
                f_y = -(a_function(t)*ppr) + (i + i**2 + i**3 - i**4)/((1 - i)**3) - (c_function(t)*(i**2)) + (d_function(t)*(i**((e_function(t)))))
                if f_y <= 0.005 and f_y >= -0.005:
                    # print("y-value:" +str(i))
                    # print("f_y-value:" +str(f_y))
                    # print ('y should be: {0}'.format(i))
                    return i 
            y += 0.01
            
    except Exception:
        error_message = "sorry! something went wrong"
        return error_message

def z_fac(ppr,t,y):
    try:
        z= (a_function(t)*ppr)/y
    
    except ZeroDivisionError:
        z = "unknown"
    except Exception:
        z = "sorry! something went wrong"
    return z