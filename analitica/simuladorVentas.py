import random
from datetime import datetime,timedelta

def generar_ventas(numeroVentas):
    
   
    productos=[
        {"nombre":"Camisa Polo de Hombre Slim Fit Manga Corta con Textura Bordado de Pato en Algodón","precio":150000,"descuento":False},
        {"nombre":"Camisa Polo de Hombre Classic Fit Cuello Nerú Manga Corta Textura Piqué Jacquard en Algodón","precio":200000,"descuento":False},
        {"nombre":"Camisa Polo de Hombre Slim Fit Cuello Nerú Manga Corta Sesgos en Contraste en Mezcla de Algodón","precio":110000,"descuento":True},
        {"nombre":"Camisa Polo de Hombre Classic Fit Manga Larga Varsity con Cierre Efecto Desgaste en Algodón","precio":205000,"descuento":False},
        {"nombre":"Camiseta Polo M/C","precio":98000,"descuento":False},
        {"nombre":"Jean de Hombre Skinny Fit Tiro Medio Lavado Oscuro Clásico con Raspones en Mezcla de Algodón Famous","precio":490000,"descuento":False},
        {"nombre":"Jean de Hombre Rider Skinny Fit Tiro Bajo Lavado Medio Rotos Detalles en Costuras en Mezcla de Algodón","precio":357000,"descuento":True},
        {"nombre":"Chaqueta de Hombre Bomber Acolchada Rombos y Gráficos Bordados en Mezcla de Algodón y Poliéster","precio":1500000,"descuento":False},
        {"nombre":"Chaqueta de Hombre Doble Faz Cuello Alto Windbreaker Bolsillo Canguro en Mezcla de Algodón y Poliéster","precio":680000,"descuento":False},
        {"nombre":"Chaqueta Tipo Trucker en Denim para Hombre","precio":820000,"descuento":False}
    ]

    
    tallas=["XS","S","M","L","XL","XXL","XXXL"]

    
    
    vendedores=["Carol Serna","Juliana Saldarriaga","Esteban Mejia","Arley Ramirez","Stiven Lopera","Carlos Mora","Daniela Sevilla","Andres Villegas"]

    fechaInicio=datetime(2026,1,2)

    ventas=[]
    for _ in range(numeroVentas):
        producto = random.choice(productos)
        cantidad = random.randint(1, 5)
        fecha = fechaInicio + timedelta(days=random.randint(0, 60))

        venta = {
            "producto": producto["nombre"],
            "precioUnitario": producto["precio"],
            "talla": random.choice(tallas),
            "cantidad": cantidad,
            "vendedor": random.choice(vendedores),
            "fecha": fecha.strftime("%Y-%m-%d"),   
            "total": cantidad * producto["precio"]
        }
        ventas.append(venta)

        #Inyectando errores de calidad 
     

    return ventas