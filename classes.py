from random import randint
class Pessoa:
    ano_atual = 2021
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
         print(self.ano_atual-self.idade)

    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1000, 19999)
        return rand

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

class BaseDeDados:
    def __init__(self):
        self.dados = {}
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'allison')
bd.inserir_cliente(2, 'eduardo')

print(bd.dados)



class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome 
        self.valor = valor

carrinho1 = CarrinhoDeCompras()
p1 = Produto('leite', 10)
p2 = Produto('cafe', 5)
carrinho1.inserir_produtos(p1)
carrinho1.lista_produto()



class Person(object):
    species = "homo sapiens"

    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return self.name

    def rename(self, renamed):
        self.name = renamed

    def __eq__(self, other):
        return type(self.name) != type(other)


pessoa1 = Person('allison')
print(pessoa1)
pessoa1.rename('eduardo')
print(pessoa1.name)
print(pessoa1.species)
print(pessoa1.__eq__(123))



from datetime import datetime
from random import randint
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) # atributo de classe
    def __init__(self, nome, idade, comendo=False, falando=False): 
        self.nome = nome   # atributo de instância 
        self.idade = idade 
        self.comendo = comendo 
        self.falando = falando 

    def __str__(self):
        return self.nome


    def falar(self, assunto):
        if not self.comendo:
            print(f'{self.nome} está falando sobre {assunto}')
            return

        print(f'{self.nome} não pode falar pois está comendo {self.alimento}')


    def comer(self, alimento = ''):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return

        self.alimento = alimento
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False

 
    def get_ano_nascimento(self):  # método de instância
        print(f'{self.nome} nasceu em {Pessoa.ano_atual - self.idade}')


    @classmethod # método de classe
    def por_ano_nascimento(cls, nome, ano_nacimento):
        idade = cls.ano_atual - ano_nacimento
        return cls(nome, idade)

    @staticmethod # método estático
    def gera_id():
        rand = randint(10000, 19999)
        return rand





p1 = Pessoa('allison', 22)
p1.comer('abacaxi')
p1.comer('mamão')
p1.parar_comer()
p1.falar('politica')
p1.get_ano_nascimento()
print(p1.gera_id())





class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco 
    
    def __str__(self):
        return self.nome

    def desconto(self, percentual):
        self.preco = self.preco*(1-percentual/100)

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # checando a classe da instaância
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('camisa', 'R$100')
p1.desconto(10)
print(p1.preco)



class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_cliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self):
        del self.__dados['cliente']


            


bd =BaseDeDados()
bd.inserir_cliente(1, 'allison')
bd.inserir_cliente(2, 'eduardo')
bd.lista_cliente()
print(bd._BaseDeDados__dados)




class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nome} está falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando')

class ClienteVip(Cliente):
    def falar(self):
        super().falar()
        Cliente.comprar(self)
        print(f'o cliente {self.nome} está falando') 


c2 = ClienteVip('allison', 22)
c2.falar()




class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)




from abc import abstractmethod
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass

class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.falar('um assunto')
c.falar('outro assunto')




class Retangulo:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __repr__(self):
        return 'retangulo {} {}'.format(self.x, self.y)
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

r1 = Retangulo(1, 2)
r2 = Retangulo(2, 3)

print(r1 + r2)






from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade 

    @property
    def nome(self):     # como nome é privado, ou seja, que não deve ser alterado depois de criado
        return self._nome  # criamos uma property para visualizar o nome caso necessário 

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta 
        self.saldo = saldo 

    def depositar(self, valor):
        self.saldo += valor 
        self.detalher()
    
    def detalher(self):
        print(f'a conta {self.conta} agora tem o saldo de {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('saldo insuficiente') 
            return
        self.saldo -= valor 
        self.detalher()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite 
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('saldo insuficiente') 
            return

        self.saldo -= valor 
        self.detalher()



class Banco():
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False
            
        if cliente.conta.agencia not in self.agencias:
            return False
        
        return True


banco = Banco()

cliente1 = Cliente('allison', 22)

conta1 = ContaPoupanca(1111, 23123, 100)

cliente1.inserir_conta(conta1)

cliente1.conta.sacar(20)





x = {'allison': 1, 'eduardo': 2}
for i, j in x.items():
    print(i, j)








# Python program showing a use 
# of get() and set() method in 
# normal function 
  
class Geek: 
    def __init__(self, age = 0): 
         self._age = age 
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 
  
raj = Geek() 
  
# setting the age using setter 
raj.set_age(21) 
  
# retrieving age using getter 
print(raj.get_age()) 
  
print(raj._age) 

raj.set_age(31)

print(raj._age)

raj._age = 40

print(raj._age)






class location:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 


    @property  # criando uma propriedade que depende de outras propriedades 
    def loc(self):
        return [self.x, self.y]

    def move_left(self):
        self.x -= 1

    
    def move_right(self):
        self.x += 1


    def move_up(self):
        self.y += 1


    def move_down(self):
        self.y -= 1


    def __repr__(self):
        return f'{type(self).__name__}(x={self.x}, y={self.y})'

    

    


objeto = location()
print(objeto.loc)
objeto.move_up()
objeto.move_right()
print(objeto.loc)
print(objeto)