import ollama

class ProductOwner:
    def __init__(self, model_name):
        self.model_name = model_name

    def generar_requisitos(self, problema):
        prompt = f"Eres un Product Owner. Analiza el siguiente problema y genera una lista de requisitos funcionales y no funcionales, priorizados según las necesidades del cliente. Problema: {problema}"
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={"temperature": 0.3, "max_tokens": 300}
        )
        return response['response']