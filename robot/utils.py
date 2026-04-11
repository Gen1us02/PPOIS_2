def convert_from_library_sensor(lib_sensor):
    if lib_sensor == "temperature":
        return "Температурный"

    if lib_sensor == "optical":
        return "Оптический"

    if lib_sensor == "gps":
        return "GPS"

    return "Дистанционный"

def convert_to_library_sensor(sensor):
    if sensor == "Температурный":
        return "TEMPERATURE"

    if sensor == "Оптический":
        return "OPTICAL"

    if sensor == "GPS":
        return "GPS"

    return "DISTANCE"
