
# print ('ingrese un valor: ')
# a=input()
# print ('ingrese un valor: ')
# b=input()
# print ('ingrese un valor: ')
# c=input()

# print(a,b,c)

# def mensaje():
#     print('Ingrese un dato: ')

# mensaje()
# a=input()
# mensaje()
# b=input()
# mensaje()
# c=input()

# print(a,b,c)

# def saludo (nombre):
#     print('Hola' ,nombre)

# saludo('Juan')
# saludo('Carlos')


# def direct(ciudad,barrio,calle):
#     print('La ciudad de entrega es: ',ciudad)
#     print('El sector es: ',barrio)
#     print('el pedido esta en la calle ', calle)

# ba=input('Ingrese el barrio ')
# ci=input('ingrese la ciudad: ')
# cl=input('Ingrese la direccion de su domicilio: ')

# direct(ci,ba,cl)

# def res(a,b):
#     resultado = a - b
#     print('\n',resultado)
    
# res(a=4,b=5)
# res(b=8,a=2)
# res(5,b=2)
# res(a=6,5)

# def resta(a,b):
#     print(a-b)

# x=resta(5,1)
# opt=x+1
# print(opt)

# def saludo3(lista):
#     for i in lista:
#         print('hola, ',i)
#         print('')

# saludo3(['Juan'])
# saludo3(['Juan', 'Carlos'])
# saludo3(['Juan', 'Carlos','Ana'])
# saludo3(('Juan', 'Carlos','Dillan'))

def crealista(n):
    lista=[]
    for item in range(1,n+1):
        lista.append(item)
    return lista

print(crealista(50))