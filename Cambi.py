valor = int(input("Ingrese la cantidad de dinero= "))
mone50, mone20, mone10, mone5, mone2, mone1 = 0, 0, 0, 0, 0, 0
excepcion = valor >= 1000
while (excepcion == True):
    while valor >= 50000:
        mone50 = mone50 + 1
        valor -= 50000
    while valor >= 20000:
        mone20 += 1
        valor -= 20000
    while valor >= 10000:
        mone10 += 1
        valor -= 10000
    while valor >= 5000:
        mone5 += 1
        valor -= 5000
    while valor >= 2000:
        mone2 += 1
        valor -= 2000
    while valor >= 1000:
        mone1 += 1
        valor -= 1000
    print("La cantidad de billetes para su cambio son");print("//", str(mone50)+" Billetes de 50,000", "//", str(mone20)+" Billetes de 20,000 //", str(mone10)+" Billetes de 10,000 //")
    print("//", str(mone5)+" Billetes de 5,000", "//", str(mone2)+" Billetes de 2,000", "y", "//", str(mone1)+" Billetes de 1,000 //")
    break
if excepcion == False:
    print("Señ@r no tenemos cambios con monedas")
