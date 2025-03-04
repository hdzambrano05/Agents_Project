import ollama

class Team:
    def __init__(self, model_name):
        self.model_name = model_name

    def validar_viabilidad(self, requisitos):
        prompt = f"Eres un equipo de desarrollo. Revisa los siguientes requisitos y verifica que sean técnicamente viables. Sugiere mejoras si es necesario. Requisitos: {requisitos}"
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={"temperature": 0.3, "max_tokens": 300}
        )
        return response['response']