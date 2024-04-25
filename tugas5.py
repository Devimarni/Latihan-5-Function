#Latihan 1
def konversi_suhu(suhu, dari, ke):
    if dari == "C" and ke == "F":
        hasil = (suhu * 9/5) + 32
        return hasil
    elif dari == "F" and ke == "C":
        hasil = (suhu - 32) * 5/9
        return hasil
    elif dari == "C" and ke == "K":
        hasil = suhu + 273.15
        return hasil
    elif dari == "K" and ke == "C":
        hasil = suhu - 273.15
        return hasil
    elif dari == "F" and ke == "K":
        hasil = (suhu - 32) * 5/9 + 273.15
        return hasil
    elif dari == "K" and ke == "F":
        hasil = (suhu - 273.15) * 9/5 + 32
        return hasil
    elif dari == ke:
        return suhu
    else:
        return "Konversi tidak valid!"

def main():
    print("Selamat datang di program konversi suhu ruangan!")
    suhu = float(input("Masukkan suhu: "))
    satuan_awal = input("Masukkan satuan suhu (C/F/K): ").upper()
    satuan_tujuan = input("Konversi ke (C/F/K): ").upper()

    hasil_konversi = konversi_suhu(suhu, satuan_awal, satuan_tujuan)
    if isinstance(hasil_konversi, float):
        print(f"Hasil konversi: {hasil_konversi:.2f} {satuan_tujuan}")
    else:
        print(hasil_konversi)

if __name__ == "__main__":
    main()



#Tugas 2
def sorts(name, chapter):
    print("Nama Saya     :", name)
    print("Saya sedang mengerjakan latihan soal :", chapter)

def main():
    nama = input      ("Masukkan Nama       : ")
    latihan_ke = input("Masukkan Latihan ke : ")

    sorts(nama, latihan_ke)

if __name__ == "__main__":
    main()




#latihan 3
def pembagian(x, y, z=0):
    if z == 0:
        return "Tidak bisa melakukan pembagian dengan nol"
    else:
        return x * y / z

print(pembagian(20, 10, 3.2))




#Latihan 4
def sorts(*x):
    for i in x:
        print(i)

sorts(10, 20)
sorts(50, 70)
sorts(90, 30)



