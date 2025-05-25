# src/enricher.py

import pandas as pd
import numpy as np
import os
import traceback
from src.logger import CustomLogger

class DataEnricher:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.logger = CustomLogger('DataEnricher', '__init__')

    def enrich(self):
        logger = CustomLogger('DataEnricher', 'enrich')
        try:
            logger.info(f"Cargando datos crudos desde {self.input_path}")
            df = pd.read_csv(self.input_path)

            # --- LIMPIEZA Y TRANSFORMACIÓN ---
            logger.info("Transformando tipos de datos y limpiando valores")

            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Precios: punto como decimal, eliminar comas
            for col in ['Open', 'High', 'Low', 'Close']:
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(',', '')
                    .replace({'-': np.nan})
                    .astype(float)
                )

            # Volumen: eliminar comas de miles y convertir a float
            df['Volume'] = (
                df['Volume']
                .astype(str)
                .str.replace(',', '')
                .replace({'-': np.nan})
                .astype(float)
                .astype('Int64')
            )

            df = df.sort_values('Date').reset_index(drop=True)
            df.dropna(subset=['Date', 'Close'], inplace=True)

            # --- KPIs FINANCIEROS ---
            logger.info("Calculando KPIs financieros")

            df['Daily_Return'] = (df['Close'].pct_change() * 100).round(4)
            df['MA_7_Close'] = df['Close'].rolling(7, min_periods=1).mean().round(4)
            df['STD_7_Close'] = df['Close'].rolling(7, min_periods=1).std().round(4)
            df['Cumulative_Return'] = ((1 + df['Daily_Return'] / 100).cumprod() - 1).round(4)
            df['Momentum_7'] = (df['Close'] / df['Close'].shift(7) - 1).round(4)

            df.dropna(inplace=True)

            # --- GUARDAR RESULTADO ---
            logger.info(f"Guardando datos enriquecidos en {self.output_path}")
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            df.to_csv(self.output_path, index=False)

            logger.info("Enriquecimiento completado con éxito.")

        except Exception:
            logger.error(f"Error durante el enriquecimiento:\n{traceback.format_exc()}", exc_info=True)
