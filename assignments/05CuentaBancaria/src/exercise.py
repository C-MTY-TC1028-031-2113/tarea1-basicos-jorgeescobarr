def cuenta_bancaria():
    smm= float(input("Saldo del mes anterior: "))
    ing= float(input("Dame los ingresos: "))
    egr= float(input("dame los egresos: "))
    cheq= float(input("dame el numero de cheques: "))
    sf= (smm+ing-egr-(cheq*13))
    sf2= sf*0.075
    sf3= sf-sf2
    print("el saldo final es: " + str(sf3))

cuenta_bancaria()

