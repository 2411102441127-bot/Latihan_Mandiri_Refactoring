class ValidatorManager:
    def validate(self, jenis, data):
        if jenis == "sks":
            return data <= 24
        elif jenis == "prasyarat":
            return data == True
        elif jenis == "semester":
            return 1 <= data <= 8
        else:
            return False


# testing
vm = ValidatorManager()
print("Validasi SKS:", vm.validate("sks", 20))
print("Validasi Prasyarat:", vm.validate("prasyarat", True))
print("Validasi Semester:", vm.validate("semester", 5))
