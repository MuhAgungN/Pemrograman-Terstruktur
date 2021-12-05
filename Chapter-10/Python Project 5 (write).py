file = open("pp5.txt", "a")

while True:
    print('-------------------------------')
    bil1 = input('bil1 : ')
    bil2 = input('bil2 : ')
    
    print('-------------------------------')
    myString = bil1+'|'+bil2+'\n'    
    file.write(myString)

    ulangi = input('Ulangi lagi inputnya (y/n) ? : ')
    if ulangi in ('N', 'n'):
        break

file.close()
