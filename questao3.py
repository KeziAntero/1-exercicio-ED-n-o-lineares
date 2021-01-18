#Construa uma classe chamada Buscador com um método chamado busca_binaria que 
# faça a busca binária em um vetor já ordenado. EX: buscando 5


def busca_binaria(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2
        if array[m] == item:
            return m
        if item < array[m]:
            return busca_binaria(array, item, begin, m-1)
        else:
            return busca_binaria(array, item, m+1, end)
    return None

lista = [2,3,4]
busca_binaria(lista, 4, 0, len(lista)-1)
busca_binaria(lista, 4)