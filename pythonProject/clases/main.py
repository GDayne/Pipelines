from calculadora import Calculadora
from lista_tareas import ListaDeTareas

def main():
    # Instanciamos las clases
    calc = Calculadora()
    lista = ListaDeTareas()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Calculadora")
        print("2. Lista de Tareas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n--- Calculadora ---")
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Operaciones:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            operacion = input("Selecciona una operación: ")

            if operacion == "1":
                print(f"Resultado: {calc.sumar(a, b)}")
            elif operacion == "2":
                print(f"Resultado: {calc.restar(a, b)}")
            elif operacion == "3":
                print(f"Resultado: {calc.multiplicar(a, b)}")
            elif operacion == "4":
                print(f"Resultado: {calc.dividir(a, b)}")
            else:
                print("Operación no válida.")

        elif opcion == "2":
            print("\n--- Lista de Tareas ---")
            print("1. Agregar tarea")
            print("2. Eliminar tarea")
            print("3. Mostrar tareas")
            sub_opcion = input("Selecciona una opción: ")

            if sub_opcion == "1":
                tarea = input("Ingresa la tarea: ")
                print(lista.agregar_tarea(tarea))
            elif sub_opcion == "2":
                indice = int(input("Ingresa el índice de la tarea a eliminar: ")) - 1
                print(lista.eliminar_tarea(indice))
            elif sub_opcion == "3":
                print(lista.mostrar_tareas())
            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
