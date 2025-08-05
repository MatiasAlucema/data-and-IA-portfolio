# Proyecto Integral de Data Science: Gobernanza y Análisis Predictivo de Permisos de Circulación

### Resumen del Proyecto

Este repositorio documenta un proyecto de principio a fin en el campo de la ciencia de datos, diseñado para demostrar mi experiencia en el ciclo de vida completo del análisis y modelado de datos. El proyecto aborda desafíos comunes del mundo real, como la mala calidad de los datos y el desbalance de clases, para construir un modelo predictivo robusto.

A través de un dataset sintético de permisos de circulación, el proyecto valida mis habilidades clave en:
* **Ingeniería de Datos:** Gestión, limpieza y estandarización de grandes volúmenes de datos.
* **Análisis Exploratorio de Datos (EDA):** Extracción de insights valiosos y visualización de tendencias.
* **Machine Learning:** Desarrollo de modelos de clasificación y su evaluación crítica.
* **Resolución de Problemas:** Diagnóstico de fallos de modelos (ej. desbalance de clases) y aplicación de técnicas avanzadas (ej. SMOTE).

### Estructura del Repositorio

* `data_generation.py`: Script para generar el dataset sintético con errores intencionales.
* `02_data_validation_cleaning.ipynb`: Documenta el proceso de limpieza y estandarización del dataset.
* `03_feature_engineering_modeling.ipynb`: Contiene el desarrollo del modelo, incluyendo la ingeniería de características y la resolución del problema de desbalance de clases.
* `04_exploratory_analysis.ipynb`: Presenta un análisis detallado de los datos limpios a través de visualizaciones.
* `requirements.txt`: Lista de todas las librerías necesarias para replicar el entorno de trabajo.

### Metodología y Flujo de Trabajo

1.  **Ingesta y Limpieza de Datos:** El proceso comenzó con la generación de un dataset con errores. Se utilizó Python (`pandas`) para limpiar los datos, manejar valores nulos, estandarizar formatos y corregir inconsistencias, asegurando un dataset de alta calidad.
2.  **Análisis de Datos:** Se llevó a cabo un EDA exhaustivo, visualizando la distribución de permisos por tipo de vehículo y zona, así como las tendencias de emisión a lo largo del tiempo.
3.  **Modelado Predictivo:** Se entrenó un `RandomForestClassifier` para predecir el estado de un permiso. Los resultados iniciales mostraron una **precisión general alta (79%)** pero una **incapacidad total para predecir la clase minoritaria ("Inactivo")**.
4.  **Solución al Desbalance de Clases:** Se diagnosticó un severo desbalance de clases y se aplicaron dos técnicas de corrección:
    * **Ponderación de Clases:** Esta técnica falló, con el modelo aún incapaz de predecir la clase minoritaria.
    * **Sobremuestreo (SMOTE):** Esta técnica fue exitosa. Creó datos sintéticos de la clase minoritaria, lo que permitió que el modelo aprendiera de manera efectiva.

### Resultados y Conclusiones Finales

El proyecto culmina con un modelo final que equilibra de manera efectiva la capacidad predictiva.

* **Modelo con SMOTE:**
    * **Precisión General (Accuracy):** 77.07% (ligeramente menor, pero más honesta).
    * **Recall (Clase "Inactivo"):** 0.06 (una mejora del 600% sobre el modelo inicial).
    * **Matriz de Confusión:** El modelo logró identificar correctamente 12 permisos inactivos, una mejora significativa con respecto a los 3 del modelo original y 1 del modelo con ponderación de clases.

**Conclusión:** Aunque la precisión general fue ligeramente inferior, el modelo con SMOTE es el más útil y robusto. La mejora sustancial en el `recall` para la clase "Inactivo" demuestra que el modelo ha aprendido a detectar casos raros, una habilidad crucial para la detección de fraudes, el análisis de riesgos u otras aplicaciones del mundo real.

### Discusión: Del Ejercicio a la Aplicación Real

El problema de predecir el estado de un permiso se usó para ilustrar habilidades técnicas. En un contexto empresarial, una tarea más valiosa sería predecir la **probabilidad de que un permiso genere una infracción** o que sea **fraudulento**. Este proyecto demuestra la capacidad para abordar problemas de datos y aplicar soluciones técnicas de manera estratégica.

### Tecnologías Utilizadas

* Python
* Pandas / Numpy
* Scikit-learn
* Matplotlib / Seaborn
* Imbalanced-learn
* Jupyter Notebooks

### Cómo Ejecutar el Proyecto

1.  Clona el repositorio en tu máquina local.
    ```bash
    git clone https://github.com/MatiasAlucema/data-and-IA-portfolio.git
    ```
2.  Instala todas las librerías necesarias.
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecuta el script de generación de datos.
    ```bash
    python data_generation.py
    ```
4.  Abre los Jupyter Notebooks en orden para seguir el flujo de trabajo (`02`, `04`, `03`) y recrear el análisis y los resultados.
    ```bash
    jupyter notebook
    ```
