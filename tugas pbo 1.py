class Mahasiswa():
    def __init__(self, nama, umur, jurusan ):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan 
    def get_info(self):
        print(f"Nama    : {self.nama}")
        print(f"Umur    : {self.umur}")
        print(f"Jurusan : {self.jurusan}")
    def set_nama(self, nama_baru):
        self.nama = nama_baru 
    def set_umur(self, umur_baru):
        self.umur = umur_baru 

Mahasiswa_1 = Mahasiswa("Lia", 18, "Pendidikan Teknik Informatika")

Mahasiswa_1.set_nama("Lia Puspitasari")
Mahasiswa_1.set_umur(19)
Mahasiswa_1.get_info()
print()