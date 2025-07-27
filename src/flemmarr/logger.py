import logging
import os
import sys

def setup_logging(name="flemmarr") -> logging.Logger:
    """
    Set up a reusable logger with a consistent format and level.

    Args:
        name (str): The name of the logger. Use __name__ to get module-specific loggers,
                    or leave as default for a shared root logger.

    Returns:
        logging.Logger: Configured logger instance.
    """

    # Get log level from environment variable, fallback to INFO
    log_level = os.getenv("FLEMMARR_LOG_LEVEL", "INFO").upper()

    # Create (or get) the logger by name
    logger = logging.getLogger(name)

    # Set the logger's level (e.g., DEBUG, INFO)
    logger.setLevel(getattr(logging, log_level, logging.INFO))

    # Only add a handler if one hasn't already been attached
    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)

        # Define how log messages will appear
        formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Shared default logger used by modules that don't need their own named logger
logger = setup_logging()
