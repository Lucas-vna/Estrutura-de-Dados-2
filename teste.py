import sys
import random

def bubbleSort(vetor, tamVetor):
    #trocou = true
    swapped = True

    trocas = 0

    #while true:
    while swapped == True:
      #trocou = false
      swapped = False

      for i in range(0, tamVetor-1):
          if vetor[i] > vetor[i + 1]:
              vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
              trocas += 1; 
              #trocou = false
              swapped = True

    print(trocas)
    print(vetor)

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

#abrindo o arquivo e lendo o número  para o tamanho do vetor
entrada = open("input1.txt", "r")

tamanho = entrada.readline() #N = número de posições do vetor
metodo = entrada.readline() #Letra é a identificação do método
 
vetor = []
teste = int(tamanho)

for i in range (teste):
    vetor.append(random.randint(1,teste))
print(vetor)

bubbleSort(vetor, teste)

saida = open("SaidaATV1-ed2.txt","w")

