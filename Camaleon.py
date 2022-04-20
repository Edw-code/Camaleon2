#Camaleon
import tkinter as tk
import random

#libreria importada
WDW = tk.Tk()

#funcion de aplicar colores
def cls():

    #colores aplicados
 clores = [ "red", "yellow","blue", "purple", "green", "orange", "pink", "light green","black"]
 
 #accion que aplica color
 Multicls= random.choice(clores)
 WDW.config(background=Multicls)

 #texto que indica el color
 clr = tk.Label(WDW, text =Multicls, font= "Purisa 15", width=8, height=1, fg="black", bg= "white")
 clr.place(x = 380, y = 150)
    
#ventana
WDW.geometry("600x400")
WDW.resizable(False,False)
WDW.title ("ventana multicolor")

#Titulo1
Titulo=tk.Label(text="Color de fondo:", font= "Tahoma 15", bg="black", fg="white",width= 15, height=1)
Titulo.place(x=180, y=150)

#boton
Btn = tk.Button(WDW, text="Precioname", width=14, height=2, command=cls)
Btn.place(x=240, y=270 )

#Para que no se cierre la ventana
WDW.mainloop()