import numpy as np

def length_perpendicular(len_waterline : int):
    return 0.96 - 0.98  * len_waterline

def block_coefficient(volume_displaced : float, len_waterline : float, breadth_waterline : float, draught : float):
    return volume_displaced / (len_waterline * breadth_waterline * draught)

def midship_coefficient(midship_area : float, breadth_waterline : float, draught : float):
    return midship_area / (breadth_waterline * draught)

def calculate_deadweight(displacement : float, lightweight : float):
    return displacement - lightweight

def prismatic_coefficient(volume_displaced : float,
                          midship_area : float,
                          len_waterline : float,
                          breadth_waterline : float,
                          draught : float
                          ):
    
    return (block_coefficient(volume_displaced, len_waterline, breadth_waterline, draught) 
            / midship_coefficient(midship_area, breadth_waterline, draught)
            )

def fitness_ratio(volume_displaced : float, len_waterline : float):
    return len_waterline / volume_displaced**(1/3)