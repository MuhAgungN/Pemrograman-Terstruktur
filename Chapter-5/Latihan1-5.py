kode=int(input("Masukkan kode karyawan	: "))
nama=str(input("Masukkan nama karyawan	: "))
gol=str(input("Masukkan golongan       : "))
status=str(input("Masukkan status         : "))
if(status == "Menikah"):
    jmlanak=int(input("Masukkan jumlah anak    : "))
    tjgistrisuami=1
elif(status == "Belum"):
    jmlanak = 0
    tjgistrisuami = 0

print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")
print("Nama Karyawan		: ", nama, "(Kode: ", kode, ")")
print("Golongan		: ", gol)
print("Status Menikah          : ", status)
print("Jumlah Anak             : ", jmlanak)
print("-----------------------------------------------------------")

#golongan A
if (gol == "A"):
    gajipokoka = 10000000 
    print("Gaji Pokok		: Rp", gajipokoka)
    tjgistrisuamia = round(gajipokoka*tjgistrisuami*10/100)
    print("Tunjangan Istri/Suami   : Rp", tjgistrisuamia)
    tjganaka = round(gajipokoka*jmlanak*5/100)
    print("Tunjangan Anak          : Rp", tjganaka)
    print("----------------------------------------------------------- +")
    gajikotora = gajipokoka+tjgistrisuamia+tjganaka
    print("Gaji Kotor		: Rp", gajikotora)
    potongan = round(10000000*2.5/100)
    print("Potongan (2.5 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajikotora-potongan))

#golongan B
if (gol == "B"):
    gajipokokb = 8500000 
    print("Gaji Pokok		: Rp", gajipokokb)
    tjgistrisuamib = round(gajipokokb*tjgistrisuami*10/100)
    print("Tunjangan Istri/Suami   : Rp", tjgistrisuamib)
    tjganakb = round(gajipokokb*jmlanak*5/100)
    print("Tunjangan Anak          : Rp", tjganakb)
    print("----------------------------------------------------------- +")
    gajikotorb = gajipokokb+tjgistrisuamib+tjganakb
    print("Gaji Kotor		: Rp", gajikotorb)
    potongan = round(8500000*2.0/100)
    print("Potongan (2.0 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajikotorb-potongan))

#golongan C
if (gol == "C"):
    gajipokokc = 7000000 
    print("Gaji Pokok		: Rp", gajipokokc)
    tjgistrisuamic = round(gajipokokc*tjgistrisuami*10/100)
    print("Tunjangan Istri/Suami   : Rp", tjgistrisuamic)
    tjganakc = round(gajipokokc*jmlanak*5/100)
    print("Tunjangan Anak          : Rp", tjganakc)
    print("----------------------------------------------------------- +")
    gajikotorc = gajipokokc+tjgistrisuamic+tjganakc
    print("Gaji Kotor		: Rp", gajikotorc)
    potongan = round(7000000*1.5/100)
    print("Potongan (1.5 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajikotorc-potongan))
    
#golongan D
if (gol == "D"):
    gajipokokd = 5500000 
    print("Gaji Pokok		: Rp", gajipokokd)
    tjgistrisuamid = round(gajipokokd*tjgistrisuami*10/100)
    print("Tunjangan Istri/Suami   : Rp", tjgistrisuamid)
    tjganakd = round(gajipokokd*jmlanak*5/100)
    print("Tunjangan Anak          : Rp", tjganakd)
    print("----------------------------------------------------------- +")
    gajikotord = gajipokokd+tjgistrisuamid+tjganakd
    print("Gaji Kotor		: Rp", gajikotord)
    potongan = round(5500000*1.0/100)
    print("Potongan (1.0 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajikotord-potongan))