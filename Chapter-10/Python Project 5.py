file = open("pp5.txt", "r")
hasil = open("hasilpp5.txt", "a")

read = file.readlines()

for i in range(len(read)):
    fix = read[i].replace('\n', '') 
    split = fix.split("|")
    print(str(int(split[0]) + int(split[1])))
    hasil.write(str(int(split[0]) + int(split[1]))+'\n')
file.close()
hasil.close()