import logging
import time
from functools import wraps


def setup_logger(name: str):

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(name)


logger = setup_logger(__name__)


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        logger.info(f"Executing function: {func.__name__}")

        start_time = time.time()

        try:
            result = func(*args, **kwargs)

            execution_time = round(time.time() - start_time, 4)

            logger.info(
                f"Function {func.__name__} executed successfully "
                f"in {execution_time} seconds"
            )

            return result

        except Exception as e:

            logger.error(
                f"Function {func.__name__} failed with error: {e}"
            )

            raise e

    return wrapper