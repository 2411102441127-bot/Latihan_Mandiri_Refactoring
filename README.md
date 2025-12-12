# Latihan_Mandiri_Refactoring
# Refactoring Sistem Validasi Registrasi Mahasiswa

## 1. Analisis Pelanggaran SOLID

### a. SRP (Single Responsibility Principle)
Kode awal memiliki satu class yang menangani banyak jenis validasi sekaligus (SKS, Prasyarat, Semester).  
Hal ini melanggar SRP karena 1 class harus memiliki 1 tanggung jawab.

### b. OCP (Open/Closed Principle)
Jika ingin menambah validasi baru, harus mengubah isi method validate() dan menambah if/else.  
Ini melanggar OCP.

### c. DIP (Dependency Inversion Principle)
Kode awal bergantung pada string dan logika konkret, bukan abstraksi (interface).  
Ini melanggar DIP.

---

## 2. Sebelum Refactoring

```python
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

## 3. Sesudah Refactoring(SRP + OCP + DIP)

from abc import ABC, abstractmethod

class IValidator(ABC):
    @abstractmethod
    def validate(self, data):
        pass

class SKSValidator(IValidator):
    def validate(self, data):
        return data <= 24

class PrasyaratValidator(IValidator):
    def validate(self, data):
        return data is True

class SemesterValidator(IValidator):
    def validate(self, data):
        return 1 <= data <= 8

class ValidatorManager:
    def _init_(self, validator: IValidator):
        self.validator = validator

    def do_validate(self, data):
        return self.validator.validate(data)
