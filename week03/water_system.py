def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column in meters."""
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height):
    """Calculate the presure gain from water column height in kilopascals."""
    