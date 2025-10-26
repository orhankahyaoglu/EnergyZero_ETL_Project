from __future__ import annotations
import pendulum
import logging

from airflow.decorators import dag, task

# Python'ın standart loglama kütüphanesini kullanıyoruz
log = logging.getLogger(__name__)

@dag(
    dag_id="test_logging_dag",
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["test", "log"],
)
def logging_test_pipeline():
    
    @task
    def check_log_output():
        
        # 1. Standart Python print() fonksiyonu (Airflow bunu yakalamalı)
        print(">>> [PRINT] Bu bir Python print() çıktısıdır. Loglarda görünmeli.")
        
        # 2. Python logging kütüphanesi ile INFO seviyesinde log
        log.info(">>> [INFO] Bu, logger.info() ile üretilmiş bir mesajdır.")
        
        # 3. Python logging kütüphanesi ile WARNING seviyesinde log
        log.warning(">>> [WARNING] Bu, logger.warning() ile üretilmiş bir mesajdır.")
        
        # 4. Görevin başarısız olmasını tetikleyen bir log (opsiyonel, deneme amaçlı)
        # raise Exception("Görevi bilerek başarısız yapıyorum ki loglarda hata mesajı da görünsün.")
        
        return "Loglama testi tamamlandı"

    check_log_output()

logging_test_pipeline()