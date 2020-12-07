# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:52:19 2020

@author: convi
"""

#11.Crie um programa para ler uma string fornecida pelo usuário. Informe se essa stringforma um palíndromo.

palavra = input("")

for i in range(int(len(palavra)/2)):
    if(palavra[i] != palavra[-i - 1]):
        print("não é palindromo")
print("é palindromo")


#12 Crie um programa para ler duas strings fornecidas pelo usuário. Verifique se elasforam um anagrama.


a = input('digite uma palavra:')
b = input('digite outra palavra:')

x = list(a)
x.sort()
print(x)

y = list(b)
y.sort()
print(y)

if x == y:
    print('é um anagrama')
else:
    print('não é um anagrama')


#13.Faça um programa para multiplicar matrizes 3x3.

 
m1 =  [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m2 =  [[0, 0, 0], [1, 1, 1], [2, 2, 5]]

resultado = []
for i in range(len(m1)):
    linha = []
    for j in range(len(m2[0])):
        linha.append(m1[i][j] * m2[i][j])
    resultado.append(linha)
    
print(resultado)

"""
#14.Faça um programa para calcular a soma
, a subtração e a multiplicação de matrizes.
Você pode fornecer a matriz no código, em vez de ler o que o usuário digitar, 
mas suasfunções que fazem os cálculos devem ser úteis para qualquer tamanho de matriz desde que aspropriedades matemáticas sejam respeitadas.
"""

m1 =  [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m2 =  [[0, 0, 0], [1, 1, 1], [2, 2, 5]]

def calcula(operacao):
    resultado = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m2[0])):
            if(operacao == "soma"):
                linha.append(m1[i][j] + m2[i][j])
            elif(operacao == "mult"):
                linha.append(m1[i][j] * m2[i][j])
            elif(operacao == "sub"):
                linha.append(m1[i][j] - m2[i][j])
        resultado.append(linha)
    return resultado

print(calcula("soma"))
print(calcula("mult"))
print(calcula("sub"))


"""
15.Crie um programa que verifica todos os números perfeitos em um intervalo fornecidopelo usuário.
 Ou seja, o usuário fornece dois valores (inicial e final) 
 e o programa verifica seexiste e quais são os números perfeitos nesse intervalo. 
 Para saber o que são númerosperfeitos, busque na wikipedia.
"""
inicial = int(input(""))
final = int(input(""))

if(inicial <= 0):
    inicial = 1

for i in range(inicial, final + 1):
    soma_divisores = 0
    for j in range(1, i):
        if(i % j == 0):
            soma_divisores += j
    if(soma_divisores == i):
        print(i, " é um numero perfeito")
