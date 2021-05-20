#Solution №1

n = int(input())
d = {
    n == 10: 'A+\nExcellent',
    n == 9: 'A\nVery good',
    n == 8: 'A-\nVery good',
    n == 7: 'B+\nGood',
    n == 6: 'B-\nGood',
    n == 5: 'C+\nSatisfactory',
    n == 4: 'C-\nSatisfactory',
    n == 3: 'F\nFail\nGO TO ПЕРЕСДАЧА!',
    n == 2: 'F\nFail\nGO TO ПЕРЕСДАЧА!',
    n == 1: 'F\nFail\nGO TO ПЕРЕСДАЧА!',
    n == 0: 'Дисциплинарный проступок\nGO TO ПЕРЕСДАЧА!',
    n < 0 or n > 10: 'В Высшей школе экономики такой оценки нет!'
        }
print(d[True])
