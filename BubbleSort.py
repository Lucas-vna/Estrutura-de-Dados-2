
def BubbleSort(meuVetor, N):
    #trocou = true
    swapped = True

    trocas = 0

    #while true:
    while swapped == True:
      #trocou = false
      swapped = False

      for i in range(0, N-1):
          if meuVetor[i] > meuVetor[i + 1]:
              meuVetor[i], meuVetor[i + 1] = meuVetor[i + 1], meuVetor[i]
              trocas += 1; 
              #trocou = false
              swapped = True

    print("quantidade de trocas feitas: ", trocas)

#main
meuVetor = [-82, 23, -31, 44, -38, -94, 32, -71, -93, 38, -9, -95, -60, 17, -1]
N = len(meuVetor)

BubbleSort(meuVetor, N)

print(meuVetor)
