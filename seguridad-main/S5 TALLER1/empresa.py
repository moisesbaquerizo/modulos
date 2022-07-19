class Empresa:
    def __init__(self,ruc, nombre, telf, dirc, correo):
        self.ruc = ruc
        self.razonsocial = nombre
        self.telf = telf
        self.dirc = dirc
        self.correo = correo

if __name__ == "__main__":
    emp1 = Empresa("0988691612", "Somos más", "0835363232", "guayaquil", "Mbaquerizop@gmail.com")
    print(emp1.razonsocial, emp1.ruc)