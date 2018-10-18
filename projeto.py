from sympy import *
initialY, initialT, h, stepCount, functi, y, t, order = symbols('initialT initialY h stepCount functi y t order')
e = open("entrada.txt", "r")
s = open("saida.txt", "w")

aux_arr = []

aborder2 = [-0.5, 1.5]
aborder3 = [5/12.0, -4/3.0, 23/12.0]
aborder4 = [-3/8.0, 37/24.0, -59/24.0, 55/24.0]
aborder5 = [251/720.0, -637/360.0, 109/30.0, -1387/360.0, 1901/720.0]
aborder6 = [-95/288.0, 959/480.0, -3649/720.0, 4991/720.0, -2641/480.0, 4277/1440.0]
aborder7 = [19087/60480.0, -5603/2520.0, 135713/20160.0, -10754/945.0, 235183/20160.0, -18637/2520.0, 198721/60480.0]
aborder8 = [-5257/17280.0, 32863/13440.0, -115747/13440.0, 2102243/120960.0, -296053/13440.0, 242653/13440.0, -1152169/120960.0, 16083/4480.0]

amorder2 = [0.5, 0.5]
amorder3 = [-1/12.0, 2/3.0, 5/12.0]
amorder4 = [1/24.0, -5/24.0, 19/24.0, 3/8.0]
amorder5 = [-19/720.0, 53/360.0, -11/30.0, 323/360.0, 251/720.0]
amorder6 = [3/160.0, -173/1440.0, 241/720.0, -133/240.0, 1427/1440.0, 95/288.0]
amorder7 = [-863/60480.0, 263/2520.0, -6737/20160.0, 586/945.0, -15487/20160.0, 2713/2520.0, 19087/60480.0]
amorder8 = [275/24192.0, -11351/120960.0, 1537/4480.0, -88547/120960, 123133/120960.0, -4511/4480, 139849/120960.0, 5257/17280.0]

diorder2 = [-1/3.0, 4/3.0]
diorder3 = [2/11.0, -9/11.0, 18/11.0]
diorder4 = [-3/25.0, 16/25.0, -36/25.0, 48/25.0]
diorder5 = [12/137.0, -75/137.0, 200/137.0, -300/137.0, 300/137.0]
diorder6 = [-10/147.0, 72/147.0, -225/147.0, 400/147.0, -450/147.0, 360/147.0]

def ab(initialPoints, initialT, h, stepCount, functi, order):
    s.write("Metodo de Adam Bashforth\n")
    s.write("y("+str(initialT)+") = "+str(initialPoints[0])+"\n")
    s.write("h = "+str(h)+"\n")
    count = 0
    s.write(str(count)+" "+str(initialPoints[0])+"\n")
    for i in range(order-1):
        count = count + 1
        s.write(str(count)+" "+str(initialPoints[i+1])+"\n")
    if order == 2:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[1] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[2] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[3] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[4] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(stepCount-order+1):
                aux = aux + h*aborder6[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[5] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")
    elif order == 7:
        for j in range(stepCount):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[6] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[7] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " "+ str(finalY)+"\n")




