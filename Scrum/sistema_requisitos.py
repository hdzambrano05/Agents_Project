from Agentes.product_owner import ProductOwner
from Agentes.scrum_master import ScrumMaster
from Agentes.team import Team

class SistemaRequisitos:
    def __init__(self):
        self.po = ProductOwner("deepseek-r1")
        self.sm = ScrumMaster("deepseek-r1")
        self.team = Team("deepseek-r1")

    def levantar_requisitos(self, problema):
        print(f"Problema: {problema}\n")

        # Product Owner genera los requisitos
        requisitos_po = self.po.generar_requisitos(problema)
        print(f"**Requisitos iniciales (Product Owner):**\n{requisitos_po}\n")

        # Scrum Master valida los requisitos
        validacion_sm = self.sm.validar_requisitos(requisitos_po)
        print(f"**Validación (Scrum Master):**\n{validacion_sm}\n")

        # Team valida la viabilidad técnica
        validacion_team = self.team.validar_viabilidad(requisitos_po)
        print(f"**Validación técnica (Team):**\n{validacion_team}\n")

        # Respuesta final combinada
        respuesta_final = (
            f"**Requisitos finales:**\n{requisitos_po}\n\n"
            f"**Validación Scrum Master:**\n{validacion_sm}\n\n"
            f"**Validación Team:**\n{validacion_team}"
        )
        return respuesta_final