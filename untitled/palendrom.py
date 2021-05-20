namber = input('Какое число? ')
# namber = str(548969845)
leight_namber = len(namber)
half_namber = leight_namber // 2

for nam in range(half_namber):
    if namber[nam] == namber[leight_namber - 1 - nam]:
        continue
    else:
        print('no')
        break
else:
    print('yes')

########################################################################

namber = input('What namber is ')
if namber == namber[::-1]:
    print('YES')
else:
    print('NO')
