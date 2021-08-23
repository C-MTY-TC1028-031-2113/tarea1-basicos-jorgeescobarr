def peso():
    pi=float(input("dame tu peso inicial: "))
    pf=float(input("dame el peso final: "))
    meses= float(input("dame la cantidad de meses: "))
    bpm= ((pi-pf)/meses)
    print("lo que debes bajar por mes es: " + str(bpm))
peso()