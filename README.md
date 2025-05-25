# NVIDIA Historical Data Collector

Este proyecto esta orientado a automatizar la recolección continua de datos históricos del comportamiento bursátil de NVIDIA Corporation. Se implementa un sistema que extrae datos desde Yahoo Finance, los limpia, almacena en una base de datos SQLite y los exporta a un archivo CSV versionado, todo bajo un entorno de ejecución automatizada con GitHub Actions. Además, se enriquece la información con indicadores financieros, se desarrolla un modelo predictivo para estimar el precio de cierre del día siguiente y se crea un panel de control para visualizar los KPIs fundamentales.

## Estructura del proyecto
```
├── .github/
│ └── workflows/
│ └── update_data.yml
├── docs/
│ └── report_entrega1y2
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