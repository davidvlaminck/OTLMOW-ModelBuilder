import logging

logger = logging.getLogger(__name__)


class AttributeDeprecationWarning(DeprecationWarning):
    def __init__(self, msg):
        super().__init__(msg)
        logger.warning(msg)


