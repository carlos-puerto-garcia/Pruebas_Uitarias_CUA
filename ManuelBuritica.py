def entrada (edad, precio):    
    if(edad>=18 and precio>=20000):
        print ("¡Puede entrar a la fiesta!")
        return 1
    else:
        print ("No puede entrar, lo siento.")
        return 0
