import re


def compare_versions(first_version: str, second_version: str) -> bool:
    v1_parts = list(map(int, first_version.split(".")))
    v2_parts = list(map(int, second_version.split(".")))

    for i in range(max(len(v1_parts), len(v2_parts))):
        v1_value = v1_parts[i] if i < len(v1_parts) else 0
        v2_value = v2_parts[i] if i < len(v2_parts) else 0
        if v1_value != v2_value:
            return v1_value > v2_value

    return True


def validate_version(version: str) -> bool:
    pattern = re.compile(r"^\d+(?:\.\d+)+$")

    return pattern.match(version)
