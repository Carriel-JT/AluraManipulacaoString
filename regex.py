import re

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalala 932166547 haoehaeahuashuash 3221-1223"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email4)
print(retorno)
#estudando expressões regulares.