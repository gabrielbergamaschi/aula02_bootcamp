# Exercícios

# Inteiros (int)

# Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 8  # Exemplo de entrada
num2 = 12  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num = int(input("Digite um número: "))
num = 18  # Exemplo de entrada
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
num1 = 5  # Exemplo de entrada
num2 = 7  # Exemplo de entrada
resultado_multiplicacao = num1 * num2
print("O resultado da multiplicação é:", resultado_multiplicacao)

# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 20  # Exemplo de entrada
num2 = 3  # Exemplo de entrada
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é:", resultado_divisao_inteira)

# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num = int(input("Digite um número: "))
num = 6  # Exemplo de entrada
resultado_quadrado = num**2
print("O quadrado do número é:", resultado_quadrado)

# ===========================================================================================


# ===========================================================================================


# Números de Ponto Flutuante (float)


# Escreva um programa que receba dois números flutuantes e realize sua adição.

# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 2.5  # Exemplo de entrada
num2 = 4.5  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 3.5  # Exemplo de entrada
num2 = 7.5  # Exemplo de entrada
media = (num1 + num2) / 2
print("A média é:", media)

# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
base = 2.0  # Exemplo de entrada
expoente = 3.0  # Exemplo de entrada
potencia = base**expoente
print("O resultado da potência é:", potencia)

# Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Digite a temperatura em Celsius: "))
celsius = 30.0  # Exemplo de entrada
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Digite o raio do círculo: "))
raio = 5.0  # Exemplo de entrada
area = 3.14159 * raio**2
print("A área do círculo é:", area)


# ===========================================================================================


# ===========================================================================================


# Strings (str)


# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Digite um texto: ")
texto = "Olá, mundo!"  # Exemplo de entrada
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome_completo = input("Digite seu nome completo: ")
nome_completo = "Fulano de Tal"  # Exemplo de entrada
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)

# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
frase = "  Olá, mundo!  "  # Exemplo de entrada
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato dd/mm/aaaa: ")
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# Escreva um programa que concatene duas strings fornecidas pelo usuário.

# parte1 = input("Digite a primeira parte do texto: ")
# parte2 = input("Digite a segunda parte do texto: ")
parte1 = "Olá,"  # Exemplo de entrada
parte2 = " mundo!"  # Exemplo de entrada
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)


# ===========================================================================================


# ===========================================================================================


# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# Exemplo de entrada
num1 = 5
num2 = 5
resultado_igualdade = num1 == num2
print("Resultado da igualdade:", resultado_igualdade)

# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# Exemplo de entrada
resultado_diferenca = num1 != num2
print("Resultado da diferença:", resultado_diferenca)
