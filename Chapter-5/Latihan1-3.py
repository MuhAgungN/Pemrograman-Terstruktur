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


#Sebab
print("Sebab : ")
if bhsindonesia>60:
    print("- Nilai Bahasa Indonesia lebih dari 60")
else :
    print("- Nilai Bahasa Indonesia kurang dari 60")
if matematika>70:
    print("- Nilai Matematika lebih dari 70")
else :
    print("- Nilai Matematika kurang dari 70")
if ipa>60:
    print("- Nilai IPA lebih dari 60")
else :
    print("- Nilai IPA kurang dari 60")
