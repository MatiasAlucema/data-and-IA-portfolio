import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_data(num_records=5000):
    """
    Genera un dataset sintético de permisos de circulación con errores intencionales.
    
    Args:
        num_records (int): Número de registros a generar.
    
    Returns:
        pd.DataFrame: DataFrame de pandas con los datos generados.
    """
    
    # Lista de posibles valores
    tipos_vehiculo = ['Coche', 'Moto', 'Camion', 'Furgoneta', 'Bicicleta', 'Monopatin']
    zonas = ['Zona A', 'Zona B', 'Zona C', 'Zona D']
    
    # Generar datos limpios
    data = {
        'id_permiso': np.arange(1, num_records + 1),
        'tipo_vehiculo': np.random.choice(tipos_vehiculo, num_records),
        'fecha_emision': [datetime.now() - timedelta(days=np.random.randint(1, 365)) for _ in range(num_records)],
        'duracion_dias': np.random.randint(1, 30, num_records),
        'zona_circulacion': np.random.choice(zonas, num_records),
        'estado': np.random.choice(['Activo', 'Inactivo'], num_records, p=[0.8, 0.2])
    }
    df = pd.DataFrame(data)
    
    # --- Introducir Errores y Valores Faltantes intencionalmente ---
    
    # 1. Valores faltantes
    df.loc[df.sample(frac=0.05).index, 'duracion_dias'] = np.nan
    df.loc[df.sample(frac=0.02).index, 'zona_circulacion'] = np.nan
    
    # 2. Inconsistencias de formato
    df.loc[df.sample(frac=0.03).index, 'tipo_vehiculo'] = df['tipo_vehiculo'].str.upper()
    df.loc[df.sample(frac=0.02).index, 'tipo_vehiculo'] = 'coche ' # Espacio en blanco
    df.loc[df.sample(frac=0.01).index, 'tipo_vehiculo'] = 'OTRO' # Categoría no esperada
    
    # 3. Datos incorrectos o fuera de rango
    df.loc[df.sample(frac=0.02).index, 'duracion_dias'] = -10 # Duración negativa
    df.loc[df.sample(frac=0.01).index, 'fecha_emision'] = '2025-25-50' # Fecha inválida
    
    # 4. Duplicados
    df_duplicados = df.sample(frac=0.01).copy()
    df = pd.concat([df, df_duplicados], ignore_index=True)
    
    return df

if __name__ == '__main__':
    df = generate_synthetic_data(num_records=5000)
    # Crea el directorio 'data/raw' si no existe
    import os
    os.makedirs('data/raw', exist_ok=True)
    
    file_path = 'data/raw/permisos_circulacion_bruto.csv'
    df.to_csv(file_path, index=False)
    print(f"Dataset sintético creado en: {file_path}")
    print(f"Total de registros generados: {df.shape[0]}")