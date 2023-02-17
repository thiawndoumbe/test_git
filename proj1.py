# exercice sur les dictionnaire
coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]
ordinates = []
for i in coordinates:
    ordinates.append(i)
    print(ordinates)
dict_coordinates={}    
for i in coordinates :
    c=(i[0])
    v=i[1]
    dict_coordinates[v]=c
    print(dict_coordinates)
coordinates=[(4,3),(9,3),(12,7),(13,7),(18,6),(20,19)]
coordinates2=[]
for i in coordinates :
    y=i[1]
    x=i[0]
    if y>7:
         nouveau_point=(x,7)
    else:
         nouveau_point=(x,y)
    coordinates2.append(nouveau_point)    
print(coordinates2) 