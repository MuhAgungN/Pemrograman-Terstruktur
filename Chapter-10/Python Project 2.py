file = open("pp2.txt", "a")

while True:
    print('-------------------------------')
    nim = input('Masukkan NIM         :')
    nama = input('Masukkan Nama Mhs    :')
    alamat = input('Masukkan Alamat      :')
    print('-------------------------------')
    myString = nim+'|'+nama+'|'+alamat+'\n'    
    file.write(myString)

    ulangi = input('Ulangi lagi inputnya (y/n) ? : ')
    if ulangi in ('N', 'n'):
        break
file.close()

print('-------------------------------')
  