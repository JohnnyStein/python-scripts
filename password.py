
import random

caixaalta = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
caixabaixa = caixaalta.lower()
numeros = "0123456789"
especiais = "()[]{}<>-_+*/#!@#$%¨&"

alta, baixa, nums, sims = True, True, True, True

tudo = ""

if alta:
    tudo += caixaalta
if baixa:
    tudo += caixabaixa
if nums:
    tudo += numeros
if sims:
    tudo += especiais

tamanho = 40
contagem = 20

for x in range(contagem):
    senha = "".join(random.sample(tudo, tamanho))
    print("A senha gerada é: " + senha)