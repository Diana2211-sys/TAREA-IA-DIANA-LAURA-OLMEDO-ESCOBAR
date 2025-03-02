from gettext import find


INICIO  
    suma ← 0  
    PARA i DESDE 1 HASTA 50 HACER  
        SI i MOD 2 = 0 ENTONCES  
            suma ← suma + i  
        FIN SI  
    FIN PARA  
    IMPRIMIR "La suma de los números pares es:", suma  
find