# Refleksi Mengapa pendekatan Dependency injection lebih efektif mencegah code smell dari pada menggunakan method if/else

1. Menghindari Long If–Else (Code Smell)
if/else membuat kode panjang dan sulit dibaca saat metode terus bertambah.
DI mengganti if/else dengan polimorfisme, sehingga kode tetap bersih.

2. Mencegah Pelanggaran Open–Closed Principle
Dengan if/else, setiap metode baru harus mengubah kode lama.
Dengan DI, fitur baru cukup menambah class baru, tanpa mengubah kode utama.


3. Mengurangi Tight Coupling
if/else membuat kelas bergantung pada detail implementasi.
DI membuat kelas bergantung pada interface, sehingga lebih fleksibel.


4. Lebih Mudah Dites
if/else sulit dimock saat testing.
DI memungkinkan inject mock/fake object untuk pengujian.

5. Kode Lebih Mudah Dirawat & Dikembangkan
Perubahan kecil tidak berdampak ke banyak bagian.
Risiko bug saat pengembangan lanjutan lebih kecil.

Pendekatan Dependency Injection membuat kode lebih modular, mudah diuji, dan mudah dikembangkan tanpa mengubah struktur existing. Dibanding menggunakan if/else, DI membantu mengurangi code smell dan menjaga kode mengikuti prinsip SOLID, terutama DIP dan OCP.
