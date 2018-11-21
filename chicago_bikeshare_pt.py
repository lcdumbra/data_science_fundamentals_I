# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt


# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
"""
Imprime as 20 primeiras linhas de dados
como range(20) vai de 0 a 19, é necessário o i+1 para imprimir os 20 primeiros dados
"""
for i in range(20):
  print("Linha " + str(i+1) + ": ")
  print(data_list[i+1])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

#Imprime apenas o genero das primeiras 20 linhas
#Como agora não tem cabeçalho, não deve ser colocado o i+1
#O 6 indica a posição do genero em linha do dataset
for i in range(20):
  print("Genero na linha " + str(i+1) + ": ")
  print(data_list[i][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in data:
      column_list.append(i[index])
    return column_list
'''
A função recebe o dataset e o index (coluna a ser passada para outra lista)
Para cada linha no dataset, será copiado para a nova lista apenas a coluna(index)
E o retorno sera uma nova lista com a coluna copiada do dataset
'''


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for i in range(len(data_list)): # percorre todo o dataset
  if data_list[i][6] == 'Male': # se o genero for 'Male', soma mais um na variavel 'male'
    male += 1
  elif data_list[i][6] == 'Female': # se o genero for 'Female', soma mais um na variavel "female"
    female += 1
  else: # caso seja null, não faz nada e continua
    continue

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0
    for i in range(len(data_list)): # percorre todo o dataset que foi passado no parametro
      if data_list[i][6] == 'Male': # se o genero for 'Male', soma mais um na variavel 'male'
        male += 1
      elif data_list[i][6] == 'Female': # se o genero for 'Female', soma mais um na variavel "female"
        female += 1
      else: # caso seja null, não faz nada e continua
        continue
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    answer = ""
    if count_gender(data_list)[0] > count_gender(data_list)[1]:
      answer = "Male"
    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
      answer = "Female"
    else:
      answer = "Equal"
    return answer

'''
A função recebe um conjunto de dados como parametro
Se o retorno da função count_gender na primeira posição, que representa Male, for maior o retorno será 'Male'
Se o retorno da função count_gender na segunda posição, que representa Female, for maior o retorno será 'Female'
Senao, o retorno sera 'Equal'
'''

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque alguns dados nao tem nem Male e nem Female. Ou seja, estao vazios"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

'''
Calculando o minimo
Definido um valor alto para min_trip
Percorre a lista trip_duration_list, comparando o item atual com o proximo
Caso o atual seja menor, o mesmo será salvo em min_trip
Caso contrário, continua.
No fim, teremos a menor duração de viagem
'''
min_trip = 10000000
for i in range(len(trip_duration_list)-1):
  if int(trip_duration_list[i]) < int(min_trip):
    min_trip = int(trip_duration_list[i])
  else:
    continue

'''
Calculando o maximo
Percorre a lista trip_duration_list, comparando o item atual com o valor em max_trip
Se o item for maior, atualiza o valor.
Caso contrário, continua.
No fim, teremos a maior duração de viagem
'''
for i in range(len(trip_duration_list)-1):
  if int(trip_duration_list[i]) > int(max_trip):
    max_trip = int(trip_duration_list[i])
  else:
    continue

'''
Calculando a media
Definir uma variável chamada 'soma' para guardar as somas dos valores da lista
A média será a divisão entre 'soma' e o tamanho da lista
'''
soma = 0
for i in range(len(trip_duration_list)):
  soma += float(trip_duration_list[i])
mean_trip = float(soma / len(trip_duration_list))

'''
Calculando a mediana
Primeiro, é verificado o tamanho da lista
Se for par, a mediana será a divisão entre os valores nas posições [(tamanho-1)/2] e [(tamanho-1)/2]+1
Se for impar, a mediana será o valor na posição [(tamanho-1)/2].
'''
if (len(trip_duration_list) % 2) == 0: # se o tamanho for par, pegar o item no meio e o proximo e dividir por 2
  index_half = int(sorted(trip_duration_list, key = int)[len(trip_duration_list)/2])
  index_half_plus_one = int(sorted(trip_duration_list, key = int)[(len(trip_duration_list)/2)+1])
  median_trip = int((index_half + index_half_plus_one) / 2)
else: # se o tamanho for impar, pegar o valor do meio
  median_trip = int(sorted(trip_duration_list, key = int)[len(trip_duration_list)//2])

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set()
start_stations_list = []
for item in data_list:
  start_stations_list.append(item[3])
start_stations = set(start_stations_list)
#Percorre o dataset e adiciona em uma nova lista apenas a coluna com as start_station(posicao 3)
#Adiciona a nova lista no conjunto (set) start_stations, inicialmente vazia.

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")

answer = "no"
def count_items(column_list):
   item_types = []
   count_items = []
   return item_types, count_items

answer = input("Resposta: ")

if answer == "yes":
    def count_items(column_list):
      item_types = []
      count_items = []
      count = 0
      for item in column_list:
        count_items.append(1)
        for item_tipos in item_types:
          if item_tipos == item:
            count +=1
          else:
            continue
        if count == 0:
          item_types.append(item)
        else:
          count = 0
          continue
      return item_types, count_items
'''
Ao digitar yes, a funcao count_items implementada é chamada
A funçao percorre o parametro column_list compararando cada item aos itens presentes em item_types
Em cada comparação, é adicionado 1 a lista de count_items para ser feita o somatório e descobrir quantos itens foram verificados
Se houver item igual, é somado mais um no contador. Senão, continua
Se o contador estiver zerado, significa que o item verificado é novo. Portanto, é adicionado em item_types.
Caso contrário, o contador é zerado para a verificação do proximo item.
No fim, é retornado a lista dos tipos e a lista com os '1's para fazer o somatório e descobrir a quantidade de itens verificados
'''

    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
