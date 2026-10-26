import logging

logger = logging.getLogger(__name__)


class IncorrectTypeWarning(Warning):
    def __init__(self, msg):
        logger.warning(msg)
