import pandas as pd

def crear_dataframe(lista):
    return pd.DataFrame(lista)

def inspeccionar(df):
    print(df.head())
    print(df.info())
    print(df.describe())