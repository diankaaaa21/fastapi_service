import logging

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)
file_formater = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formater)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
