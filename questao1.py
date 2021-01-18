#Construa uma função que receba uma lista com dois vetores e retorne um vetor com os 
# valores que estão presentes nos dois vetores passados.

def (list_igual):
list1 = [1, 2, 4, 8, 15]
list2 = [4, 5, 6, 1, 8]
list_igual = []
for item in list1:
  if item in list2:
    list_igual.append(item)

print(list_igual)