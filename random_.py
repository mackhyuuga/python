import random 
import string

#g erando números aleatórios
inteiro = random.randint(10, 20)
real = random.uniform(10, 20)
decimal = random.random()
x = random.randrange(0, 100, 10) # gera um número entre a e b pulando de p em p

# trabalhando com listas
pessoas = ['allison', 'eduardo', 'sousa', 'bonfim']
sortei = random.choice(pessoas)
duas_pessoas = random.sample(pessoas, 2)
random.shuffle(pessoas)   # embaralha os nomes

# gerando uma senha 
letras = string.ascii_letters
numeros = string.digits
caracteres = '!@#$%¨&*()_-'
geral = letras + numeros + caracteres
senha = ''.join(random.choices(geral, k = 7))


print(senha)