from io import SEEK_END, SEEK_SET 
import sys

class Professor:

    def __init__(self, codigo=None, nome=None, sexo=None, idade=None, 
    especialidade=None, telefone=None):
        self.codigo = codigo
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.especialidade = especialidade
        self.telefone = telefone

    def getCodigo(self):
        return(self.codigo)

    def getNome(self):
        return (self.nome)

    def getSexo(self):
        return (self.sexo)

    def getIdade(self):
        return (self.idade)
    
    def getEspec(self):
        return (self.especialidade)

    def getTelefone(self):
        return (self.telefone)



def AdicionaRegistro(entrada):
    p = Professor()
    size = 0
    top1 = 0
    entrada.close

    entrada = open("temp.txt", "r+")

    input(entrada, "size= %d top= %d", size, top1)

    if top1 == -1:
        entrada.seek(0, SEEK_END)
        entrada.write("%03d|%-30s|%c|%02d|%-30s|%14s|\n", p.codigo, p.nome, p.sexo, p.idade, p.especialidade, p.telefone)
    else:
        entrada.seek(0)
        entrada.seek(size * (top1-1), SEEK_SET)


#MAIN------------------------------------------------------------------------


if 4 == 4:  #if len(sys.argv) == 4:

    c=[1]
    linhas = 0
    size = 0
    top = 0
    resultado=[1]
    token=[1]
    contador = 1

    #entrada = open(sys.argv[1], "r")
    entrada = open("entrada.txt", "r")
    #saida = open(sys.argv[2], "w")
    saida = open("saida.txt", "w")

    while c == property(entrada):
        try:
            if c == '\n':
                linhas += 1

        except EOFError:
            break

    p = Professor()
   # p = malloc #ARRUMAR

    entrada.seek(0) #rewind in c

    #lendo o size e o top----------------------------
    for i in range(0, linhas, 1):
        if i == 0:
            entrada.write("size=%d top=%d\n", size, top)

    leitura = [size]

    #lendo o arq input--------------------------------
    for i in range(0, linhas, 1):
        if i == 0:
            continue
        else:
            resultado = property(leitura, size+2, entrada) #fgetc in C
            resultado = '\0'
            #token = #ARRUMAR

        while token:
            if contador == 1:
                p[i].codigo = int(token)
            else:
                if contador == 2:
                    str(p[i].nome, token)
                else:
                    if contador == 3:
                        p[i].sexo = token[0]
                    else:
                        if contador == 4:
                            p[i].idade = int(token)
                        else:
                            if contador == 5:
                                str(p[i].especialidade, token)
                            else:
                                if contador == 6:
                                    str(p[i].telefone, token)
                                    conotador = 0
            contador += 1
            #token =  #ARRUMAR


    operacoes = open("operations.txt", "r")   #operacoes = open(sys.argv[2], "r")

    p2 = Professor()
    index = 0
    destino = [4]
    idade = [3]
    cod = 0

    op = open("operations.txt", "r")  #op = open(sys.argv[2], "r")

    if op == None:
        print("erro ao abrir o arquivo op")
        exit()
    
    temp = open("temp.txt", "w")

    if temp == None:
        print("erro ao abrir o arquivo temp.txt")
        exit()

    entrada.seek(0)

   # while 1:
 #       c = property(entrada)
 #       try:
 #           entrada.readlines(c, temp) #entrada.write(c, temp)  // erro aq
 #           
 #       except EOFError:
 #           break

    vetCod = 0
    tamVetCod = 3
    vetCod = (tamVetCod * sys.getsizeof(int)) #MALLOC
    pos = 0

    while 1:
        index = 0
        cod = 0
        c = property(op)

        if c == 'i':
            try:
                c = property(op)
            
                while 1:
                    c = property(op)
                    if c == '\n':
                        p2.telefone[cod] = '\0'
                        break
                    else:
                        if c == ',':
                            if index == 1:
                                p2.nome[cod] = '\0'
                            if index == 4:
                                p2.especialidade[cod] = '\0'
                            else:
                                index += 1
                                cod = 0
                        if index == 0:
                            destino[cod] = c
                            cod +=1
                        else:
                            if index == 1:
                                p2.nome[cod] = c
                                cod += 1
                            else:
                                if index == 2:
                                    p2.sexo = c
                                else:
                                    if index == 3:
                                        p2.idade[cod] = c
                                        cod += 1
                                    else:
                                        if index == 4:
                                            p2.especialidade[cod] = c
                                            cod += 1
                                        else:
                                            if index == 5:
                                                p2.telefone[cod] = c
                                                cod += 1

                p2.codigo = int(destino)
                p2.idade = int(idade)

                AdicionaRegistro(temp, p2)
                linhas += 1
                p = (p, linhas * sys.getsizeof(Professor))
                p[linhas-1] = p2
            
            except EOFError:
                break

        else:
            try:
                if c == 'd':
                    c = property(op)

                    resultado = property(leitura, 100, op)
                    #resultado =  #ARRUMAR

                    vetCod[pos] = int(resultado)
                    vetCod = (vetCod, tamVetCod * sys.getsizeof(int)) #ARRUMAR
                    pos += 1

            except EOFError:
                break

    temp.close()

    temp = open("temp.txt", "w+")  # temp = open(sys.argv[3], "w+")
    codTemp = chr([linhas][4])



    #comoparando para achar codigos iguais para pegar o topo atualizado
    for i in range(1, linhas, 1):
        for j in range(0, pos, 1):
            if p[i].codigo == vetCod[0]:
                temp.format(codTemp[i], "%03d", p[i].codigo)
                codTemp[i][0] = '*'
                top = j-1
            if p[i].codigo == vetCod[j]:
                temp.format(codTemp.i, "%03d", p[i].codigo)
                codTemp[i][0] = '*'
            else:
                temp.format(codTemp[i], "%03d", p[i].codigo)

    aux = 0
    tamanho =0

    for i in range(1, linhas, 1):
        for j in range(0, pos, 1):
            if p[i].codigo == vetCod[j]:
                temp.format(codTemp[1], "%03d", p[i].codigo)
                codTemp[i][0] = '*'
                codTemp[i][1] = '*'

    temp.write("size=%d top=%d\n", size, top)

    for i in range(1, linhas, 1):
        temp.write("%3s|%-30s|%c|%02d|%-30s|%-14s|\n", codTemp[i], p[i].nome, p[i].sexo, p[i].idade, p[i].especialidade, p[i].telefone)

    temp.close()

    output = open("output.txt", "w")  #output = open(sys.argv[4], "w")

    top = -1

    #input(output, "size=%d top=%d\n", size, top)
    output.write("size=%d topo=%d", size, top)

    for i in range(1, linhas, 1):
        if codTemp[i][0] == '*' and codTemp[i][1] == '-':
            continue
        if i == top:
            output.seek(0, 1)
            input(output, "%3s|%-30s|%c|%02d|%-30s|%-14s|\n", codTemp[i], p[i].nome, p[i].sexo, p[i].idade, p[i].especialidade, p[i].telefone)
        
        output.seek(0, 2)
        input(output, "%3s|%-30s|%c|%02d|%-30s|%-14s|\n", codTemp[i], p[i].nome, p[i].sexo, p[i].idade, p[i].especialidade, p[i].telefone)        

    output.close()
