#List a dan b
print('1. List a dan b')
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('a = ', a)
print('b = ', b)
print('-------------------------------')

#Menyisipkan angka pada list a dan b
 #Nomor 2
a.insert(3, 10)
b.insert(2, 15)
 #Nomor 3
a.append(4)
b.append(8)

print('2. Setelah disisipi angka')
print('a = ', a)
print('b = ', b)
print('-------------------------------')

#Sort Ascending
print('3. Setelah sorting ascending')
a.sort()
print('a = ', a)
b.sort()
print('b = ', b)
print('-------------------------------')

#List c dan d
print('4. List c dan d')
c = a[0:8]
d = b[2:10]
print('c = ', c)
print('d = ', d)
print('-------------------------------')

#Penjumlahan elemen c dan d
print('5. Penjumlahan elemen c dan d (c + d = e)')
hasil = []
cplusd = []
if len(c) == len(d):
    for i in range(len(c)):
        cplusd=c[i]+d[i]
        hasil.append(cplusd)
    print('e = ',hasil)
print('-------------------------------')

#List e bentuk tuple
print('6. List e bentuk tuple')
list_e = hasil
tuple_e = tuple(hasil)
print('e = ', tuple_e)
print('-------------------------------')

#nilai minimum dari elemen tuple_e
print('7. Nilai min, max, jumlahan seluruh elemen dari e')
print('Nilai minimum dari tuple', tuple_e, 'adalah', min(tuple_e))
#nilai maximum dari elemen tuple_e
print('Nilai maximum dari tuple', tuple_e, 'adalah', max(tuple_e))
#penjumlah seluruh elemen tuple_e
print('Jumlah seluruh elemen tuple', tuple_e, 'adalah', sum(tuple_e))
print('-------------------------------')

#Nomor 9
print('8. myString')
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)
print('-------------------------------')

#Nomor 10
print('9. Huruf penyusun')
huruf = set(myString)
print(huruf)
print('-------------------------------')

#Nomor 11
print('10. Huruf penyusun setelah diubah ke list')
tuple_ku = huruf
list_ku = list(huruf)
print(list_ku)
print('-------------------------------')

print('11. Huruf penyusun setelah diurutkan')
list_ku.sort()
print(list_ku)

