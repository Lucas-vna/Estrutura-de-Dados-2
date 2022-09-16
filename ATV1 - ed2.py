#ATV1 - ed2

#FUNÇÕES NORMAIS--------------------------------------------------------------------------------------------------------------------------

#INSERTION SORT
def insertionSort(vetor, tamVetor):
    trocas = 0

    #para i entre 1 e len(meuVetor):
    for i in range(1, len(vetor)):
        aux = vetor[i]
        j = i-1

        #enquanto i >= 0 and aux < meuVetor[j-1]
        while j >= 0 and aux < vetor[j]:
            vetor[j + 1] = vetor[j]
            j = j - 1
            trocas += 1

        vetor[j + 1] = aux

    print(trocas)
#-----------------------------------------------------------------------------------------------------------------------------------------

#SELECTION SORT   
def selectionSort(vetor, tamVetor):
    trocas = 0

    #repetir entre 0 e tamanho-1 vezes 
    for aux in range(0, tamVetor-1):
        #definir a primeira posicao do vetor como o menor numero
        menor = aux

        for i in range(aux+1, tamVetor):
            #if elemento < menor atual
            if vetor[i] < vetor[menor]:
                #elemento = menor
                menor = i
                #contagem de trocas feitas
                trocas += 1
        #trocar o menor para a primeira posicao nao organizada
        (vetor[aux], vetor[menor]) = (vetor[menor], vetor[aux])

    print(trocas)
#-----------------------------------------------------------------------------------------------------------------------------------------

#BUBBLE SORT
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
#-----------------------------------------------------------------------------------------------------------------------------------------

#MERGE SORT #contador de trocas não feito

#funcao principal
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
#-----------------------------------------------------------------------------------------------------------------------------------------

#QUICK SORT contador de troca nao feito
def Particiona(vetor, Inicio, Fim): 
    trocas = 0

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
            trocas += 1

    #Trocar o pipvo com o maior elemento especificado por i
    (vetor[i+1], vetor[Fim]) = (vetor[Fim], vetor[i+1])
    trocas += 1

    #Retornar a posiçao em que a partiçao foi feita
    return i+1

    print(trocas)

#Função Principal
def quickSort(vetor, Inicio, Fim):
    if (Inicio < Fim):

        #Achar o pivo, fazendo com que os elementos menores que o pivo fiquem
        #ao lado esquerdo, e os maiores ao lado direito do pivo
        pivo = Particiona(vetor, Inicio, Fim)

        #Chamada recursiva para a esquerda do pivo
        quickSort(vetor, Inicio, pivo-1)

        #Chamada recursiva para a direita do pivo
        quickSort(vetor, pivo+1, Fim)
#-----------------------------------------------------------------------------------------------------------------------------------------

#HEAP SORT contador de troca nao feito
def heapify(vetor, tamVetor, i):
    trocas = 0
      
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
        trocas += 1
        heapify(vetor, tamVetor, maior)
    
    print(trocas)
  
  
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
#-----------------------------------------------------------------------------------------------------------------------------------------





#FUNÇÕES REVERSE--------------------------------------------------------------------------------------------------------------------------

#INSERTION SORT REVERSE
def insertionSortREV(meuVetor, tamVetor):
    trocas = 0

    #para i entre 1 e len(meuVetor):
    for i in range(1, len(meuVetor)):
        aux = meuVetor[i]
        j = i-1

        #enquanto i >= 0 and aux < meuVetor[j-1]
        while j >= 0 and aux > meuVetor[j]:
            meuVetor[j + 1] = meuVetor[j]
            j = j - 1
            trocas += 1

        meuVetor[j + 1] = aux

    print(trocas)
#-----------------------------------------------------------------------------------------------------------------------------------------


#SELECTION SORT REVERSE
def selectionSortREV(meuVetor, tamanhoVetor):
    trocas = 0

    #repetir entre 0 e tamanho-1 vezes 
    for aux in range(0, tamanhoVetor-1):
        #definir a primeira posicao do vetor como o menor numero
        menor = aux

        for i in range(aux+1, tamanhoVetor):
            #if elemento < menor atual
            if meuVetor[i] > meuVetor[menor]:
                #elemento = menor
                menor = i
                #contagem de trocas feitas
                trocas += 1
        #trocar o menor para a primeira posicao nao organizada
        (meuVetor[aux], meuVetor[menor]) = (meuVetor[menor], meuVetor[aux])

    print(trocas)
#-----------------------------------------------------------------------------------------------------------------------------------------

