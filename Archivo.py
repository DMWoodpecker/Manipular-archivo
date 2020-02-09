import re
class Archivo:
    def __init__(self,nombre):
        self.f= open("C:\\Users\\Fernando\\Desktop\\Prueba.txt", "rt")
        self.nombre="C:\\Users\\Fernando\\Desktop\\Prueba.txt"
    def __del__(self):
        self.f.close()
    def muestra(self):
        i=1
        for linea in self.f:
            s="{:3} {}".format(i,linea)
            print(s)
            i+=1
        self.f.seek(0)
    def cuentaVocales(self):
        cadena1= self.f.read()
        contadorvocales=0
        for i in cadena1:
            if(i=='A' or i=='a' or i=='á'or i=='E' or i=='e' or i=='é' or i=='I' or i=='i' or i=='í' or i=='O' or i=='o' or i=='ó' or i=='U' or i=='u' or i=='ú'):
                contadorvocales+=1
        print("La cantidad de vocales es :",contadorvocales)
    def cuentaPalabras(self):
        self.f=open("C:\\Users\\Fernando\\Desktop\\Prueba.txt", "rt")
        cadena2=self.f.read()
        numeropalabras=0
        np=cadena2.split()
        npalabras=len(np)
        print("Cantidad de palabras:",npalabras)
    def cuentaConsonantes(self):
        self.f=open("C:\\Users\\Fernando\\Desktop\\Prueba.txt", "rt")
        cadena3=self.f.read()
        nc=0
        for i in cadena3:
            if i in set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"):
                nc+=1
        print("La cantidad de consonantes es:",nc)
    def cuentaLineas(self):
        self.f=open("C:\\Users\\Fernando\\Desktop\\Prueba.txt", "rt")
        cadena4=self.f.readlines()
        nl=0
        for linea in cadena4:
            nl+=1
        print("La cantidad de lineas es:",nl)


        """def cVocales(s):
            cv=0
            for i in range(len(s)):
                if s[i].lower() in set("aeiouáéíóú"):
                    cv+=1
            return cv
            c=0
            for linea in self.f:
                c+=cVocales(s)
            self.f.seek(0)
            return c
            print(s)"""
x=Archivo("Prueba.txt")
y=Archivo("dos.txt")
x.muestra()
x.cuentaVocales()
x.cuentaPalabras()
x.cuentaConsonantes()
x.cuentaLineas()
print(x.nombre)