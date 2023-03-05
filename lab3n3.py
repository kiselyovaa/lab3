bykva = 'ф'
x = input('введите слово: ')
for word in x.split():
    if bykva in word.lower():
        print('ого! это слово редкое')
    else:
        print('эх, это не редкое слово')
