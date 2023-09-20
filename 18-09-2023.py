
# print('INICIO')
# try:
#     print('1')
#     x=1/0
#     print('2')
# except:
#     print('Hay un error')
# print('3')
# print('FIN')


# try:
#     x=int(input('Enter a numbre: '))
#     y=1/x
#     print(y)
# except ZeroDivisionError:
#     print('You cannot divide by zero, sorry')
# except ValueError:
#     print('You must enter an integer value')
# except:
#     print('Oh dear, something went wrong...')
# print('THE END')

import math
x=float(input('Ingrese un numero: '))
assert x>0.0
x=math.sqrt(x)
print(x)