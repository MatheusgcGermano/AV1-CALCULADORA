print('----------------------------------------------')
print('----------CALCULADORA PROVA AV1---------------')
print('----------------------------------------------')

ligado = True

while ligado:
    num1 = int(input('digite seu primeiro numero: '))
    num2 = int(input('digite seu segundo numero: '))

    opcao= str(input('digite a operação que deseja: '))


    if opcao =='+':
        soma= num1 + num2 
        print(f' o resultado da soma é: {soma:.2f}')

    elif opcao =='-':
        subtracao= num1 - num2
        print(f'subtração: {subtracao:.2f}')

    elif opcao =='*':
        Multiplicacao= num1 * num2
        print(f'resultado da multiplicação é: {Multiplicacao:.2f}')

    elif opcao =='/':
        Divisao= num1 / num2
        print(f'resultado da divisão é: {Divisao:.2f}')

    elif opcao =='//':
        parte_inteira = num1 // num2
        print(f'parte inteira: {parte_inteira:.2f}')

    elif opcao =='%':
        resto = num1 % num2
        print(f'resto da divisão é: {resto:.2f}')

    elif opcao =='**':
        potencia = num1 ** num2
        print(f'potência é: {potencia:.2f}')

    elif opcao =='**':
        raiz = num1 ** (1 / num2)
        print(f'raiz é: {raiz:.2f}')

    else:
        print('operação invalida')

    continuar = input('Deseja realizar outra operação? (s/n): ')
    if continuar.lower() != 's':
        ligado = False
        print('Calculadora encerrada.')
    else:
        print('Resposta incorreta. Por favor, digite "s" para continuar ou "n" para encerrar.')