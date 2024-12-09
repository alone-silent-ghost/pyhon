import random

planetas = ["Mercurio", "Venus", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
distancias = [91691000.0, 41400000.0, 78340000.0, 628730000.0, 1275000000.0, 2723950000.0, 4351400000.0]
velocidad = 100000  # Velocidad en km/h
recursos = [0.0, 0.0]  # Almacenar combustible y oxígeno
planetaSeleccionado = -1

# Variables para controlar si una opción ha sido completada
destinoSeleccionado = False
naveSeleccionada = False
recursosIntroducidos = False
mostrarProgreso = 0
iniciarSimulacion = False

def mostrar_menu():
    print("\n==========================================================")
    print("******* Bienvenidos al Simulador Interplanetario ********")
    print("    ----- Creador FABIAN DIAZ -----")
    print("==========================================================")
    print("\nMenú Principal:")
    if not destinoSeleccionado:
        print("1. Seleccionar un planeta de destino")
    if not naveSeleccionada:
        print("2. Seleccionar una nave espacial")
    if not recursosIntroducidos:
        print("3. Introducir cantidades de combustible y oxígeno")
    print("4. Iniciar la simulación del viaje")
    print("5. Salir del programa")
    opcion = int(input("Elige una opción: "))
    print("Presiona ENTER para continuar")
    return opcion

def seleccionar_destino():
    print("\nSelecciona el planeta destino:")
    for i in range(len(planetas)):
        print(f"{i + 1}. {planetas[i]}")
    opcion = int(input()) - 1
    print(f"Has seleccionado {planetas[opcion]}. Distancia: {distancias[opcion]} km")

    # Mostrar sugerencia de recursos necesarios para el viaje
    combustible_necesario = calcular_combustible(distancias[opcion])
    oxigeno_necesario = calcular_oxigeno(distancias[opcion])
    print("Sugerencia de recursos para este viaje:")
    print(f"Combustible: {combustible_necesario:.2f} litros")
    print(f"Oxígeno: {oxigeno_necesario:.2f} litros")

    return opcion

def seleccionar_nave():
    global velocidad  # Añadir esta línea para declarar la variable global
    print("\nSelecciona una nave para el viaje:")
    naves = ["Nave Apolo11 (Velocidad: 100,000 km/h)", "Nave Romulus(Velocidad: 200,000 km/h)"]
    for i in range(len(naves)):
        print(f"{i + 1}. {naves[i]}")
    nave_seleccionada = int(input()) - 1
    if nave_seleccionada == 1:
        velocidad = 200000  # Si selecciona la Nave Romulos, aumenta la velocidad
    print(f"Has seleccionado {naves[nave_seleccionada]}")

def introducir_recursos():
    combustible = float(input("\nIntroduce la cantidad de combustible en litros: "))
    oxigeno = float(input("Introduce la cantidad de oxígeno en litros: "))
    return [combustible, oxigeno]

def calcular_tiempo(distancia):
    tiempo = distancia / velocidad  # tiempo en horas
    print(f"Tiempo estimado de viaje: {tiempo} horas")
    return tiempo

def calcular_combustible(distancia):
    return distancia / 10.0  # Combustible necesario en litros

def calcular_oxigeno(distancia):
    return distancia / 100.0  # Oxígeno necesario en litros

def validar_recursos(recursos_introducidos, recursos_necesarios):
    if recursos_introducidos[0] < recursos_necesarios[0] or recursos_introducidos[1] < recursos_necesarios[1]:
        print("¡Advertencia! No tienes suficientes recursos para completar el viaje.")
        return False
    return True

def iniciar_simulacion():
    if planetaSeleccionado == -1:
        print("Por favor, selecciona un planeta de destino primero.")
    else:
        tiempo_viaje = calcular_tiempo(distancias[planetaSeleccionado])
        recursos_necesarios = [calcular_combustible(distancias[planetaSeleccionado]), calcular_oxigeno(distancias[planetaSeleccionado])]
        if validar_recursos(recursos, recursos_necesarios):
            print("Iniciando simulación...")
            if simular_viaje(distancias[planetaSeleccionado], tiempo_viaje, recursos):
                print(f"¡Llegaste a {planetas[planetaSeleccionado]} con éxito!")
            else:
                print("El viaje fracasó.")
        else:
            print("Recursos insuficientes.")

def simular_viaje(distancia, tiempo, recursos):
    global velocidad  # Añadir esta línea para declarar la variable global
    combustible = recursos[0]
    oxigeno = recursos[1]
    progreso = 0
    estado_nave = 100.0  # Estado inicial de la nave en porcentaje

    while progreso < distancia:
        progreso += velocidad
        combustible -= velocidad / 10.0
        oxigeno -= velocidad / 100.0
        estado_nave -= random.random() * 0.003  # Desgaste aleatorio de la nave
        
        # Mostrar progreso y recursos actuales
        mostrar_progreso(progreso, distancia, combustible, oxigeno, estado_nave)

        # Fallos aleatorios con motivo y daño detallado
        if random.random() < 0.0099:
            print("¡Fallo en el motor! La velocidad de la nave ha disminuido.")
            velocidad = max(50000, velocidad * 0.7)
        if random.random() < 0.0080:
            print("¡Fallo en el sistema de oxígeno! El consumo de oxígeno se ha duplicado.")
            oxigeno -= velocidad / 50.0
        if random.random() < 0.008:
            danio = 2
            estado_nave -= danio
            print(f"¡Impacto de meteoritos! Daño: {danio}. Integridad restante: {estado_nave}%")

        # Verificar si los recursos están agotados o si la nave tiene problemas
        if combustible < 0 or oxigeno < 0 or estado_nave <= 50:
            print("El viaje ha fallado. La nave se quedó sin recursos o sufrió un fallo crítico.")
            return False

    print("¡Viaje completado con éxito!")
    return True

def mostrar_progreso(progreso, distancia, oxigeno, danio, estado_nave):
    progreso_porcentaje = int((progreso / distancia) * 100)
    barra = "[" + "=" * (progreso_porcentaje // 2) + " " * (50 - progreso_porcentaje // 2) + "]"
    print(f"{barra} {progreso_porcentaje}%")
    print(f"Oxígeno restante: {oxigeno:.2f} litros")
    print(f"Integridad de la nave: {estado_nave:.2f}%")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            if not destinoSeleccionado:
                planetaSeleccionado = seleccionar_destino()
                destinoSeleccionado = True
            else:
                print("Destino ya seleccionado.")
        elif opcion == 2:
            if not naveSeleccionada:
                seleccionar_nave()
                naveSeleccionada = True
            else:
                print("Nave ya seleccionada.")
        elif opcion == 3:
            if not recursosIntroducidos:
                recursos = introducir_recursos()
                recursosIntroducidos = True
            else:
                print("Recursos ya introducidos.")
        elif opcion == 4:
            if destinoSeleccionado and naveSeleccionada and recursosIntroducidos:
                iniciar_simulacion()
            else:
                print("Asegúrate de seleccionar un destino, una nave y de introducir los recursos antes de iniciar la simulación.")
        elif opcion == 5:
            print("Saliendo del programa...")
            print("¡¡¡Te esperamos pronto!!!!")
            print("Creadores Codigo: Fabian Daza y Edwin Lozano")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

