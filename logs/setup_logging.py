import logging
import logging.config
import os
import yaml

def setup_logger(name, log_file="logs/app.log", level=logging.DEBUG):
    """
    Set up logging for a specific module using centralized logger configuration.
    
    Args:
        name (str): Name of the logger.
        log_file (str): Path to the log file.
        level (int): Logging level.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Load YAML configuration if it exists
    config_file = os.path.join(os.path.dirname(__file__), "log_config.yaml")
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
            logging.config.dictConfig(config)
    else:
        # Fallback to basic logging configuration
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(),
            ],
        )
    
    return logging.getLogger(name)
