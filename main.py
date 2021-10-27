class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color == "rojo"):
            self.color = color
        elif (color == "verde"):
            self.color = color
        elif (color == "amarillo"):
            self.color = color
        elif (color == "negro"):
            self.color = color
        elif (color == "blanco"):
            self.color = color
        else:
            pass    

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro): 
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cont = 0
        if (self.asientos != []):
            for asiento in self.asientos:
                if(type(asiento)==Asiento):
                    cont += cont
        return cont            

    def verificarIntegridad(self):
        check = "Auto original"
        if (self.motor.registro != self.registro):
            check = "Las piezas no son originales"
        for asiento in self.asientos:
            if (asiento != None):
                if (asiento.registro != self.registro):
                    check = "Las piezas no son originales"
                    break
        return check        


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo == "electrico"):
            self.tipo = tipo
        elif (tipo == "gasolina"):
            self.tipo = tipo
        else:
            pass              

