# Muestra en pantalla el título del programa
print("=== Sistema de Consumo de Energía ===")

# try intenta ejecutar el código que puede generar errores
try:

    # Solicita al usuario ingresar los kWh consumidos
    # input() recibe el dato como texto
    # float() convierte el texto en número decimal
    kwh = float(input("Ingrese los kWh consumidos: "))

    # Estructura condicional para determinar la tarifa según el consumo

    # Si el consumo es menor o igual a 100 kWh
    if kwh <= 100:
        tarifa = 300   # Se asigna una tarifa de $300 por kWh

    # Si el consumo es mayor a 100 pero menor o igual a 300
    elif kwh <= 300:
        tarifa = 400   # Se asigna una tarifa de $400 por kWh

    # Si el consumo es mayor a 300
    else:
        tarifa = 500   # Se asigna una tarifa de $500 por kWh

    # Calcula el costo total multiplicando
    # los kWh consumidos por la tarifa correspondiente
    total = kwh * tarifa

    # Muestra una línea en blanco antes de los resultados
    print("\n--- Resultado ---")

    # Muestra el consumo ingresado
    print("Consumo:", kwh, "kWh")

    # Muestra la tarifa aplicada
    print("Tarifa aplicada: $", tarifa, "por kWh")

    # Muestra el total a pagar
    print("Total a pagar: $", total)

# except captura el error si el usuario escribe letras u otro dato inválido
except ValueError:
    print("Error: Debe ingresar un número válido de kWh.")
