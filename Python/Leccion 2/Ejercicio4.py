# Ejercicio 4: Etapas de Vida
edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad < 10: #Sintaxis simplificada
    mensaje = "La infancia es increible y  bella"
elif 10 <= edad < 20:
    mensaje = "Tienes mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad < 40:
    mensaje = "Adulto"
else:
    mensaje = "Error, etapa no reconocida"
print (f"Tu edad es {edad}, {mensaje} ")
