batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedi = []

while True:
    nilai = input("Masukkan nilai (atau ketik 'selesai' untuk berhenti): ")
    if nilai.lower() == 'selesai':
        if len(nilai_masuk) < 5:
            print("Minimal harus memasukkan 5 nilai.")
            continue
        if len(lulus) == 0 or len(remedi) ==0:
            print("Harus ada nilai lulus dan nilai remedi.")
            continue

        break

    nilai = float(nilai)

    if nilai < 0 or nilai > 100:
        print("Nilai harus berada di antara 0-100.") 
        continue

    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)

print("Nilai yang masuk:", nilai_masuk)

delete = input("Apakah ada nilai yang ingin dihapus? (iya/tidak) ")

if delete.lower() == "iya":
    nilai_hapus = float(input("Masukkan nilai yang ingin dihapus: "))

    if nilai_hapus in nilai_masuk:
        nilai_masuk.remove(nilai_hapus)

        if nilai_hapus in lulus:
            lulus.remove(nilai_hapus)

        if nilai_hapus in remedi:
            remedi.remove(nilai_hapus)

        print("Nilai berhasil dihapus.")
    else:
        print("Nilai tidak ditemukan.")


print("HASIL")
print("Nilai masuk :", nilai_masuk)
print("Nilai lulus :", lulus)
print("Nilai remedi :", remedi)