#MERGE SORT REVERSE ----- #contador de trocas não feito
#funcao principal
def mergeSortREV(vetor):

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
            if P1[i] > P2[j]:              #se o numero que estiver na posicao i de P1 for maior que o número que estiver na posicao j de P2:
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
#-----------------------------------------------------------------------------------------------------------------------------------------

#QUICK SORT REVERSE ----- contador de troca nao feito
def Particiona(vetor, Inicio, Fim): 
    trocas = 0

    #escolher o número mais a direita como pivo
    pivo = vetor[Fim]

    #ponteiro para maioor elemento 
    i = Inicio-1

    #Passar por todos os elementos
    #comparar cada elemento com o pivo
    for j in range (Inicio, Fim):
        if vetor[j] >= pivo:
            #se um elemento menor que o pivo for encontrado
            #trocar com o maior elemento apontado popor i
            i = i + 1

            #trocando o elemento em i com o elemento em j
            (vetor[i], vetor[j]) = (vetor[j], vetor[i])
            trocas += 1

    #Trocar o pipvo com o maior elemento especificado por i
    (vetor[i+1], vetor[Fim]) = (vetor[Fim], vetor[i+1])
    trocas += 1

    #Retornar a posiçao em que a partiçao foi feita
    return i+1

    print(trocas)

#Função Principal
def quickSortREV(vetor, Inicio, Fim):
    if (Inicio < Fim):

        #Achar o pivo, fazendo com que os elementos menores que o pivo fiquem
        #ao lado esquerdo, e os maiores ao lado direito do pivo
        pivo = Particiona(vetor, Inicio, Fim)

        #Chamada recursiva para a esquerda do pivo
        quickSort(vetor, Inicio, pivo-1)

        #Chamada recursiva para a direita do pivo
        quickSort(vetor, pivo+1, Fim)
#-----------------------------------------------------------------------------------------------------------------------------------------

#HEAP SORT REVERSE ------ contador de troca nao feito
def heapify(vetor, tamVetor, i):
    trocas = 0
      
      #Acha o maior entre as raizes e filhos
    menor = i
    L = 2 * i + 1
    R = 2 * i + 2
  
    if L < tamVetor and vetor[L] < vetor[menor]:
        menor = L
  
    if R < tamVetor and vetor[R] < vetor[menor]:
        menor = R
  
    #Se a raiz não for maior, troca com o maior e continua a função
    if menor != i:
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
        trocas += 1
        heapify(vetor, tamVetor, menor)
    
    print(trocas)
  
  
def heapSortREV(vetor, tamVetor):
    tamVetor = len(vetor)
  
    #Constroi a heap maxima
    for i in range(int(tamVetor/2) - 1, -1, -1):
        heapify(vetor, tamVetor, i)
  
    for i in range(tamVetor-1, -1, -1):
        #Troca
        vetor[0], vetor[i] = vetor[i], vetor[0]
  
          #Heapify o elemento da raiz
        heapify(vetor, i, 0)
#-----------------------------------------------------------------------------------------------------------------------------------------

#BUBBLE SORT REVERSE
def bubbleSortREV(meuVetor, N):
    #trocou = true
    swapped = True

    trocas = 0

    #while true:
    while swapped == True:
      #trocou = false
      swapped = False

      for i in range(0, N-1):
          if meuVetor[i] < meuVetor[i + 1]:
              meuVetor[i], meuVetor[i + 1] = meuVetor[i + 1], meuVetor[i]
              trocas += 1; 
              #trocou = false
              swapped = True

    print(trocas)
#-----------------------------------------------------------------------------------------------------------------------------------------



#MAIN-------------------------------------------------------------------------------------------------------------------------------------

#abrindo o arquivo e lendo o número  para o tamanho do vetor
entrada = open("C:/Python/input1.txt", "r")

N = entrada.readline() #N = número de posições do vetor
Letra = entrada.readline() #Letra é a identificação do método

vetor = []
tamVetor = len(vetor)

if Letra == 'c' and N > 1 :

    for i in range (N):
        vetor.append(i+1)
    print(vetor)

    insertionSort(vetor, tamVetor)
    selectionSort(vetor, tamVetor)
    bubbleSort(vetor, tamVetor)
    mergeSort(vetor)
    quickSort(vetor, 0, tamVetor-1)
    heapSort(vetor)

if Letra == 'd' and N > 1:
    teste 




print(N)
print(Letra)


saida = open("SaidaATV1-ed2.txt","w")


