# NVIDIA Historical Data Collector

Este proyecto esta orientado a automatizar la recolección continua de datos históricos del comportamiento bursátil de NVIDIA Corporation. Se implementa un sistema que extrae datos desde Yahoo Finance, los limpia, almacena en una base de datos SQLite y los exporta a un archivo CSV versionado, todo bajo un entorno de ejecución automatizada con GitHub Actions. Además, se enriquece la información con indicadores financieros, se desarrolla un modelo predictivo para estimar el precio de cierre del día siguiente y se crea un panel de control para visualizar los KPIs fundamentales.

## Clonar el Repositorio

* https://github.com/JulioMunozIUD/piv_act_2.git

## Crear y Activar un Entorno Virtual

* python -m venv venv
* source venv/bin/activate  # En Linux/Mac
* venv\Scripts\activate     # En Windows

## Instalar Dependencias

* pip install --upgrade pip
* pip install -e .

## Estructura del proyecto
```
├── .github/
│ └── workflows/
│ └── update_data.yml
├── docs/
│ ├── guion_enlace_video.pdf
│ └── reporte_final.pdf
│
├── src/
│ ├── static/
│ │ ├── dashboard/
│ │ │ └── dashboard.pbit
│ │ ├── data/
│ │ │ ├── enriched_data.csv
│ │ │ ├── historical.db
│ │ │ └── historical.csv
│ │ └── models/
│ │   ├── metrics.csv
│ │   └── model.pkl
│ ├── collector.py
│ ├── logger.py
│ ├── enricher.py
│ └── modeller.py
├── setup.py
├── requirements.txt
├── README.md
└── main.py

```
## Uso del proyecto

* Recolectar datos históricos: python collector.py 
* Enriquecer con KPIs financieros: python enricher.py
* Entrenar modelo y predecir el precio de cierre: python modeller.py
* Visualizar resultados en un dashboard interactivo: dashboard.pbit

## Automatización con GitHub Actions

El archivo .github/workflows/main.yml automatiza todo el flujo con cada push al branch main. Las acciones incluyen:

* Clonar el repositorio
* Crear entorno virtual y configurar Python 3.9.2
* Instalar dependencias del proyecto
* Ejecutar los scripts: collector.py, enricher.py, modeller.py
* Hacer commit automático de los resultados generados (CSV, DB, model.pkl)
* Esto permite mantener actualizado el repositorio con nuevos datos y modelos cada vez que se realicen cambios en el código.

## Referencias y documentación

* [Yahoo Finance API (via yfinance)](https://github.com/ranaroussi/yfinance)
* [Scikit-learn: Modelos de regresión](https://scikit-learn.org/stable/supervised_learning.html)
* [GitHub Actions](https://docs.github.com/en/actions)
* [Documentación Python 3](https://docs.python.org/3)
* [Documentación GitHub](https://docs.github.com/)