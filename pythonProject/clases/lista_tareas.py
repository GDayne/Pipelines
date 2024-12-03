class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        return f"Tarea '{tarea}' agregada."

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice)
            return f"Tarea '{tarea_eliminada}' eliminada."
        return "Índice no válido."

    def mostrar_tareas(self):
        if not self.tareas:
            return "No hay tareas pendientes."
        return "\n".join([f"{i + 1}. {t}" for i, t in enumerate(self.tareas)])