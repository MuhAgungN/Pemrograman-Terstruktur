file = open("pp2.txt", "r")

data = file.readlines()

data1 = []

for i in range(len(data)):
    fix = data[i].replace('\n', '') 
    split = fix.split("|")
    Dict = {"nim": split[0], "nama": split[1], "alamat": split[2] }
    data1.append(Dict)

while True:
    cari = input('Masukkan NIM yang mau dicari : ')

    for i in range(len(data1)):
        if cari in data1[i]['nim']:
            print('-------------------------------')
            print('Data Mahasiswa')
            print('NIM     : ', str(data1[i]['nim']))
            print('Nama    : ', str(data1[i]['nama']))
            print('Alamat  :', str(data1[i]['nim']))

        if cari not in data1[0]['nim']:
            if cari not in data1[1]['nim']:
                if cari not in data1[2]['nim']:
                    print("\"Data mahasiswa tidak ditemukan\"")

    print('-------------------------------')
    ulang = input('Ingin mengulangi (y/n)?')
    if ulang in ('N', 'n'):
        break

file.close()