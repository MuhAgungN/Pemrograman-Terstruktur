def sum(*myData) :
    i = 0
    for data in myData:
        i += data
    return i
    print (i)

def average(*myData):
    j = 0
    for data in myData:
        j += 1
    print (sum(*myData)/j)
    
def maks(*myData):
    maks = max(myData)
    print(maks)

def mins(*myData):
    mins = min(myData)
    print(mins)


