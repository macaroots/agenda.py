def cadastrar():
	nome = input("Informe o nome: ")
	idade = int(input("Informe a idade: "))
	with open('agenda.txt', 'a') as arquivo:
		arquivo.write('{};{}\n'.format(nome, idade))
		arquivo.close()


def listar():
	arquivo = open('agenda.txt', 'r')
	print("Nome\tIdade")
	for linha in arquivo.readlines():
		pessoa = linha.strip().split(";")
		print('{}\t{}'.format(pessoa[0], pessoa[1]))
	arquivo.close()

while True:
	print("1 - Cadastrar | 2 - Listar | 3 - Sair")
	resposta = input("Informe a opção:")
	
	if resposta == "1":
		cadastrar()
		
	elif resposta == "2":
		listar()
		
	elif resposta == "3":	
		break
