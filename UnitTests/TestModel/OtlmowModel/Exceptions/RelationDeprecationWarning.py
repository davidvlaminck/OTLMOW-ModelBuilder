import logging

logger = logging.getLogger(__name__)


class RelationDeprecationWarning(DeprecationWarning):
    def __init__(self, msg):
        super().__init__(msg)
        logger.warning(msg)
