file = open("pp2.txt", "r")

data = file.readlines()

data1 = []

for i in range(len(data)):
    fix = data[i].replace('\n', '') 
    split = fix.split("|")
    Dict = {"nim": split[0], "nama": split[1], "alamat": split[2] }
    data1.append(Dict)

print(data1)
file.close()



