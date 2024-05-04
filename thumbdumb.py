from decimal import Decimal

while True:
    insert = float(input())
    if insert == 1:
        print("Down")
        break

    minuto = int(insert)
    segundo = float((insert-minuto)*10)
    totalsec = (minuto*12) + (segundo/5)
    minsegmen = totalsec/60
    finalmin = int(minsegmen)
    medsec = minsegmen - finalmin
    finalsec = (medsec/10)*6

    ey2 = finalmin*2
    ey3 = finalmin*3
    ey4 = finalmin*4
    ex2 = (finalsec*2)
    ex3 = (finalsec*3)
    ex4 = (finalsec*4)

    if  ex2 >= 0.60:
        ex2 = ex2-0.60
        ey2 = ey2 + 1

    if 1.19>= ex3 >=0.60:
        ex3 = ex3-0.60
        ey3 = ey3 + 1

    if ex3>=1.20:
        ex3 = ex3-1.20
        ey3 = ey3 + 2

    if 1.19>= ex4 >=0.60:
        ex4 = ex4-0.60
        ey4 = ey4 + 1

    if 1.79>= ex4 >=1.20:
        ex4 = ex4-1.20
        ey4 = ey4 + 2

    if ex4>=1.8:
        ex4 = ex4-1.8
        ey4 = ey4 + 3

    finalsec = Decimal(finalsec).quantize(Decimal("1.00"))
    ex2 = Decimal(ex2).quantize(Decimal("1.00"))
    ex3 = Decimal(ex3).quantize(Decimal("1.00"))
    ex4 = Decimal(ex4).quantize(Decimal("1.00"))

    result = finalmin + finalsec

    print(result, " ", (ex2+ey2), " ", (ex3+ey3), " ", (ex4+ey4))

    #print(result, " ", 2*result, " ", 3*result, " ", 4*result)

    #thumbdumb calculator

