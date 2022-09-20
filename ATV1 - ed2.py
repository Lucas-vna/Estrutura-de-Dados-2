#ATV1 - ed2
from getopt import getopt
from random import randint
import random
import sys
import getopt
import time

trocas = 0
dif = 0

#FUNÇÕES NORMAIS--------------------------------------------------------------------------------------------------------------------------


#INSERTION SORT
def insertionSort(vetor, tamVetor):
    global trocas
    global dif

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

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Insertion Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#SELECTION SORT   
def selectionSort(vetor, tamVetor):
    global trocas

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

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Selection Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#BUBBLE SORT
def bubbleSort(vetor, tamVetor):
    #trocou = true
    swapped = True

    global trocas

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

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Bubble Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#MERGE SORT
def mergeSort(vetor):
    global trocas

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
                i += 1    
                trocas += 1                 #aumenta a posicao que vai ser comparada do poteiro i (avanca uma casa no vetor ex: sai da posicao 0 para 1)
            else:
                vetor[k] = P2[j]        #copia esse numero da P2 para a posicao k do vetor aux
                j += 1    
                trocas += 1                 #aumenta a posicao que vai ser comparada do poteiro j (avanca uma casa no vetor ex: sai da posicao 0 para 1)
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

def imprimeVetorMerge():
    mergeSort(vetor)

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Merge Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#QUICK SORT 
def Particiona(vetor, Inicio, Fim): 
    global trocas

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

#Função Principal
def quickSort(vetor, Inicio, Fim):
    if (Inicio > Fim):

        #Achar o pivo, fazendo com que os elementos menores que o pivo fiquem
        #ao lado esquerdo, e os maiores ao lado direito do pivo
        pivo = Particiona(vetor, Inicio, Fim)

        #Chamada recursiva para a esquerda do pivo
        quickSort(vetor, Inicio, pivo-1)

        #Chamada recursiva para a direita do pivo
        quickSort(vetor, pivo+1, Fim)

def imprimeVetorQuick():
    tamVetor = len(vetor)

    quickSort(vetor, 0, tamVetor-1)

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Quick Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#HEAP SORT
def heapify(vetor, tamVetor, i):
    global trocas
      
    #Acha o maior entre as raizes e filhos
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < tamVetor and vetor[i] < vetor[l]:
        maior = l
  
    if r < tamVetor and vetor[maior] < vetor[r]:
        maior = r
  
    #Se a raiz não for maior, troca com o maior e continua a função
    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        trocas += 1
        heapify(vetor, tamVetor, maior)
  
