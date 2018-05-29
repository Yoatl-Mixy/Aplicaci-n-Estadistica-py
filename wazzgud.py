import math
print ('+--------------------------------+')
print ('+-------     Equipo 1       -----+')
print ('+-Gabriel Aaron Mancera Martinez-+')
print ('+--- Alejandra Ortiz Ramirez ----+')
print ('+--- Guadalupe Campos Cazares ---+')
print ('+-------------------------------+')
print ('|   Aplicacion Estadistica      |')
print ('+-------------------------------+')
num_array = list()
num = raw_input("| Tamanio de la lista:")
print ('+-------------------------------+')
print ('|       Ingresa el numero:      |')
for i in range(int(num)):
    n = raw_input("numero :")
    num_array.append(float(n))
print ('|-------------------------------|')
print 'Lista: ',num_array
print ('|-------------------------------|')
#menor a mayor
num_array.sort()
print 'Numero menor a mayor', num_array
print ('|-------------------------------|')

#mediana
if len(num_array)%2==0:
  n = len(num_array)
  mediana =(num_array[n/2-1]+ num_array[n/2] )/2
else:
  mediana = num_array[len(num_array)/2] 
  print 'mediana: ', mediana
  print ('|-------------------------------|')

#media
media = sum(num_array)/len(num_array)
print 'media: ', media
print ('|-------------------------------|')


#lista menos media
for i in range(0, len(num_array)):
  num_array[i]=num_array[i]-media
print 'Lista menos media: ', num_array
print ('|-------------------------------|')


#el cuadrado menos la media
cuadrado = num_array
for i in range(0, len(cuadrado)):
  cuadrado[i]=cuadrado[i]**2
print 'El cuadrado de lista menos la media: ', cuadrado
print ('|-------------------------------|')

#okoko
prom_promcuad = sum(cuadrado)/((len(cuadrado)-1))
print 'Promedio de la lista menos la media, al cuadrado: ', prom_promcuad
print ('|-------------------------------|')

raiz= prom_promcuad
raiz = math.sqrt(prom_promcuad)
print 'Promedio de la lista menos la media, al cuadrado: ', raiz
print ('|-------------------------------|')


