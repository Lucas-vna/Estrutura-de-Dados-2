import sys
import random

def mergeSort(vetor):

    if len(vetor) > 1:
        
        #Meio é o ponto onde o vetor vai ser dividido em 2 sub vetores
        Meio = len(vetor)//2
        P1 = vetor[:Meio] 
        P2 = vetor[Meio:]

        #definindo as duas partes
        mergeSort(P1)
        mergeSort(P2)

        #ponteiros
        #i contém o numero de P1, comeca em 1
        #j contém o numero de P2, comeca em 1
        #k contém o numero de funcao aux, comeca em p
        i = j = k = 0

        #Até chegarmos no final da P1 ou P2, pega a maior parte dos elementos de P1 e P2 
        # e os coloca na posicao correta no vetor aux
        while i < len(P1) and j < len(P2): #oq faz: enquanto a qntd de numeros no ponteiro i forem menores que o tamanho da P1 e enquanto a qntd de numeros no ponteiro j forem menores que o tamanho da P2 
            if P1[i] < P2[j]:              #se o numero que estiver na posicao i de P1 for maior que o número que estiver na posicao j de P2:
                vetor[k] = P1[i]        #copia esse numero da P1 para a posicao k do vetor aux
                i += 1                     #aumenta a posicao que vai ser comparada do poteiro i (avanca uma casa no vetor ex: sai da posicao 0 para 1)
            else:
                vetor[k] = P2[j]        #copia esse numero da P2 para a posicao k do vetor aux
                j += 1                     #aumenta a posicao que vai ser comparada do poteiro j (avanca uma casa no vetor ex: sai da posicao 0 para 1)
            k += 1                         #aumenta a posicao do vetor, fazendo com que o proximo numero seja alocado na posicao seguinte 
                                        
        
        #Quando acabar os elementos de P1 ou P2, pega os remanescentes e os
        # coloca no vetor aux
        while i < len(P1):
            vetor[k] = P1[i]
            i += 1
            k += 1

        while j < len(P2):
            vetor[k] = P2[j]
            j += 1
            k += 1  

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

#abrindo o arquivo e lendo o número  para o tamanho do vetor
entrada = open("input1.txt", "r")
saida = open("SaidaATV1-ed2.txt","w")

tamanho = entrada.readline() #N = número de posições do vetor
metodo = entrada.readline() #Letra é a identificação do método
 
vetor = []
teste = int(tamanho)

for i in range (teste):
    vetor.append(random.randint(1,teste))
print(vetor)

mergeSort(vetor)

saida.write(' '.join(str(e) for e in vetor))

