# Rae Perumahan

## Deskripsi Program

Program ini dibuat menggunakan Python dengan konsep OOP (Object Oriented Programming).

Tema yang digunakan adalah **Rae Perumahan**. Program ini digunakan untuk menyimpan dan menampilkan data perumahan, rumah, dan pemilik.

Di dalam program terdapat 3 class utama, yaitu:

* `Perumahan`
* `Rumah`
* `Pemilik`

Program ini juga menggunakan class attribute, instance attribute, method, encapsulation, getter, setter, dan validasi data.

---

## Class yang Digunakan

### 1. Class Perumahan

Class `Perumahan` digunakan untuk menyimpan data perumahan.

Atribut yang digunakan:

* `nama_perumahan` → nama perumahan
* `lokasi` → lokasi perumahan
* `total_rumah` → jumlah rumah

Atribut object:

* `kode`
* `nama`

Method yang digunakan:

* `tampilkan_info()` → menampilkan data perumahan
* `ubah_lokasi()` → mengubah lokasi menggunakan class method
* `validasi_kode()` → mengecek kode menggunakan static method

---

### 2. Class Rumah

Class `Rumah` digunakan untuk menyimpan data rumah yang ada di dalam perumahan.

Atribut class:

* `jenis_properti`
* `status_default`
* `total_rumah`

Atribut object:

* `kode_rumah`
* `tipe`
* `__harga`
* `__status`

`__harga` dan `__status` dibuat private supaya datanya tidak diubah secara langsung.

Method yang digunakan:

* `tampilkan_info()` → menampilkan data rumah
* `buat_rumah()` → membuat object rumah menggunakan class method
* `validasi_harga()` → mengecek harga menggunakan static method

Class `Rumah` juga mempunyai getter dan setter untuk:

* `harga`
* `status`

Setter digunakan untuk mengecek data sebelum data diubah.

Contohnya, harga tidak boleh kurang dari atau sama dengan 0 dan status hanya boleh `Kosong` atau `Terisi`.

---

### 3. Class Pemilik

Class `Pemilik` digunakan untuk menyimpan data pemilik rumah.

Atribut class:

* `jenis_data`
* `negara`
* `total_pemilik`

Atribut object:

* `id_pemilik`
* `nama`
* `__no_hp`

`__no_hp` dibuat private dan diakses menggunakan property.

Method yang digunakan:

* `tampilkan_info()` → menampilkan data pemilik
* `tambah_pemilik()` → membuat object pemilik menggunakan class method
* `validasi_nama()` → mengecek nama menggunakan static method

Getter dan setter digunakan untuk mengakses dan mengubah nomor HP.

Nomor HP tidak boleh diisi kosong.

---

## Konsep OOP yang Digunakan

Program ini menggunakan beberapa konsep OOP.

### Class Attribute

Class attribute adalah atribut yang digunakan bersama oleh object dalam satu class.

Contohnya:

```python
nama_perumahan = "Rae Perumahan"
lokasi = "Jl. Harmoni"
total_rumah = 0
```

### Instance Attribute

Instance attribute adalah atribut yang dimiliki oleh masing-masing object.

Contohnya:

```python
self.kode = kode
self.nama = nama
```

### Instance Method

Instance method menggunakan `self` dan digunakan untuk menjalankan fungsi pada object.

Contohnya:

```python
def tampilkan_info(self):
```

### Class Method

Class method menggunakan `@classmethod` dan `cls`.

Contohnya:

```python
@classmethod
def ubah_lokasi(cls, lokasi_baru):
```

### Static Method

Static method tidak menggunakan `self` ataupun `cls`.

Contohnya:

```python
@staticmethod
def validasi_kode(kode):
```

---

## Encapsulation dan Property

Encapsulation digunakan untuk membatasi akses langsung ke data tertentu.

Pada program ini terdapat beberapa atribut private, seperti:

```python
self.__harga
self.__status
self.__no_hp
```

Atribut tersebut tidak diakses langsung dari luar class. Sebagai gantinya digunakan `@property` sebagai getter dan setter.

Contohnya:

```python
@property
def harga(self):
    return self.__harga

@harga.setter
def harga(self, harga_baru):
    if harga_baru > 0:
        self.__harga = harga_baru
```

Dengan cara ini, data bisa diperiksa terlebih dahulu sebelum diubah.

---

## Pengujian Program

Program membuat minimal 2 object dari setiap class.

Object `Perumahan`:

```python
perumahan1 = Perumahan("P01", "Rae Harmoni")
perumahan2 = Perumahan("P02", "Rae Sejahtera")
```

Object `Rumah`:

```python
rumah1 = Rumah("R01", "36", 250000000)
rumah2 = Rumah("R02", "45", 350000000)
```

Object `Pemilik`:

```python
pemilik1 = Pemilik("PM01", "Rae", "081234567890")
pemilik2 = Pemilik.tambah_pemilik(
    "PM02",
    "Budi",
    "082345678901"
)
```

Program juga melakukan pengujian data valid dan tidak valid.

Contohnya pada harga rumah:

```python
rumah1.harga = 300000000
```

Data tersebut diterima karena harganya lebih dari 0.

Kemudian dicoba data yang tidak valid:

```python
rumah1.harga = -50000000
```

Data tersebut ditolak karena harga tidak boleh kurang dari atau sama dengan 0.

Pengujian juga dilakukan pada status rumah dan nomor HP pemilik.

---

## Cara Menjalankan Program

Pastikan Python sudah terinstall.

Buka terminal pada folder program, kemudian jalankan:

```bash
python main.py
```

Setelah dijalankan, program akan menampilkan data perumahan, rumah, pemilik, penggunaan method, serta hasil pengujian getter dan setter.

---

## Struktur File

```text
posttest/posttest_1/main.py/
│
├── main.py
│
└── README.md
```

`main.py` berisi class dan program utama, sedangkan `README.md` berisi penjelasan mengenai program.
