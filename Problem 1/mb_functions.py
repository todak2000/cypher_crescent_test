import math
import numpy as np

# F function
def mbf_function(Np_array, Bo_array, Bg_array, Rp_array, Rs_array):
    r_array = np.subtract(Rp_array,Rs_array)
    bgr_array = np.multiply(r_array, Bg_array)
    br_array = np.add(Bo_array,bgr_array)
    f_array = np.multiply(br_array, Np_array)
    return f_array

# Eo function
def mbe_function(Bo_array, Bg_array, Rs_array):
    boi = Bo_array[0]
    rsi = Rs_array[0]
    rs_new_array = []
    bo_new_array = []
    for rs in Rs_array:
        new_rs = rsi - rs
        rs_new_array.append(new_rs)

    rsbg_array = np.multiply(rs_new_array, Bg_array)

    for bo in Bo_array:
        new_bo = bo - boi
        bo_new_array.append(new_bo)
    
    mbe_array = np.add(bo_new_array,rsbg_array)
    return mbe_array

# F/Eo function
def feo_function(mbf, mbe):
    feo_array = np.divide(mbf,mbe)
    return feo_array

# We/Eo function
def weo_function(qd_array, mbe):
    weo_array = np.divide(qd_array, mbe)
    return weo_array
