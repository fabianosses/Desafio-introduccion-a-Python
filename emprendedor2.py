# Fórmula utilidades:
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺T

# importa libreria math
import math

#solicitud de inputs
p = float(input("Ingrese precio de suscripción:\n>"))
u_normal = int(input("Ingrese número de usuarios normal:\n>"))
u_premium = int(input("Ingrese número de usuarios premium:\n>"))
gt = float(input("Ingrese gasto total:\n>"))

# cálculo de utilidades
utilidades = float((p*u_normal)+(p*1.5*u_premium)-gt)

print(f"la utilidad es : {utilidades:.1f}")