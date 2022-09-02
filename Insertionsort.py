
def Insertionsort(meuVetor, tamVetor):

    for i in range(1, len(meuVetor)):
        aux = meuVetor[i]
        j = i-1

        while j >= 0 and aux < meuVetor[j]:
            meuVetor[j + 1] = meuVetor[j]
            j = j - 1

        meuVetor[j + 1] = aux

#main
meuVetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
tamVetor = len(meuVetor)

Insertionsort(meuVetor, tamVetor)

print(meuVetor)
