import gc
import weakref


class Ruangan:
    total_ruangan = 0

    def __init__(self, nama, luas):
        self.nama = nama
        self.luas = luas
        Ruangan.total_ruangan += 1

    def __del__(self):
        type(self).total_ruangan -= 1

    def tampilkan_info(self):
        print(f"  - {self.nama} ({self.luas} m2)")

class Perumahan:
    nama_perumahan = "Rae Perumahan"
    lokasi = "Jl. Harmoni"
    total_rumah = 0

    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.daftar_rumah = []

    def tampilkan_info(self):
        print("Kode Perumahan :", self.kode)
        print("Nama Perumahan :", self.nama)
        print("Lokasi         :", Perumahan.lokasi)
        print("Jumlah Rumah   :", len(self.daftar_rumah))

    def tambah_rumah(self, rumah):
        """Objek rumah dibuat di luar, lalu hanya 'dimasukkan' ke perumahan."""
        if rumah in self.daftar_rumah:
            print(f"Rumah {rumah.kode_rumah} sudah terdaftar!")
            return
        self.daftar_rumah.append(rumah)
        print(f"Rumah {rumah.kode_rumah} masuk ke {self.nama}.")

    def hapus_rumah(self, kode_rumah):
        """Rumah dikeluarkan dari perumahan, tetapi objeknya TETAP ADA."""
        for rumah in self.daftar_rumah:
            if rumah.kode_rumah == kode_rumah:
                self.daftar_rumah.remove(rumah)
                print(f"Rumah {kode_rumah} dikeluarkan dari {self.nama}.")
                return rumah
        print(f"Rumah {kode_rumah} tidak ditemukan!")
        return None

    def tampilkan_daftar_rumah(self):
        print(f"Daftar rumah di {self.nama}:")
        if not self.daftar_rumah:
            print("  (kosong)")
        for rumah in self.daftar_rumah:
            print(f"  - {rumah.kode_rumah} | Tipe {rumah.tipe} | {rumah.status}")

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

    def __init__(self, kode_rumah, tipe, harga, harga_modal=None):
        self.kode_rumah = kode_rumah
        self.tipe = tipe

        self._harga = harga
        self._status = "Kosong"

        self.__harga_modal = harga_modal if harga_modal is not None else harga * 0.8

        self.pemilik = None

        self.__daftar_ruangan = []

        Rumah.total_rumah += 1
        Perumahan.total_rumah += 1

    def tampilkan_info(self):
        print("Kode Rumah :", self.kode_rumah)
        print("Tipe       :", self.tipe)
        print("Harga      : Rp{:,.0f}".format(self._harga))
        print("Status     :", self._status)
        print("Pemilik    :", self.pemilik.nama if self.pemilik else "-")
        if self.__daftar_ruangan:
            print("Ruangan    :")
            for ruangan in self.__daftar_ruangan:
                ruangan.tampilkan_info()

    def hitung_harga_akhir(self):
        return self._harga

    def hitung_margin(self):
        return self._harga - self.__harga_modal

    def tambah_ruangan(self, nama, luas):
        """Ruangan DIBUAT di dalam Rumah, bukan dari luar."""
        self.__daftar_ruangan.append(Ruangan(nama, luas))

    @property
    def daftar_ruangan(self):
        return list(self.__daftar_ruangan)

    def total_luas_ruangan(self):
        return sum(r.luas for r in self.__daftar_ruangan)

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru > 0:
            self._harga = harga_baru
            print("Harga berhasil diubah.")
        else:
            print("Harga harus lebih dari 0!")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status_baru):
        if status_baru in ["Kosong", "Terisi"]:
            self._status = status_baru
            print("Status berhasil diubah.")
        else:
            print("Status hanya boleh 'Kosong' atau 'Terisi'!")

    @classmethod
    def buat_rumah(cls, data):
        return cls(**data)

    @staticmethod
    def validasi_harga(harga):
        return harga > 0

class RumahSubsidi(Rumah):
    def __init__(self, kode_rumah, tipe, harga, subsidi_pemerintah, harga_modal=None):
        super().__init__(kode_rumah, tipe, harga, harga_modal)
        self.subsidi_pemerintah = subsidi_pemerintah

    def hitung_harga_akhir(self):
        return self._harga - self.subsidi_pemerintah

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jenis      : Rumah Subsidi")
        print("Subsidi    : Rp{:,.0f}".format(self.subsidi_pemerintah))
        print("Harga Akhir: Rp{:,.0f}".format(self.hitung_harga_akhir()))

