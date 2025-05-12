# Fórmula velocidad de escape:
# 𝑉e = raíz(2*g*r)

# importa libreria math
import math

#solicitud de inputs
radio = float(input("Ingrese radio del planeta en kilómetros:\n>"))
g = float(input("ingrese la constante aceleración de gravedad g en m/s^2:\n>"))

# cálculo velocidad de escape de planeta Tierra
vel_escape = math.sqrt(2*g*radio*1000)

# imprimir velocidad de escape
print(f"la velocidad de escape es : {vel_escape:.1f}","m/s")