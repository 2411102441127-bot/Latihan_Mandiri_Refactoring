from abc import ABC, abstractmethod

# abstract validator
class Validator(ABC):
    @abstractmethod
    def validate(self, data):
        pass

# Validator Class Sesuai SRP
# validator sks
class SKSValidator(Validator):
    def validate(self, data):
        return data <= 24

# validator prasyarat
class PrasyaratValidator(Validator):
    def validate(self, data):
        return data["lulus_prasyarat"] == True

# validator semester (challenge OCP)
class SemesterValidator(Validator):
    def validate(self, data):
        return 1 <= data <= 8

# manager (DIP + OCP)
class ValidatorManager:
    def __init__(self, validator: Validator):
        self.validator = validator

    def do_validate(self, data):
        return self.validator.validate(data)


# testing
print("Validasi SKS:", ValidatorManager(SKSValidator()).do_validate(20))
print("Validasi Prasyarat:", ValidatorManager(PrasyaratValidator()).do_validate({"lulus_prasyarat": True}))
print("Validasi Semester:", ValidatorManager(SemesterValidator()).do_validate(4))
