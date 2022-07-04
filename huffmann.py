Q = [['a', 45], ['b', 13], ['c', 12], ['d', 16], ['e', 9], ['f', 5]]
C = []
n = len(Q)

def extrairMinimo(Q):
    i = 0
    menor = 99999
    for no in Q:
        if no[1] < menor:
            menor = no[1]
    
    # print(menor)
    while i < len(Q):
        if Q[i][1] == menor:
            retirado = Q.pop(i)
            break
        else:
            i+=1
    
    return retirado

def huffmann():
    for j in range(0, n - 1):
        esquerdo = extrairMinimo(Q)
        direito = extrairMinimo(Q)
        frequencia = esquerdo[1] + direito[1]
        Z = [[esquerdo, direito], frequencia]
        # print(Z)
        Q.append(Z)
        C.append(Z)

huffmann()