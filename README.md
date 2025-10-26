
# ⚡ EnergyZero ETL Project

> ETL pipeline that extracts and processes hourly energy prices from the **EnergyZero API** using **Python** and **Apache Airflow**.  
> Developed as part of the **Werhere IT Academy – Azure Data Engineering & Analytics Module**.

---

This repository demonstrates an end-to-end data engineering workflow: extracting energy price data, transforming it with pandas, and automating the process through Airflow DAGs.  
It also includes Docker setup, logging, and visualization of results using boxplots.


# ⚡ EnergyZero ETL Project

This repository is part of the **Werhere IT Academy – Azure Data Engineering & Analytics Module (Week 8: Data Processing and ETL with Python)**.  
It showcases an end-to-end **ETL (Extract, Transform, Load)** pipeline for energy price data retrieved from the **EnergyZero API**, processed using **Python and Airflow**, and stored in structured formats for analytics.

---

## 🧠 Project Overview

The **EnergyZero ETL Project** automates the collection, transformation, and storage of energy price data.  
It includes:

- Extraction of hourly energy data from the EnergyZero API  
- Transformation and cleaning of datasets with **pandas**  
- Storage of processed data in **CSV** and **Parquet** formats  
- Visualization of hourly price distributions as boxplots  
- Scheduling and monitoring via **Apache Airflow DAGs**

---

## 🧩 Tech Stack & Libraries

| Purpose | Technology / Library |
|----------|----------------------|
| Workflow orchestration | Apache Airflow |
| Data processing & transformation | pandas |
| API data retrieval | requests |
| Parquet read/write | pyarrow, fastparquet |
| Visualization | matplotlib, seaborn (if used) |
| Containerization | Docker, Docker Compose |

---

## 🏗️ Project Structure
ENERGYZERO_ETL/
│
├── dags/ # Airflow DAG definitions
│ ├── energyzero_dag.py # Main ETL DAG
│ └── test_logging_dag.py # DAG for logging/test runs
│
├── scripts/ # Python ETL scripts
│ ├── extract_energyzero.py # Extracts data from EnergyZero API
│ ├── transform_pandas.py # Cleans and transforms data
│ └── hourly_boxplot.py # Generates visualizations
│
├── data/
│ ├── raw/ # Unprocessed data (JSON from API)
│ │ └── sample_energy.json
│ ├── processed/ # Cleaned/ready-to-use data
│ │ ├── energy_prices.csv
│ │ └── energy_prices.parquet
│ └── postgres/ # Placeholder for DB output (if used)
│
├── outputs/ # Generated visualizations (boxplots)
│ ├── hourly_price_boxplot_*.png
│
├── logs/ # Airflow and ETL execution logs
│
├── plots/ # Additional visualizations
│
├── energy_boxplot/ # Dockerfile for containerized visualization
│
├── .env # Environment variables (API keys, configs)
├── docker-compose.yml # Airflow & ETL container orchestration
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Setup & Execution

### 1️⃣ Clone the repository
```bash
git clone https://github.com/orhankahyaoglu/EnergyZero_ETL_Project.git
cd EnergyZero_ETL_Project

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS / Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up environment variables

Create a .env file (if not already) and include necessary configuration such as:
ENERGYZERO_API_URL=...
ENERGYZERO_API_KEY=...

5️⃣ Run the ETL pipeline locally
python scripts/extract_energyzero.py
python scripts/transform_pandas.py
python scripts/hourly_boxplot.py

6️⃣ (Optional) Run with Docker & Airflow
docker-compose up -d

Then open http://localhost:8080
 to access the Airflow UI and trigger DAGs manually.

📊 Outputs

Processed data:

data/processed/energy_prices.parquet

data/processed/energy_prices.csv

Visualizations:

outputs/hourly_price_boxplot_*.png

These can be used in Power BI, Databricks, or any analytics environment.

🎯 Learning Objectives

Through this project, you will learn to:

Interact with REST APIs using Python

Clean and transform data using pandas

Implement a modular ETL structure

Automate workflows using Airflow

Visualize time-series data distributions

📚 References

Werhere IT Academy Handbook

EnergyZero API

Apache Airflow Documentation

👨‍💻 Author

Orhan Kahyaoğlu
📦 GitHub: @orhankahyaoglu


---

İstersen bu README’yi sana **Türkçe versiyon** olarak da çevirebilirim — hem eğitim hem GitHub gösterimi için iki dilli (EN + TR) yapmak da güzel olur.  
İster misin İngilizce–Türkçe çift dilli hale getireyim?

Şunu dedin:
senin yazdıklarının hepsini koyalıyıp readme içine yapıştıracak mıyım
ChatGPT:

Evet ✅ tam olarak öyle!

GitHub projenin kök klasöründe (yani ENERGYZERO_ETL/ dizininde) zaten bir README.md dosyan var.
Şöyle yapıyorsun 👇

🔧 Adım adım:

VS Code’da proje dizininde README.md dosyasını aç.

İçindeki eski içeriği tamamen sil (veya yedeğini al).

Benim gönderdiğim README.md içeriğini tamamını kopyala ve yapıştır.

Dosyayı kaydet (Ctrl+S).

Terminalden şu komutları çalıştır:

git add README.md
git commit -m "Update README with full project documentation"
git push

👨‍💻 Author

Orhan Kahyaoğlu
📦 GitHub: @orhankahyaoglu

