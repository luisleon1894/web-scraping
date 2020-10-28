# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:30:54 2020

@author: Sergi, Luis
"""

from webscrapingclass import WebScrapingMustang
from urllib.request import urlopen

#Inicializamos la clase donde que contendrá los métodos necesarios
ws = WebScrapingMustang()

# Download HTML
url = "https://www.mustang.es/es/"
html = ws.download_html(url)

# Get the names and links of navmenu
navmenu = ws.get_nav_menu(html)

def __menu():
    while True:
        print("\n\n--------------Menú-------------------")
        print("Que desea hacer: \n" +
          "- Opción 1: Mostrar los productos de una página en concreto\n" +
          "- Opción 2: Mostrar todos los productos\n" +
          "- Opción 3: Guardar en formato csv la información de todos los productos\n" + 
          "- Opcion 4: Volver a escoger una categoria\n" +
          "- Opción 5: Salir\n")
        while True:
            respuesta = int(input("Selecciona una opción: \n"))
            if (0 < respuesta < 6): break
            print("Error! Opción no válida\n")
        print("Cargando petición...")
        if (respuesta == 1):
            if (enlaces):
                while True:
                    respuestaPag = int(input("Introduce una página válida. (Páginas disponibles 1 - " + str(len(enlaces)-1) + ")\n"))
                    if (respuestaPag < len(enlaces) and 0 < respuestaPag): 
                        print("Mostramos los productos de la página: " + str(respuestaPag) + "\n")
                        break
                    print("Error! Página no válida\n")
            else: print("Solo hay disponible una única página\n")
            productos = ws.get_productos(enlaces[respuestaPag-1] if enlaces else link_scraping) #primera página
            print(productos)
        elif (respuesta == 2):
            todos_productos = ws.get_productos(enlaces[len(enlaces) - 1] if enlaces else link_scraping) #última página
            print("Mostramos todos productos\n")
            print(todos_productos)
        elif (respuesta == 3):
            if (not ws.data):
                print("Para poder guardar los productos en un csv, primero se deben mostrar usando la opción 1 o 2")
                continue
            filename = input("Por favor introducir nombre del fichero\n")
            ws.data2csv(filename)
        elif (respuesta == 4):
            return "repetir"
        else: # #♥respuesta == 5
            print("Muchas gracias! Hasta la próxima!\n")    
            return "exit"




while True:

    # Entrar categoría que se quiere hacer scraping
    link_scraping = ws.read_category(navmenu)
    
    print("Cargando categoria seleccionada...")
    html_category = ws.download_html(link_scraping)
    
    # Obtener los enlaces de la paginación de la categoria
    enlaces = ws.get_links_pagination(html_category, [])
    
    resultado = __menu()
    
    if(resultado == "exit"):
        break;

