from datetime import *

file = open("pp2.txt", "r")

data = file.readlines()

data1 = []

def diffDate():
    global now
    global dmax
    now = datetime.date(datetime.now())
    dmax = date(2021, 12, 15)
    delta = now - dmax
    return delta.days

denda = diffDate() * 2000
dpinjam = date(2021, 12, 8)

for i in range(len(data)):
    fix = data[i].replace('\n', '') 
    split = fix.split("|")
    Dict = {"code": split[0], "name": split[1], "title": split[2]}
    data1.append(Dict)

while True:
    cari = input('Masukkan Kode yang mau dicari : ')

    for i in range(len(data1)):
        if cari in data1[i]['code']:
            print('-------------------------------')
            print('Data Peminjaman Buku')
            print('Kode Member              : ', str(data1[i]['code']))
            print('Nama Member              : ', str(data1[i]['name']))
            print('Judul Buku               : ', str(data1[i]['title']))
            print('Tanggal Mulai Peminjaman : ', dpinjam)
            print('Tanggal Maks Peminjaman  : ', dmax)
            print('Tanggal Pengembalian     : ', now)
            print('Terlambat                : ', diffDate())
            print('Denda                    : ', denda)
            print('-------------------------------')

        if cari not in data1[0]['code']:
            if cari not in data1[1]['code']:
                if cari not in data1[2]['code']:
                    print("\"Data mahasiswa tidak ditemukan\"")
    
    
    ulang = input('Ingin mengulangi (y/n)?')
    if ulang in ('N', 'n'):
        break

file.close()
