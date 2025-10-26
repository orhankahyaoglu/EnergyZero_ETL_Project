import pandas as pd
import matplotlib
matplotlib.use("Agg")  # 👈 Airflow gibi GUI olmayan ortamlarda kilitlenmeyi önler
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime

# === Klasörler ===
data_dir = Path("data/processed")
output_dir = Path("outputs")
output_dir.mkdir(parents=True, exist_ok=True)

# === Veri dosyası seçimi ===
data_file = None
for ext in ("parquet", "csv"):
    f = data_dir / f"energy_prices.{ext}"
    if f.exists():
        data_file = f
        break

if not data_file:
    raise FileNotFoundError("❌ energy_prices.parquet veya energy_prices.csv bulunamadı.")

print(f"📂 Veri dosyası: {data_file}")

# === Veri oku ===
if data_file.suffix == ".parquet":
    df = pd.read_parquet(data_file)
else:
    df = pd.read_csv(data_file)

# === Saat sütunu ekle ===
df["ReadingDate"] = pd.to_datetime(df["ReadingDate"])
df["Hour"] = df["ReadingDate"].dt.hour

# === Fiyat sütunu tespiti ===
price_col = None
for col in ["Price_with_VAT", "Price", "price_with_vat", "price"]:
    if col in df.columns:
        price_col = col
        break

if not price_col:
    raise KeyError("❌ Price_with_VAT veya Price sütunu bulunamadı.")

# === Price sütununu float yap (boş grafiği önlemek için) ===
df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
df = df.dropna(subset=[price_col])  # NaN değerleri temizle

# === Boxplot ===
plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")

# Boxplot
sns.boxplot(
    x="Hour",
    y=price_col,
    data=df,
    palette="OrRd",
    width=0.6,
    linewidth=1.2,
    fliersize=2
)

# Ortalama çizgisi (overlay)
sns.pointplot(
    x="Hour",
    y=price_col,
    data=df,
    color="black",
    markers="o",
    scale=0.6,
    errorbar=None
)

plt.title("Price Distribution by Hour of the Day (with VAT)", fontsize=14, weight="bold")
plt.xlabel("Hour (0–23)", fontsize=12)
plt.ylabel("Price (EUR/kWh)", fontsize=12)
plt.xticks(range(24))
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Y ekseni aralığını veriye göre ayarla
plt.ylim(df[price_col].min() * 0.95, df[price_col].max() * 1.05)
plt.tight_layout()

# === Dosya kaydı ===
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = output_dir / f"hourly_price_boxplot_{timestamp}.png"
plt.savefig(output_path, dpi=300)
plt.close()

print(f"✅ Grafik kaydedildi: {output_path}")
