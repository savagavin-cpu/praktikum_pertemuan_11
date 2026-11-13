#program 11.1 multi keys & nesting dictionary
import datetime

mahasiswa1 ={
    'nama':'ucup sarucup',
    'nim':'1902200213278648973468',
    'sks_lulus':130,
    'beasiswa': False,
    'lahir':datetime.datetime(2001,4,10) #tahun, tanggal, bulan
}

mahasiswa2 ={
    'nama':'azan isya',
    'nim':'190220021327868742786',
    'sks_lulus':140,
    'beasiswa': True,
    'lahir':datetime.datetime(1996,3,10) #tahun, tanggal, bulan
}

mahasiswa3 ={
    'nama':'slamat tinggal',
    'nim':'1902200213271346',
    'sks_lulus':100,
    'beasiswa': True,
    'lahir':datetime.datetime(1130,2,10) #tahun, tanggal, bulan
}
data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
}

print(f"{'KEY': <6} {'nama': <6} {'SKS': <3} {'beasiswa': <9} {'lahir': <10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("&x")

    print(f"{KEY: <6} {NAMA: <17} {SKS: <3} {BEASISWA: <9} {LAHIR: <10}")



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
    mahasiswa['sks lulus']=int(input("sks lulus: "))
    TAHUN_LAHIR = int(input("tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("tanggal lahir (1-31): "))
    mahasiswa['lahir']
    datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    print(mahasiswa)