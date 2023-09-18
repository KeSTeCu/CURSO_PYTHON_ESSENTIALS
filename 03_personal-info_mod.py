

# nombre=input('\nINGRESE SU NOMBRE: ')
# apellido=input('Ingrese su aprellido: ')
# locacion=input('Ingrese su locacion: ')
edad=int(input('\nIngrese su edad: '))

# print('era una vez un unicornio tuerto llamado ', nombre,'de la tribu ', apellido, ', ubicado en la no tan magica tierra de ', locacion,' en esta tribu existe una costumbre la cual era que a la tierna edad de ',edad,' años debian domar un capibara')


if edad >=0 and edad<=12:
    print('\nLa fruta aun no madura\n')

elif edad>12 and edad<=21:
    print('\nEres COLAGENO\n')

elif edad >21 and edad<=60:
    print('\nBOOMER\n')

elif edad>60:
    print('\nSigues vivo? \n\t\tFELICITACIONES :O\n')

else:
    print('\nPerate aun ni naces')

