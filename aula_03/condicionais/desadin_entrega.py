# Agora, a nossa pizzaria está cobrando uma `taxa fixa de R$5 por entrega`, além de `R$1 por km até 5km,` e `R$2 por km até 10km`. Mais ainda `não entregamos com a distância superior a 10km`.

# Pegando como base essas possibilidades, faça um programa que responda as seguintes perguntas:

# - Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
# - Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
# - Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria.




taxa = 5

distancia = int (input("Insira a distância"))
valor_menor_5 = 1
valor_menor_10 = 2 

if distancia <= 5:
    frete = taxa + (distancia *1)
    print(f"O valor dp frete é de R$ {frete}")
elif distancia <= 10:
    frete = taxa + (distancia * 2 )
    print(f"O valor dp frete é de R$ {frete}")
else: print("🛑  Infelizmente, não entregamos nessa distância.")

