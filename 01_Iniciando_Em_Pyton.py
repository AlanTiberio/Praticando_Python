# Importando a bliblioteca  para que possamos utilizar a data atual
from datetime import date
data = date.today()

nome = "Carlitos"
sobrenome = "Alburquerque"
ano_nascimento = 1996
idade = data.year - 1996
maior_de_idade = ""
altura_metros = 1.78

#Verificando se é maior ou menor de idade
if idade >= 18:
    maior_de_idade == "Você é Maior de idade"
else:    
    maior_de_idade == "Você é Menor de idade"

#Realizando a impressão dos resultados no terminal  
print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print("Idade: ", idade)
print("Ano de Nascimento: ", ano_nascimento)
print("E maior de Idade?: ", maior_de_idade)
print("Altura em Metros: ", altura_metros)