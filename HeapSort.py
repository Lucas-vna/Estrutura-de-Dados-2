#Heap Sort in python
def heapify(vetor, tamVetor, i):
      #Acha o maior entre as raizes e filhos
      maior = i
      L = 2 * i + 1
      R = 2 * i + 2
  
      if R < tamVetor and vetor[i] < vetor[L]:
          maior = L
  
      if R < tamVetor and vetor[maior] < vetor[R]:
          maior = R
  
      #Se a raiz não for maior, troca com o maior e continua a função
      if maior != i:
          vetor[i], vetor[maior] = vetor[maior], vetor[i]
          heapify(vetor, tamVetor, maior)
  
  
def heapSort(vetor):
      tamVetor = len(vetor)
  
      #Constroi a heap maxima
      for i in range(tamVetor//2, -1, -1):
          heapify(vetor, tamVetor, i)
  
      for i in range(tamVetor-1, 0, -1):
          #Troca
          vetor[i], vetor[0] = vetor[0], vetor[i]
  
          #Heapify o elemento da raiz
          heapify(vetor, i, 0)
  
  
vetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
heapSort(vetor)
tamVetor = len(vetor)

print("Sorted array is")
for i in range(tamVetor):
    print("%d " % vetor[i], end='')
