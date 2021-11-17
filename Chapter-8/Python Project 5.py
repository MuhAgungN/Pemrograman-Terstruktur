def kuadrat(bil):
    kuadrat = []
    for i in bil:
        kuadrat.append(i ** 2)
    return kuadrat

bil = [2, 4, 5, 666] 
print('bil = ', bil)
print('hasil = kuadrat(bil)')
print('bil setelah dikuadratkan = ', kuadrat(bil))
