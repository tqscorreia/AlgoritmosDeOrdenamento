from sys import stdin, stdout
from xlwt import Workbook
import time
import random

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

def arrayDesc(i):
    n = i * 100000
    lista = []
    for i in range(n):
        lista.append(n - i)
    return lista

def arrayAleatorio(i):
    n = i * 100000
    lista = []
    for i in range(n):
        lista.append(i)
    random.shuffle(lista)
    return lista

def array5(i):
    n = i*100000
    lista = []
    desord = []
    for i in range(0, int(n*0.95)):
        lista.append(i)
    for i in range(int(n*0.95), n):
        desord.append(i)
    random.shuffle(desord)
    for i in desord:
        lista.append(i)
    return lista

def array1(i):
    n = i * 100000
    lista = []
    desord = []
    for i in range(0, int(n*0.99)):
        lista.append(i)
    for i in range(int(n*0.99), n):
        desord.append(i)
    random.shuffle(desord)
    for i in desord:
        lista.append(i)
    return lista


def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i] // exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)

    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 1, 'RANDOM')
sheet1.write(0, 2, 'DESC')
sheet1.write(0, 3, '5%')
sheet1.write(0, 4, '1%')

for i in range(1, 11):

    lista = arrayAleatorio(i)
    n = len(lista)
    sheet1.write(i, 0, n)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 1, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = arrayAleatorio(i)
    n = len(lista)
    sheet1.write(q, 0, n)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 1, int((fim - ini) * 1000))
    q += 1

print("--------------------------------------------")
for i in range(1, 11):

    lista = arrayDesc(i)
    n = len(lista)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 2, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = arrayDesc(i)
    n = len(lista)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 2, int((fim - ini) * 1000))
    q += 1

print("--------------------------------------------")
for i in range(1, 11):

    lista = array5(i)
    n = len(lista)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 3, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = array5(i)
    n = len(lista)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 3, int((fim - ini) * 1000))
    q += 1

print("--------------------------------------------")
for i in range(1, 11):

    lista = array1(i)
    n = len(lista)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 4, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = array1(i)
    n = len(lista)

    ini = time.time()
    radixSort(lista)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 4, int((fim - ini) * 1000))
    q += 1
print("--------------------------------------------")

wb.save('RS.xls')
