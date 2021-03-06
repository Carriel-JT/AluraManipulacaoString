from ExtratorArgumentosUrl import ExtratorArgumentosUrl

string = 'bytebank'
stringNova = string.replace('bank', 'rodrigo')
print(stringNova)

string = 'bytebankbytebyte'
stringNova = string.replace('byte', 'rodrigo')
print(stringNova)

string = 'bytebankbytebyte'
stringNova = string.replace('byte', 'rodrigo', 1)
print(stringNova)

banco1 = 'bytebank'
banco2 = 'Bytebank'
print(banco1 == banco2)
banco2 = 'Bytebank'.upper()
print(banco2)

banco2 = 'Bytebank'.lower()
print(banco2)

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)

urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com.br"
url3 = "https://bytebank.com/cambio/teste/teste"

print(url1.find(urlByteBank))
print(url2.find(urlByteBank))
print(url3.find(urlByteBank))

print(url1.startswith(urlByteBank))
print(url2.startswith(urlByteBank))
print(url3.startswith(urlByteBank))

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"

argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaDestino, moedaOrigem)

print(argumentosUrl == argumentosUrl2)
