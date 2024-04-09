import logging


def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set the global logging level to DEBUG

    # Create a file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set the logging level for this handler

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
