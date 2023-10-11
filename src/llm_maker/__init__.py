import logging
import os
from rich.logging import RichHandler


FORMAT = '%(message)s'
logging.basicConfig(
    level='DEBUG', format=FORMAT, datefmt='[%X]', handlers=[RichHandler()]
)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
