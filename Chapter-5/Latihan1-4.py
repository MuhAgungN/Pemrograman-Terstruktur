kode=int(input("Masukkan kode karyawan	: "))
nama=str(input("Masukkan nama karyawan	: "))
gol=str(input("Masukkan golongan       : "))

print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")
print("Nama Karyawan		: ", nama, "(Kode: ", kode, ")")
print("Golongan		: ", gol)
print("-----------------------------------------------------------")

#golongan A
if (gol == "A"):
    gajipokoka = 10000000 
    print("Gaji Pokok		: Rp", gajipokoka)
    potongan = round(10000000*2.5/100)
    print("Potongan (2.5 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	       : Rp", (gajipokoka-potongan))

#golongan B
if (gol == "B"):
    gajipokokb = 8500000 
    print("Gaji Pokok		: Rp", gajipokokb)
    potongan = round(8500000*2.0/100)
    print("Potongan (2.0 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajipokokb-potongan))

#golongan C
if (gol == "C"):
    gajipokokc = 7000000 
    print("Gaji Pokok		: Rp", gajipokokc)
    potongan = round(7000000*1.5/100)
    print("Potongan (1.5 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajipokokc-potongan))

#golongan D
if (gol == "D"):
    gajipokokd = 5500000 
    print("Gaji Pokok		: Rp", gajipokokd)
    potongan = round(5500000*1.0/100)
    print("Potongan (1.0 %)	: Rp", potongan)
    print("----------------------------------------------------------- -")
    print("Gaji Bersih	        : Rp", (gajipokokd-potongan))

