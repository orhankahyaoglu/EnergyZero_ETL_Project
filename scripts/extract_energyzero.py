import requests
import json
from datetime import datetime, timedelta, timezone
import os

# 1️⃣ EnergyZero API URL ve parametreler
BASE_URL = "https://api.energyzero.nl/v1/prices"  # Örnek URL, gerçek URL farklı olabilir
DAYS = 7

# 2️⃣ Kaydedilecek klasör
RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/raw")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# 3️⃣ Tarih aralığını hesapla (timezone-aware UTC)
end_date = datetime.now(timezone.utc).date()
start_date = end_date - timedelta(days=DAYS)

# 4️⃣ API isteği parametreleri
params = {
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat()
}

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Hata varsa raise eder
    data = response.json()
    
    # 5️⃣ Dosya adı
    filename = f"energy_prices_{start_date}_{end_date}.json"
    filepath = os.path.join(RAW_DATA_DIR, filename)

    # 6️⃣ JSON olarak kaydet
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Veriler kaydedildi: {filepath}")

except requests.exceptions.RequestException as e:
    print(f"❌ API isteği başarısız: {e}")
