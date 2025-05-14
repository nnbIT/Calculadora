# ╔══════════════════════════════════════╗
# ║        CALCULADORA BÁSICA            ║
# ╚══════════════════════════════════════╝

# Objetivo Principal
#   - Realizar operaciones básicas: +, -, /, *, %
# Objetivos Secundarios
#   - Atrapar errores (números no válidos, división por 0, operaciones inválidas)
#   - Confirmar datos ingresados
#   - Finalizar programa tras 5 errores

# Diagrama Lógico (versión comentada del flujo)

# INICIO
#   │
#   ▼
# Mostrar menú de operaciones
#   │
#   ▼
# Solicitar operación al usuario (+, -, *, /, % o "salir")
#   │
#   ├──► Si escribe 'salir' ──► Mostrar despedida y terminar programa
#   │
#   ├──► Si es una operación válida:
#   │       │
#   │       ▼
#   │   Confirmar operación seleccionada
#   │       ├──► Si confirma, continuar
#   │       └──► Si no, volver a pedir operación
#   │
#   ▼
# Pedir primer número (con validación y confirmación)
#   │
#   ▼
# Pedir segundo número (con validación y confirmación)
#   │
#   ▼
# Ejecutar la operación correspondiente
#   │
#   ├──► Si es / o %, verificar que el segundo número no sea 0
#   │       └──► Si lo es, mostrar error y no ejecutar
#   │
#   ▼
# Mostrar el resultado
#   │
#   ▼
# Esperar a que el usuario presione Enter para continuar
#   │
#   └──► Volver al menú inicial
#
# SI operación es inválida:
#   ├──► Aumentar contador de errores
#   ├──► Mostrar mensaje de advertencia
#   └──► Si errores == 5 → terminar programa


#Hi!, i nnbIT this calculator is my first work here; i want a calculator more direct and a little funny.
