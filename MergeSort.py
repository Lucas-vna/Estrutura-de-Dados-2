#funcao principal
def MergeSort(meuVetor):

    if len(meuVetor) > 1:
        
        #Meio é o ponto onde o vetor vai ser dividido em 2 sub vetores
        Meio = len(meuVetor)//2
        P1 = meuVetor[:Meio] 
        P2 = meuVetor[Meio:]

        #definindo as duas partes
        MergeSort(P1)
        MergeSort(P2)

        #ponteiros
        #i contém o numero de P1, comeca em 1
        #j contém o numero de P2, comeca em 1
        #k contém o numero de funcao aux, comeca em p
        i = j = k = 0

        #Até chegarmos no final da P1 ou P2, pega a maior parte dos elementos de P1 e P2 
        # e os coloca na posicao correta no vetor aux
        while i < len(P1) and j < len(P2): #oq faz: enquanto os numeros no ponteiro i forem menores que o tamanho da P1 e enquanto os numeros no ponteiro j forem menores que o tamanho da P2 
            if P1[i] < P2[j]:              #se o numero que estiver na posicao i de P1 for maior que o número que estiver na posicao j de P2
                meuVetor[k] = P1[i]        #copia esse numero da P1 para a posicao k do vetor aux
                i += 1                     #aumenta a posicao que vai ser comparada do poteiro i (avanca uma casa no vetor ex: sai da posicao 0 para 1)
            else:
                meuVetor[k] = P2[j]        #copia esse numero da P2 para a posicao k do vetor aux
                j += 1                     #aumenta a posicao que vai ser comparada do poteiro j (avanca uma casa no vetor ex: sai da posicao 0 para 1)
            k += 1                         #aumenta a posicao do vetor, fazendo com que o proximo numero seja alocado na posicao seguinte 
                                        
        
        #Quando acabar os elementos de P1 ou P2, pega os remanescentes e os
        # coloca no vetor aux
        while i < len(P1):
            meuVetor[k] = P1[i]
            i += 1
            k += 1

        while j < len(P2):
            meuVetor[k] = P2[j]
            j += 1
            k += 1

#printando o vetor
def PrintVetor(meuVetor):
    for i in range(len(meuVetor)):
        print(meuVetor[i], end = " ")
    print()


#Main
meuVetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
tamVetor = len(meuVetor)

MergeSort(meuVetor)

print("Vetor ordenado: ")
PrintVetor(meuVetor)
