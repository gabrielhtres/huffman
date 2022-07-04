def extrairMinimo(Q): # Função que extrai o nó com frequência mínima de Q
    i = 0 # Variável auxiliar
    menor = 99999 # Variável auxiliar
    for no in Q: # Laço que busca o nó de menor frequência
        if no[1] < menor:
            menor = no[1]
    
    while i < len(Q): # Laço que retira o menor nó encontrado da lista Q
        if Q[i][1] == menor:
            retirado = Q.pop(i)
            break
        else:
            i+=1
    
    return retirado # Retorno do nó retirado

def huffmann(): # Função principal de Huffman
    for j in range(0, n - 1): # Laço que executa n - 1 vezes
        esquerdo = extrairMinimo(Q) # Extração do nó mínimo de Q e atribuição ao filho esquerdo
        direito = extrairMinimo(Q) # Extração do nó mínimo de Q e atribuição ao filho direito
        frequencia = esquerdo[1] + direito[1] # Soma das frequências dos nós extraidos
        Z = [[esquerdo, direito], frequencia] # Alocação do novo nó Z
        Q.append(Z) # Inserção do novo nó criado na variável Q

# ------------------------ Início da execução do código ---------------------------------------
Q = [['a', 45], ['b', 13], ['c', 12], ['d', 16], ['e', 9], ['f', 5]] # Atribuição da tabela dos caracteres
                                                                     # e sua frequência na variável Q
n = len(Q) # Atribuição do tamanho de Q na variável N

huffmann() # Execução da funcão principal
print()
print()
print(Q) # Impressão da variável Q final
print()
print()