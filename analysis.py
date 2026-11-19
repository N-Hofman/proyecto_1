import json 

def data(arch):
        with open(arch, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos['ventas']
        return []

def facturado(ventas):
    total = 0
    for venta in ventas:
        total += venta['cantidad'] * venta['precio_unitario']
    return total
print("Total facturado:", facturado(data('data.json')))

def ventas_tipo(ventas):
    tipo = {}
    for venta in ventas:
        x = venta['categoria']
        total= venta['precio_unitario'] * venta['cantidad']
        if x in tipo:
            tipo[x] += total
        else:
            tipo[x] = total
            
    return tipo
print("Ventas de cada tipo:", ventas_tipo(data('data.json')))

def mas_vendido(ventas):
    productos = {}
    for venta in ventas:
        x = venta['producto']
        y = venta['cantidad']
        
        if x in productos:
            productos[x] += y
        else:
            productos[x] = y
    producto= max(productos, key=productos.get)
    maximo = productos[producto]
    
    return producto, maximo
print("El producto más vendido es:", mas_vendido(data('data.json')))
