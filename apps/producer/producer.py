import os
import time
import logging
from kafka import KafkaProducer

LOG_DIR = "/logs"
LOG_FILE = f"{LOG_DIR}/producer.log"

os.makedirs(LOG_DIR, exist_ok=True)

# -----------------------
# Logging configuration
# -----------------------
logger = logging.getLogger("producer")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | producer | %(message)s"
)

# stdout handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# file handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# -----------------------
# Env vars
# -----------------------
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

logger.info("Producer starting")
logger.info(f"Kafka: {KAFKA_BOOTSTRAP}")
logger.info(f"Topic: {KAFKA_TOPIC}")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP,
    acks="all",
    retries=5
)

counter = 0

while True:
    msg = f"event-{counter}"
    try:
        producer.send(KAFKA_TOPIC, msg.encode())
        logger.info(f"Sent message: {msg}")
    except Exception as e:
        logger.error(f"Send failed: {e}")

    counter += 1
    time.sleep(5)

