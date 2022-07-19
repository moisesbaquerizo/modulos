from empresa import Empresa
from Muestra import  Mostrar, Detalle
from usuario import Cliente, Coach
from interface import RutinaCliente, RutinaCoach
from helpers import Helper
import os

helper = Helper()
lista = ["1) Coach ","2) Cliente ","3) Salir"]
opcion = ""
while opcion !="3":
  os.system("cls")
  opcion =helper.menu(lista, "USUARIOS")
  os.system("cls")
  if opcion == '2':
    opc1 = ""
    while opc1 != '2':
      os.system("cls")
      print("▣"*40,"MODULOS","▣"*40)
      opc1 = helper.menu(["1) Rutinas", "2) Salir"], "MODULOS")
      os.system("cls")
      if opc1 == "1":
        print("▣"*40,"RUTINAS","▣"*40)
        emp1= Empresa("0988691612", "Somos más", "0835363232", "guayaquil", "Mbaquerizop@gmail.com")
        usu = Cliente("moises", "0929608511", "0990255359","moisesbaquerizo098@gmail.com","Milagro", "001", True)
        mos = Mostrar(usu, "Cliente")
        mos.agregarDetalle("mancuernas", "20 minutos", "4 series")
        mos.agregarDetalle("sentadillas", "20 minutos", "4 series")  
        mos.agregarDetalle(nombre, tiempo, serie)
        mos.mostrarInfo(emp1.razonsocial, emp1.ruc)
        input("\n"
          "Presiona una tecla para continuar:)")
      elif opc1 == "2":
        input("Saliendo..." 
            "\n" "Presione una tecla para continuar...")
        break
  
  elif opcion == '1':
    opc1 = ""
    while opc1 != '3':
      os.system("cls")
      print("▣"*40,"MODULOS","▣"*40)
      opc1 = helper.menu(["1) Rutinas","2) Añadir Rutina" ,"3) Salir"], "MODULOS")
      os.system("cls")
      if opc1 == "1":
        print("▣"*40,"RUTINAS","▣"*40)
        emp1= Empresa("0988691612", "Somos más", "0835363232", "guayaquil", "Mbaquerizop@gmail.com")
        usu = Coach("moises", "0929608511", "0990255359","moisesbaquerizo098@gmail.com","Milagro", "001", True)
        mos = Mostrar(usu, "Coach") 
        mos.agregarDetalle("mancuernas", "20 min", "4 series")
        mos.agregarDetalle("sentadillas", "20 min", "4 series")
        mos.agregarDetalle(nombre, tiempo, serie)
        mos.mostrarInfo(emp1.razonsocial, emp1.ruc)
        input("\n"
          "Presiona una tecla para continuar:)")
      elif opc1 == "2":
        print("▣"*40,"AÑADIR RUTINAS","▣"*40)
        nombre =input("Ingrese nombre de rutina: ")
        tiempo =input("Ingrese tiempo de rutina: ")
        serie =input("Ingrese serie de rutinas: ")
        usu = Coach("moises", "0929608511", "0990255359","moisesbaquerizo098@gmail.com","Milagro", "001", True)
        usu = Mostrar(usu, "Coach")
        usu.agregarDetalle(nombre, tiempo, serie)
      elif opc1 == "3":
        input("Saliendo..." 
            "\n" "Presione una tecla para continuar...")
        break
  
  elif opcion == "3":
    print("¡Gracias por visitarnos!")