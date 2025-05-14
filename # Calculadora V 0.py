# Calculadora V 0.2


import tkinter as tk
from tkinter import messagebox

def calcular(op):
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())

        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            resultado = num1 - num2
        elif op == '*':
            resultado = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("⚠️ No se puede dividir por cero.")
            resultado = num1 / num2
        elif op == '%':
            if num2 == 0:
                raise ZeroDivisionError("⚠️ No se puede sacar módulo con cero.")
            resultado = num1 % num2

        resultado_var.set(f"{num1} {op} {num2} = {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "❌ Ingresa valores numéricos válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Ventana principal
root = tk.Tk()
root.title("🧮 Calculadora Básica")
root.geometry("320x300")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Estilo común
fuente_general = ("Segoe UI", 12)

# Título
tk.Label(root, text="Calculadora Básica", font=("Segoe UI", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Entrada de números
entrada_frame = tk.Frame(root, bg="#f0f0f0")
entrada_frame.pack(pady=10)

tk.Label(entrada_frame, text="Número 1:", font=fuente_general, bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entrada1 = tk.Entry(entrada_frame, font=fuente_general, width=15)
entrada1.grid(row=0, column=1, padx=5)

tk.Label(entrada_frame, text="Número 2:", font=fuente_general, bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entrada2 = tk.Entry(entrada_frame, font=fuente_general, width=15)
entrada2.grid(row=1, column=1, padx=5)

# Botones de operación
frame_botones = tk.Frame(root, bg="#f0f0f0")
frame_botones.pack(pady=10)

boton_color = "#4caf50"
texto_color = "white"

for oper in ['+', '-', '*', '/', '%']:
    tk.Button(
        frame_botones,
        text=oper,
        font=fuente_general,
        width=4,
        bg=boton_color,
        fg=texto_color,
        relief='raised',
        command=lambda o=oper: calcular(o)
    ).pack(side='left', padx=5)

# Resultado
resultado_var = tk.StringVar()
resultado_var.set("Resultado:")
tk.Label(root, textvariable=resultado_var, font=("Segoe UI", 13, "bold"), bg="#f0f0f0", fg="#333").pack(pady=15)

root.mainloop()
