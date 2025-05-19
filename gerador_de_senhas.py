"""
# Simulação de gerador de senha com função "aleatória" simples
# Este código simula a geração de uma senha aleatória, usando a biblioteca random.


import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_-"
senha = ""

for i in range(8):
    aleatorio = random.choice(caracteres)
    senha += aleatorio

print("Senha gerada:", senha)


-----------------------------------------------------------------------------------------------------------------------------


# Simulação de gerador de senha com função "aleatória" simples
# Este código simula a geração de uma senha aleatória, mas não usa a biblioteca random.
# Este código não é seguro para uso real, pois a geração de senhas deve ser feita com métodos criptograficamente seguros.

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_-"
senha = ""

# Função de número "aleatório" simulada
def aleatorio_simples(indice):
    return (ord(str(indice)[-1]) * indice) % len(caracteres)

for i in range(8):
    index = aleatorio_simples(i + 1)
    senha += caracteres[index]

print("Senha gerada:", senha)



-----------------------------------------------------------------------------------------------------------------------------


# Simulação de gerador de senha com função "aleatória" simples
# Este código simula a geração de uma senha aleatória, mas não usa a biblioteca random, nem comandos pré-definidos. 
# A função de geração de senha é baseada em uma semente e um valor simples calculado a partir dela.
# Este código não é seguro para uso real, pois a geração de senhas deve ser feita com métodos criptograficamente seguros.   

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_-"
senha = ""

# Função para contar caracteres
def contar(t):
    contador = 0
    for _ in t:
        contador += 1
    return contador

# Função para gerar um "valor" baseado na posição dos caracteres
def valor_simples(txt, pos):
    valor = 0
    for i in range(contar(txt)):
        if (i + pos) % 2 == 0:
            valor += i + pos
        else:
            valor += i * pos
    return valor

semente = input("Digite uma semente: ")

total_caracteres = contar(caracteres)  

for i in range(8):
    valor = valor_simples(semente, i + 1)
    indice = valor % total_caracteres
    senha += caracteres[indice]
    # altera a semente para a próxima iteração
    semente = semente[-1] + semente + senha[-1]

print("Senha gerada:", senha)

"""