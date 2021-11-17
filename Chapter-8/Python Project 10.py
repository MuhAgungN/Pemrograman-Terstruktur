def tampilkan_data(data):
    print('Daftar buah dan harganya :')
    i = 1
    for key, value in buah.items():
        print(i,'.', key, ':', value)
        i += 1

buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

print('-------------------------------')
tampilkan_data(buah)
print('-------------------------------')

total_semua = 0

while True:
    nama = (input('Nama buah yang dibeli : '))
    harga = buah[nama]
    massa = int(input('Berapa Kg             : '))
    total_harga = harga * massa
    total_semua += total_harga
    print('-------------------------------')
    tambah = input('Beli buah yang lain (y/n) ? : ')
    print('-------------------------------')
    if (tambah == 'n' or tambah == 'N'):
        print('Total harga :', total_semua)
        break