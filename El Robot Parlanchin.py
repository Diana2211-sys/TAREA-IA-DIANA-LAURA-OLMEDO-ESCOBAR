def robot_responde(mensaje):
    if mensaje.lower() == "hola":
        return "¡Hola soy el robot parlanchin !"
    elif mensaje.lower() == "adios":
        return "¡Hasta luego, parlanchin!"
    else:
        return "No entiendo, intenta de nuevo"

def main():
    print("¡Bienvenido al robot conversacional!")
    while True:
        mensaje = input("Escribe un mensaje: ")
        if mensaje.lower() == "salir":
            break
        respuesta = robot_responde(mensaje)
        print("Robot: ", respuesta)

if __name__ == "__main__":
    main()
