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
canvas.create_line(0, 450, 500, 450)


# --------------------------------MODELO BAILEY BASILI-------------------------------------------------------------------------------
# imagen de la formula
imgmod1 = PhotoImage(file="formula.png")
imagefrml = Label(canvas, image=imgmod1).place(x=10, y=50)

# variable
s = IntVar()
pf = IntVar()
# operaciones


def calculateE(vs):
    infovariables = vs.get()
    e = (5.5+0.73*pow(infovariables, 1.16))
    showwhite = Label(canvas, text="", width=50, bg="white").place(x=70, y=165)
    showlabele = Label(canvas, text=e, bg="white").place(x=70, y=165)


def m2calculateE(vs):
    m2infopfbox = float(vs.get())
    m2e =((0.355*m2infopfbox)-91.4)
    m2showwhite = Label(canvas, text="", width=50, bg="white").place(x=70, y=370)
    m2showlabele = Label(canvas, text=m2e, bg="white").place(x=70, y=370)

# widgets
titlebailey = Label(canvas, text="MODELO BAILEY - BASILI",
                    bg='white').place(x=180, y=10)
infovariable = Label(canvas, text="E es el esfuerzo(persona-mes o persona- años) \n S el tamaño en miles de líneas de código ",
                     bg="white").place(x=250, y=60)
textcalc = Label(canvas, text="Dale valor a S para calcular E :",
                 bg='white').place(x=10, y=100)
values = Label(canvas, text="S = ", font=fonttimes,
               bg='white').place(x=10, y=120)
valueE = Label(canvas, text="E = ", font=fonttimes,
               bg='white').place(x=10, y=155)
sbox = Entry(canvas, width=20, textvariable=s).place(x=70, y=131, height=20)
btcalculate = Button(canvas, text="Calcular E",
                     command=lambda: calculateE(s)).place(x=210, y=130)

# --------------------------------Modelo de Albrecht y Gaffney------------------------------------------------------------------------------
# imagen de la formula
imgmod2 = PhotoImage(file="modelo2.png")
imagefrml2 = Label(canvas, image=imgmod2).place(x=10, y=260)

# widgets
titlealbrecht = Label(canvas, text="MODELO DE ALBRECHT Y GAFFNEY",
                      bg='white').place(x=150, y=220)
infovatiablem2 = Label(canvas, text="E es el esfuerzo(persona-mes) \n PF es el valor de los Puntos de Funcion ",
                       bg="white").place(x=250, y=260)



m2info = Label(canvas, text="Dale valor a PF para calcular E :",
                   bg='white').place(x=10, y=300)
m2pflabel = Label(canvas, text="PF = ", font=fonttimes,
                  bg='white').place(x=10, y=320)
m2Evalue = Label(canvas, text="E = ", font=fonttimes,
                 bg='white').place(x=10, y=360)
pfboxm2 = Entry(canvas, width=20, textvariable=pf).place(x=90, y=330, height=20)
btcalculatem2 = Button(canvas, text="Calcular E",
                       command=lambda: m2calculateE(pf)).place(x=220, y=325)


pwindow.mainloop()
