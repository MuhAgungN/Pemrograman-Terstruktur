file = open("pp6.txt", "r")
hasil = open("hasilpp6.txt", "a")

read = file.read()

Set = set(read)

Set.remove(' ')

List = list(Set)

List.sort(reverse=True)

n = 2

data = read.replace(List[0], chr(ord(List[0])+n))

i = 1
while True:
    data = data.replace(List[i], chr(ord(List[i])+n))
    i += 1

    if(i == 10):
        break

data = data.replace(chr(91), chr(65))
data = data.replace(chr(92), chr(66))

print(data)
hasil.write(data)
file.close()
hasil.close()