class RumahKomersial(Rumah):
    def __init__(self, kode_rumah, tipe, harga, fasilitas, biaya_fasilitas, harga_modal=None):
        super().__init__(kode_rumah, tipe, harga, harga_modal)
        self.fasilitas = fasilitas
        self.biaya_fasilitas = biaya_fasilitas

    def tambah_fasilitas(self, nama, biaya):
        self.fasilitas.append(nama)
        self.biaya_fasilitas += biaya

    def hitung_harga_akhir(self):
        return self._harga + self.biaya_fasilitas

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jenis      : Rumah Komersial")
        print("Fasilitas  :", ", ".join(self.fasilitas))
        print("Biaya Fasil: Rp{:,.0f}".format(self.biaya_fasilitas))
        print("Harga Akhir: Rp{:,.0f}".format(self.hitung_harga_akhir()))


class Pemilik:
    jenis_data = "Pemilik"
    negara = "Indonesia"
    total_pemilik = 0

    def __init__(self, id_pemilik, nama, no_hp):
        self.id_pemilik = id_pemilik
        self.nama = nama
        self.__no_hp = no_hp
        self.daftar_rumah = []
        Pemilik.total_pemilik += 1

    def tampilkan_info(self):
        print("ID Pemilik :", self.id_pemilik)
        print("Nama       :", self.nama)
        print("No. HP     :", self.__no_hp)
        kode = [r.kode_rumah for r in self.daftar_rumah]
        print("Rumah      :", ", ".join(kode) if kode else "-")

    def beli_rumah(self, rumah):
        if rumah.pemilik is not None or rumah.status != "Kosong":
            print(f"Rumah {rumah.kode_rumah} tidak tersedia untuk dibeli!")
            return False
        rumah.pemilik = self
        self.daftar_rumah.append(rumah)
        rumah.status = "Terisi"
        print(f"{self.nama} berhasil membeli rumah {rumah.kode_rumah}.")
        return True

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

    @classmethod
    def tambah_pemilik(cls, id_pemilik, nama, no_hp):
        return cls(id_pemilik, nama, no_hp)

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

print("Validasi kode P01:", Perumahan.validasi_kode("P01"))
print("Validasi kode A:", Perumahan.validasi_kode("A"))


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

print("Validasi harga 250000000:", Rumah.validasi_harga(250000000))
print("Validasi harga -1000:", Rumah.validasi_harga(-1000))


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
pemilik2 = Pemilik.tambah_pemilik("PM02", "Budi", "082345678901")

pemilik1.tampilkan_info()
print()

pemilik2.tampilkan_info()


print("\nSTATIC METHOD PEMILIK")
print("-" * 50)

print("Validasi nama Rae:", Pemilik.validasi_nama("Rae"))
print("Validasi nama kosong:", Pemilik.validasi_nama(""))


print("\nGETTER & SETTER PEMILIK")
print("-" * 50)

print("No. HP pemilik1 :", pemilik1.no_hp)

print("\nSetter dengan data valid:")
pemilik1.no_hp = "089876543210"
print("No. HP baru     :", pemilik1.no_hp)

print("\nSetter dengan data tidak valid:")
pemilik1.no_hp = ""


# =====================================================================
#                      LANJUTAN POSTTEST
# =====================================================================

# ---------------------------------------------------------------------
# 1. INHERITANCE
# ---------------------------------------------------------------------
print("\n" + "=" * 50)
print("INHERITANCE")
print("=" * 50)

print("\nOBJEK SUBCLASS: RUMAH SUBSIDI")
print("-" * 50)

rumah_subsidi = RumahSubsidi("R04", "36", 200000000, 25000000)
rumah_subsidi.tampilkan_info()

print("\nOBJEK SUBCLASS: RUMAH KOMERSIAL")
print("-" * 50)

rumah_komersial = RumahKomersial(
    "R05", "72", 600000000,
    ["Kolam Renang", "Smart Home"], 50000000
)
rumah_komersial.tampilkan_info()

print("\nOBJEK SUBCLASS (CLASS METHOD buat_rumah DIWARISI)")
print("-" * 50)

rumah_subsidi2 = RumahSubsidi.buat_rumah({
    "kode_rumah": "R06",
    "tipe": "30",
    "harga": 180000000,
    "subsidi_pemerintah": 20000000
})
print("Tipe objek       :", type(rumah_subsidi2).__name__)
print("Harga akhir R06  : Rp{:,.0f}".format(rumah_subsidi2.hitung_harga_akhir()))


