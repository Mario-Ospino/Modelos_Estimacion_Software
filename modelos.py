from tkinter import *
from tkinter import font

# ventana principal
pwindow = Tk()
pwindow.geometry("1100x420")
pwindow.title("Modelos de Estimacion")
canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)
# funtes
fonttimes = font.Font(family="Times", size=24, weight="bold")

# figuras geometricas
canvas.create_line(0, 200, 550, 200)
canvas.create_line(0, 410,1100, 410)
canvas.create_line(550,410,550,0)



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
    showwhite = Label(canvas, text="", width=30, bg="white").place(x=70, y=165)
    showlabele = Label(canvas, text=e, bg="white").place(x=70, y=165)




# widgets
titlebailey = Label(canvas, text="MODELO BAILEY - BASILI",
                    bg='white').place(x=180, y=10)
infovariable = Label(canvas, text="E: es el esfuerzo(persona-mes o persona- años) \n S: el tamaño en miles de líneas de código ",
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

#operaciones
def m2calculateE(vs):
    m2infopfbox = float(vs.get())
    m2e =((0.355*m2infopfbox)-91.4)
    m2showwhite = Label(canvas, text="", width=30, bg="white").place(x=70, y=370)
    m2showlabele = Label(canvas, text=m2e, bg="white").place(x=70, y=370)
# widgets
titlealbrecht = Label(canvas, text="MODELO DE ALBRECHT Y GAFFNEY",
                      bg='white').place(x=150, y=220)
infovatiablem2 = Label(canvas, text="E: es el esfuerzo(persona-mes) \n PF: es el valor de los Puntos de Funcion ",
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
# --------------------------------Modelo Ecuacion del Software------------------------------------------------------------------------------
# imagen de la formula
imgmod3 = PhotoImage(file="modelo3.png")
imagefrml3 = Label(canvas, image=imgmod3).place(x=710, y=50)

# variable
ldc = IntVar()
t = IntVar()
p = IntVar()
# operaciones
def m3calculateE(lineascodigo,tiempo,productividad):
    m3p=productividad.get()
    m3t=tiempo.get()
    m3ldc=lineascodigo.get()

    b=0
    if m3ldc >= 5000 or m3ldc <=15000:
        b=0.16
    if m3ldc >70000:
        b=0.39

    if b != 0:
        m3e =pow((m3ldc*(pow(b,0.3333)/m3p)),3)*(1/pow(m3t,4))
        m3showwhite = Label(canvas, text="", width=10, bg="white").place(x=930, y=300)
        m3showlabele = Label(canvas, text=m3e, bg="white").place(x=930, y=300)
    
# widgets
titleecuation= Label(canvas, text="LA ECUACION DEL SOFTWARE",
                      bg='white').place(x=750, y=10)
infovatiablem3 = Label(canvas, text="E: esfuerzo  (persona-mes o persona-año) , B: es el factor especial de habilidades\n(5K-15K o mayor 70K). P: parámetro de productividad (madurez, nivel de lenguaje,entre otros) \n y T: la duración del proyecto (meses o años) ",
                       bg="white").place(x=600, y=100)

textcalc3 = Label(canvas, text="Dale valor a LDC(miles) y a T para calcular E :",
                 bg='white').place(x=580, y=180)

#ldc
m3ldclabel = Label(canvas, text="LDC = ", font=fonttimes,
                  bg='white').place(x=580, y=230)
m3ldcbox = Entry(canvas, width=20, textvariable=ldc).place(x=695, y=240, height=20)
#t
m3Tlabel = Label(canvas, text="T = ", font=fonttimes,
                  bg='white').place(x=580, y=280)
m3tbox = Entry(canvas, width=20, textvariable=t).place(x=650, y=290, height=20)
#p
m3plabel = Label(canvas, text="P = ", font=fonttimes,
                  bg='white').place(x=580, y=330)
m3pbox = Entry(canvas, width=20, textvariable=p).place(x=650, y=340, height=20)

#e
m3Evalue = Label(canvas, text="E = ", font=fonttimes,
                 bg='white').place(x=850, y=290)
m3btcalculate = Button(canvas, text="Calcular E",
                       command=lambda: m3calculateE(ldc,t,p)).place(x=850, y=250)


pwindow.mainloop()
