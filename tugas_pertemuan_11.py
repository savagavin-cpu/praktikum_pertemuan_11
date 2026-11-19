# SISTEM MANAJEMEN PERPUSTAKAAN


# Dictionary utama perpustakaan
perpustakaan = {}

while True:
    print("\nSISTEM MANAJEMEN PERPUSTAKAAN")
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    # MENAMBAHKAN BUKU
    if pilihan == "1":
        print("\nTAMBAH BUKU")

        kode_buku = input("Kode Buku: ").upper()
        judul = input("Judul Buku: ")
        penulis = input("Penulis: ")
        tahun = int(input("Tahun Terbit: "))
        tanggal_pinjam = input(
            "Tanggal Terakhir Pinjam (YYYY-MM-DD): "
        )

        status = input(
            "Status (TERSEDIA/TIDAK): "
        ).upper()

        # Memeriksa status buku
        if status not in ["TERSEDIA", "TIDAK"]:
            print("Status tidak valid!")
            continue

        # Membuat Multi Keys
        key_buku = (kode_buku, tahun)

        # Memeriksa apakah buku ada
        if key_buku in perpustakaan:
            print("Buku sudah terdaftar!")
            continue

        # Nesting Dictionary
        data_buku = {
            "judul": judul,
            "penulis": penulis,
            "tahun_terbit": tahun,
            "tanggal_terakhir_pinjam": tanggal_pinjam,
            "status": status
        }

        # Menyimpan data buku
        perpustakaan[key_buku] = data_buku

        print("\nBuku berhasil ditambahkan!")

    # MENAMPILKAN BUKU
    elif pilihan == "2":
        print("\n DAFTAR BUKU PERPUSTAKAAN ")

        if len(perpustakaan) == 0:
            print("Belum ada data buku.")
        else:
            for key, buku in perpustakaan.items():
                print("\nKEY:", key)
                print("Judul Buku:", buku["judul"])
                print("Penulis:", buku["penulis"])
                print("Tahun Terbit:", buku["tahun_terbit"])
                print(
                    "Tanggal Terakhir Pinjam:",
                    buku["tanggal_terakhir_pinjam"]
                )
                print("Status:", buku["status"])
                print("-" * 40)

    # KELUAR
    elif pilihan == "3":
        print("\nTerima kasih")
        break

    else:
        print("\nPilihan tidak ada")