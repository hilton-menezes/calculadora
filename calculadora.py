import os
import platform

def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Erro: divisão por zero!'
    return x / y

def limpar_tela():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def calculadora():
    while True:
        limpar_tela()
        print("="*30)
        print("      CALCULADORA SIMPLES      ")
        print("="*30)
        print("[1] Soma (+)        [2] Subtração (-)")
        print("[3] Multiplicação (*) [4] Divisão (/)")
        print("[5] Sair")
        print("-"*30)
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '5':
            print("\nSaindo da calculadora. Até logo!\n")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("\nOpção inválida. Pressione Enter para tentar novamente.")
            input()
            continue

        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\nEntrada inválida. Pressione Enter para tentar novamente.")
            input()
            continue

        if escolha == '1':
            resultado = soma(num1, num2)
            operador = '+'
        elif escolha == '2':
            resultado = subtrai(num1, num2)
            operador = '-'
        elif escolha == '3':
            resultado = multiplica(num1, num2)
            operador = '*'
        elif escolha == '4':
            resultado = divide(num1, num2)
            operador = '/'

        print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
        print("-"*30)
        continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nObrigado por usar a calculadora!\n")
            break

if __name__ == "__main__":
    calculadora() 
