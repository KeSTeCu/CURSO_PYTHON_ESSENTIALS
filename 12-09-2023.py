
# datos=1
# nativa=100
# if datos==nativa:
#     print('1')

#     print('Las variables son iguales')

#     print('2')
# else:
#     if datos==nativa:
#         print('Las variables son diferentes')
#     else:
#         if datos


# acl=int(input('Ingrese el dato del # ACL'))
# if acl>=1 & acl<=99:
#     print('Es un ACL estandar')
# elif acl>=100 & acl<=199:
#     print('Es un ACL extendida')
# else:
#     print('El valor ingresado no es un ACL')

# lista=[1,2,3,4,5,6,7]
# print(len(lista))
# print(lista[0])

# for i in lista :
#     print(i, end=" ")

# for item in range(1,11,1):
#     print(item)

##EJERCICIO DE TABLA DE MULTIPLICAR
# for i in range(1,16,1):
#     print('\t\tTabla del ',i)
#     for j in range (1,16,1):
#         print(i*j,end=' ')
#     print('\n')


## EJERCICIO DE CLASIFICACION
#lista3=[]
# lista_r=[]
# lista_s=[]
# lista_varios=[]
# lista2=['R1','R2','R3','R4','S1','S2','S3','AP1', 'FW1','OLT1']
# print('\nLa lista 2 es:\n', lista2)

# for item in lista2:
#     if 'R' in item:
#         lista3.append(item)
# print('\nLa lista 3 es:\n', lista3,'\n')

# for item in lista2:
#     if 'R' in item:
#         lista_r.append(item)
#     elif 'S' in item:
#         lista_s.append(item)
#     else:
#         lista_varios.append(item)
# print('\nLa lista R es:\n', lista_r,'\n')
# print('\nLa lista S es:\n', lista_s,'\n')
# print('\nLa lista VARIOS es:\n', lista_varios,'\n')

## WHILE
# numero= input('Ingrese el numero que debo contar: ')
# numero=int(numero)
# contador =1
# while contador <= numero:
#     print(contador)
#     contador+=1


## WHILE CON TRUE
# numero= input('Ingrese el numero que debo contar: ')
# numero=int(numero)
# contador =1
# while True:
#     print(contador)
#     contador+=1
#     if contador > numero:
#         break

while True:
    x=input('Enter a number to count to : ')
    if x== 'q' or x== 'quit':
        break
    x= int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
