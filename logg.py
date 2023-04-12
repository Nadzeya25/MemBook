import logging

logging.basicConfig(
    level=logging.INFO,
    filename="my_log.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S',
    encoding='utf-8',
)