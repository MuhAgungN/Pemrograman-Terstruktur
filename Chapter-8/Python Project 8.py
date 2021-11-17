#8.	Berdasarkan data list buah dari nomor 7, 
#buatlah sebuah function untuk menentukan rata-rata harga satuan dari keseluruhan buah yang ada!
def tampilkan_data(data):
    i = 1
    for key, value in data.items():
        print(i,'.', key, ':', value)
        i += 1

def harga_buah(data):
    sum = 0
    jumlah = 0
    for harga in data.values():
        sum += harga
        jumlah += 1
    return sum/jumlah

buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

print('Daftar buah dan harganya :')
tampilkan_data(buah)
print('Rata-rata seluruh harga buah adalah', harga_buah(buah))