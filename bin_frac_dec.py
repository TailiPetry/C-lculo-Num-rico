#conversão binario para decimal
def bin_frac_dec(binario, casas) :
 
 	# split() = separa a parte inteira e decimal
	inteira, frac = str(binario).split(".")

	# Corversão de string para inteiro
	inteira = int(inteira)


	#len() = numero de itens em inteira
	aux = len(str(inteira))
	decimal = 0
	i = 0

	while aux >= 0:
		# resto recebe a parte inteira MOD 10 = resto da divisão por dez
		resto = inteira % 10
		# decimal recebe o valor antigo de decimal mais resto multiplicado a 2 elevado a i
		decimal = decimal + (resto * (2**i))
		# reduz uma unidade de aux
		aux = aux - 1
		# aumenta uma unidade de i
		i = i + 1
		# inteira recebe o valor da divisão inteira da parte_inteira por 10
		inteira = inteira // 10

	# Separação para a parte fracionaria
	ponto = binario.find('.')

	# se não houver ponto
	if (ponto == -1) :
		ponto = casas

	aux = 2
	fracionaria = 0

	#Parte fracionária Bin -> dec
	for i in range(ponto + 1, casas):
		# Fracionaria recebe binario na posicao i, diminui 0, e divide por aux
		# ord() =  conversao binaria
		fracionaria += ((ord(binario[i]) - ord('0')) / aux);
		# aux multiplica 2 (equivale e exponencial)
		aux *= 2.0
	
	# soma a parte decimal e a fracionaria
	res = decimal + fracionaria

	return res

def bin_dec(numero):
	#len() = numero de itens em inteira
	aux = len(str(numero))
	decimal = 0
	i = 0

	while aux >= 0:
		# resto recebe a parte inteira MOD 10 = resto da divisão por dez
		resto = numero % 10
		# decimal recebe o valor antigo de decimal mais resto multiplicado a 2 elevado a i
		decimal = decimal + (resto * (2**i))
		# reduz uma unidade de aux
		aux = aux - 1
		# aumenta uma unidade de i
		i = i + 1
		# inteira recebe o valor da divisão inteira da parte_inteira por 10
		numero = numero // 10

	return decimal

if __name__ == "__main__" :
	print("1 - BINÁRIO FRACIONÁRIO - DECIMAL")
	print("2 - BINÁRIO - DECIMAL")
	op = int(input("Digite a opção escolhida:" ))

	if op == 1: 
		print("BINÁRIO FRACIONÁRIO - DECIMAL")
		print("Utilize '.'")
		n = input("Numero: ")
		print(bin_frac_dec(n,len(n)))
	else:
		print("BINÁRIO - DECIMAL")
		n = int(input("Numero: "))
		print(bin_dec(n))
	
	
