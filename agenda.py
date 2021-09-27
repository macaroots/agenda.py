pessoas = []

def cadastrar():
	nome = input("Informe o nome: ")
	idade = int(input("Informe a idade: "))
	pessoa = [nome, idade]
	pessoas.append(pessoa)

def listar():
	print("Nome\tIdade")
	for pessoa in pessoas:
		print('{}\t{}'.format(pessoa[0], pessoa[1]))

while True:
	print("1 - Cadastrar | 2 - Listar | 3 - Sair")
	resposta = input("Informe a opção:")
	
	if resposta == "1":
		cadastrar()
		
	elif resposta == "2":
		listar()
		
	elif resposta == "3":	
		break
