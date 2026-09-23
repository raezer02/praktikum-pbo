class Perumahan:
    nama_perumahan = "Rae Perumahan"
    lokasi = "Jl. Harmoni"
    total_rumah = 0

    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def tampilkan_info(self):
        print("Kode Perumahan :", self.kode)
        print("Nama Perumahan :", self.nama)
        print("Lokasi         :", Perumahan.lokasi)

    @classmethod
    def ubah_lokasi(cls, lokasi_baru):
        if lokasi_baru.strip() != "":
            cls.lokasi = lokasi_baru
            print("Lokasi berhasil diubah.")
        else:
            print("Lokasi tidak boleh kosong!")

    @staticmethod
    def validasi_kode(kode):
        return len(kode) >= 2


class Rumah:
    jenis_properti = "Rumah"
    status_default = "Kosong"
    total_rumah = 0

    def __init__(self, kode_rumah, tipe, harga):
        self.kode_rumah = kode_rumah
        self.tipe = tipe

        self.__harga = harga
        self.__status = "Kosong"

        Rumah.total_rumah += 1
        Perumahan.total_rumah += 1

    def tampilkan_info(self):
        print("Kode Rumah :", self.kode_rumah)
        print("Tipe       :", self.tipe)
        print("Harga      : Rp{:,.0f}".format(self.__harga))
        print("Status     :", self.__status)

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
            print("Harga berhasil diubah.")
        else:
            print("Harga harus lebih dari 0!")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru in ["Kosong", "Terisi"]:
            self.__status = status_baru
            print("Status berhasil diubah.")
        else:
            print("Status hanya boleh 'Kosong' atau 'Terisi'!")

    @classmethod
    def buat_rumah(cls, data):
        return cls(
            data["kode_rumah"],
            data["tipe"],
            data["harga"]
        )

    @staticmethod
    def validasi_harga(harga):
        return harga > 0


class Pemilik:
    jenis_data = "Pemilik"
    negara = "Indonesia"
    total_pemilik = 0

    def __init__(self, id_pemilik, nama, no_hp):

        self.id_pemilik = id_pemilik
        self.nama = nama

        self.__no_hp = no_hp

        Pemilik.total_pemilik += 1

    def tampilkan_info(self):
        print("ID Pemilik :", self.id_pemilik)
        print("Nama       :", self.nama)
        print("No. HP     :", self.__no_hp)

    @property
    def no_hp(self):
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, no_hp_baru):
        if no_hp_baru.strip() != "":
            self.__no_hp = no_hp_baru
            print("No. HP berhasil diubah.")
        else:
            print("No. HP tidak boleh kosong!")

    # Class method
    @classmethod
    def tambah_pemilik(cls, id_pemilik, nama, no_hp):
        return cls(id_pemilik, nama, no_hp)

    # Static method
    @staticmethod
    def validasi_nama(nama):
        return nama.strip() != ""



print("\nRAE PERUMAHAN")
print("-" * 50)


print("\nOBJEK PERUMAHAN")
print("-" * 50)

perumahan1 = Perumahan("P01", "Rae Harmoni")
perumahan2 = Perumahan("P02", "Rae Sejahtera")

perumahan1.tampilkan_info()
print()

perumahan2.tampilkan_info()


print("\nSTATIC METHOD PERUMAHAN")
print("-" * 50)

print(
    "Validasi kode P01:",
    Perumahan.validasi_kode("P01")
)

print(
    "Validasi kode A:",
    Perumahan.validasi_kode("A")
)


print("\nCLASS METHOD PERUMAHAN")
print("-" * 50)

Perumahan.ubah_lokasi("Jl. Harmoni Baru")

print("Lokasi sekarang :", Perumahan.lokasi)

print("\nOBJEK RUMAH")
print("-" * 50)

rumah1 = Rumah("R01", "36", 250000000)
rumah2 = Rumah("R02", "45", 350000000)

rumah1.tampilkan_info()
print()

rumah2.tampilkan_info()


print("\nSTATIC METHOD RUMAH")
print("-" * 50)

print(
    "Validasi harga 250000000:",
    Rumah.validasi_harga(250000000)
)

print(
    "Validasi harga -1000:",
    Rumah.validasi_harga(-1000)
)


print("\nCLASS METHOD RUMAH")
print("-" * 50)

data_rumah = {
    "kode_rumah": "R03",
    "tipe": "50",
    "harga": 450000000
}

rumah3 = Rumah.buat_rumah(data_rumah)

rumah3.tampilkan_info()


print("\nGETTER & SETTER RUMAH")
print("-" * 50)

print("Harga rumah1 :", rumah1.harga)

print("\nSetter dengan data valid:")
rumah1.harga = 300000000
print("Harga baru   :", rumah1.harga)

print("\nSetter dengan data tidak valid:")
rumah1.harga = -50000000

print("\nStatus awal   :", rumah1.status)

print("\nSetter status valid:")
rumah1.status = "Terisi"
print("Status baru   :", rumah1.status)

print("\nSetter status tidak valid:")
rumah1.status = "Rusak"


print("\nOBJEK PEMILIK")
print("-" * 50)
pemilik1 = Pemilik("PM01", "Rae", "081234567890")
pemilik2 = Pemilik.tambah_pemilik(
    "PM02",
    "Budi",
    "082345678901"
)

pemilik1.tampilkan_info()
print()

pemilik2.tampilkan_info()


print("\nSTATIC METHOD PEMILIK")
print("-" * 50)

print(
    "Validasi nama Rae:",
    Pemilik.validasi_nama("Rae")
)

print(
    "Validasi nama kosong:",
    Pemilik.validasi_nama("")
)


print("\nGETTER & SETTER PEMILIK")
print("-" * 50)

print("No. HP pemilik1 :", pemilik1.no_hp)

print("\nSetter dengan data valid:")
pemilik1.no_hp = "089876543210"
print("No. HP baru     :", pemilik1.no_hp)

print("\nSetter dengan data tidak valid:")
pemilik1.no_hp = ""


print("\nTOTAL DATA")
print("-" * 50)

print("Total rumah   :", Rumah.total_rumah)
print("Total pemilik :", Pemilik.total_pemilik)
