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

def partition(arr, low, high):
    i = (low - 1)
    r1 = low
    r2 = high
    r3 = (high+low)//2

    mediana = [arr[r1], arr[r2], arr[r3]]

    s_med = sorted(mediana)

    pivot = s_med[1]
    #print(pivot)
    if pivot == arr[r1]:
        arr[high], arr[r1] = pivot, arr[high]
    elif pivot == arr[r2]:
        arr[high], arr[r2] = pivot, arr[high]
    else:
        arr[high], arr[r3] = pivot, arr[high]


    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)

def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

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
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 1, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = arrayAleatorio(i)
    n = len(lista)
    sheet1.write(q, 0, n)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 1, int((fim - ini) * 1000))
    q += 1

print("--------------------------------------------")
for i in range(1, 11):

    lista = arrayDesc(i)
    n = len(lista)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 2, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = arrayDesc(i)
    n = len(lista)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 2, int((fim - ini) * 1000))
    q += 1

print("--------------------------------------------")
for i in range(1, 11):

    lista = array5(i)
    n = len(lista)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 3, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = array5(i)
    n = len(lista)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 3, int((fim - ini) * 1000))
    q += 1

print("--------------------------------------------")
for i in range(1,11):

    lista = array1(i)
    n = len(lista)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(i, 4, int((fim-ini)*1000))

q = 11
for i in range(20, 110, 10):

    lista = array1(i)
    n = len(lista)

    ini = time.time()
    quickSort(lista, 0, n-1)
    fim = time.time()
    #print("tempo em millis "+str((fim-ini)*1000))
    sheet1.write(q, 4, int((fim - ini) * 1000))
    q += 1
print("--------------------------------------------")

wb.save('QS.xls')
