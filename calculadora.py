import tkinter as tk
from ejercicio8 import postfixConvert
from ejercicio4 import parserPostfixToBinaryTree

def btn_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def btn_clear():
    entry.delete(0, tk.END)

def btn_equal():
    try:
        expression = entry.get()
        print(expression)
        postfix = postfixConvert(expression)
        rootNode = parserPostfixToBinaryTree(postfix)
        entry.delete(0, tk.END)
        entry.insert(tk.END, rootNode.eval())
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# Crear la ventana
window = tk.Tk()
window.title("Calculadora LAB10 EDYA")

# Crear la caja de entrada
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Crear los botones numéricos
btn_1 = tk.Button(window, text="1", command=lambda: btn_click(1))
btn_1.grid(row=1, column=0)
btn_2 = tk.Button(window, text="2", command=lambda: btn_click(2))
btn_2.grid(row=1, column=1)
btn_3 = tk.Button(window, text="3", command=lambda: btn_click(3))
btn_3.grid(row=1, column=2)
btn_4 = tk.Button(window, text="4", command=lambda: btn_click(4))
btn_4.grid(row=2, column=0)
btn_5 = tk.Button(window, text="5", command=lambda: btn_click(5))
btn_5.grid(row=2, column=1)
btn_6 = tk.Button(window, text="6", command=lambda: btn_click(6))
btn_6.grid(row=2, column=2)
btn_7 = tk.Button(window, text="7", command=lambda: btn_click(7))
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(window, text="8", command=lambda: btn_click(8))
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(window, text="9", command=lambda: btn_click(9))
btn_9.grid(row=3, column=2)
# ... Crear los demás botones numéricos

# Crear los botones de operaciones
btn_plus = tk.Button(window, text="+", command=lambda: btn_click("+"))
btn_plus.grid(row=4, column=0)
btn_minus = tk.Button(window, text="-", command=lambda: btn_click("-"))
btn_minus.grid(row=4, column=1)
btn_prod = tk.Button(window, text="*", command=lambda: btn_click("*"))
btn_prod.grid(row=4, column=2)
btn_div = tk.Button(window, text="/", command=lambda: btn_click("/"))
btn_div.grid(row=5, column=1)
btn_pot = tk.Button(window, text="^", command=lambda: btn_click("^"))
btn_pot.grid(row=5, column=0)
btn_par1 = tk.Button(window, text="(", command=lambda: btn_click("("))
btn_par1.grid(row=6, column=0)
btn_par2 = tk.Button(window, text=")", command=lambda: btn_click(")"))
btn_par2.grid(row=6, column=1)
# ... Crear los demás botones de operaciones

# Crear el botón de igual
btn_equal = tk.Button(window, text="=", command=btn_equal)
btn_equal.grid(row=5, column=2, columnspan=1)

# Crear el botón de limpiar
btn_clear = tk.Button(window, text="C", command=btn_clear)
btn_clear.grid(row=7, column=1, columnspan=1)

# Iniciar el bucle principal de la ventana
window.mainloop()
