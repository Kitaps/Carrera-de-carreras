

import serial
#****************
# CONFIGURACIÓN *
#****************

puertocom="COM4"
pasos_parado=500

ser = serial.Serial(puertocom, 9600)

#***********
#  BENJA   *
#***********
def pasos(x):

    return int(round(x*pasos_parado/100,2))

#
#***********
# PATRICK  *
#***********


import Tkinter
#import tkinter.font
import tkFont
while True:
    class carrera:
        def __init__(self, titulo, institucion, duracion, ing, ara):
            self.titulo=titulo
            self.institucion=institucion
            self.duracion=float(duracion)
            self.ara=int(ara)
            self.ing=int(ing)

        def name(self):
            n=self.titulo
            return n
        def nombre(self):
            return (self.titulo[2:-1],self.institucion[2:-1])
        
        def deuda(self):
            d=((self.duracion)*(self.ara)/2)
            return d

        def ganancia(self):
            g=(self.ing)*6
            return g
        

    #buscar carrera respectiva aseleccion
    def seleccionado (carrera,institucion):
        for i in range (0, len(l_c)):
            if carrera == str(l_c[i].name()) and institucion==str(l_c[i].institucion):
                return(l_c[i])

    #lista_carreras
    l_c=[]
    data=open("dataset_export.txt")
    for line in data:
        #separo
        s=line.split(",")
        s[0]=s[0].strip("'")
        #s[0]=s[0].replace("ñ", "n")
        s[1]=s[1].strip("' ")
        #s[1]=s[1].replace("ñ", "n")
        

        
        micarrera=carrera(s[0],s[1],s[2],s[3],s[4])
        l_c.append(micarrera)
    data.close()

    #lista_titulos
    l_t=[]
    for i in range(0, len(l_c)):
        if l_c[i].name() not in l_t:
            l_t.append(l_c[i].name())

    #lista_institutos
    def listinst(titulo):
        l_i=[]
        for i in range(0, len(l_c)):
            if str(l_c[i].name())==(titulo):
                l_i.append(str(l_c[i].institucion))
        return (l_i)




    #Scrollbar entera probajada de internet lulz
    from Tkinter import *

    class ListBoxChoice(object):
        def __init__(self, master=None, title=None, message=None, list=[]):
            self.master = master
            self.value = None
            self.list = list[:]
            
            self.modalPane = Toplevel(self.master)

            self.modalPane.transient(self.master)
            self.modalPane.grab_set()

            self.modalPane.bind("<Return>", self._choose)
          
            
            
            
            if title:
                self.modalPane.title(title)

            if message:

    #LETRA PARA EL TITULO
                
                Label(self.modalPane, text=message, font=("Helvetica", "20")).pack(padx=5, pady=5)

            listFrame = Frame(self.modalPane)
            #  listFrame = Frame(self.modalPane)
          #  listFrame.pack(side=TOP, padx=5, pady=5)
          
    #ACA VA EL TAMANIO DE LA VENTANA!!! (Espaciado entre widgets)
            listFrame.pack(side=TOP, padx=250, pady=170)        
            
            scrollBar = Scrollbar(listFrame)
            scrollBar.pack(side=RIGHT, fill=Y,expand=1)
            self.listBox = Listbox(listFrame, selectmode=SINGLE)
            self.listBox.pack(side=LEFT, fill=BOTH, expand=1)
            scrollBar.config(command=self.listBox.yview)
            self.listBox.config(yscrollcommand=scrollBar.set, width=90)
            self.list.sort()
            for item in self.list:
                self.listBox.insert(END, item)

            buttonFrame = Frame(self.modalPane)
            buttonFrame.pack(side=BOTTOM)

            chooseButton = Button(buttonFrame, text="Elegir", command=self._choose,font=("Helvetica", "16"))
            chooseButton.pack()

            randomButton =Button(buttonFrame, text="Random", command=self._random)
            randomButton.pack()#(side=LEFT)

            

        def _choose(self, event=None):
            try:
                firstIndex = self.listBox.curselection()[0]
                self.value = self.list[int(firstIndex)]
            except IndexError:
                self.value = None
                #meti esto aca abajo
                self.value = "'1random"
            self.modalPane.destroy()

        def _random(self, event=None):
            self.value = "'1random"
            self.modalPane.destroy()


     
            
        def returnValue(self):
            self.master.wait_window(self.modalPane)
            return self.value

    """
    #IMAGEN!!!

            self.filename = PhotoImage(file = "linux.gif")
            
            imageFrame = Frame(self.modalPane)
            imageFrame.pack(side=BOTTOM)
    #Tamanio Imagen Box
            canvas = Tkinter.Canvas(imageFrame,  width=500, height=500)
    #Posicion Centro Imagen
            image = canvas.create_image(250, 250,  image=self.filename)
            canvas.pack()
    """      

    #

    if __name__ == '__main__':
        
        root = Tk()
        root.geometry("0x0+0+0")
        
        
        returnValue = 0
       # list = [random.randint(1,100) for x in range(50)]
        list = l_t
        while returnValue == 0:
            #helv36 = font(family="Helvetica",size=36,weight="bold")
            returnValue = ListBoxChoice(root, "Carrera", "\nPaso 1 de 5 \nElige una carrera para el estudiante a la izquierda",  list).returnValue()
            #return returnValue

    #print (returnValue)
    titulo_uno=returnValue
    lista_instituciones=listinst(titulo_uno)


    if lista_instituciones != []:
        if __name__ == '__main__':
        #import random
            root = Tk()
            root.geometry("0x0+0+0")
           
            returnValue = 0
       # list = [random.randint(1,100) for x in range(50)]
            list = lista_instituciones
            listaux_uno = lista_instituciones
            while returnValue == 0:
                returnValue = ListBoxChoice(root, "Institucion", "\nPaso 2 de 5 \nAhora elige una insitución de interés para este estudiante", list).returnValue()
    """
    if __name__ == '__main__':
        #import random
        root = Tk()
        root.geometry("0x0+0+0")
           
        returnValue = 0
       # list = [random.randint(1,100) for x in range(50)]
        list = lista_instituciones
        while returnValue == 0:
            returnValue = ListBoxChoice(root, "Institución", "Porfavor seleccione institución de interés, o Random para que sea al azar", list).returnValue()

    #print (returnValue)
    """
    #print (returnValue)
    institucion_uno=returnValue

    if __name__ == '__main__':
        import random
        root = Tk()
        root.geometry("0x0+0+0")
        
        
        returnValue = 0
       # list = [random.randint(1,100) for x in range(50)]
        list = l_t
        while returnValue == 0:
            returnValue = ListBoxChoice(root, "Carrera", "\nPaso 3 de 5 \nAhora elige una carrera para el estudiante a la derecha\n", list).returnValue()
            #return returnValue

    #print (returnValue)
    titulo_dos=returnValue
    lista_instituciones=listinst(titulo_dos)

    if lista_instituciones != []:
        if __name__ == '__main__':
        #import random
            root = Tk()
            root.geometry("0x0+0+0")
        
        
            returnValue = 0
       # list = [random.randint(1,100) for x in range(50)]
            list = lista_instituciones
            listaux_dos=lista_instituciones
            while returnValue == 0:
                returnValue = ListBoxChoice(root, "Institución", "\nPaso 4 de 5 \nPor ultimo, una institución para este otro estudiante", list).returnValue()

    #print (returnValue)
    institucion_dos=returnValue

    #ahora buscamos el objeto seleccionado deentrelalista de carreras

    ########################################################################
    if titulo_uno == "'1random":
        import random
        nr=random.randint(0, len(l_c)-1)
        sel_uno= l_c[nr]
    #
    elif institucion_uno=="'1random":
        import random
        nr=random.randint(0, len(listaux_uno)-1)
        institucion_uno= listaux_uno[nr]
        sel_uno=seleccionado(titulo_uno, institucion_uno)

    else:
        sel_uno=seleccionado(titulo_uno, institucion_uno)

    if titulo_dos == "'1random":
        import random
        nr=random.randint(0, len(l_c)-1)
        sel_dos= l_c[nr]
    #
    elif institucion_dos=="'1random":
        import random
        nr=random.randint(0, len(listaux_dos)-1)
        institucion_dos= listaux_dos[nr]
        sel_dos=seleccionado(titulo_dos, institucion_dos)

    else:
        sel_dos=seleccionado(titulo_dos, institucion_dos)
        
    print("izquierdo "+sel_uno.titulo+ sel_uno.institucion+ str(sel_uno.ara))
    print("derecho "+sel_dos.titulo+ sel_dos.institucion+str(sel_dos.ara))

    #Considerando Duracion en semestres, ingreso mensual, arancel anual:

    from Tkinter import *

    class ListBoxChoice(object):
        def __init__(self, master=None, title=None, message=None, list=[]):
            self.master = master
            self.value = None
            self.list = list[:]
            
            self.modalPane = Toplevel(self.master)

            self.modalPane.transient(self.master)
            self.modalPane.grab_set()

            self.modalPane.bind("<Return>", self._choose)
            
            
            
            
            if title:
                self.modalPane.title(title)

            if message:

    #LETRA PARA EL TITULO
                
                Label(self.modalPane, text=message, font=("Helvetica", "20")).pack(padx=5, pady=5)

            listFrame = Frame(self.modalPane)
            #  listFrame = Frame(self.modalPane)
          #  listFrame.pack(side=TOP, padx=5, pady=5)
          
    #ACA VA EL TAMANIO DE LA VENTANA!!! (Espaciado entre widgets)
            listFrame.pack(side=TOP, padx=50, pady=50)        
            
            scrollBar = Scrollbar(listFrame)
            scrollBar.pack(side=RIGHT, fill=Y,expand=1)
            self.listBox = Listbox(listFrame, selectmode=SINGLE)
            self.listBox.pack(side=LEFT, fill=BOTH, expand=1)
            scrollBar.config(command=self.listBox.yview)
            self.listBox.config(yscrollcommand=scrollBar.set, width=90)
            self.list.sort()
            for item in self.list:
                self.listBox.insert(END, item)

            buttonFrame = Frame(self.modalPane)
            buttonFrame.pack(side=BOTTOM)

            chooseButton = Button(buttonFrame, text="Elegir", command=self._choose,font=("Helvetica", "16"))
            chooseButton.pack()

            randomButton =Button(buttonFrame, text="Random", command=self._random)
            randomButton.pack()#(side=LEFT)

            

        def _choose(self, event=None):
            try:
                firstIndex = self.listBox.curselection()[0]
                self.value = self.list[int(firstIndex)]
            except IndexError:
                self.value = None
                #meti esto aca abajo
                self.value = "'1random"
            self.modalPane.destroy()

        def _random(self, event=None):
            self.value = "'1random"
            self.modalPane.destroy()


 
            
        def returnValue(self):
            self.master.wait_window(self.modalPane)
            return self.value











    #Paso 5de5
    ejemder=sel_dos
    ejemizq=sel_uno



    import Tkinter
    from Tkinter import *
    top= Tkinter.Tk()
    #top.geometry("0x0+0+0")
    top.geometry("6000x300+0+0")

    def start():
        top.destroy()
        top.quit()



    boton_enter = Tkinter.Button (top, text="COMPARAR",font=("Helvetica", "16"), command= start)
    boton_enter.pack(pady=50)

    """
    photo = PhotoImage(file="elsuper.gif")
    label=Label(image=photo)
    label.image=photo
    label.pack()
    """








    texto_izq=str(2*"\n"+"\t"+ejemizq.titulo+ 2*"\n"+ "\t"+ejemizq.institucion)
    label_izq= Text (top,font=("Helvetica", "10") ,relief=GROOVE, bg="gray93")
    label_izq.insert(INSERT, str(texto_izq))


    label_izq.pack(side=LEFT)



    texto_der=str(2*"\n"+"\t"+ejemder.titulo+ 2*"\n"+"\t"+ ejemder.institucion)
    label_der= Text (top,font=("Helvetica", "10") ,relief=GROOVE,bg="gray93")
    label_der.insert(INSERT, str(texto_der))
    #("Aca va el texto del derecho")
    label_der.pack(side=LEFT)




    top.mainloop()







    ###Primero Recibe los nombres, institucion, duracion ingreso y arancel de la carrera
    ####Nombre y Institucion no sirve de nada, es solo lo que usa el usuario para elegir

    ###Entonces lo primero es la deuda que va a tener distintas relaciones
    ####Primero la relacion que hay entre la deuda total de una con la otra
    #####Esto sirve para ver cuanto baja el que baja menos vs el que baja hasta abajo
    ###Definimos tambien la recuperacion de ambos monos semestral
    ####Esta recuperacion es respecto al con mayor costo

    if ejemizq.deuda()<=ejemder.deuda():
        deudader=100
        deudaizq=ejemizq.deuda()/ejemder.deuda()*100
        recizq=ejemizq.ganancia()/ejemder.deuda()*100
        recder=ejemder.ganancia()/ejemder.deuda()*100
    else:
        deudader=ejemder.deuda()/ejemizq.deuda()*100
        deudaizq=100
        recder=ejemder.ganancia()/ejemizq.deuda()*100
        recizq=ejemizq.ganancia()/ejemizq.deuda()*100

    ###Luego tenemos el tiempo que necesita cada uno para llegar a su punto mas bajo (cantidad de semestres)
    ####Entonces si los monos se mueven respecto a semestres, por cada semestre bajaran una porcion    

    porcionder=deudader/(ejemder.duracion)
    porcionizq=deudaizq/(ejemizq.duracion)

    ###Hacemos avanzar cada uno alternadamente por semestres
    llevader=1
    llevaizq=1
    ###Los fin son las metas que tienen que restar
    finder=deudader
    finizq=deudaizq

    motorder=0
    motorizq=0


    while finder >0 and finizq >0:
        if llevader<deudader:
    ###Aqui se supone que entonces baja
            llevader=llevader+porcionder
            motorder=porcionder
            ###print("derecha "+str(porcionder))
            #######################################################Aqui la variable motorder debe envier la informacion
            #Y aqui sube
        elif llevader>=deudader:
            if finder>=recder:
                finder=finder-recder
            ###print("derecha"+str(recder))
                motorder=-recder

            elif finder<recder:
                motorder=-finder
                finder=finder-recder
            #######################################################Aqui la variable motorder debe envier la informacion

        print("     "+str(motorder))    

        if llevaizq<deudaizq:
    ###Aqui se supone que entonces baja
            llevaizq=llevaizq+porcionizq
            ###print("izquierda "+str(porcionizq))
            motorizq=porcionizq
            #######################################################Aqui la variable motorizq debe envier la informacion
            #Y aqui sube
        elif llevaizq>deudaizq:
            if finizq>=recizq:
                finizq=finizq-recizq
                motorizq=-recizq

            elif finizq<recizq:
                motorizq=-finizq
                finizq=finizq-recizq

            
            ###print("izquierda "+str(recizq))
            
            #######################################################Aqui la variable motorizq debe envier la informacion
        senal_envio="c"+str(1)+"a"+str(pasos(motorizq))+"b"+str(pasos(motorder))+"n"
        print("senal enviada: ",senal_envio)
        ser.write(senal_envio)
        print("leído por arduino: ",ser.readline())
        print(motorizq)

    if finder<0:
        print("Gana DER")
    else:
        print("Gana IZQ")


    #En este momento, o el Der o Izq esta arriba, entonces tenemos que restarle lo q falta
    subirder=0
    subirizq=0
    if finder<0:
        if llevaizq<deudaizq:
            subirizq=-(llevaizq)
        elif llevaizq>=deudaizq:
            if finizq>0:
                subirizq=-(finizq)
            
            

    #Lo mismo para si izq llega primero:
    elif finizq<0:
        if llevader<deudader:
            subirder=-(llevader)
        elif llevader>=deudader:
            if finder>0:
                subirder=-(finder)
        
        
    

    senal_reset="c"+str(0)+"a"+str(pasos(subirizq)-80)+"b"+str(pasos(subirder)-100)+"n"
    print("señal enviada: ",senal_reset)
    ser.write(senal_reset)
    print("leído por arduino: ",ser.readline())

    #Las variables son:
    #       reset: Para tu reset (es un escalar independiente de que motor queras usar, si queres usar un motor especifico usas:
    #               subirizq o subirder
    #       motorder: la variable porcentual del motor derecho
    #       motorizq: la variable porcentual del motor izuierdo

    


    import Tkinter
    from Tkinter import *
    top= Tkinter.Tk()
    #top.geometry("0x0+0+0")
    top.geometry("+600+200")

    def start():
        top.destroy()
        top.quit()



    boton_enter = Tkinter.Button (top, text="RESTART",font=("Helvetica", "30"), command= start)
    boton_enter.pack(pady=50)
    top.mainloop()























    """
    #***********
    # PROGRAMA *
    #***********
    import serial
    ser=serial.Serial(puertocom,baudrate=9600)
    print(ser.name)
    seleccion=[sel_uno.nombre(),sel_dos.nombre()]
    print("escogiste: \n"+str(seleccion[0][0])+" en "+str(seleccion[0][1])+"\n"+str(seleccion[1][0])+" en "+str(seleccion[1][1]))

    print(steps(sel_uno,sel_dos))
    #[[steps caida1, tiempo caida1, steps subida1, tiempo subida1],[steps caida2, tiempo caida2, steps subida2, tiempo subida2]])
    mono1=steps(sel_uno,sel_dos)[0]
    mono2=steps(sel_uno,sel_dos)[1]
    senal_envio="d"+str(mono1[1])+"s"+str(mono1[0])+"u"+str(mono1[3])+"z"+str(mono1[2])
    senal_envio2="e"+str(mono2[1])+"t"+str(mono2[0])+"v"+str(mono2[3])+"y"+str(mono2[2])
    print(senal_envio)
    print(senal_envio2)
    senal_sumada=senal_envio+senal_envio2
    ser.write(senal_sumada)
    #senal_final=bytes(senal_sumada, 'utf-8')
    #ser.write(senal_final)
    #print(senal_final)
    print(senal_sumada)
    """
