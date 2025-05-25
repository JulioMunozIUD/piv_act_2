from src.collector import HistoricalDataCollector
from src.enricher import DataEnricher
from src.modeller import ModelTrainer


if __name__ == "__main__":
    db_path = "src/static/data/historical.db"
    csv_path = "src/static/data/historical.csv"
    enriched_csv = "src/static/data/enriched_data.csv"
    model_path = "src/static/models/model.pkl"

    collector = HistoricalDataCollector(db_path, csv_path)
    collector.run()

    enricher = DataEnricher(csv_path, enriched_csv)
    enricher.enrich()

    trainer = ModelTrainer(data_path="src/static/data/enriched_data.csv")
    trainer.entrenar()

   