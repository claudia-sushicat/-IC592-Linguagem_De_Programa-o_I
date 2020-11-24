# -*-  -*-
"""
Aluna: Claudia Barreto de Oliveira
IC 592
    
'''



         |     |              |     |
         |     |              |     |    
          - = -               - = -       
                 \   /\  /
                  \/   \/
                  
'''        
"""


'''
1.Faça programas que:
    a.Leia um número e imprima o seu quadrado.
    b.Leia dois números e imprima a divisão do primeiro pelo segundo.
    c.Leia um número e imprima o resto da divisão desse número por 2.
    d.Leia dois número e imprima a média.
    e.Calcule   a   área   de   uma   circunferência   considerando   que   o   usuário   informe   ocomprimento do raio. 
        Para essa questão, declare uma variável “pi” com valor de 3,14 euse como valor de π. Calcule também o comprimento e o diâmetro.
'''
x = float(input('digite um número'))    
y = float(input('digite um segundo número'))    

def quadrado(x):
    calculo = x ** 2
    return calculo

print(quadrado(x))

def divisao(x,y):
    calculo = (x/y)
    return calculo

print(divisao(x,y))    

def divisao_resto(x):
    calculo = x % 2
    return calculo

print(divisao_resto(x))


def media(x,y):
    calculo = ((x + y) / 2)
    return calculo

print(media(x,y))


pi = 3.14
raio = float(input('digite o raio'))

area_circunferencia = pi * (raio**2)
print(area_circunferencia)

diametro =  2 * raio
print(diametro)

comprimento = 2 * pi * raio
print(comprimento)

'''
2.Indique qual o resultado será obtido das seguintes expressões 
(lembre-se de usar “.” não“,” para casas decimais):
    a.4*4 + 1
    b.6 +20-23
    c.3,0* 5,0 +1
    d.1/4+2
    e.29,0/7+4
    f.3/6,0-7
    g.2 / 2
    h.2 // 2
    i.4 % 2
    j.( 100 // 5 ) % 5
'''

