file = open("hasilpp6.txt", "r")
hasil = open("pp7.txt", "a")

read = file.read()

Set = set(read)

Set.remove(' ')

List = list(Set)

List.sort()

n = 2

data = read.replace(List[0], chr(ord(List[0])-n))

i = 1
while True:
    data = data.replace(List[i], chr(ord(List[i])-n))
    i += 1

    if(i == 10):
        break

data = data.replace(chr(63), chr(89))
data = data.replace(chr(64), chr(90))

print(data)
hasil.write(data)
file.close()
hasil.close()


