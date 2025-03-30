import random

def generar_codigo_secreto():
    codigo_secreto = {}
    operaciones = [
        "{} + {}", "{} - {}", "{} * {}", "{} // {}", "{} % {}", "{} ** {}"
    ]
    
    for _ in range(5):
        num_clave = random.randint(1, 10)
        op = random.choice(operaciones)
        a, b = random.randint(1, 10), random.randint(1, 10)
        expresion = op.format(a, b)
        
        try:
            resultado = eval(expresion)  # Calcula el resultado de la expresión
            codigo_secreto[num_clave] = expresion
        except ZeroDivisionError:
            continue  # Evita divisiones por cero
    
    return codigo_secreto

def jugar():
    codigo_secreto = generar_codigo_secreto()
    print("Bienvenido al juego de descifrado de código secreto!\n")
    
    respuestas_correctas = 0
    
    for clave, expresion in codigo_secreto.items():
        respuesta_usuario = input(f"Resuelve: {expresion} = ")
        
        if respuesta_usuario.isdigit() and int(respuesta_usuario) == eval(expresion):
            respuestas_correctas += 1
        else:
            print("Acceso Denegado. Fallaste en una respuesta.")
            return
    
    if respuestas_correctas == len(codigo_secreto):
        print("¡Código Descifrado! Has ganado.")
    else:
        print("Acceso Denegado.")

if __name__ == "__main__":
    jugar()
