# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:58:51 2020

@author: claudia barreto :)
"""
#LPI pratica
"""
Indique qual o resultado será obtido das seguintes expressões (lembre-se de usar “.” não “,” para casas decimais)
"""
a = 44 + 1
b = 6 + 20 - 23
c = 3.0 + 5.0 - 1
d= (1/4) + 2
e = (29.0/7) + 4
f = (3/6.0) - 7
g = 2 / 2
h = 2 // 2
i = 4 % 2
j = (100//5) % 5

print(a ,"",b,"",c,"",d,"",e,"",f,"",g,"",h,"",i,"",j,"")

"""
Faça uma função python para multiplicar dois números.
"""

x = float(input('digite um valor'))
y = float(input('digite outro valor'))

def multiplicacao(x,y):
    calculo = x ** y
    return calculo

resultado = multiplicacao(x,y)
print(resultado)


"""
Faça uma função para calcular a raiz do número passado. a. Raiz quadrada. b. Raiz cúbica. c.Passe também o expoente índice da raiz.

"""

indice = 2
valor = int(input('digite o valor a ser calculado a raíz'))
def calcular_raiz_quadrada(valor):
    x = valor ** (1/2) 
    return x

resultado = calcular_raiz_quadrada(valor)
print(resultado, " o índice é:", indice)

indice = 3
valor = int(input('digite o valor a ser calculado a raíz'))
def calcular_raiz_cubica(valor):
    x = valor ** (1/3) 
    return x

resultado = calcular_raiz_cubica(valor)
print(resultado, " o índice é:", indice)

"""
Faça um função para calcular a área de: um quadrado, um triângulo, um retângulo. Para cada função, determine os parâmetros que precisam.

"""

valor_base = float(input('digite o valor da base'))
valor_altura= float(input('digite o valor da altura'))

def calcular_area_retangulo(valor_base,valor_altura):
    base = float(valor_base)
    altura = float(valor_altura)
    calculo = base * altura
    return calculo


def calcular_area_triangulo_retangulo(valor_base,valor_altura):
    base = float(valor_base)
    altura = float(valor_altura)
    calculo = ((base * altura)/2)
    return calculo


def calcular_area_quadrado(valor_base):
    base = float(valor_base)
    calculo = (base * base)
    return calculo
#porque tanto a base quanto a altura tem o msm comprimento então, só deixei o nome de base msm podia ter colocado lado

resultado_triangulo = calcular_area_triangulo_retangulo(valor_base,valor_altura)
resultado_quadrado = calcular_area_quadrado(valor_base)
resultado_retangulo = calcular_area_retangulo(valor_base,valor_altura)
print(resultado_retangulo, resultado_quadrado,resultado_triangulo)


"""
Faça um função para receber 3 parâmetros com valores inteiros. Considere que os valores inteiros correspondem ao tamanho de três arestas. Verifique se é possível formar um triângulo com essas arestas (nesse caso usaremos o 'if' para verificar condições).

"""

a = float(input('digite um valor'))
b = float(input('digite outro valor'))
c = float(input('digite um ultimo valor'))


if a>=b+c or b>=c+a or c>=a+b :
   print("triangulo inexistente.")
else:
    print("é um triangulo")

"""

6. Faça programas que:
  a. Leia um número e imprima o seu quadrado.
##  b. Leia dois números e imprima a divisão do primeiro pelo segundo.
  c. Leia um número e imprima o resto da divisão desse número por 2.
  d. Leia dois número e imprima a média.
  e. Calcule a área de uma circunferência considerando que o usuário informe o comprimento do raio. Para essa questão, declare uma variável “pi” com valor de 3,14 e use como valor de π. Calcule também o comprimento e o diâmetro.


"""

#a

numero = float(input('digite um número'))
quadrado = numero ** 2
print(quadrado)

#b
numero_um = float(input('digite um numero'))
numero_dois = float(input('digite um numero para o divisor'))
divisao = numero_um/numero_dois

#c

numero = float(input('digite um valor a ser dividido'))
divisao_resto = numero % 2 
print(divisao_resto)

#d 

valor_um = int(input('digite o primeiro valor'))
valor_dois = int(input('digite o segundo valor'))
media = valor_um + valor_dois / 2
print(media)

#e 

pi = 3.14
raio = float(input('digite o raio'))

area_circunferencia = pi * (raio**2)
print(area_circunferencia)

diametro =  2 * raio
print(diametro)

comprimento = 2 * pi * raio
print(comprimento)

'''

7. Indique o resultado lógico das seguintes expressões (faça com o python): 
  a. 2 < 3
  b. ( 6 < 3 ) OU ( 10 > 11 )
  c. ((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) )
  d. !( 2 < 3 )

'''

2 < 3
#TRUE

( 6 < 3 ) or ( 10 > 11 )
#false

((( 6 // 3 ) % 2 ) > 5 ) and ( 2 < ( 3 % 2 ) )
#false

!( 2 < 3 )
#nao roda