import os
import logging
from kafka import KafkaConsumer

LOG_DIR = "/logs"
LOG_FILE = f"{LOG_DIR}/consumer.log"

os.makedirs(LOG_DIR, exist_ok=True)

# -----------------------
# Logging configuration
# -----------------------
logger = logging.getLogger("consumer")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | consumer | %(message)s"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# -----------------------
# Env vars
# -----------------------
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

logger.info("Consumer starting")
logger.info(f"Kafka: {KAFKA_BOOTSTRAP}")
logger.info(f"Topic: {KAFKA_TOPIC}")

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP,
    group_id="demo-group",
    auto_offset_reset="earliest"
)

for msg in consumer:
    logger.info(f"Received message: {msg.value.decode()}")

