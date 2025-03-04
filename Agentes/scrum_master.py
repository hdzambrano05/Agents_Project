import ollama

class ScrumMaster:
    def __init__(self, model_name):
        self.model_name = model_name

    def validar_requisitos(self, requisitos):
        prompt = (
            f"Eres un Scrum Master con más de 20 años de experiencia en gestión de proyectos ágiles. "
            f"Revisa los siguientes requisitos y verifica que sean claros, completos y libres de errores. "
            f"Sugiere mejoras si es necesario. Requisitos: {requisitos}"
        )
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={"temperature": 0.3, "max_tokens": 500}
        )
        return response['response']