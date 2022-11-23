spoty={}
while True:
    nombre=(input('ingrese nombre del artista'))
    cancion=(input("ingresee nombre de la cancion"))
    if cancion == '':
        break
    spoty.update({nombre:cancion})
print(spoty)





