'''--> Comentário de Bloco
Título: Revisão de Python
Autor: Marcos (co ajuda do profe. Berssa)
Data:2024/07/02
'''
# --> Comentário de linha
# Objetivo: Revisar os Fundamentos de Progamação em Python

print('Hello World!')

# Saida --> print()
print('Profe. Berssa Lindu!') # 'String'
print('100 + 100')            # 'String'
print(100 + 100)              # operação

# Entrada --> input()
nome = input('Digite seu nome: ')
print('Você disse: ',nome)
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor:'))
total = valor1 + valor2
print('Soma dos valores digitados é: ', total)

# Variáveis --> espaço de memória que armazena valores temporariamente
# str --> armazena textos e caracteres --> %s ou %c
Nome = 'Marcos'
print('A variavel nome é do tipo: ', type(Nome), 'e tem armazenado o valor: %s' %nome)
# int --> Armazena números inteiros positivos e negativos
valorX = -81
print('A variavel valorX é do tipo: ', type(valorX), 'e tem armazenado o valor: %d' %valorX)
# float --> armazena números de ponto flutuante positivos e negativos --> NÃO USAR "," (NUNCA) USAR "." --> %f == %.2f
pi = 3.14159
print('A variavel pi é do tipo: ', type(pi), 'e tem armazenado o valor: %d' %pi)
# bool --> Armazena true ou false
teste = 10 > 50
print('A variavel teste é do tipo: ', type(teste), 'e tem armazenado o valor: ', teste)

# Operadores --> realiza oprações
# Aritimeticos -->  Cauculos +, -, *, /, **, //, %
print(5*5)
print(15/4)  # --> resultado em float
print(10//3) # --> resultado em int
print(10%4) 
# Atribuição
A = 10
A += 1 #Incremento soma 1
A -= 1 #Decremento diminue 1
# Relacionais --> Fazem comparaçãoe retornam true ou false
A == 10 # == é igual == True
A != 10 #diferente == false
# # >; <; >=; <=
# # Lógicos --> Concatenação de operadores relacionais
# # and == e;  or == ou; not == não

# Repetição
# laço for --> Quando eu sei quantas vezes vai repetir
for i in range(11, 102, 2):
  print(i)
# outra forma de fazer 
palavra = 'Progamação'
for letra in palavra:
  print(letra)
# laço while --. quando eu não sei quantas vezes vai repetir
tecla = 1
while tecla != 0 : # --> repete até a condição ser false
  tecla = int(input('Digite um número:  '))
  
# Condição --> if, else, elif
idade = int(input('Digite sua idade: '))
if idade >= 18: # testa e faz se o resultado true 
  print('pode ir pro Bailão')
elif idade >= 16: #Faz se o if == false e o elif == true 
  print('Vai pro Bailão com a Mamãe e o Papai!')
else: # Faz se o if e o elif == a false
  print('Não vai pro Bailão Hoje!')

# Funções --> def
def soma(X, Y):
  R = X + Y
  return R

print(soma(10,5))
print(soma(100, 50))
A = int(input('Dgigte um valor; '))
B = int(input('Dgigte outro valor; '))
print('Soma de %d e% é igual a %d' %(A, B,  (soma(A,B))))