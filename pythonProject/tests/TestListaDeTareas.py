import unittest
from clases.lista_tareas import ListaDeTareas

class TestListaDeTareas(unittest.TestCase):

    def setUp(self):
        self.lista = ListaDeTareas()

    def test_agregar_tarea(self):
        self.assertEqual(self.lista.agregar_tarea("Comprar pan"), "Tarea 'Comprar pan' agregada.")
        self.assertEqual(len(self.lista.tareas), 1)

    def test_eliminar_tarea(self):
        self.lista.agregar_tarea("Comprar pan")
        self.lista.agregar_tarea("Hacer ejercicio")
        self.assertEqual(self.lista.eliminar_tarea(0), "Tarea 'Comprar pan' eliminada.")
        self.assertEqual(len(self.lista.tareas), 1)

        # Prueba eliminar con índice no válido
        self.assertEqual(self.lista.eliminar_tarea(10), "Índice no válido.")

    def test_mostrar_tareas(self):
        self.assertEqual(self.lista.mostrar_tareas(), "No hay tareas pendientes.")
        self.lista.agregar_tarea("Comprar pan")
        self.lista.agregar_tarea("Hacer ejercicio")
        self.assertEqual(self.lista.mostrar_tareas(), "1. Comprar pan\n2. Hacer ejercicio")

if __name__ == "__main__":
    unittest.main()
