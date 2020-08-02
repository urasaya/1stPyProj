#Quadratic solved.
a, b, c = input("Enter a three value: ").split() 
if (a==int(0)): #Check that a is not equal to zero.
    print("The Equation becomes linear.")
print("X ={:5.2f}".format(-int(b)/int(c)))
Equa = int(b)**2-4*int(a)*int(c)
if not (Equa>0): #Check that Equa is more than zero.
    X1 = (-int(b)+((Equa)**1/2)/(2*int(a)))
    X2 = (-int(b)-((Equa)**1/2)/(2*int(a)))
    print("The Equation has two distinct real roots.")
    if (Equa==0): #Check that Equa is equal to zero.
        X1 = (-int(b)/2*int(a))
        X2 = (-int(b)/2*int(a))
        print("The Equation has double roots.")
    j=complex(0,-1)
    X1 = (-int(b)+(j*(-Equa)**1/2)/(2*int(a)))
    X2 = (-int(b)-(j*(-Equa)**1/2)/(2*int(a)))
    print("The Equation has complex roots.")
    print("X1 ={:5.2f},X2={:5.2f}".format(X1,X2))
print("END.")