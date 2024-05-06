# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:38:29 2024

@author: juger
"""

archivo = open ("archivo_de_prueba.txt","wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a Villa el Salvador."
archivo.write(contenido)
archivo.close()
