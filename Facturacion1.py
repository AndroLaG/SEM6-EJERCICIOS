# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:38:56 2024

@author: juger
"""

# Dado el subtotal, calcular el IGV y el total

import financieros
subtotal = 1000.49
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal):.2f}")
