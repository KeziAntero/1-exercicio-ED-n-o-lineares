#Construa uma classe chamada Ordenador com um método chamado bubble_sort 
# que faça a ordenação de um vetor com o algoritmo bubble_sort.

class Ordenador:
def bubble_Sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [8,26,93,17,98]
bubble_Sort(alist)
print(alist)
