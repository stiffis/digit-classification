import pandas as pd
from sklearn import datasets

myData=datasets.load_digits()
print(myData)

"""
print('\nEl value asociado al key target es:')
print(myData['target']) #es una lista de aplanadas por eso los 2 corchetes, los targets son enteros(el objetivo)

#Imprime la ultima de las imagenes aplanadas
print('\nLa ultima aplanada es: ')
print(myData['data'][-1])#-1 refiere a el ultimo elemento

#imprime primer y ultimo target
print('\nEl primer target es: ')
print(myData['target'][0])#0 refiere a el primer elemento

print('\nEl ultimo targey es: ')
print(myData['target'][-1])#-1 refiere a el ultimo elemento

#####la cantidad de target es la key target_names
#_--------------------------------------------------------------
#images es lista de matrices osea las imagenes como matriz
#array es todo junto lo q antes era una matriz ahora es una lista

#imprimiendo la primera y ultima matriz
print('\nLa primera: ')
print(myData['images'][0])

print('\nLa ultima matriz: ')
print(myData['images'][-1])


#veamos cuantos digitos o matrices
print('\nCantidad de digitos')
print(len(myData['data']))
print(len(myData['target']))
print(len(myData['images']))


#a paretir de ahora comenzamos a almar el .xls que esta en Canvas
df1=pd.DataFrame(data=myData['images'][0])
print()
print(df1)

#((#(valor 2- valor1)todo al cuadrado)suma todo los pixeles)raizcuadrada #2 para la segunda images #1 para la primera images

#primero guardamos la primera matriz
df1 = pd.DataFrame(data=myData['images'][0])
print()
print(df1)


#creamos un separador
separador=pd.DataFrame(data=[[0,0,0,0,0,0,0,0]])

#concatenamos df1 con el separador
df1 = pd.concat([df1,separador], ignore_index=True)

#luego temporalmente guardaos la segunda matriz
df2 = pd.DataFrame(data=myData['images'][1])

#concatenamos df1y df2
print()
df3 = pd.concat([df1,df2], ignore_index=True)#para la continuacion de indices el ingore
print(df3)

print('\nVa quedando asi: ')
print(df1)

#ahora iterativamente hacemos el proceso
for i in range(2,1797):
    df1 = pd.concat([df1, separador], ignore_index=True)
    df2 = pd.DataFrame(data=myData['images'][i])
    df1 = pd.concat([df1, df2], ignore_index=True)

df1 = pd.concat([df1, separador], ignore_index=True)

#hacer una lista que tenga 9 veces cada target
#los targets estan en myData['target']
listanueva=[]
i=0
while i <= 1796:
    _=0
    while _<= 8:

        listanueva.append(myData['images'][i])
        _+=1
    i+=1

#agregar esta nueva lista a df1

print()
print(df1)
print(len(listanueva))
#agregando lista nueva a su costado
df1['nueva']=listanueva
df1.to_csv('haquedadoasi.csv')

print()
#print(df1)
#### promedio de todos los pixeles, ejemplo primer pixel de todos los 5
#### hacer matrices promedio de cada target
#### generar los diez
#### ponerlo a en un dataframe, y que sea comprensible
####

"""