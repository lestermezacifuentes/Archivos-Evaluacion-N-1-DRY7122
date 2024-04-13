Numero = int (input("Ingrese su el numero de ACL:"))

if Numero >=0 and Numero <= 99  :
    print("La ACL corresponde a una ACL Estandar")
elif Numero >=100 and Numero <=200 :
    print("La ACL corresponde a una ACL Extendida")  
else:
    print("El numero de ACL no corresponde")
