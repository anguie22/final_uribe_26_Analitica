import random
from datetime import datetime, timedelta

def generar_empleados(cantidad_empleados):
    nombres = [
        "Juan", "María", "Carlos", "Ana", "Luis", "Lucía",
        "Diego", "Elena", "Jorge", "Camila", "Andrés", "Valentina"
    ]
    
    apellidos = [
        "Pérez", "García", "Rodríguez", "López",
        "Martínez", "Sánchez", "Gómez", "Ramírez", "Torres"
    ]

    fecha_actual = datetime.now()
    empleados = []

    for i in range(cantidad_empleados):
        nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"

        dias_antiguedad = random.randint(0, 1800)
        fecha_ingreso = fecha_actual - timedelta(days=dias_antiguedad)

        empleado = {
            "id": i + 1,
            "nombre_completo": nombre_completo,
            "salario_base": random.randint(1800000, 7000000),
            "documento": str(random.randint(10000000, 99999999)),
            "fecha_ingreso": fecha_ingreso.strftime("%Y-%m-%d")
        }

        empleados.append(empleado)

    return empleados


