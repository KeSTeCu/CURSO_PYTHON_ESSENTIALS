def isYearLeap(year):
    if year % 4 != 0: #no divisible entre 4
        print(year,"No es bisiesto")
        return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print(year,"Es bisiesto")
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print(year,"No es bisiesto")
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        print(year,"Es bisiesto")
        return True


def daysInMonth(year, month):
    if month in [4, 6, 9, 11]:
        #print('\t30 dias')
        return 30
    # Febrero depende de si es o no bisiesto
    if month == 2:
        if isYearLeap(year):
            #print('\n29 dias')
            return 29
        else:
            #print('\t28 dias')
            return 28
    else:
        # En caso contrario, tiene 31 días
        #print('\t31 dias')
        return 31



def dayOfYear(year, month, day):
    cant_dia=0
    dif=0
    total=0
    for i in range(month):
        num_dia=daysInMonth(year,i)
        cant_dia=num_dia+cant_dia
    
    dia_mes=daysInMonth(year,month)
    print('El mes ', month,'tiene ', dia_mes,'dias')
    if day<dia_mes:
        dif=cant_dia-dia_mes
        total=dif+day
        print('Los dias transcurridos son: ',total)
    elif day==dia_mes:
        print ('Los dias transcurridos son: ', cant_dia)
# put your new code here

#


print(dayOfYear(2000, 12, 31))