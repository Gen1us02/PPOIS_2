def get_initial_data_for_sensor_type(sensor_type_name: str) -> dict:
    type_name_lower = sensor_type_name.lower()
    if type_name_lower == "температурный":
        return {"temperature": 27, "temp_unit": "C"}
    elif type_name_lower == "оптический":
        return {"object_count": 0}
    elif type_name_lower == "дистанционный":
        return {"distance": 0, "dist_unit": "m"}
    elif type_name_lower == "gps":
        return {"latitude": 53.9, "longitude": 27.34}
    return {}
