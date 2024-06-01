# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # Earth's acceleration due to gravity 
WATER_DENSITY = 998.2  # Density of water
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Dynamic viscosity of water in Pa.s 

PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65  # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018  # (unitless)
HOUSEHOLD_VELOCITY = 1.75  # (meters / second)


def water_column_height(tank_height, water_height):
    """Calculates the height of water column."""
    return tank_height - water_height


def pressure_gain_from_water_height(height):
    """Calculates the pressure gained from a height of water."""
    return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height


def pressure_loss_from_pipe(length, diameter, flow_rate, friction_factor):
    """Calculates the pressure loss due to pipe friction."""
    velocity = (4 * flow_rate) / (3.14159 * diameter ** 2)
    return (friction_factor * length / diameter) * (WATER_DENSITY * velocity ** 2 / 2)


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the pressure loss due to the fittings."""
    return -0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the Reynolds number."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates the pressure loss due to a reduction in pipe's diameter."""
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * fluid_velocity ** 2 / 2000


def kpa_to_psi(kpa):
    """Converts pressure from kilopascals to pounds per square inch (psi)."""
    return kpa * 0.145038


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")


if __name__ == "__main__":
    main()
