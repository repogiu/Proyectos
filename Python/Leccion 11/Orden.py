from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos) # conversion a una lista (se asigna los productos a una lista)

    def agregar_producto(self, producto):
        self._productos.append(producto)  # Esto es para agregar un nuevo producto

    def calcular_total(self):
        total = 0  # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self): # muestra la lista de producto cuando creamos el objeto
        productos_str = '' # lista vacia
        for producto in self._productos:
            productos_str += producto.__str__() + '|' # concatenamos cada producto en la lista vacia separados con el operador py
        return f'Orden: {self.id_orden}, \nProducto: {productos_str}' # se concatena al metodo str de la clase producto


if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00) # aqui nos pide que importemos la clase producto
    producto2 = Producto('Pantalon', 150.00)

    productos1 = [producto1, producto2]  # Lista de productos
    orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos, genera el numero de orden
    print(orden1) # imprime la lista de productos1
    orden2 = Orden(productos1)
    print(orden2)
# Tarea: Modificar la orden2, ingresando nuevos productos con sus nombres y precios
# crear una nueva lista de productos y agregarla a la orden2