# Fórmula utilidades:
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺T

# importa libreria math
import math

#solicitud de inputs
p = float(input("Ingrese precio de suscripción:\n>"))
u_normales = int(input("Ingrese número de usuarios normales:\n>"))
gt = float(input("Ingrese gasto total:\n>"))
util_anterior = float(input("ingrese utilidad de año anterior:\n"))

# cálculo de utilidad actual
util_actual = float(p*u_normales-gt)

# cálculo de razon de utilidades
razon = float(util_actual/util_anterior)

print(f"la utilidad actual es : {util_actual:.2f}")
print(f"la utilidad anterior es : {util_anterior:.2f}")
print(f"la razón de utilidad actual/anterior es : {razon:.2f}")