print("\nMETHOD OVERRIDING (POLIMORFISME)")
print("-" * 50)

for r in [rumah1, rumah_subsidi, rumah_komersial]:
    print(
        f"{r.kode_rumah} ({type(r).__name__:<15}) -> "
        "Harga akhir: Rp{:,.0f}".format(r.hitung_harga_akhir())
    )


print("\nPENGECEKAN HUBUNGAN INHERITANCE")
print("-" * 50)

print("RumahSubsidi turunan Rumah   :", issubclass(RumahSubsidi, Rumah))
print("RumahKomersial turunan Rumah :", issubclass(RumahKomersial, Rumah))
print("rumah_subsidi isinstance Rumah:", isinstance(rumah_subsidi, Rumah))
print("MRO RumahSubsidi :", [c.__name__ for c in RumahSubsidi.__mro__])


print("\nATRIBUT PROTECTED & PRIVATE")
print("-" * 50)

print("Protected _harga (akses langsung) :", rumah_subsidi._harga)
print("Margin via method (data private)  : Rp{:,.0f}".format(rumah_subsidi.hitung_margin()))

try:
    print(rumah_subsidi.__harga_modal)
except AttributeError as e:
    print("Akses langsung __harga_modal ditolak ->", e)

rumah_komersial.tambah_fasilitas("Taman Pribadi", 15000000)
print("\nSetelah tambah fasilitas di subclass:")
print("Harga akhir R05 : Rp{:,.0f}".format(rumah_komersial.hitung_harga_akhir()))


print("\n" + "=" * 50)
print("RELASI UML")
print("=" * 50)

print("\nAGREGASI: PERUMAHAN o-- RUMAH")
print("-" * 50)

for r in [rumah1, rumah2, rumah3, rumah_subsidi, rumah_komersial]:
    perumahan1.tambah_rumah(r)

print()
perumahan1.tampilkan_daftar_rumah()

print("\nRumah R03 dikeluarkan dari perumahan:")
rumah_keluar = perumahan1.hapus_rumah("R03")
perumahan1.tampilkan_daftar_rumah()

print("\nObjek rumah R03 masih ada setelah dikeluarkan:")
print("Kode :", rumah_keluar.kode_rumah, "| Tipe :", rumah_keluar.tipe)
print("Rumah R03 masih bisa dimasukkan ke perumahan lain:")
perumahan2.tambah_rumah(rumah_keluar)

print("\nASOSIASI: PEMILIK -- RUMAH")
print("-" * 50)

pemilik1.beli_rumah(rumah2)
pemilik1.beli_rumah(rumah_subsidi)
pemilik2.beli_rumah(rumah2)          
pemilik2.beli_rumah(rumah_komersial)

print()
pemilik1.tampilkan_info()
print()
pemilik2.tampilkan_info()

print("\nDari sisi Rumah (asosiasi dua arah):")
print("Pemilik rumah R02 :", rumah2.pemilik.nama)
print("Pemilik rumah R05 :", rumah_komersial.pemilik.nama)

print("\nKOMPOSISI: RUMAH *-- RUANGAN")
print("-" * 50)

rumah_komersial.tambah_ruangan("Ruang Tamu", 20)
rumah_komersial.tambah_ruangan("Kamar Tidur", 15)
rumah_komersial.tambah_ruangan("Dapur", 10)

rumah_komersial.tampilkan_info()
print("\nTotal luas ruangan R05 :", rumah_komersial.total_luas_ruangan(), "m2")
print("Total objek Ruangan    :", Ruangan.total_ruangan)

print("\nRumah sementara dibuat lalu dihapus:")
rumah_sementara = Rumah("R99", "21", 100000000)
rumah_sementara.tambah_ruangan("Kamar Percobaan", 9)
ref_ruangan = weakref.ref(rumah_sementara.daftar_ruangan[0])

print("Total objek Ruangan sebelum dihapus :", Ruangan.total_ruangan)
print("Ruangan masih ada                   :", ref_ruangan() is not None)

del rumah_sementara
gc.collect()

print("Total objek Ruangan setelah dihapus :", Ruangan.total_ruangan)
print("Ruangan masih ada                   :", ref_ruangan() is not None)

print("\nTOTAL DATA")
print("-" * 50)

print("Total rumah   :", Rumah.total_rumah)
print("Total pemilik :", Pemilik.total_pemilik)