def esBisiesto (year):
    if year % 4 == 0:
        print ("Es divisible entre 4")
        if year % 100 == 0:
            print ("Es divisible entre 100")
            if year % 400 == 0:
                print ("Es divisible entre 400")
                return True
            return False
        return True
    return False

print (esBisiesto(2022))