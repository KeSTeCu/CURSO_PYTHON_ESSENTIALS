

def isYearLeap(year):

    if year % 4 != 0: #no divisible entre 4
        print("No es bisiesto")
        return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        print("Es bisiesto")
        return True


def daysInMonth(year, month):
    if month in [4, 6, 9, 11]:
        print('\t30 dias')
        return 30
    # Febrero depende de si es o no bisiesto
    if month == 2:
        if isYearLeap(year):
            print('\n29 dias')
            return 29
        else:
            print('\t28 dias')
            return 28
    else:
        # En caso contrario, tiene 31 días
        print('\t31 dias')
        return 31


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("\tOK")
    else:
        print("Failed")



# isYearLeap(yr)