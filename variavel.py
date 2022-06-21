# Números Float também podem ser números científicos com um "e" para indicar a potência de 10 ( no
# exemplo que temos, é potência de base 100) (VOOLLTAAAAAAAAAAAAAAAAAAAAAAAAAAR DUVIDA)
x = 35e3
y = 12E4
z = -87.7e100

print(z)

print(type(x))
print(type(y))
print(type(z))


# ABAIXO, USAMOS O CASTING ( CONVERTEREMOS UM TIPO DE DADO EM OUTRO)
# Transformando um número INT (tipo de dado inteiro) em outro tipo de dado chamado Float
x = 5 # INT
y = float(x) #criei outra variável que chamei de y e coloquei o argumento "x" dentro da função float
# Nesse caso, o "x" que representava um valor inteiro, agora passará a ser float ( no terminal aparecerá
# o valor 5.0)
print(y)

# Irei converter INTEIRO em NÚMERO COMPLEXO ---> No terminal vai aparecer 1 + 0j
x = 1
y = complex(x)
print(type(y))
print(y)


# USANDO CASTING( CONVERTENDO FLOAT(Y) E STRING EM INT(Z))
x = int(1)
y = int(2.8) # Convertendo FLOAT em INT
z = int("3") # Convertendo STRING em INT
print(x)
print(y)
print(z)