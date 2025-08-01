# Proyecto: Gobernanza y Análisis de Datos de Permisos de Circulación

### Resumen del Proyecto

Este proyecto demuestra mi experiencia en la **gobernanza y calidad de datos**, aplicando un enfoque riguroso para la validación, limpieza y estandarización de grandes volúmenes de información. A través de un dataset sintético de permisos de circulación, simulo un proceso real de gestión de datos para asegurar su integridad y consistencia, preparándolo para análisis avanzados y la toma de decisiones estratégicas.

El proyecto valida las siguientes habilidades clave:
* **Gestión de la Calidad de Datos:** Identificación y corrección de inconsistencias, valores faltantes y errores de formato.
* **Estandarización de Datos:** Unificación de formatos de texto y valores para garantizar la consistencia.
* **Preparación de Datos:** Transformación de datos brutos en datasets limpios y confiables, listos para análisis.

### Estructura del Repositorio

* `data_generation.py`: Script de Python para generar un dataset sintético de 5000 registros, incluyendo errores y inconsistencias intencionales para simular datos del mundo real.
* `02_data_validation_cleaning.ipynb`: Un Jupyter Notebook que detalla todo el proceso de **validación y limpieza de datos**. Aquí se muestra paso a paso cómo se detectaron y corrigieron los problemas del dataset, culminando en un conjunto de datos limpio y confiable.
* `README.md`: Este documento que describe el proyecto, su metodología y cómo ejecutarlo.

### Metodología

El flujo de trabajo sigue las mejores prácticas en el ciclo de vida de la calidad de datos:

1.  **Generación de Datos Brutos:** Se utiliza un script de Python (`data_generation.py`) para crear un dataset inicial que representa los desafíos comunes en los datos de permisos de circulación (duplicados, valores nulos, formatos inconsistentes, etc.).
2.  **Auditoría y Validación:** A través del notebook, se realiza una inspección exhaustiva de los datos para identificar la magnitud de los problemas de calidad.
3.  **Proceso de Limpieza:** Se aplican técnicas de `pandas` y `numpy` para:
    * Eliminar filas duplicadas.
    * Manejar valores faltantes mediante estrategias de imputación.
    * Estandarizar formatos de texto y corregir errores tipográficos.
    * Corregir valores numéricos fuera de rango.
4.  **Verificación y Almacenamiento:** Se valida el resultado de la limpieza y se guarda el dataset limpio en un nuevo archivo, listo para su uso.

### Próximos Pasos (Opcional)

Este proyecto puede ser ampliado para incluir:
* **Análisis Exploratorio de Datos (EDA):** Generar visualizaciones e insights a partir del dataset limpio.
* **Modelado Predictivo:** Utilizar el dataset limpio para entrenar un modelo de Machine Learning que prediga la probabilidad de una infracción.
* **Ingeniería de Datos:** Crear un script de `ETL (Extract, Transform, Load)` más robusto para automatizar el proceso de limpieza.

### Tecnologías Utilizadas

* Python
* Pandas
* Numpy
* Jupyter Notebooks

### Cómo Ejecutar el Proyecto

1.  Clona este repositorio:
    `git clone https://github.com/MatiasAlucema/data-and-IA-portfolio.git`
2.  Instala las dependencias:
    `pip install -r requirements.txt`
3.  Ejecuta el script para generar los datos brutos:
    `python data_generation.py`
4.  Abre el Jupyter Notebook para ver el proceso de limpieza:
    `jupyter notebook 02_data_validation_cleaning.ipynb`