def am(initialPoints, initialT, h, stepCount, functi, order):
    s.write("Metodo de Adam Multon\n")
    s.write("y("+str(initialT)+") = "+str(initialPoints[0])+"\n")
    s.write("h = "+str(h)+"\n")

    count = 0
    s.write(str(count)+" "+str(initialPoints[0])+"\n")
    for i in range(order-1):
        count = count+1
        s.write(str(count)+" "+str(initialPoints[i+1])+"\n")
    if order == 2:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[1] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder2[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[0] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[2] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder3[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[1] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[3] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder4[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[4] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder5[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[3] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[5] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder6[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 7:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[6] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder7[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[5] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            yfromAB = initialPoints[7] + aux
            initialPoints.pop(0)
            initialPoints.append(yfromAB)
            initialT = initialT + h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder8[i]*functi.subs([(t, initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[6] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")


def fi(initialPoints, initialT, h, stepCount, functi, order):
    s.write("Metodo da Formula Inversa de Diferenciacao\n")
    s.write("y("+str(initialT)+") = "+str(initialPoints[0])+"\n")
    s.write("h = "+str(h)+"\n")

    count = 0
    s.write(str(count)+" "+str(initialPoints[0])+"\n")
    for i in range(order-1):
        count = count+1
        s.write(str(count)+" "+str(initialPoints[i+1])+"\n")
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder2[i]*initialPoints[i]
            finalY = aux + (2/3.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder3[i]*initialPoints[i]
            finalY = aux + (6/11.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder4[i]*initialPoints[i]
            finalY = aux + (12/25.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder5[i]*initialPoints[i]
            finalY = aux + (60/137.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder6[i]*initialPoints[i]
            finalY = aux + (60/147.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")





def euler(initialY, initialT, h, stepCount, functi):
    count = 0
    s.write("Metodo de Euler\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")

    for i in range(stepCount):
        count = count + 1
        finalY = initialY + functi.subs([(t, initialT), (y, initialY)])*h
        s.write(str(count) + " "+str(finalY)+"\n")
        initialY = finalY
        initialT = initialT+h

def inv_euler(initialY, initialT, h, stepCount, functi):
    count = 0
    s.write("Metodo de Euler Inverso\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")


    for i in range(stepCount):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)])*h
        s.write(str(count) + " "+str(finalY)+"\n")
        initialY = finalY
        initialT = initialT+h

def apr_euler(initialY, initialT, h, stepCount, functi):
    count = 0
    s.write("Metodo de Euler Aprimorado\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")


    for i in range(stepCount):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + (functi.subs([(t,initialT),(y,initialY)]) + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)]))*h*0.5
        s.write(str(count) + " "+str(finalY)+"\n")
        initialY = finalY
        initialT = initialT+h

def rg_k(initialY, initialT, h, stepCount, functi):
    count = 0
    s.write("Metodo de Runge Kutta\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")

    for i in range(stepCount):
        count = count+1
        k1 = functi.subs([(t,initialT),(y,initialY)])
        k2 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k1))])
        k3 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k2))])
        k4 = functi.subs([(t, initialT+h),(y, initialY+h*k3)])
        finalY = initialY + (h*(k1+2*k2+2*k3+k4))/6
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT + h
        initialY = finalY



def ab_e(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adam Bashforth por Euler\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n") 
    for i in range(order-1):
        count = count+1
        yfromOther = initialY + functi.subs([(t, initialT), (y, initialY)])*h
        initialPoints.append(yfromOther)
        initialY = yfromOther
        s.write(str(count) + " " + str(yfromOther)+"\n")
        initialT = initialT+h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[1] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[2] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[3] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[4] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
            
    elif order == 6:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[5] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 7:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[6] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[7] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")

def ab_ie(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adam Bashforth por Euler Inverso\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)])*h
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count) +" "+str(finalY)+"\n")
        initialT = initialT+h       
    initialT = fixedT
    if order == 2:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[1] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[2] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[3] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[4] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
            
    elif order == 6:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[5] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 7:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[6] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[7] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")

def ab_ae(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adam Bashforth por Euler Aprimorado\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + (functi.subs([(t,initialT),(y,initialY)]) + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)]))*h*0.5
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT+h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[1] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[2] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[3] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[4] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
            
    elif order == 6:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[5] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 7:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[6] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[7] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
def ab_rk(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adam Bashforth por Runge Kutta\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count+1
        k1 = functi.subs([(t,initialT),(y,initialY)])
        k2 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k1))])
        k3 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k2))])
        k4 = functi.subs([(t, initialT+h),(y, initialY+h*k3)])
        finalY = initialY + (h*(k1+2*k2+2*k3+k4))/6
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT + h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[1] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[2] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[3] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[4] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
            
    elif order == 6:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[5] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 7:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[6] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount-order+1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t,  initialT + h*i),(y, initialPoints[i])])
            finalY = initialPoints[7] + aux
            initialPoints.pop(0)
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count) + " " + str(finalY)+"\n")

