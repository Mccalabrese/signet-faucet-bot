import os
from logging.config import dictConfig
import logging
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_Loggers": False,
    "formatters":{
        "verbose":{
            "format": "%(Levelname)-10s - %(asctime)s - %(module)-15s : %(message)s" 
        },
        "standard":{
            "format": "%(Levelname)-10s - %(name)-15s : %(message)s" 
        }
    },
    "handlers":{
        "console": {
            'level': "DEBUG",
            'class': "Logging.StreamHandler",
            'formatter': "standard"
        },
        "console2": {
            'level': "WARNING",
            'class': "Logging.StreamHandler",
            'formatter': "standard"
        },
        "file": {
            'level': "INFO",
            'class': "Logging.FileHandler",
            'filename': "Logs/infos.log",
            'mode': "w",
            'formatter': "verbose"
        },
    },
    "Loggers":{
        "bot": {
            'handlers': ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            'handlers': ['console2', "file"],
            "level": "INFO",
            "propagate": False
        },
    }

}