def heapSort(vetor):
    global trocas
    tamVetor = len(vetor)
  
    #Constroi a heap maxima
    for i in range(tamVetor//2, -1, -1):
        heapify(vetor, tamVetor, i)
  
    for i in range(tamVetor-1, 0, -1):
        #Troca
        vetor[i], vetor[0] = vetor[0], vetor[i]
        trocas += 1

        #Heapify o elemento da raiz
        heapify(vetor, i, 0)

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Heap Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------



## FUNÇÕES REVERSE (ORDEM DECRESCENTE) ##

#--------------------------------------------------------------------------------------------------------------------------


#INSERTION SORT REVERSE
def insertionSortREV(meuVetor, tamVetor):
    global trocas

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

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Insertion Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#SELECTION SORT REVERSE
def selectionSortREV(meuVetor, tamanhoVetor):
    global trocas

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

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Selection Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#BUBBLE SORT REVERSE
def bubbleSortREV(meuVetor, N):
    #trocou = true
    swapped = True

    global trocas

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

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Bubble Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------


#MERGE SORT REVERSE
def mergeSortREV(vetor):
    global trocas

    if len(vetor) > 1:
        
        #Meio é o ponto onde o vetor vai ser dividido em 2 sub vetores
        Meio = len(vetor)//2
        P1 = vetor[:Meio] 
        P2 = vetor[Meio:]

        #definindo as duas partes
        mergeSortREV(P1)
        mergeSortREV(P2)

        #ponteiros
        #i contém o numero de P1, comeca em 1
        #j contém o numero de P2, comeca em 1
        #k contém o numero de funcao aux, comeca em p
        i = j = k = 0

        #Até chegarmos no final da P1 ou P2, pega a maior parte dos elementos de P1 e P2 
        # e os coloca na posicao correta no vetor aux
        while i < len(P1) and j < len(P2): #oq faz: enquanto a qntd de numeros no ponteiro i forem menores que o tamanho da P1 e enquanto a qntd de numeros no ponteiro j forem menores que o tamanho da P2 
            if P1[i] >= P2[j]:              #se o numero que estiver na posicao i de P1 for maior que o número que estiver na posicao j de P2:
                vetor[k] = P1[i]        #copia esse numero da P1 para a posicao k do vetor aux
                i += 1    
                trocas += 1                 #aumenta a posicao que vai ser comparada do poteiro i (avanca uma casa no vetor ex: sai da posicao 0 para 1)
            else:
                vetor[k] = P2[j]        #copia esse numero da P2 para a posicao k do vetor aux
                j += 1    
                trocas += 1                 #aumenta a posicao que vai ser comparada do poteiro j (avanca uma casa no vetor ex: sai da posicao 0 para 1)
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

def imprimeVetorMergeREV():
    mergeSortREV(vetor)

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Merge Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")


#-----------------------------------------------------------------------------------------------------------------------------------------

#QUICK SORT REVERSE 
def ParticionaREV(vetor, Inicio, Fim): 
    global trocas

    #escolher o número mais a direita como pivo
    pivo = vetor[Fim]

    #ponteiro para maioor elemento 
    i = Inicio-1

    #Passar por todos os elementos
    #comparar cada elemento com o pivo
    for j in range (Inicio, Fim):
        if vetor[j] > pivo:
            #se um elemento menor que o pivo for encontrado
            #trocar com o maior elemento apontado popor i
            i = i + 1

            #trocando o elemento em i com o elemento em j
            (vetor[i], vetor[j]) = (vetor[j], vetor[i])
            trocas += 1

    #Trocar o pivo com o maior elemento especificado por i
    (vetor[i+1], vetor[Fim]) = (vetor[Fim], vetor[i+1])
    trocas += 1

    #Retornar a posiçao em que a partiçao foi feita
    return i+1

#Função Principal
def quickSortREV(vetor, Inicio, Fim):
    if Inicio < Fim:

        #Achar o pivo, fazendo com que os elementos menores que o pivo fiquem
        #ao lado esquerdo, e os maiores ao lado direito do pivo
        pivo = ParticionaREV(vetor, Inicio, Fim)

        #Chamada recursiva para a esquerda do pivo
        quickSortREV(vetor, Inicio, pivo-1)

        #Chamada recursiva para a direita do pivo
        quickSortREV(vetor, pivo+1, Fim)

def imprimeVetorQuickREV():
    tamVetor = len(vetor)

    quickSortREV(vetor, 0, tamVetor-1)

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Quick Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")

#-----------------------------------------------------------------------------------------------------------------------------------------

#HEAP SORT REVERSE
def heapifyREV(vetor, tamVetor, i):
    global trocas
      
      #Acha o maior entre as raizes e filhos
    menor = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < tamVetor and vetor[l] < vetor[menor]:
        menor = l
  
    if r < tamVetor and vetor[r] < vetor[menor]:
        menor = r
  
    #Se a raiz não for maior, troca com o maior e continua a função
    if menor != i:
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
        trocas += 1
        heapifyREV(vetor, tamVetor, menor)
  
  
def heapSortREV(vetor, tamVetor):
    global trocas
    tamVetor = len(vetor)
  
    #Constroi a heap maxima
    for i in range(int(tamVetor//2) - 1, -1, -1):
        heapifyREV(vetor, tamVetor, i)
  
    for i in range(tamVetor-1, -1, -1):
        #Troca
        vetor[0], vetor[i] = vetor[i], vetor[0]
        trocas += 1
  
          #Heapify o elemento da raiz
        heapifyREV(vetor, i, 0)

    vetorStr = str(vetor)
    trocasStr = str(trocas)

    saida.write("Heap Sort: ")
    saida.write(vetorStr)
    saida.write(", ")
    saida.write(trocasStr)
    saida.write("comp, ")

#-----------------------------------------------------------------------------------------------------------------------------------------



#ARGV-------------------------------------------------------------------------------------------------------------------------------------

def main(argv):
   inputfile = 'input1.txt'
   outputfile = 'SaidaATV1-ed2.txt'

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile = input1.txt","ofile = SaidaATV1-ed2.txt"])
   except getopt.GetoptError:
      print ('test.py -i <input1.txt> -o <SaidaATV1-ed2.txt>')
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <input1.txt> -o <SaidaATV1-ed2.txt>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)



#MAIN-------------------------------------------------------------------------------------------------------------------------------------

main(sys.argv[3:])

print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Argument {i:>6}: {arg}")

#abrindo o arquivo e lendo o número  para o tamanho do vetor
entrada = open("C:/Users/miste/Desktop/Faculdade/Estrutura de Dados/teste/input1.txt", "r")
saida = open("SaidaATV1-ed2.txt","w")

entrada.seek(0,0)

tamVetor = (entrada.readline()).replace('\n', '') #N = número de posições do vetor
letra = (entrada.readline()).replace('\n', '') #Letra é a identificação do método

vetor = []
tamanho = int(tamVetor)

inicio = 0
fim = 0
dif = 0

if letra == 'c' and tamanho > 1 :

    for i in range (tamanho):
        vetor.append(random.randint(1,tamanho))

    #chamando a funcao com timer -> insertion
    inicio = time.time()
    insertionSort(vetor, tamVetor)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> selection
    inicio = time.time()
    selectionSort(vetor, tamanho)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> bubble
    inicio = time.time()
    bubbleSort(vetor, tamanho)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> merge
    inicio = time.time()
    imprimeVetorMerge()
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> quick
    inicio = time.time()
    imprimeVetorQuick()
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> heap
    inicio = time.time()
    heapSort(vetor)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")


if letra == 'd' and tamanho > 1:

    for i in range (tamanho):
        vetor.append(random.randint(1,tamanho))

    #chamando a funcao com timer -> insertion
    inicio = time.time()
    insertionSortREV(vetor, tamanho)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> selection
    inicio = time.time()
    selectionSortREV(vetor, tamanho)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> bubble
    inicio = time.time()
    bubbleSortREV(vetor, tamanho)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> merge
    inicio = time.time()
    imprimeVetorMergeREV()
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> quick
    inicio = time.time()
    imprimeVetorQuickREV()
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

    #chamando a funcao com timer -> heap
    inicio = time.time()
    heapSortREV(vetor, tamanho)
    time.sleep(10)
    fim = time.time()
    dif = (fim - inicio) * 1000
    saida.write("{:.2f}".format(dif))
    saida.write(" ms")
    saida.write("\n")

if letra == 'r':

    tamanho = 32000

    for i in range (tamanho):
        vetor.append(random.randint(0,tamanho))

    randomico = randint(0,11)

    if randomico % 2 == 0:
        #chamando a funcao com timer -> insertion
        inicio = time.time()
        insertionSort(vetor, tamVetor)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> selection
        inicio = time.time()
        selectionSort(vetor, tamanho)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> bubble
        inicio = time.time()
        bubbleSort(vetor, tamanho)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> merge
        inicio = time.time()
        imprimeVetorMerge()
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> quick
        inicio = time.time()
        imprimeVetorQuick()
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> heap
        inicio = time.time()
        heapSort(vetor)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

    else:
        #chamando a funcao com timer -> insertion
        inicio = time.time()
        insertionSortREV(vetor, tamanho)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> selection
        inicio = time.time()
        selectionSortREV(vetor, tamanho)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> bubble
        inicio = time.time()
        bubbleSortREV(vetor, tamanho)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> merge
        inicio = time.time()
        imprimeVetorMergeREV()
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> quick
        inicio = time.time()
        imprimeVetorQuickREV()
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

        #chamando a funcao com timer -> heap
        inicio = time.time()
        heapSortREV(vetor, tamanho)
        time.sleep(10)
        fim = time.time()
        dif = (fim - inicio) * 1000
        saida.write("{:.2f}".format(dif))
        saida.write(" ms")
        saida.write("\n")

entrada.close()
saida.close()
