from Persona import * # si ponemos Persona en vez de * no se estaria importando la clase empleado

persona1 = Persona('Osvaldo', 40)
print(persona1) # nos muestra el espacio en memoria, para ello definimos un metodo de sobreescritura en la clase padre (persona), el metodo str

empleado3 = Empleado('Pablo', 23, 57000)
print(empleado3) # nos muestra el metodo dunder str de la clase empleado