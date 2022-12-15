#função responsável por separar a parte fracionária da parte inteira
def float_binario(numero, casas): 	

	# split() = separa a parte inteira e decimal
	inteira, frac = str(numero).split(".")

	# Corversão de string para inteiro
	inteira = int(inteira)
	frac = int (frac)

	#conversão da parte inteira para binário
	parte_int = inteira
	aux = 1
	lista = []

	#enquanto o aux for maior ou igual há 1
	while aux >= 1:
		# resto recebe a parte inteira MOD 2 = resto da divisão por dois
		resto = parte_int % 2
		#lista guarda o resto
		lista.insert(0,resto)
		#aux recebe o valor da divisão inteira da parte_inteira por 2
		aux = parte_int // 2
		#parte_inr passa a receber o valor de aux para a nova comparação
		parte_int = aux


	# join() = une todos os itens da lista e coverte para string
	# para formar o numero binário
	res = ''.join([str(item) for item in lista]) + "."
 

	# De acordo com o numero de casas decimais escolhida
	for x in range(casas):

		# Multiplica o valor fracinal por 2 e separa a parte inteira/fracional
		inteira, frac = str((decimal_conversao(frac)) * 2).split(".")

		# Converte fracional para inteiro novamente
		frac = int(frac)

		# As partes inteiras são armezadas na variável resultado
		res += inteira

	return res

# A função converte o valor passado para a representação decimal 
def decimal_conversao(num):
	while num > 1:
		num /= 10
	return num

def int_binario(numero):
# conversão da parte inteira para binário
	parte_int = numero
	aux = 1
	lista = []

	# enquanto o aux for maior ou igual há 1
	while aux >= 1:
		# resto recebe a parte inteira MOD 2 = resto da divisão por dois
		resto = parte_int % 2
		# lista guarda o resto
		lista.insert(0,resto)
		# aux recebe o valor da divisão inteira da parte_inteira por 2
		aux = parte_int // 2
		# parte_inr passa a receber o valor de aux para a nova comparação
		parte_int = aux


		# join() = une todos os itens da lista e coverte para string
		# para formar o numero binário
		res = ''.join([str(item) for item in lista])
	return res

#menu de escolhas 
if __name__ == "__main__" :
	print("1 - DECIMAL FRACIONÁRIO - BINÁRIO")
	print("2 - DECIMAL - BINÁRIO")
	op = int(input("Digite a opção escolhida:" ))

	if op == 1: 
		print("Numero DECIMAL FRACIONÁRIO a ser convertido :")
		print("Utilize '.'")
		n = input("Numero: ")
	

		print(float_binario(n, len(n)))
	
	else:
		print("Numero DECIMAL a ser convertido :")
		n = int(input("Numero: "))

		print(int_binario(n))
	
