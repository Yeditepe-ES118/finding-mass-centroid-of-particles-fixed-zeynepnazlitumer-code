import numpy as np


def centroid(p1x, p1y, p2x, p2y, p3x, p3y, m1, m2, m3):
    positions = np.array([[p1x, p2x, p3x],
                          [p1y, p2y, p3y]])

    masses = np.array([m1, m2, m3]) #1-D
    
    tot_mass = np.sum(masses)
    
    cx = (positions[0,:]*masses) / tot_mass
    cy = (positions[1,:]*masses) / tot_mass
    
    
    return tot_mass,cx, cy
    
centroid(0,0,0,1,1,0,3,4,5)