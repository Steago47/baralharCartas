import random
import sys
import math

print("Queres baralhar por exclusão (e), grelha (g) ou por ordenação (o)? Se quiseres ajuda (a) e uma explicação, escreve a e carrega no Enter")
type = input()
print("Quantas cartas queres baralhar?")
noCards = int(input())

if type == "e":
	for i in range(0, noCards, 1):
		if noCards - i != 1:
			print("Tens " + str(noCards - i) + " cartas na mão. Mete a seguinte no baralho:")
		else:
			print("Tens " + str(noCards - i) + " carta na mão. Mete a seguinte no baralho:")
		print(random.randint(1, noCards - i))
		input()
		
elif type == "o":
	cartasExistentes = list(range(1, noCards + 1))
	cartasIn = cartasExistentes
	while len(cartasExistentes) > 0:
		carta = random.randint(1, noCards)
		if carta in cartasExistentes:
			dezena = int(carta / 10)
			if dezena == carta / 10:  #faz com que os numeros acabados em 0 apareçam no final da dezena
				dezena = dezena - 1
			dezena = 10 * dezena
			cartasDezena = str()
			for i in range(1, 11):
				if dezena + i in cartasExistentes:
					if dezena + i == carta:
						cartasDezena = cartasDezena + "<"
					cartasDezena = cartasDezena + str(dezena + i)
					if dezena + i == carta:
						cartasDezena = cartasDezena + ">"
					cartasDezena = cartasDezena + " , "
				else:
					cartasDezena = cartasDezena + "_ , "
			print("Mete a carta número " + str(carta)+ " no baralho. As cartas restantes nesta dezena são:")
			print(cartasDezena)
			cartasExistentes.remove(carta)
			input()
			
elif type == "g":
	rows = int(input("Quantas filas tens na grelha?   "))
	columns = int(input("Quantas colunas tens na grelha?   "))
	cartasExistentes = list(range(1, noCards + 1))
	cartasPassadas = list()
	
	if rows * columns < noCards:
		print("A tua grelha é demasiado pequena.")
		sys.exit()
	print("As colunas vão ser dadas como letras (A, B, C, etc, e as filas como números (1, 2, 3, etc). Exemplo: A9 (primeira coluna, nona fila)")
	while len(cartasExistentes) != len(cartasPassadas):
		carta = random.randint(1, noCards)
		if carta not in cartasPassadas:
			print("Mete a carta da seguinte posição no baralho:")
			fila = int(math.ceil(carta / columns))
			coluna = carta % columns
			if coluna == 0:
				coluna = columns
			coluna = chr(ord("@") + coluna)
			print(coluna + str(fila))
			cartasPassadas.append(carta)
			
			"""
			print the grid
			"""
			filaPrint = str()
			for i in range(rows):
				filaPrint = ""
				for j in range(columns):
					
					if i * columns + j + 1 == carta:
						filaPrint = filaPrint + "O "
					elif i * columns + j + 1 in cartasPassadas or i * columns + j + 1 not in cartasExistentes:
						filaPrint = filaPrint + "_ "
					else:
						filaPrint = filaPrint + "X "
				print(filaPrint)
			input()
elif type == "a":
	print("O programa diz-te que carta meter no baralho. Também te diz quantas cartas te faltam meter. Para passares à próxima carta, carrega no Enter. Para prosseguires na explicação, carrega no Enter.")
	input()
	print("O modo de exclusão (e) assume que tens as cartas numa pilha, e pede-te para retirares a carta número n e metê-la numa nova pilha que formará o baralho. Este modo é o preferido para baralhar poucas cartas.")
	input()
	print("O modo de grelha (g) assume que meteste as cartas numa grelha do estilo batalha naval, e vais pegando numa carta de cada vez para formares o baralho. Este modo oferece uma representação visual da grelha para te ajudar a encontrares a carta.")
	input()
	print("O modo de ordenação (o) assume que deste um número a cada carta (virada do avesso) e o programa diz-te que carta deves pegar a seguir para meteres na nova pilha. O programa diz-te que cartas faltam nessa dezena para te ajudar a encontrar a carta que sugeriu.")
	input()
	print("Se as palavras com acentos ou cedilhas aparecem incorretamente, usa um interpretador que leia UTF-8. Se o texto desaparece no fim da linha, usa um interpretador que molde o texto.")
    
else:
	print("Não selecionaste e, g, o ou a.")