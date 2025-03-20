import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Personalizada")  # Título de la ventana
root.geometry("400x500")  # Tamaño de la ventana (ancho x alto)

# Iniciar la aplicación
root.mainloop()

# Pantalla para mostrar los números y resultados
pantalla = tk.Entry(root, font=("Arial", 24), justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Función para agregar números y operaciones a la pantalla
def agregar_a_pantalla(valor):
    pantalla.insert(tk.END, valor)

# Función para limpiar la pantalla
def limpiar_pantalla():
    pantalla.delete(0, tk.END)

# Función para calcular el resultado
def calcular_resultado():
    try:
        resultado = eval(pantalla.get())  # Evalúa la expresión en la pantalla
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Lista de botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '=', '%'
]

# Posicionar los botones en la ventana
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(root, text=boton, font=("Arial", 18), command=calcular_resultado).grid(row=fila, column=columna, columnspan=2, sticky="nsew")
        columna += 1
    elif boton == 'C':
        tk.Button(root, text=boton, font=("Arial", 18), command=limpiar_pantalla).grid(row=fila, column=columna, sticky="nsew")
    elif boton == '%':
        tk.Button(root, text=boton, font=("Arial", 18), command=lambda: agregar_a_pantalla('/100')).grid(row=fila, column=columna, sticky="nsew")
    else:
        tk.Button(root, text=boton, font=("Arial", 18), command=lambda b=boton: agregar_a_pantalla(b)).grid(row=fila, column=columna, sticky="nsew")
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
        
# Configurar el layout para que los botones se expandan con la ventana
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    
# Función para convertir Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit():
    try:
        celsius = float(pantalla.get())
        fahrenheit = (celsius * 9/5) + 32
        pantalla.delete(0, tk.END)
        pantalla.insert(0, f"{fahrenheit:.2f} °F")
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Botón para conversión de unidades
tk.Button(root, text="°C to °F", font=("Arial", 18), command=convertir_celsius_a_fahrenheit).grid(row=6, column=0, columnspan=2, sticky="nsew")
