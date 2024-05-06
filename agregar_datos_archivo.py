# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:41:16 2024

@author: juger
"""

archivo = open("noticia.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: Wikipedia"

archivo.write(contenido)

archivo.close()
