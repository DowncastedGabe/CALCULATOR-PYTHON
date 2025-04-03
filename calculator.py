def calculadora (operacao):
    def soma (a, b ):
        return a + b

    def sub (a, b):
        return a - b
    
    def mult (a, b):
        return a * b
    
    def div (a, b):
        return a / b   
    

    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return mult
        case '/':
            return div
        
print('Escolha a operação desejada:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Sair')
print('Digite a operação desejada: ')
operacao = input()

if operacao == '5':
    print('Saindo...')
    exit()
elif operacao not in ['1', '2', '3', '4']:
    print('Operação inválida!')
    exit()
else:
    operacao = '+' if operacao == '1' else '-' if operacao == '2' else '*' if operacao == '3' else '/'
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))

    resultado = calculadora(operacao)(a, b)
    print(f'O resultado da operação {operacao} entre {a} e {b} é: {resultado}')
