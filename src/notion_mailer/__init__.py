import logging
import sys

RESET = "\033[0m"
COLORS = {
    "INFO": "\033[92m",
    "WARNING": "\033[93m",
    "ERROR": "\033[91m",
    "DEBUG": "\033[94m",
    "CRITICAL": "\033[95m",
}

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
    
formatter = logging.Formatter(
     "[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
    
logger.addHandler(handler)
