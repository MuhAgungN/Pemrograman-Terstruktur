def dataStat(x) : 
    a = ratarata = sum(x) / len(x)
    b = maks = max(x)
    c = mins = min(x)

    return [round(a), b, c]


x = [2, 3, 4, 5, 6, 6, 6]
print('Data x = ', x)
print('Nilai [Rata-rata, Max, Min] dari x')
print('adalah ', dataStat(x))