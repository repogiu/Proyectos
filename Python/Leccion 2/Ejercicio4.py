# Ejercicio 4: Etapas de Vida
# Hacer un programa que cuando el usuario ingrese su edad imprima
# la etapa de vida en una breve oracion
# 0 a 10 = La infancia es increible y bella
# 10 a 19 = Tienes muchos cambios, mucho que estudiar
# 20 a 29 = Amor y comienza el trabajo

edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad < 10: # Sintaxis simplificada
    mensaje = "La infancia es increible y  bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad < 40:
    mensaje = "Eres Adulto"
else:
    mensaje = "Error, etapa no reconocida"
print (f"Tu edad es {edad}, {mensaje} ")
