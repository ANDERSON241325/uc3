"""
Os conjuntos não são ordenados , são mutáveis, heterogêneos ou homogêneos e não permitem elementos duplicados.
"""

# Declaração dos conjuntos 
ingredientes = {"mussarela", "calabresa", "tomate", "azeitona"}
print("🧀 Ingredientes básicos:", ingredientes)

# Operações com os conjuntos 
# Adicionar Itens:
ingredientes.add("oregáno")
print("🧀 Ingredientes atualizados:", ingredientes)

# Remover Itens:
ingredientes.remove("tomate")
print("🧀 Ingredientes após a remoção:", ingredientes)

# União de Conjuntos:
adicionais = {"bacon","palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("🍅 Todos os ingredientes:", todos_ingredientes)

# Interação de conjuntos: aparece em ambos os conjuntos 
pizza_vegana = {"tomate", "azeitona", "rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("🥦 Ingredientes comuns ", comuns)
