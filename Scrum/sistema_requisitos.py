from Agentes.product_owner import ProductOwner
from Agentes.scrum_master import ScrumMaster
from Agentes.team import Team
import json
import os
from threading import Thread

INTERACTION_DB = "interactions.json"

class SistemaRequisitos:
    def __init__(self):
        self.po = ProductOwner("deepseek-r1")
        self.sm = ScrumMaster("deepseek-r1")
        self.team = Team("deepseek-r1")
        self.cache = {}
        self.interactions = self._cargar_interacciones()

    def _cargar_interacciones(self):
        if os.path.exists(INTERACTION_DB):
            with open(INTERACTION_DB, "r") as f:
                return json.load(f)
        return []

    def _guardar_interaccion(self, problema, requisitos, validacion_sm, validacion_team, feedback=None):
        interaccion = {
            "problema": problema,
            "requisitos": requisitos,
            "validacion_sm": validacion_sm,
            "validacion_team": validacion_team,
            "feedback": feedback
        }
        self.interactions.append(interaccion)
        with open(INTERACTION_DB, "w") as f:
            json.dump(self.interactions, f, indent=4)

    def _mejorar_modelo(self):
        print("Mejorando el modelo basado en interacciones pasadas...")
        # Aquí podrías implementar un proceso de fine-tuning del modelo.

    def levantar_requisitos(self, problema):
        if problema in self.cache:
            return self.cache[problema]

        print(f"Problema: {problema}\n")

        # Product Owner genera los requisitos
        requisitos_po = self.po.generar_requisitos(problema)
        print(f"**Requisitos iniciales (Product Owner):**\n{requisitos_po}\n")

        # Scrum Master y Team validan los requisitos en paralelo
        def validar_sm():
            return self.sm.validar_requisitos(requisitos_po)

        def validar_team():
            return self.team.validar_viabilidad(requisitos_po)

        sm_thread = Thread(target=validar_sm)
        team_thread = Thread(target=validar_team)

        sm_thread.start()
        team_thread.start()

        sm_thread.join()
        team_thread.join()

        validacion_sm = validar_sm()
        validacion_team = validar_team()

        print(f"**Validación (Scrum Master):**\n{validacion_sm}\n")
        print(f"**Validación técnica (Team):**\n{validacion_team}\n")

        # Respuesta final combinada
        respuesta_final = (
            f"**Requisitos finales:**\n{requisitos_po}\n\n"
            f"**Validación Scrum Master:**\n{validacion_sm}\n\n"
            f"**Validación Team:**\n{validacion_team}"
        )
        self.cache[problema] = respuesta_final

        # Guardar la interacción
        self._guardar_interaccion(problema, requisitos_po, validacion_sm, validacion_team)

        # Mejorar el modelo basado en las interacciones
        if len(self.interactions) % 5 == 0:  # Mejorar cada 5 interacciones
            self._mejorar_modelo()

        return respuesta_final