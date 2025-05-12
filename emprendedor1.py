# Fórmula utilidades:
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺T

# importa libreria math
import math

#solicitud de inputs
p = float(input("Ingrese precio de suscripción:\n>"))
u = int(input("Ingrese número de usuarios:\n>"))
gt = float(input("Ingrese gasto total:\n>"))

# cálculo de utilidades
utilidades = float(p*u-gt)

print(f"la utilidad es : {utilidades:.1f}")