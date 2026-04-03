def get_initial_data_for_sensor_type(sensor_type_name: str) -> dict:
    type_name_lower = sensor_type_name.lower()
    if type_name_lower == "температурный":
        return {"Температура": 27, "Температурный юнит": "C"}
    elif type_name_lower == "оптический":
        return {"Количество объектов": 0}
    elif type_name_lower == "дистанционный":
        return {"Расстояние": 0, "Дистанционный юнит": "m"}
    elif type_name_lower == "gps":
        return {"Широта": 53.9, "Долгота": 27.34}
    return {}
