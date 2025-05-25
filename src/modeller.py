import pandas as pd
import numpy as np
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from src.logger import CustomLogger

class ModelTrainer:
    def __init__(self, data_path, model_path='src/static/models/model.pkl', metrics_path='src/static/models/metrics.csv'):
        self.data_path = data_path
        self.model_path = model_path
        self.metrics_path = metrics_path
        self.logger = CustomLogger('ModelTrainer', '__init__')

    def entrenar(self):
        logger = CustomLogger('ModelTrainer', 'entrenar')
        try:
            logger.info(f"Cargando datos desde {self.data_path}")
            df = pd.read_csv(self.data_path)

            # Ordenar por fecha para asegurar el orden temporal
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values(by='Date').reset_index(drop=True)

            # Variables predictoras y objetivo (Close del día siguiente)
            features = ['Open', 'High', 'Low', 'Volume']
            target = 'Close'

            if not all(col in df.columns for col in features + [target]):
                raise ValueError("Faltan columnas necesarias para entrenar el modelo.")

            # Shift para predecir el Close del día siguiente
            df['Target_Close'] = df['Close'].shift(-1)
            df = df.dropna()  # Elimina última fila con Target nulo

            X = df[features]
            y = df['Target_Close']

            model = LinearRegression()
            model.fit(X, y)

            # Guardar modelo
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            with open(self.model_path, 'wb') as f:
                pickle.dump(model, f)
            logger.info(f"Modelo entrenado y guardado en {self.model_path}")

            # Predicciones y métricas
            y_pred = model.predict(X)
            rmse = sqrt(mean_squared_error(y, y_pred))
            mae = mean_absolute_error(y, y_pred)
            r2 = r2_score(y, y_pred)

            logger.info(f"RMSE: {rmse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}")

            # Guardar métricas
            metrics_df = pd.DataFrame([{
                'RMSE': rmse,
                'MAE': mae,
                'R2': r2
            }])
            os.makedirs(os.path.dirname(self.metrics_path), exist_ok=True)
            metrics_df.to_csv(self.metrics_path, index=False)
            logger.info(f"Métricas guardadas en {self.metrics_path}")

        except Exception as e:
            import traceback
            logger.error(f"Error entrenando modelo: {e}\n{traceback.format_exc()}")

    def predecir(self, input_data: pd.DataFrame):
        logger = CustomLogger('ModelTrainer', 'predecir')
        try:
            logger.info("Cargando modelo desde archivo .pkl")
            with open(self.model_path, 'rb') as f:
                model = pickle.load(f)

            features = ['Open', 'High', 'Low', 'Volume']
            if not all(col in input_data.columns for col in features):
                raise ValueError("Faltan columnas necesarias para predecir.")

            predictions = model.predict(input_data[features])
            logger.info("Predicciones generadas correctamente")
            return predictions

        except Exception as e:
            import traceback
            logger.error(f"Error haciendo predicciones: {e}\n{traceback.format_exc()}")
            return None

