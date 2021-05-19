'''miDiccionario = {"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)
miDiccionario["Italia"] = "Roma"
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)
miDiccionario = {"Alemania" : "Berlín", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario)
miTupla = ["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario = {miTupla[0]:"Madrid",miTupla[1]:"París",miTupla[2]:"Londres",miTupla[3]:"Alemania"}
print(miDiccionario["Francia"])'''
miDiccionario = {23:"Jordan", "Nombre":"Michael","Equipo":"Chicago",
"Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))