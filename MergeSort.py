#funcao principal
def MergeSort(meuVetor):

    if len(meuVetor) > 1:
        
        #Meio é o ponto onde o vetor vai ser dividido em 2 partes
        Meio = len(meuVetor)//2
        P1 = meuVetor[:Meio] 
        P2 = meuVetor[Meio:]

        #definindo as duas partes
        MergeSort(P1)
        MergeSort(P2)

        i = j = k = 0

        #Até chegarmos no final da P1 ou P2, pega a maior parte dos elementos de P1 e P2 
        # e os coloca na posicao correta no vetor
        while i < len(P1) and j < len(P2):
            if P1[i] < P2[j]:
                meuVetor[k] = P1[i]
                i += 1
            else:
                meuVetor[k] = P2[j]
                j += 1
            k += 1
        
        #Quando acabar os elementos de P1 e P2, pega os remanescentes e os
        # coloca no vetor
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
if __name__ == '__main__':
    meuVetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
    tamVetor = len(meuVetor)

    MergeSort(meuVetor)

    print("Vetor ordenado: ")
    PrintVetor(meuVetor)
