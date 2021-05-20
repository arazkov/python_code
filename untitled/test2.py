# # задача Элера №2 числа Фибоначчи

def fibonachi(max):
    fibonachi_list = [1, 2]
    nam_next = 0
    while nam_next <= max:
        nam_next = fibonachi_list[-1] + fibonachi_list[-2]
        fibonachi_list.append(nam_next)
        if nam_next > max:
            fibonachi_list.remove(nam_next)
    return fibonachi_list

fibo = fibonachi(4000000)
fibo_2 = []
print(fibo)
for i in fibo:
    if i % 2 == 0:
        fibo_2.append(i)
print(fibo_2)
print(sum(fibo_2))

# # задача Элера №4 "наибольшее произведение-палендром"

def palendrom(d_nam_1, d_nam_2):
    namber = str(d_nam_1 * d_nam_2)

    if namber == namber[::-1]:
        return d_nam_1 * d_nam_2


nam_pal = 0
for nam_1 in range(100, 1000):
    for nam_2 in range(100, 1000):
        if palendrom(nam_1, nam_2):
            if palendrom(nam_1, nam_2) > nam_pal:
                nam_pal = palendrom(nam_1, nam_2)
print(nam_pal)

# # задача Элера №5 "наименьшее кратное"

nams = range(20, 1000000)
nams_list = list(nams)
del_nams = 2
delite = True
for nam in nams:
    while delite:
        if nam % del_nams == 0:
            del_nams += 1
            if del_nams > 15:
                break
        else:
            del_nams = 2
            nams_list.remove(nam)
            break
print(nams_list)

# # задача Элера №6

nams = list(range(1, 101))
sum_kvad = 0
kvad_sum = 0
for nam in nams:
    sum_kvad += nam ** 2
for nam2 in nams:
    kvad_sum += nam2
kvad_sum = kvad_sum ** 2
print(f'{str(sum_kvad)} {str(kvad_sum)}')
print(kvad_sum - sum_kvad)

# # задача Эйлера № 7

def natural(lower, upper):
    natural_list = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                natural_list.append(num)
    return natural_list

print(natural(1, 200)[5])

# # задача Элера №8

namber_1000 = '''73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'''

namber_1000_lst = list(namber_1000)
# print(namber_1000_lst)
nam = 0
for i in range(len(namber_1000)):
    if i == 997:
        break
    nam2 = int(namber_1000_lst[i]) * int(namber_1000_lst[i + 1]) * int(namber_1000_lst[i + 2]) * int(namber_1000_lst[i + 3])
    if nam2 > nam:
        nam = nam2
print(nam)