names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
vals = names.values()
print(vals, type(vals))

vals_list = list(vals)
print(vals_list, type(vals_list))
ret = sum(vals_list)
print('출생아 수 총계: %d' %ret)
