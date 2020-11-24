# pylint: disable=too-few-public-methods
""" Define logging system """

import sys
import logging
import time
from datetime import datetime


class NoErrorFilter(logging.Filter):
    """ Excludes all logs levels errors """

    def filter(self, record):
        return record.levelno != logging.ERROR


def get_formatter():
    """" Return the format of the log message """
    aplication_name = "clothing-manager"
    return aplication_name \
        + " %(name)-4s %(asctime)-6s %(levelname)-8s %(message)s"


def get_datefmt():
    """ Return date formatter """
    return "%m-%d-%Y %H:%M:%S"


def apply_file_handler():
    """ apply File Handler """
    file_path = "./clothing-manager-{}.log".format(
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(logging.Formatter(
        get_formatter(), get_datefmt()))
    return file_handler


def apply_console_handler(level):
    """ apply Console Handler """
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(level=level.upper() or logging.INFO)
    console_handler.addFilter(NoErrorFilter())
    return console_handler


def apply_error_stream_handler():
    """ Apply Stream Handler to send logging.ERROR to stderr """
    error_handler = logging.StreamHandler(stream=sys.stderr)
    error_handler.setLevel(level=logging.ERROR)
    return error_handler


def conf_logging(level=''):
    """ apply basic config log """
    logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s",
                        level=logging.DEBUG,
                        datefmt=get_datefmt(),
                        handlers=[apply_console_handler(level),
                                  apply_file_handler(),
                                  apply_error_stream_handler()])
    logging.Formatter.converter = time.gmtime
