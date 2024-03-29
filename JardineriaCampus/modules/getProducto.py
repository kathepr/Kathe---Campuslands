from tabulate import tabulate
import requests
import json
import os

#FUNCION 1:
# Devuelve listado con todos los productos que pertenecen a gama Ornamentales
# Que tienen más de 100 unidades en stock
# Listado debe estar ordenado pro precio de venta0
# Mostrar en primer lugar los de mayor precio.
def getAllProducto():
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = json.loads(peticion.text)
    return data


def getProductoCodigo(id):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    data = json.loads(peticion.text)
    return data
    



def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in getAllProducto():
        if val.get("gama") == gama and val.get("cantidadEnStock") >= stock:
                condiciones.append(val)
    def price(val):
        return val.get("precio_venta")    
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidadEnStock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones



def menu():
    
    while True: 
        print("""

                                *****************************
                                    Reportes de Productos
                                *****************************
    0. Regresar al menú principal     
    1. Obtener todos los productos de una categoría ordenando sus precios de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100)

    """)

        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion == 0 or opcion == 1:
                if(opcion == 1):
                    gama = input("Ingrese la gama que deseas filtrar: ")
                    stock = int(input("Ingrese las unidades que seas mostrar: "))
                    print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="rounded_grid"))
                elif(opcion == 0):
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")

        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            

    
