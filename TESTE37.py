num = int(input('Escolha um número: '))
print('''Escolha uma das bases para conversão:
(1) para binário
(2) para octal 
(3) para hexadecimal''')
opção = int(input('Escolha sua opção: '))

if opção == 1:
    print('Seu número {} em binário fica {}:'.format(num, bin(num)[2:]))
elif opção == 2:
    print('Seu número {} em binário fica {}:'.format(num, oct(num)[2:]))
elif opção == 3:
    print('Seu número {} em binário fica {}:'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
