import pandas as pd
from analitica.analisis import crear_dataframe, inspeccionar
from analitica.simuladorVentas import generar_ventas 


ventas = generar_ventas(10)

df = crear_dataframe(ventas)

inspeccionar(df)
