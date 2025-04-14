from loguru import logger
import sys

def setup_logger():
    logger.add(
        "logs/debug.log",
        rotation='1 mb',
        level="DEBUG")
    return logger
logger = setup_logger()