import tkinter as tk

def suma():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1+n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
    
def resta():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1-n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
    
def multiplicacion():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1*n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
    
def division():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1/n2
    label_resultado.config(text = "Resultado: "+ str(resultado))
    
def insertar(numeros):
    obtener = ventana.focus_get()
    if isinstance(obtener, tk.Entry):
        obtener.insert(tk.END,numeros)

def borrar():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    label_resultado.config(text="Resultado :")
    

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg = "lightblue")
    
    
num1 = tk.Entry(ventana, text="", bg="white", fg="black", width=20)
num2 = tk.Entry(ventana, tex="", bg="white", fg="black", width=20)
label_resultado = tk.Label(ventana,text = "Resultado : ", width=30, bg="white", fg="black")

#botones
boton1 = tk.Button(ventana, bg = "white", fg = "black", text = "1", width = 2, height = 2, command=lambda: insertar("1"))
boton2 = tk.Button(ventana, bg = "white", fg = "black", text = "2", width = 2, height = 2, command=lambda: insertar("2"))
boton3 = tk.Button(ventana, bg = "white", fg = "black", text = "3", width = 2, height = 2, command=lambda: insertar("3"))
boton4 = tk.Button(ventana, bg = "white", fg = "black", text = "4", width = 2, height = 2, command=lambda: insertar("4"))
boton5 = tk.Button(ventana, bg = "white", fg = "black", text = "5", width = 2, height = 2, command=lambda: insertar("5"))
boton6 = tk.Button(ventana, bg = "white", fg = "black", text = "6", width = 2, height = 2, command=lambda: insertar("6"))
boton7 = tk.Button(ventana, bg = "white", fg = "black", text = "7", width = 2, height = 2, command=lambda: insertar("7"))
boton8 = tk.Button(ventana, bg = "white", fg = "black", text = "8", width = 2, height = 2, command=lambda: insertar("8"))
boton9 = tk.Button(ventana, bg = "white", fg = "black", text = "9", width = 2, height = 2, command=lambda: insertar("9"))
boton10 = tk.Button(ventana, bg = "white", fg = "black", text = "0", width = 2, height = 2, command=lambda: insertar("0"))

boton_borrar = tk.Button(ventana, bg = "white", fg = "black", text = "AC", width = 2, height = 2, command=borrar)

boton_division = tk.Button(ventana, bg = "white", fg = "black", text = "/", width = 2, height = 2, command=division)
boton_multiplicacion = tk.Button(ventana, bg = "white", fg = "black", text = "*", width = 2, height = 2, command=multiplicacion)
boton_suma = tk.Button(ventana, bg = "white", fg = "black", text = "+", width = 2, height = 2, command= suma)
boton_resta = tk.Button(ventana, bg = "white", fg = "black", text = "-", width = 2, height = 2, command=resta)

#agregar botones
boton_division.grid(row = 4, column = 6, padx = 5, pady = 5)
boton_suma.grid(row = 0, column = 6, padx = 3, pady = 5)
boton_multiplicacion.grid(row = 3, column = 6, padx = 5, pady =5)
boton_resta.grid(row = 1, column = 6, padx = 5, pady = 5)

boton7.grid(row = 1, column = 2, padx = 5, pady = 5)
boton8.grid(row = 1, column = 3, padx = 5, pady = 5)
boton9.grid(row = 1, column = 4, padx = 5, pady = 5)

boton4.grid(row = 0, column = 4, padx = 5, pady = 5)
boton5.grid(row = 1, column = 0, padx = 5, pady = 5)
boton6.grid(row = 1, column = 1, padx = 3, pady = 5)

boton1.grid(row = 0, column = 1, padx = 5, pady = 5)
boton2.grid(row = 0, column = 2, padx = 5, pady = 5)
boton3.grid(row = 0, column = 3, padx = 5, pady = 5)

boton10.grid(row = 0, column = 0, padx = 5, pady = 5)
boton_borrar.grid(row = 5, column = 6, padx = 5, pady = 5)

num1.grid(row = 3, column = 0, columnspan=2, padx=3, pady= 3, ipadx=3, ipady=3)
num2.grid(row = 3, column = 2, columnspan=2, padx=3, pady= 3, ipadx=3, ipady=3)
label_resultado.grid(row=4, column=0, columnspan=4, padx=5, pady=5)
ventana.mainloop()