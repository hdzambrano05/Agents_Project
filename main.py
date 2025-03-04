from Scrum.sistema_requisitos import SistemaRequisitos

def chat():
    sistema = SistemaRequisitos()
    print("¡Hola! Soy un sistema para el levantamiento de requisitos de software. Describe el problema que quieres resolver. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Sistema: ¡Adiós!")
            break
        respuesta = sistema.levantar_requisitos(user_input)
        print(respuesta)

# Iniciar el chat
chat()