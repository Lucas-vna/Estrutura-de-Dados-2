#Função Auxiliar
def Particiona(vetor, Inicio, Fim): 
    
    #escolher o número mais a direita como pivo
    pivo = vetor[Fim]

    #ponteiro para maioor elemento 
    i = Inicio-1

    #Passar por todos os elementos
    #comparar cada elemento com o pivo
    for j in range (Inicio, Fim):
        if vetor[j] <= pivo:
            #se um elemento menor que o pivo for encontrado
            #trocar com o maior elemento apontado popor i
            i = i + 1

            #trocando o elemento em i com o elemento em j
            (vetor[i], vetor[j]) = (vetor[j], vetor[i])

    #Trocar o pipvo com o maior elemento especificado por i
    (vetor[i+1], vetor[Fim]) = (vetor[Fim], vetor[i+1])

    #Retornar a posiçao em que a partiçao foi feita
    return i+1

#Função Principal
def QuickSort(vetor, Inicio, Fim):
    if (Inicio < Fim):

        #Achar o pivo, fazendo com que os elementos menores que o pivo fiquem
        #ao lado esquerdo, e os maiores ao lado direito do pivo
        pivo = Particiona(vetor, Inicio, Fim)

        #Chamada recursiva para a esquerda do pivo
        QuickSort(vetor, Inicio, pivo-1)

        #Chamada recursiva para a direita do pivo
        QuickSort(vetor, pivo+1, Fim)
        
#MAIN
vetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
TamVetor = len(vetor)

QuickSort(vetor, 0, TamVetor-1)

print(vetor)
