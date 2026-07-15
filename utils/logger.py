import logging

logging.basicConfig(
    filename="logs/steelvision.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("SteelVision")
