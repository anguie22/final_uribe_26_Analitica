def generar_csv(df, ruta):
    df.to_csv(ruta, index=False)

def generar_json(df, ruta):
    df.to_json(ruta, orient="records", indent=4, force_ascii=False)