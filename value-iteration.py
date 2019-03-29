# VALUE ITERATION

# estados=[1,2,3,4,5,6,7,8,9,10]
# probabilista 0,5 ficar no mesmo lugar e 0,5 para ir para o proximo estado
# direcoes N, S, L, O
# meta S5 -- r(S5)= 0

gama = 1
r = -1
epson = 0.0001

# posição 1 teste
listaLeste = [[0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0]]
             # [0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0],
              #[0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0]]
listaSul = [[0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0]]
listaOeste = [[1,  0, 0, 0, 0, 0, 0, 0, 0, 0]]
listaNorte = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

listaInicial = [[0]*10]#,[0]*10,[0]*10]
listaNova = [[0]*10]#,[0]*10,[0]*10]
#print('\n')
#print(listaInicial)
#print('\n')

matriz = []
listaNovaLeste =  [[0]*10]
listaNovaSul =  [[0]*10]
listaNovaOeste =  [[0]*10]
listaNovaNorte =  [[0]*10]

def moedorDeRegra(matriz, listaNova):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            t = matriz[i][i]
            tn = matriz[i][j]
            listaNova[i][j] = (t *(r + (gama*listaInicial[i][i]))) + (tn *(r + (gama*listaInicial[i][j])))


moedorDeRegra(listaLeste, listaNovaLeste)
moedorDeRegra(listaSul, listaNovaSul)
moedorDeRegra(listaOeste, listaNovaOeste)
moedorDeRegra(listaNorte, listaNovaNorte)

print(listaNovaLeste, listaNovaSul, listaNovaOeste, listaNovaNorte)

print(listaNova)



