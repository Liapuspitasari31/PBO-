class Sekolah:
    def __init__(self, nama, akreditasi, jurusan):
        self.__nama = nama
        self.__akreditasi = akreditasi
        self.__jurusan = jurusan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_akreditasi(self):
        return self.__akreditasi

    def set_akreditasi(self, akreditasi):
        self.__akreditasi = akreditasi

    def get_jurusan(self):
        return self.__jurusan 

    def set__jurusan(self, jurusan):
        self.__jurusan = jurusan

sekolah_baru = Sekolah('SMAN 1 Bhakti Pertiwi', 'A', 'IPA & IPS')
sekolah_baru1 = Sekolah('SMK 2 MUHAMMADIYAH', 'B', 'Multimedia')
sekolah_baru2 = Sekolah('SMAN 2 Sragen','A' ,'Bahasa' )

nama_sekolah = sekolah_baru.get_nama()
sekolah_baru.set_nama('SMA TUNAS BANGSA')
nama_sekolah = sekolah_baru.get_nama()
print(nama_sekolah) 

nama_sekolah1 = sekolah_baru1.get_akreditasi()
sekolah_baru1.set_akreditasi('A')
nama_sekolah1 = sekolah_baru1.get_akreditasi()
print(nama_sekolah1) 

nama_sekolah2 = sekolah_baru2.get_jurusan()
sekolah_baru2.set__jurusan('MIPA')
nama_sekolah2 = sekolah_baru2.get_jurusan()
print(nama_sekolah2)