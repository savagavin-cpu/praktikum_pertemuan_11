#program 11.2 latihan dictionary bagian 1
import datetime

mahasiswa_template = {
    'nama':'nama',
    'nim':'0000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

print(f"{'selamat datang': ^20}")
print(f"{'data mahasiswa': ^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama']=input("nama mahasiswa: ")
mahasiswa['nim']=input("nim mahasiswa: ")
mahasiswa['sks_lulus']=int(input("sks lulus: "))
TAHUN_LAHIR = int(input("tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("tanggal lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

print(mahasiswa)