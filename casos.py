a=int(input("ingresa el primer numero "))
b= int (input("ingresa el segundo numero"))
print("{+} suma a+b ")
print("{-}resta a-b")
print("{*} multiplicacion a*b")
print("{/} divide a/b")
simbolo = input ("ingresa la operacion insertando su simbolo correspondiente ")
match simbolo:
    case "+":
        print("el resultado es", (a+b))
    case "-":
        print("el resultado es",(a-b))
    case "*":
        print("el resultado es ", (a*b))
    case "/":
        if b!=0:
            print("el resultado es ", (a/b))
        else:
            print("no se puede dividir entre cero")
    case _ :
        print("operacion invalida")                        