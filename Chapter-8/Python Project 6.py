def sortStringByChar(myData):
    myData1 = sorted(myData, reverse = True, key=len)
    return myData1

myData = ['apel', 'rambutan', 'jeruk', 'pir']
print('myData = ', myData)
print('myData setelah diurutkan = ', sortStringByChar(myData))