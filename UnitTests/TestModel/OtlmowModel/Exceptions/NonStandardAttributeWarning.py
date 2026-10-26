import logging

logger = logging.getLogger(__name__)


class NonStandardAttributeWarning(Warning):
    def __init__(self, msg=None):
        super().__init__(msg)
        logger.warning(msg)
