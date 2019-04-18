from tkinter import *
from tkinter import font
# ventana principal
pwindow = Tk()
pwindow.geometry("500x500")
pwindow.title("Modelos de Estimacion")
canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)
# funtes
fonttimes = font.Font(family="Times", size=24, weight="bold")

# figuras geometricas
canvas.create_line(0, 200, 500, 200)

# imagen de la formula
img = PhotoImage(file="formula.png")
imagefrml = Label(canvas, image=img).place(x=10, y=50)

#variable
s=IntVar()
# operaciones
def calculateE(vs):
    showlabele=0
    infovariables=vs.get()
    e = (5.5+0.73*pow(infovariables,1.16))
    showwhite=Label(canvas,text="",width=50,bg="white").place(x=70, y=165)
    showlabele=Label(canvas,text=e,bg="white").place(x=70, y=165)
    
# widgets
titlebailey=Label(canvas, text="MODELO BAILEY - BASILI",
                    bg='white').place(x=180, y=10)
infovariable=Label(canvas, text="E es el esfuerzo(persona-mes o persona- años) \n S el tamaño en miles de líneas de código ",
                     bg="white").place(x=250, y=60)
textcalc=Label(canvas, text="Dale valor a S para calcular E :",
                bg='white').place(x=10, y=100)
values=Label(canvas, text="S = ", font=fonttimes,
             bg='white').place(x=10, y=120)
valueE=Label(canvas, text="E = ", font=fonttimes,
             bg='white').place(x=10, y=155)
sbox=Entry(canvas, width=20,textvariable=s).place(x=70, y=131, height=20)
btcalculate=Button(canvas, text="Calcular E",
                   command= lambda: calculateE(s)).place(x=210, y=130)
pwindow.mainloop()
