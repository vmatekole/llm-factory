import logging
import os
from rich.logging import RichHandler

from dotenv import load_dotenv

load_dotenv()

LLAMA_MODEL_PATH = os.environ['LLAMA_MODEL_PATH']

FORMAT = '%(message)s'
DEBUG_LEVEL = 'INFO'
logging.basicConfig(
    level=DEBUG_LEVEL, format=FORMAT, datefmt='[%X]', handlers=[RichHandler()]
)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
