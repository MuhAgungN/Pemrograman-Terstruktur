file = open("pp1.txt", "r")
read = file.readlines()

read1 = []

for i in range(len(read)):
    fix = read[i].replace('\n', '')
    read1 += [fix]

even = []
odd = []
for i in range(len(read1)):
    if (int(read1[i]) % 2 == 0):
        even += [read1[i]]
    if (int(read1[i]) % 2 != 0):
        odd += [read1[i]]

print('Jumlah bilangan genap =',len(even))
print('Jumlah bilangan ganjil =',len(odd))
file.close()

