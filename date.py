from datetime import date, datetime, timedelta
from locale import setlocale, LC_ALL


setlocale(LC_ALL, 'pt_BR.utf-8')


# criando uma data
data = datetime(2020, 4, 17, 14,30) 
print(data)

# O módulo strftime da classe datatime é usado para formatar a data
print(data.strftime('%d/%m/%Y %H:%M:%S')) 

# O strptime converte uma string do tipo texto para um data
recebendo_data = datetime.strptime('20/08/2020', '%d/%m/%Y')
print(recebendo_data)

# Convertendo uma data em timestamp
data_timestamp = data.timestamp()
print(data_timestamp)

# Convertendo um timestamp em data
print(datetime.fromtimestamp(data_timestamp))

# Somando datas 
nova_data = data + timedelta(days=5, hours=2)
print(nova_data)

# Diferença entre duas datas 
dif = nova_data - data
print(dif)

# Data de agora 
dt = datetime.now()
print(dt.strftime('%A, %d de %B de %Y'))

# Pegando o mês atual
mes_atual = int(dt.strftime('%m'))
print(mes_atual)