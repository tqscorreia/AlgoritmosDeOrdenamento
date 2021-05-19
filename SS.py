from sys import stdin, stdout
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

def sort(lista):
    n = len(lista)
    k = 2

    #gap = n
    #gap = n // 2
    gap = n // 10
    #gap = n // (3 * k + 1)//k=1
    #gap = n // ((3 ** (k - 1) // 2))//k=2
    #gap = n // (2**k+1)

    while gap > 0:

        A102549 = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        aux = 0

        for i in range(gap, n):

            temp = lista[i]

            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap

            lista[j] = temp
        if aux < len(A102549):
            aux = +1
            ind = A102549[aux]
        else:
            ind = ind*2.25
        #gap //= ind


        k += 1

        #gap //= 2
        gap //= 10
        #gap //= (3 * k + 1)
        #gap //= ((3 ** (k - 1) // 2))
        #gap //= (2**k+1)



    #for i in range (len(lista)):
    #   outln(lista[i])





for i in range(1, 11):

    lista = arrayDesc(i)

    ini = time.time()
    sort(lista)
    fim = time.time()
    print("tempo em sec "+str(fim-ini))
    print("--------------------------------------------")

for i in range(20, 110, 10):

    lista = arrayDesc(i)

    ini = time.time()
    sort(lista)
    fim = time.time()
    print("tempo em sec "+str(fim-ini))
    print("--------------------------------------------")
