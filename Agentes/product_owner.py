import ollama

class ProductOwner:
    def __init__(self, model_name):
        self.model_name = model_name

    def generar_requisitos(self, problema):
        prompt = (
            f"Eres un Product Owner con más de 20 años de experiencia en desarrollo de software. "
            f"Analiza el siguiente problema y genera una lista detallada de requisitos funcionales y no funcionales, "
            f"priorizados según las necesidades del cliente. Problema: {problema}"
        )
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={"temperature": 0.3, "max_tokens": 500}
        )
        return response['response']