def am_e(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adam Multon por Euler\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range (order-1):
        count = count+1
        yfromOther = initialY + functi.subs([(y, initialY),(t, initialT)])*h
        initialPoints.append(yfromOther)
        initialY = yfromOther
        s.write(str(count) + " " + str(yfromOther)+"\n")
        initialT = initialT + h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

    elif order == 7:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

def am_ie(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adams Multon por Euler Inverso\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)])*h
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count) +" "+str(finalY)+"\n")
        initialT = initialT+h       
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

    elif order == 7:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

def am_ae(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adams Multon por Euler Aprimorado\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + (functi.subs([(t,initialT),(y,initialY)]) + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)]))*h*0.5
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT+h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

    elif order == 7:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

def am_rk(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Adams Multon por Runge Kutta\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count+1
        k1 = functi.subs([(t,initialT),(y,initialY)])
        k2 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k1))])
        k3 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k2))])
        k4 = functi.subs([(t, initialT+h),(y, initialY+h*k3)])
        finalY = initialY + (h*(k1+2*k2+2*k3+k4))/6
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT + h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")

    elif order == 7:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder7[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 8:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            initialPoints.pop(0)
            initialT = initialT+h
            aux = 0
            for i in range(order):
                aux = aux + h*amorder8[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            finalY = initialPoints[order-2] + aux
            initialPoints.pop(order-1)
            initialPoints.append(finalY)
            s.write(str(count)+" "+str(finalY)+"\n")
def fi_e(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Formula Inversa de Diferenciacao por Euler\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n") 
    for i in range(order-1):
        count = count+1
        yfromOther = initialY + functi.subs([(y, initialY),(t, initialT)])*h
        initialPoints.append(yfromOther)
        initialY = yfromOther
        s.write(str(count) + " " + str(yfromOther)+"\n")
        initialT = initialT + h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder2[i]*initialPoints[i]
            finalY = aux + (2/3.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder3[i]*initialPoints[i]
            finalY = aux + (6/11.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder4[i]*initialPoints[i]
            finalY = aux + (12/25.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder5[i]*initialPoints[i]
            finalY = aux + (60/137.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder6[i]*initialPoints[i]
            finalY = aux + (60/147.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")

def fi_ie(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Formula Inversa de Diferenciacao por Euler Inverso\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)])*h
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count) +" "+str(finalY)+"\n")
        initialT = initialT+h       
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder2[i]*initialPoints[i]
            finalY = aux + (2/3.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder3[i]*initialPoints[i]
            finalY = aux + (6/11.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder4[i]*initialPoints[i]
            finalY = aux + (12/25.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder5[i]*initialPoints[i]
            finalY = aux + (60/137.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder6[i]*initialPoints[i]
            finalY = aux + (60/147.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")

def fi_ae(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY)
    count = 0
    fixedT = initialT
    s.write("Metodo de Formula Inversa de Diferenciacao por Euler Aprimorado\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count + 1
        Ybysimpleeuler = initialY + functi.subs([(t,initialT),(y, initialY)])*h
        finalY = initialY + (functi.subs([(t,initialT),(y,initialY)]) + functi.subs([(t, initialT+h), (y, Ybysimpleeuler)]))*h*0.5
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT+h
    initialT = fixedT
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder2[i]*initialPoints[i]
            finalY = aux + (2/3.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder3[i]*initialPoints[i]
            finalY = aux + (6/11.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder4[i]*initialPoints[i]
            finalY = aux + (12/25.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder5[i]*initialPoints[i]
            finalY = aux + (60/137.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder6[i]*initialPoints[i]
            finalY = aux + (60/147.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")

def fi_rk(initialY, initialT, h, stepCount, functi, order):
    initialPoints = []
    initialPoints.append(initialY) 
    count = 0
    fixedT = initialT
    s.write("Metodo de Formula Inversa de Diferenciacao por Runge Kutta\n")
    s.write("y("+str(initialT)+") = "+str(initialY)+"\n")
    s.write("h = "+str(h)+"\n")
    s.write(str(count)+" "+str(initialY)+"\n")
    for i in range(order-1):
        count = count+1
        k1 = functi.subs([(t,initialT),(y,initialY)])
        k2 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k1))])
        k3 = functi.subs([(t, initialT+h*0.5),(y, initialY+(h*0.5*k2))])
        k4 = functi.subs([(t, initialT+h),(y, initialY+h*k3)])
        finalY = initialY + (h*(k1+2*k2+2*k3+k4))/6
        initialPoints.append(finalY)
        initialY = finalY
        s.write(str(count)+" "+str(finalY)+"\n")
        initialT = initialT + h
    initialT = fixedT  
    if order == 2:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder2[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder2[i]*initialPoints[i]
            finalY = aux + (2/3.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 3:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder3[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder3[i]*initialPoints[i]
            finalY = aux + (6/11.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 4:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder4[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder4[i]*initialPoints[i]
            finalY = aux + (12/25.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 5:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder5[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder5[i]*initialPoints[i]
            finalY = aux + (60/137.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    elif order == 6:
        for j in range(stepCount - order + 1):
            aux = 0
            count = count + 1
            for i in range(order):
                aux = aux + h*aborder6[i]*functi.subs([(t, initialT+(h*i)),(y, initialPoints[i])])
            ybyAB = initialPoints[order-1] + aux
            initialPoints.append(ybyAB)
            aux = 0
            for i in range(order):
                aux = aux + diorder6[i]*initialPoints[i]
            finalY = aux + (60/147.0)* h * functi.subs([(t, initialT + h*order),(y, initialPoints[order])])
            initialPoints.pop(0)
            initialPoints.pop()
            initialPoints.append(finalY)
            initialT = initialT + h
            s.write(str(count)+" "+str(finalY)+"\n")
    


for line in e:
    entry = line.split()
    metodo = str(entry[0])
    if metodo == 'euler':
        euler(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]))
        s.write("\n")
    elif metodo == 'euler_inverso':
        inv_euler(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]))
        s.write("\n")
    elif metodo == 'euler_aprimorado':
        apr_euler(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]))
        s.write("\n")
    elif metodo == 'runge_kutta':
        rg_k(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]))
        s.write("\n")
    elif metodo == 'adam_bashforth_by_euler':
        ab_e(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_bashforth_by_euler_inverso':
        ab_ie(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_bashforth_by_euler_aprimorado':
        ab_ae(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_bashforth_by_runge_kutta':
        ab_rk(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_multon_by_euler':
        am_e(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_multon_by_euler_inverso':
        am_ie(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_multon_by_euler_aprimorado':
        am_ae(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'adam_multon_by_runge_kutta':
        am_rk(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'formula_inversa_by_euler':
        fi_e(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'formula_inversa_by_euler_inverso':
        fi_ie(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'formula_inversa_by_euler_aprimorado':
        fi_ae(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'formula_inversa_by_runge_kutta':
        fi_rk(float(entry[1]), float(entry[2]), float(entry[3]), int(entry[4]), sympify(entry[5]), int(entry[6]))
        s.write("\n")
    elif metodo == 'formula_inversa' or  metodo == 'adam_multon' or  metodo == 'adam_bashforth':
        order = int(entry[len(entry)-1])
        for j in range(1, order+1):
            aux_arr.append(float(entry[j]))
        if metodo == 'formula_inversa':
            fi(aux_arr, float(entry[len(entry)-5]), float(entry[len(entry)-4]), int(entry[len(entry)-3]), sympify(entry[len(entry)-2]), order)
        elif metodo == "adam_multon":
            am(aux_arr, float(entry[len(entry)-5]), float(entry[len(entry)-4]), int(entry[len(entry)-3]), sympify(entry[len(entry)-2]), order)
        else:
            ab(aux_arr, float(entry[len(entry)-5]), float(entry[len(entry)-4]), int(entry[len(entry)-3]), sympify(entry[len(entry)-2]), order)
        aux_arr[:] = []
        s.write("\n")
e.close()
s.close()