import math

def hitung_persegi():
    try:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        keliling = 4 * sisi
        return print(f'Jadi Luas persegi adalah {luas}cm'), print(f'dan keliling persegi adalah {keliling}cm')
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def hitung_persegi_panjang():
    try:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        return print(f"Luas persegi panjang adalah : {luas}\ndan Keliling persegi panjang adalah {keliling}")
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def hitung_segitiga():
    try:
        alas = float(input('Masukkan Alas : '))
        tinggi = float(input('Masukkan Tinggi : '))
        sisi1 = float(input('Masukkan sisi 1 : '))
        sisi2 = float(input('Masukkan sisi 2 : '))
        sisi3 = float(input('Masukkan sisi 3 : '))
        keliling = sisi1 + sisi2 + sisi3
        luas = 0.5 * alas * tinggi
        return print(f'Jadi luas segitiga adalah {luas}cm\ndan keliling segitiga adalah {keliling}cm\n')
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def hitung_lingkaran():
    try:
        jari_jari = float(input('Masukkan Nilai Jari-jari : '))
        luas = math.pi * jari_jari * jari_jari
        keliling = 2 * math.pi * jari_jari
        return print(f'Jadi luas lingkaran adalah {luas}cm\ndan keliling lingkaran adalah {keliling}cm')
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def hitung_trapesium():
    try:
        panjang_atas = float(input('Masukkan nilai panjang atas : '))
        panjang_bawah = float(input('Masukkan nilai panjang bawah : '))
        sisi_kiri = float(input('Masukkan nilai sisi kiri : '))
        sisi_kanan = float(input('Masukkan nilai sisi kanan : '))
        tinggi = float(input('Masukkan nilai tinggi : '))
        luas = 0.5 * (panjang_atas + panjang_bawah) * tinggi
        keliling = panjang_atas + panjang_bawah + sisi_kiri + sisi_kanan
        return print(f'Jadi luas trapesium adalah {luas}cm\ndan keliling trapesium adalah {keliling}cm')
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def hitung_jejar_genjang():
    try:
        alas = float(input('Masukkan nilai alas : '))
        tinggi = float(input('Masukkan nilai tinggi : '))
        sisi1 = float(input('Masukkan nilai sisi 1 : '))
        sisi2 = float(input('Masukkan nilai sisi 2 : '))
        luas = alas * tinggi
        keliling = 2 * (sisi1 + sisi2)
        return print(f'Luas jejar genjang adalah {luas}cm\ndan Keliling jejar genjang  adalah {keliling}cm')
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def hitung_layang_layang():
    try:
        diagonal1 = float(input('Masukkan nilai diagonal 1 : '))
        diagonal2 = float(input('Masukkan nilai diagonal 2 : '))
        sisi1 = float(input('Masukkan nilai sisi 1 : '))
        sisi2 = float(input('Masukkan nilai sisi 2 : '))
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (sisi1 + sisi2)
        return print(f'Luas layang-layang adalah {luas}cm\ndan keliling layang-layang adalah {keliling}cm')
    except ValueError:
        print('Input yang anda masukkan tidak valid!')

def main():
    print("Aplikasi Perhitungan Luas dan Keliling Bangun Datar")
    while True:
        print("Pilih bangun datar yang ingin dihitung:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Trapesium")
        print("6. Jajar Genjang")
        print("7. Layang-layang")
        print("8. Keluar (untuk menghentikan program)")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7/8): ")

        if pilihan == '8':
            break  # Menghentikan program jika pengguna memilih keluar

        if pilihan == '1':
            hitung_persegi()

        elif pilihan == '2':
            hitung_persegi_panjang()

        elif pilihan == '3':
            hitung_segitiga()

        elif pilihan == '4':
            hitung_lingkaran()

        elif pilihan == '5':
            hitung_trapesium()

        elif pilihan == '6':
            hitung_jejar_genjang()

        elif pilihan == '7':
            hitung_layang_layang()
        else:
            print("Pilihan tidak valid.")
            continue

if __name__ == "__main__":
    main()

