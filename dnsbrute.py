import dns.resolver
import sys

resolver = dns.resolver.Resolver()

try:
	alvo = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("Insira os argumentos corretamente")
	sys.exit()

try:
	with open(wordlist, "r") as arq:
		subdominios = arq.read().splitlines()
except:
	print("Erro ao abrir o arquivo")
	sys.exit()

for subdominio in subdominios:
	try:
		subalvo = "{}.{}".format(subdominio, alvo) 
		resultados = resolver.resolve(subalvo, "A")
		for resultado in resultados:
			print("{} -> {}".format(subalvo, resultado))
	except:
		pass
