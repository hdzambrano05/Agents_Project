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

        # Solicitar feedback del usuario
        feedback = input("¿Fue útil la respuesta? (sí/no): ").strip().lower()
        if feedback in ["sí", "si", "s", "yes", "y"]:
            print("¡Gracias por tu feedback positivo!")
        else:
            print("Lamentamos que no fuera útil. ¿Cómo podríamos mejorar?")
            sugerencia = input("Sugerencia: ")
            sistema._guardar_interaccion(user_input, respuesta, "", "", sugerencia)

# Iniciar el chat
if __name__ == "__main__":
    chat()