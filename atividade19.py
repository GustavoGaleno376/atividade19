# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
# Solicitar ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Fatorial não definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")