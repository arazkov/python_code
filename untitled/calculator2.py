
formula = input('')

formula2 = list(formula)
a = float(formula2[0])
b = float(formula2[2])
if formula2[1] == '+':
    print(int(a + b))
else:
    print(int(a - b))
