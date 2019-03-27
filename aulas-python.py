n1 = int(input('\nDigite um numero :\n'))
n2 = int(input('Digite outro numero :\n'))
soma = n1 + n2
divisao = n1 / n2
subtracao =n1 - n2
multiplicacao = n1 * n2
divisaoInteira = n1 // n2
exponenciacao = n1 ** n2
raizQuadradaDeN1 = n1**(1/2)
raizCubcaN1 = n1**(1/3)

print("-"*40)
print('A soma de {} com {} é igual a: {}'.format(n1, n2, soma))
print("*"*40)
print('A divisão é : {:.3f}'.format(divisao))
print('A subtracao é : {}'.format(subtracao))
print('A multiplicacao é : {}'.format(multiplicacao))
print('A divisaoInteira é : {}'.format( divisaoInteira))
print('A exponenciacao é : {}'.format( exponenciacao))
print('A raizQuadrada De N1 é : {:.3f}'.format( raizQuadradaDeN1))
print('A raiz Cubca N1 é : {:.3f}'.format( raizCubcaN1))

print('*'*40)

listaLeste=[[0,0.5,0],[0.5,0,0.5],[0.5,0,0]]
#print(listaLeste)

for i in range(0,len(listaLeste)):
    for j in range(0,len(listaLeste[i])):
        print(listaLeste[i][j])
