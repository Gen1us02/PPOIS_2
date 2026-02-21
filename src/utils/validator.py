class Validator:
    @staticmethod
    def validate_fio_part(fio_part: str) -> bool:
        if Validator.is_empty(fio_part):
            return False
        
        if Validator.contains_number(fio_part):
            return False
        
        return True
    
    @staticmethod
    def is_empty(string: str) -> bool:
        return not string
    
    @staticmethod
    def contains_number(string: str) -> bool:
        return any(ch in "0123456789" for ch in string)
    
    @staticmethod
    def score_validation(number: int) -> bool:
        return 0 < number <= 10