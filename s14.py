import tkinter

def sumar():
    try:
        num1 = float(cajaTexto1.get())
        num2 = float(cajaTexto2.get())
        resultado = num1 + num2
        etiqueta4["text"] = f"{num1}+{num2}={resultado}."
    except:
        etiqueta4["text"] = f"Algo salio mal con la suma."


def multiplicar():
    try:
        num1 = float(cajaTexto1.get())
        num2 = float(cajaTexto2.get())
        resultado = num1 * num2
        etiqueta4["text"] = f"{num1}*{num2}={resultado}."
    except:
        etiqueta4["text"] = f"Algo salio mal con la multiplicacion."

def siguiente():
    ventana2 = tkinter.Tk()
    ventana2.geometry("40x40")
    et = tkinter.Label(ventana2,text="Hola en la ventana")
    et.pack()



ventana = tkinter.Tk()
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana,text="Calculadora")
etiqueta.pack()

etiqueta2 = tkinter.Label(ventana,text="Numero 1:")
etiqueta2.pack()

cajaTexto1 = tkinter.Entry(ventana)
cajaTexto1.pack()

etiqueta3 = tkinter.Label(ventana,text="Numero 2:")
etiqueta3.pack()

cajaTexto2 = tkinter.Entry(ventana)
cajaTexto2.pack()


boton1 = tkinter.Button(ventana,text="+",command=sumar)
boton1.pack()

boton2 = tkinter.Button(ventana,text="*",command=multiplicar)
boton2.pack()

etiqueta4 = tkinter.Label(ventana)
etiqueta4.pack()

boton3 = tkinter.Button(ventana,text="PUSH",command=siguiente)
boton3.pack()

ventana.mainloop()