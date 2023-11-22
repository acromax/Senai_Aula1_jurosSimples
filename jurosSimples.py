# programa para calcular juros simples - aula2 Python Turma 21
#apresentação
print('\n\t\t\t -- Calculadora de Juros Simples --\n')

#Entradas
c = float(input('Informe o valor do Capital: ')) #Capital
i = float(input('Informe o valor da Taxa: ')) #Taxa
n = int(input('Informe o valor do Prazo: ')) #Prazo

#Processamento
total = (c*i*n)/100

#Saída
print(f'O valor dos seus juros simples é de: {total}')