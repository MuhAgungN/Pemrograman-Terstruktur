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


print('MENU :')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')
A = 'A'
B = 'B'
C = 'C'
print('-------------------------------')
pilihan = input('Pilihan menu :')
print('-------------------------------')


if pilihan == A :
    nama_baru = input('Masukkan nama buah :')
    harga_baru = int(input('Masukkan harga satuan :'))
    print('-------------------------------')
    print('Setelah ditambah')
    tampilkan_data(buah)
    print(5,'.', nama_baru,':', harga_baru)

if pilihan == B :
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
            print('Total harga           :', total_semua)
        break
  
if pilihan == C:
    try:
        nama = (input('Nama buah yang akan dihapus : '))
        del buah[nama]
        print('Data buah dan harganya setelah ada yang dihapus : ', buah)
    except KeyError:
        print('Nama buah tidak ditemukan')