4 * 4 + 1
#17
6 + 20-23
#3
3.0 * 5.0 +1
#16
1/4 + 2
#2.25
(29/7) + 4
#8.142857142857142 
(3/6.0) - 7
#-6.5
2/2
#1
2//2
#1
4%2
#0
( 100 // 5 ) % 5
#0

'''
3.Indique o resultado lógico das seguintes expressões: 
    a.2 < 3
    b.( 6 < 3 ) OU ( 10 > 11 )
    c.((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) )
    d.!( 2 < 3 )
'''

2 < 3 #true
( 6 < 3 ) or ( 10 > 11 ) #false
((( 6 // 3 ) % 2 ) > 5 ) and ( 2 < ( 3 % 2 ) ) #false
( 2 < 3 ) # com o ! nao funciona, se for o caso de ser 3 > 2 entao é true


'''
4.Escreva   o   comando   de   atribuição   e   resolva   a   expressão   das   seguintes   fórmulas
matemáticas.
'''

#a

a = 10
b = 3
c = 3
d = 4
e = 4
f = 2
x = (( a - ((b/c) *2))/ d + (e/f)) * 2
print(x) #8

x = 4
y = ( 2 + x - (((2*(x**2)**(x + 2))))/2) - (((x+1)**1/2)/x)/( 3 ** x)
print(y)


'''
5.Faça   um   programa   para   ler   o   nome   do   usuário   e   escrever   na   tela   
“Olá   [nomeinformando]”. 
Por exemplo, considere que eu use seu programa, vou escrever meu nome e 
oprograma deve imprimir “Olá Tiago”.
'''

nome = input('digite seu nome')
print('Olá,',nome, " :) !")

'''
6.Escreva   um   programa   para   ler   3   valores   inteiros   diferentes   
e   escrevê-los   em   ordemcrescente.
'''
i = 0
qnt_valores = 3
valores = []
while i < qnt_valores:
    valores.append(int(input('digite um número')))
    i += 1
print(valores)

print(sorted(valores))

"""
7.Escreva um programa para ler um valor e escrever se é positivo ou negativo.
 Considere ovalor zero como positivo.
"""

x = int(input('digite um número'))
print(x)

if x < 0:
    print(x , ' é um número negativo')
else:
    print(x, ' é um número positivo')
    
"""
8.Escreva um programa para ler uma temperatura em graus 
Celsius, calcular e escrever ovalor correspondente em graus Fahrenheit e Kelvin
"""


temperatura = float(input('digite a temperatura'))

def conversao_temperatura():
    t_k = 273
    calculo_K =  t_k + temperatura
    calculo_F = (temperatura * (9/5)) + 32
    return calculo_K,calculo_F

print(conversao_temperatura())

'''
9.Faça um programa que leia duas entradas de tipos numéricos. 
Verifique qual o maior dos dois ou se eles são iguais
Imprima uma mensagem informando.
'''

x = int(input('digita um valor'))
y = int(input('digite outro valor'))

if x == y:
    print('são iguais :0')
elif x > y:
    print('o primeiro valor é maior que o segundo ')
elif y > x:
    print('o segundo valor é maior que o primeiro')
    
'''
10.Escreva um programa que leia um número menor igual a 10 e informe se esse número
é primo.
'''    

x = int(input('digita um número'))

def verf_primo(x):
    for i in range(2,x):
       if x % i == 0:
           return 'não é um número primo'
    return 'é um número primo'


if x <= 10:
    print(verf_primo(x))
else:
    while x > 10:
        x = int(input('digita um número entre 0 e 10'))
        print(verf_primo(x))
                  
         

'''
11.Faça   um   programa   que   leia   três   entradas   de   inteiros.
   Considere   que   cada   entradacorresponde   ao   comprimento   de   uma   aresta
   de   um   triângulo.   
   Verifique   se   os   valores passados permitem que 
   seja formado um triângulo considerando que elas devem se tocar nas extremidades.
'''

a = float(input('digite um valor'))
b = float(input('digite outro valor'))
c = float(input('digite um ultimo valor'))


if a>=b+c or b>=c+a or c>=a+b :
   print("não é possivel formar um triangulo ")
else:
    print("é possivel formar um triangulo")
    
    
'''
12.Faça um programa para calcular a área de um triângulo. 
O usuário deve fornecer osvalores da base e da altura.

'''


def calcular_area_triangulo(valor_base,valor_altura):
    base = float(valor_base)
    altura = float(valor_altura)
    calculo = ((base * altura)/2)
    return calculo


valor_base = input('Digite o valor para a base')
valor_altura = input('Digite o valor para a altura')
calculo_final = calcular_area_triangulo(valor_base,valor_altura)
print("a area do triangulo retangulo é de:", calculo_final)


'''
13.Escreva um programa que leia três entradas numéricas correspondentes às 
arestas deum triângulos. 
Caso os valores permitam que seja formado um triângulo, 
informe qual tipo de triângulo (equilátero, isósceles ou escaleno).
'''
a = int(input())
b = int(input())
c = int(input())

print(a,b,c)
if a == b or b == c or a == c:
    print('é um triangulo isosceles')
elif a != b and a != c:
    print('é um triangulo escaleno')
elif a == b and a == c:
    print('é um triangulo equilatero')
    
'''
14.Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é
 Acutângulo, Retângulo ou Obtusângulo.
 Sendo que:- Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
 - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
 - Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
'''

um = int(input('angulo um'))
dois = int(input('angulo dois'))
tres = int(input('angulo três'))
    
def validar_triangulo(um,dois,tres):
    soma_angulos_internos = um + dois + tres
    if soma_angulos_internos != 180:
        return False
    else:
        return True
    
while validar_triangulo(um,dois,tres) == False: 
    print('a soma dos angulos é diferente de 180, não configurando um Triangulo. Digite os angulos novamente')       
    um = int(input('angulo um'))
    dois = int(input('angulo dois'))
    tres = int(input('angulo três'))
        

if um > 90 or dois > 90 or tres > 90:
    print('obtusangulo')
elif um == 90 or dois == 90 or tres == 90 :
    print('triangulo retangulo')
elif um < 90 and dois < 90 and tres < 90:
    print('acutangulo')

'''
15. Escreva um programa para calcular e imprimir o número de lâmpadas necessárias
 para iluminar   um   determinado   cômodo   de   uma   residência
 Dados   de   entrada:   a   potência   da lâmpada utilizada (em watts),
 as dimensões (largura e comprimento, em metros) do cômodo.
 Considere que a potência necessária é de 18 watts por metro quadrado.¹
'''

#watt é consumo de energia ta errado o enunciado . luz -> lumens

potencia = int(input('potencia da lampada'))

largura = int(input('largura do comodo'))
comprimento = int(input('comprimento do comodo'))

def metro_quadrado_comodo(largura,comprimento):
    calculo = largura * comprimento
    return calculo
#print(metro_quadrado_comodo(largura,comprimento))


total_potencia_comodo =  18 *  metro_quadrado_comodo(largura,comprimento)

qnt_lampadas = total_potencia_comodo / potencia 
print(qnt_lampadas)


"""
16. Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
todas as suas paredes (considere que não será descontada a área ocupada por portas e
janelas). Cada caixa de azulejos possui 1,5 m2.
"""

comprimento = int(input('digite o comprimento'))
largura = int(input('digite a largura'))
altura = int(input('digite a altura'))

def volume_comodo(largura,comprimento,altura):
    calculo = largura * comprimento * altura
    return calculo

caixas_azulejo = volume_comodo(largura, comprimento, altura)/1.5

print(caixas_azulejo)



"""
17. Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se
que o preço do combustível é de R$ 1,90, escreva um programa para ler: a marcação do
odômetro (Km) no início do dia, a marcação (Km) no final do dia, o número de litros de
combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a média
do consumo em Km/L e o lucro (líquido) do dia.¹
"""
# quanto é o ganho por km ?


km_inicial = float(input('odômetro-> marcação inicio:'))
km_final = float(input('odômetro -> marcação final:'))

litros_combustivel_gasto = int(input('litros de combustivel gasto:'))

media_consumo = (km_final - km_inicial) / litros_combustivel_gasto

"""
18.




Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa. 
Caso o aluno não tenha feito a optativa deve ser fornecido o valor –1.
Calcular a média do semestre considerando que a nota mais baixa será excluída do calculo.
Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em
exame, de acordo com as informações abaixo1:

Aprovado : media >= 6.0
Reprovado: media < 3.0
Exame : media >= 3.0 e < 6.0
"""

av1 = int(input("Nota da primeira avaliação:"))
av2 = int(input("Nota da segunda avaliação:"))
opt = int(input("Nota da avaliação optativa:"))

media1 = (av1 + av2)/2
media2 = (av1 + opt)/2
media3 = (av2 + opt)/2

mediaFinal = -111

if ( (media1 > media2) and (media1 > media3) ):
    mediaFinal = media1
else:
    if (media2 > media3):
            mediaFinal = media2
    else:
            mediaFinal = media3

if (mediaFinal >= 6):
    print("Aprovado com média ",end="")
elif ( (mediaFinal >= 3) and (mediaFinal < 6) ):
    print("Exame com média ", end="")
else:
    print("Reprovado com média ",end="")

print(mediaFinal)

'''
19. Escreva um programa que leia a idade de 2 homens e 2 mulheres (considere que a
idade dos homens será sempre diferente, assim como as idades das mulheres). Calcule e
escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das
idades do homem mais novo com a mulher mais velha.
'''

# eu faço entao escroto

idade_um_mulher = int(input('digite a idade da primeira mulher'))
idade_dois_mulher = int(input('digite a idade da segunda mulher'))


idade_um_homem = int(input('digite a idade do primeiro homem'))
idade_dois_homem = int(input('digite a idade do segundo homem'))


if idade_um_mulher > idade_dois_mulher:
    mulher_mais_velha = idade_um_mulher
    mulher_nova = idade_dois_mulher
else:
    mulher_mais_velha = idade_dois_mulher
    mulher_nova = idade_um_mulher
    

if idade_um_homem > idade_dois_homem:
    homem_mais_velho = idade_um_homem
    homem_novo = idade_dois_homem
else:
    homem_mais_velho = idade_dois_homem   
    homem_novo = idade_um_homem


soma_final = homem_mais_velho + mulher_nova
produto_final = homem_novo * mulher_mais_velha

print(soma_final,' é a soma da idade da mulher mais nova e o homem mais velho')
print(produto_final,'é o produto entre a idade do homem mais novo e a mulher mais velha')

'''
20. Crie um programa para ler duas entradas de Strings fornecidas pelo usuário. Verifique
se as Strings são iguais ou diferentes. Imprima uma mensagem na saída padrão indicando o
resultado da verificação.
'''

string1 = input("Digite a primeira string")
string2 = input("Digite a segunda string")

if string1 == string2:
    print("strings iguais")
else:
    print("strings diferentes")