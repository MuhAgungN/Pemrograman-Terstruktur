from datetime import *
file = open("pp2.txt", "a")

x = datetime.date(datetime.now())
skrng = str(x)
y = x + timedelta(days=7)
kembali = str(y)
while True:
    print('-------------------------------')
    code = input('Masukkan Kode Member  : ')
    name = input('Masukkan Nama Member  : ')
    title = input('Masukkan Judul Buku   : ')
    print('-------------------------------')
    myString = code+'|'+name+'|'+title+'|'+skrng+'|'+kembali+'\n'    
    file.write(myString)

    ulangi = input('Ulangi lagi inputnya (y/n) ? : ')
    if ulangi in ('N', 'n'):
        break

file.close()
