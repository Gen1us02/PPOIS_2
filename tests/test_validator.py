from source.validator import Validator


def test_compare_versions():
    first_version = "1.0.0"
    second_version = "1.5.4"
    assert not Validator.compare_versions(first_version, second_version)
    first_version = "3.0"
    second_version = "1.0.12"
    assert Validator.compare_versions(first_version, second_version)


def test_validate_version():
    assert Validator.validate_version("1.12.3")
    assert not Validator.validate_version("akdakda")
    assert not Validator.validate_version("")
