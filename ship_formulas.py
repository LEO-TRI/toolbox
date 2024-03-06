from math import pi

rotational_efficiency = 1

def compute_length_perpendicular(len_waterline : float):
    return 0.96 - 0.98  * len_waterline #NOTE: not sure how that works to avoid negative numbers

def compute_block_coefficient(volume_displaced : float, len_waterline : float, breadth_waterline : float, draught : float):
    return volume_displaced / (len_waterline * breadth_waterline * draught)

def compute_midship_coefficient(midship_area : float, breadth_waterline : float, draught : float):
    return midship_area / (breadth_waterline * draught)

def compute_calculate_deadweight(displacement : float, lightweight : float):
    return displacement - lightweight

def compute_prismatic_coefficient(volume_displaced : float,
                          midship_area : float,
                          len_waterline : float,
                          breadth_waterline : float,
                          draught : float
                          ):
    
    return (compute_block_coefficient(volume_displaced, len_waterline, breadth_waterline, draught) 
            / compute_midship_coefficient(midship_area, breadth_waterline, draught)
            )

def compute_fitness_ratio(volume_displaced : float, len_waterline : float):
    return len_waterline / volume_displaced**(1/3)

def compute_froude_number(len_waterline : float, speed : float, g: float=9.81):
    return speed / (len_waterline * g)**(1/2)

def compute_wetted_area(len_waterline : float, volume_displaced : float, draught : float):
    
    length_perpendicular = compute_length_perpendicular(len_waterline)
    return 1.025 * ((volume_displaced / draught) + (1.7 * length_perpendicular * draught))

def compute_dynamic_pressure(speed : float, density: int=997):
    """
    Density rho is set by default to water, but can be changed to measure resistance to air for instance

    Parameters
    ----------
    speed : float
        _description_
    density : int, optional
        _description_, by default 997

    Returns
    -------
    _type_
        _description_
    """
    return 0.5 * density * speed**2

def compute_reference_force(speed : float, len_waterline : float, volume_displaced : float, draught : float, density: int=997):
    return compute_dynamic_pressure(speed, density) * compute_wetted_area(len_waterline, volume_displaced, draught)

def compute_advance_ratio(water_speed, rotation_per_minutes, diameter_propeller):
    return water_speed / (rotation_per_minutes * diameter_propeller)

def compute_thrust_coefficient(thrust_force : float, rotation_per_minutes, diameter_propeller, density: int=997):
    return thrust_force / (density * rotation_per_minutes**2 * diameter_propeller**4)

def compute_torque_coefficient(propulsion_power, rotation_per_minutes, diameter, density: int=997):
    return propulsion_power / (2 * pi * rotation_per_minutes**3 * diameter**5 * density)

def compute_apparent_slip(speed, rotation_per_minutes, density):
    return 1 - (speed / (rotation_per_minutes * density))

def compute_real_slip(water_speed, rotation_per_minutes, density):
    return 1 - (water_speed / (rotation_per_minutes * density))

def compute_open_water_efficiency(thrust_coefficient, torque_coefficient, advance_ratio):
    return (thrust_coefficient / torque_coefficient) * (advance_ratio / (2 * pi))

