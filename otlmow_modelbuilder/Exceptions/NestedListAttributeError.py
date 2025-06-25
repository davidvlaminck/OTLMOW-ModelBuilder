class NestedListAttributeError(NotImplementedError):
    def __init__(self, url):
        self.message = f"Nested list attributes are not supported for this attribute {url}"
        super().__init__(self.message)
