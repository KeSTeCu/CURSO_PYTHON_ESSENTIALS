
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


acl=int(input('Ingrese el dato del # ACL'))
if acl>=1 & acl<=99:
    print('Es un ACL estandar')
elif acl>=100 & acl<=199:
    print('Es un ACL extendida')
else:
    print('El valor ingresado no es un ACL')