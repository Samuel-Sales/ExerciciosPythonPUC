nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

if idade >= 18 :
    print(nome, 'é maior de 18 e tem', idade, 'Anos')
elif idade < 18 :
    print(nome, 'não é maior de 18 e tem', idade, 'Anos')