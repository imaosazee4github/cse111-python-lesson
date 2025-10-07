# Enhancements:
# 1. Program defines and uses constants for Earth's gravity, water density, and water viscosity.
# 2. Program includes a function (kpa_to_psi) that converts kilopascals to pounds per square inch (psi).
# 3. Program prints final pressure in both kPa and psi.
# PVC Schedule 80 pipe

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters) 11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013 # (unitless)
SUPPLY_VELOCITY = 1.65 # (meters / second)

# HDPE SDR11 pipe

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters) 1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018 # (unitless)
HOUSEHOLD_VELOCITY = 1.75 # (meters / second)

# Physical constants

WATER_DENSITY = 998.2 # density of water (kg/m^3)
GRAVITY = 9.80665 # acceleration due to gravity (m/s^2)
WATER_VISCOSITY = 0.0010016 # dynamic viscosity (Pa·s = kg/(m·s))

def water_column_height(tower_height, tank_height):
    """Compute the equivalent water column height (tower + 3/4 of tank)."""
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    """Compute pressure gain (kPa) from water column height (m)."""
    return (WATER_DENSITY * GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Compute pressure loss (kPa) in a pipe from length, diameter, and velocity."""
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Compute pressure loss (kPa) due to fittings (e.g., 90° angles)."""
    return -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
     """Compute Reynolds number (unitless)."""
     return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Compute pressure loss (kPa) due to sudden pipe diameter reduction."""
    k = (0.1 + 50 / reynolds_number) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000

def kpa_to_psi(pressure_kpa):
    """Convert pressure from kilopascals (kPa) to pounds per square inch (psi)."""
    return pressure_kpa * 0.145038


def main():
# User input
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    # Pressure from water height
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    #first section
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    #second section
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    

# Output results in kPa and psi 
    pressure_psi = kpa_to_psi(pressure) 
    print(f"Pressure at house: {pressure:.1f} kPa ({pressure_psi:.1f} psi)")

if __name__ == "__main__":
    main()