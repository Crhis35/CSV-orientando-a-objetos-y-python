
class Alumno:
    dict = {}   #Se crea un diccionario vacio
    data = []    #Se crea un conjunto vacio para almacenar los datos
    names = []   #Se crea un conjunto vacio para almacenar los nombres
    notasf = []   #Se crea un conjunto vacio para almacenar las notas
    notam = []
    al = []
    it = dict.items()
    vl = dict.values()
    ky = dict.keys()
    a=0
    b = 0
    c = 0
    d = 0
    e = 0
    def __init__(self):
        self.a=0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.pde = []
        self.file = open('Practicas/datos.csv',mode='r')
        self.dict = {}   #Se crea un diccionario vacio
        self.data = []    #Se crea un conjunto vacio para almacenar los datos
        self.names = []   #Se crea un conjunto vacio para almacenar los nombres
        self.notasf = []   #Se crea un conjunto vacio para almacenar las notas
        self.notam = []
        self.al = []    
        self.it = self.dict.items()
        self.vl = self.dict.values()
        self.ky = self.dict.keys()
    def mayor(self):
        #file = open('datos.csv', mode='r') #Se abren el archivo con los datos en modo de lectura y los toma file
        for line in self.file:    #Se utiliza un ciclo for para ir tomando los valores de file
            x = line.strip().split(',')  #Se separan los datos
            self.data.append(x)               #Se le agregan los datos al conjunto data
        for i in range(len(self.data)):   #Se utiliza un ciclo for para obtener las claves y valores
            self.names = self.data[i][0:3]     #name toma las claves que se le da
            self.notas = self.data[i][3:]      #notas toma los valores que se le da
            self.dict[tuple(self.names)] = list(self.notas)
        for k,v in self.it: #Se utiliza un ciclo for para tomar las claves y valores
        #print("El estudiante {0} {1} con el codigo {2} sus notas son {3}".format(k[1],k[2],k[0],v)) #Se imprime la clave y valores organizados
            self.notas = (float(v[0])*0.25)+(float(v[1])*0.25)+(float(v[2])*0.2)+(float(v[3])*0.3)
            self.dict[k] = self.notas
            self.notasf.append(self.notas)
        for t in range(len(self.notasf)):
            for x in range(len(self.notasf)-1):
                if self.notasf[x]< self.notasf[x+1]:
                    aux = self.notasf[x]
                    self.notasf[x] = self.notasf[x+1]
                    self.notasf[x+1] = aux
        for k1,v1 in self.it:
            if self.notasf[0] == v1:
                self.notasm = v1
                self.al = k1
        return self.notasf,self.al,self.dict,self.notas
    def menor(self):
        for k2,v2 in self.it:
            if self.notasf[len(self.notasf)-1] == v2:
                self.notasm2 = v2
                self.al2 = k2
        return self.notasm,self.al2
    def categoria(self):
        for y in self.vl:
            if y < 3:
                self.a+=1
            else:
                if y >= 3 and y < 3.4:
                    self.b+=1
                else:
                    if y >= 3.5 and y < 4:
                        self.c+=1
                    else:
                        if y >= 4 and y < 4.5:
                            self.d+=1
                        else:
                            if y >=4.5 and y==5:
                                self.e+=1
        return self.a,self.b,self.c,self.d,self.e
    def ordenar(self):
        for i1 in range(len(self.notasf)-1,0,-1):
            for i2 in range(i1):
                if self.notasf[i2]> self.notasf[i2+1]:
                    aux = self.notasf[i2]
                    self.notasf[i2] = self.notasf[i2+1]
                    self.notasf[i2+1] = aux

        for i3 in self.notasf:
            for i4 in range(len(self.data)):
                PDE=(float(self.data[i4][3])*0.25)+(float(self.data[i4][4])*0.25)+(float(self.data[i4][5])*0.2)+(float(self.data[i4][6])*0.3)    #sacar el promedio del estudiante actual
                if PDE == i3:
                    print("El estudiante", accion.data[i4][2],"con las notas",accion.data[i4][3],accion.data[i4][4],accion.data[i4][5],accion.data[i4][6],"tiene un promedio de",PDE)
    def menu(self):
        print("--------------------------- \nBienvenido Usuario \n1. Para la mayor nota. \n2. Para la menor nota. \n3. Para imprimir la categoria de los estudiantes segun las notas")
        op = int(input("Digite un numero: "))
        if op == 1:
            print("El estudiante {0}{1} de codigo {2} saco la mayor nota, su nota fue {3}.".format(accion.al[1],accion.al[2],accion.al[0],accion.notasm))
        elif op == 2:
            print("El estudiante {0} {1} de codigo {2} saco la menor nota.".format(accion.al2[1],accion.al2[2],accion.al2[0]))
        elif op == 3:
            print("Deficiente: {0} \nRegular: {1} \nAceptable: {2} \nBueno: {3} \nExcelente: {4}".format(accion.a,accion.b,accion.c,accion.d,accion.e))
        elif op == 4:
            accion.ordenar() 
        else:
            print("Error")
            accion.menu()
        co = "si"
        while co == "si":
            co = str(input("Desea continuar ingrese 'si' o 'no': "))
            if co == "si":
                accion.menu()
            else:
                print("Bye")

accion = Alumno()
accion.mayor()
accion.menor()
accion.categoria()
accion.menu()
