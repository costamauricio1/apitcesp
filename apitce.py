from unicodedata import normalize
from IPython.display import display
import pandas as pd 
#Cria um "atalho" para o pandas, o chamando de pd.
#As 4 variáveis são por causa do caminho da api. O formato foi substituído pelo
#tipo de arquivo, no caso, xml. Após vem as 4 variáveis, sendo exercício o
#ano de exercício.
#link da api https://transparencia.tce.sp.gov.br/apis

print("Olá! Seja bem vindo(a)!\n")
#declarando as variáveis
options = input("O que você quer acessar, despesas ou receitas? ")
city = input("Digite o nome da cidade do Estado de SP que quer saber: ")
year = input("Digite o ano: ")
month = input("Digite o mês: ")
#Concatenando a URL
url = "https://transparencia.tce.sp.gov.br/api/xml/"+ options +"/" + city +"/" + year +"/" + month

df = pd.read_xml(url) #df é uma variável bastante usada quando se trabalha com Pandas, significa DataFrame.
#o código acima coloca o Pandas pra ler (read) arquivos XML da variável url que declaramos acima.

#Agora vamos definir a estrutura de condicionais
#Para usar a função Display precisa de importar a primeira lib do código, senão dá bug.
if options == 'despesas':
  colunas = df[['mes','nm_fornecedor','dt_emissao_despesa','vl_despesa']]
  display(colunas)
else:
  colunas = df[['mes','ds_fonte_recurso','ds_alinea','vl_arrecadacao']]
  display(colunas)






