import re

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalala 3216-6547 haoehaeahuashuash"

padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"

retorno = re.search(padrao, email4)
print(retorno.group())
#estudando expressões regulares.