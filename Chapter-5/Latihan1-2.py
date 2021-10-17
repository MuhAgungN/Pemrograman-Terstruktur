#Input nilai
bhsindonesia = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
matematika = int(input("Masukkan nilai Matematika : "))
total = bhsindonesia+ipa+matematika

#Cek nilai yang tidak valid (di luar range 0-100)
if (bhsindonesia<0) or (bhsindonesia>100):
    print("Maaf input ada yang tidak valid")
elif (ipa<0) or (ipa>100):
    print("Maaf input ada yang tidak valid")
elif (matematika<0) or (matematika>100):
    print("Maaf input ada yang tidak valid")

