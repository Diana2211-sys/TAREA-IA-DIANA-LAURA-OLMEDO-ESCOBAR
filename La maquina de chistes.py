import random

def contar_chiste():
    chistes = [
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.",
        "¿Qué le dice un jardinero a otro? Disfrutemos mientras podamos.",
        "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Cómo se despiden los químicos? Ácido un placer."
    ]
    input("Presiona ENTER para escuchar un chiste...")
    print(random.choice(chistes))

if __name__ == "__main__":
    contar_chiste()