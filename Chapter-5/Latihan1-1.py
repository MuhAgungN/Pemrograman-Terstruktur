#Input nilai
bhsindonesia = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
matematika = int(input("Masukkan nilai Matematika : "))
total = bhsindonesia+ipa+matematika

#Lulus/Tidak Lulus
if bhsindonesia>60 and ipa>60 and matematika>70:
    print("Status Kelulusan  : LULUS")
else:
    print("Status Kelulusan  : TIDAK LULUS")
