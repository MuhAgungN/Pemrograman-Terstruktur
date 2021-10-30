def luasSegitiga(a, t):
    luas = a * t / 2
    return luas

def total(x, z):
    tot = x + z
    return tot

#Luas segitiga 1 dan segitiga 2
alas = 10
alas2 = 15
tinggi = 20
tinggi2 = 45
print('Luas segitiga dengan alas ', alas,' dan tinggi ', tinggi,' adalah ', luasSegitiga(alas, tinggi))
print('Luas segitiga dengan alas ', alas2,' dan tinggi ', tinggi2,' adalah ', luasSegitiga(alas2, tinggi2))

#Total luas segitiga 1 dan 2
segitiga1 = luasSegitiga(alas, tinggi)
segitiga2 = luasSegitiga(alas2, tinggi2)
print('Total luas kedua segitiga tersebut adalah : ', total(segitiga1, segitiga2))