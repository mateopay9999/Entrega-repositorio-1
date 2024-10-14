# Estructura de datos para el menú
menu = {
    "Aperitivo": {
        "cilantro",
        "cebolla",
        "chile",
        "ajo",
        "tomate",
        "aguacate",
        "zumo de limón",
        "sal"
    },
    "Primer plato": {
        "huevo",
        "palitos de cangrejo",
        "atún",
        "mayonesa",
        "pimientos del piquillo",
        "pimiento verde",
        "pimiento rojo",
        "cebolla",
        "vinagre",
        "sal",
        "aceite de oliva"
    },
    "Segundo plato": {
        "aceite de oliva",
        "ajo",
        "solomillo de cerdo",
        "cebolla",
        "manzana",
        "tomate concentrado",
        "calabacín",
        "brandy",
        "vino de Oporto",
        "ciruelas pasas",
        "orejones de albaricoque",
        "mostaza",
        "piñones"
    },
    "Postre": {
        "chocolate",
        "mantequilla",
        "azúcar",
        "huevo",
        "sal",
        "harina",
        "nuez"
    }
}


def crear_lista_compra(menu):
    lista_compra = set()  
    for plato, ingredientes in menu.items():
        lista_compra.update(ingredientes)  
    return lista_compra


lista_de_compra = crear_lista_compra(menu)


print("Lista de la compra:")
for ingrediente in lista_de_compra:
    print(f"- {ingrediente}")