import pandas as pd
import os
import glob
import logging

# 🔹 Log yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/raw")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/processed")
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

try:
    list_of_files = glob.glob(os.path.join(RAW_DATA_DIR, "*.json"))
    if not list_of_files:
        raise FileNotFoundError(f"{RAW_DATA_DIR} içinde JSON dosyası bulunamadı!")

    latest_file = max(list_of_files, key=os.path.getctime)
    logging.info(f"📄 İşlenecek dosya: {latest_file}")

    df = pd.read_json(latest_file)

    if "ReadingDate" not in df.columns:
        raise KeyError("'ReadingDate' sütunu JSON içinde bulunamadı!")

    df["Date"] = pd.to_datetime(df["ReadingDate"]).dt.date
    df["Hour"] = pd.to_datetime(df["ReadingDate"]).dt.hour

    if "Price" not in df.columns:
        raise KeyError("'Price' sütunu JSON içinde bulunamadı!")

    df["Price_with_VAT"] = df["Price"] * 1.21

    output_file = os.path.join(PROCESSED_DATA_DIR, "energy_prices.parquet")
    df.to_parquet(output_file, engine="pyarrow", index=False)
    logging.info(f"✅ Parquet dosyası oluşturuldu: {output_file}")

except Exception as e:
    logging.error(f"❌ Dönüştürme sırasında hata oluştu: {e}")
    raise
