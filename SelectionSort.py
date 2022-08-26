#selectionSort(array, size)
#   repeat (size - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#       if element < currentMinimum
#           set element as new minimum
#   swap minimum with first unsorted position
#end selectionSort


def SelectionSort(meuVetor, tamanhoVetor):
    trocas = 0

    #repetir entre 0 e tamanho-1 vezes 
    for aux in range(0, tamanhoVetor-1):
        #definir a primeira posicao do vetor como o menor numero
        menor = aux

        for i in range(aux+1, tamanhoVetor):
            #if elemento < menor atual
            if meuVetor[i] < meuVetor[menor]:
                #elemento = menor
                menor = i
                #contagem de trocas feitas
                trocas += 1
        #trocar o menor para a primeira posicao nao organizada
        (meuVetor[aux], meuVetor[menor]) = (meuVetor[menor], meuVetor[aux])

    print(trocas)

    
#main
meuVetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
tamanhoVetor = len(meuVetor)

SelectionSort(meuVetor, tamanhoVetor)

print(meuVetor)
