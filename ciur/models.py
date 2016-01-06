class Document(object):  # pylint: disable=too-few-public-methods
    """
    Model for encapsulate data.
    Scope:
        workaround for too-many-arguments for pylint, to not pass more than
        5 argument in a functions
    """
    def __init__(
            self,
            content,
            namespace=None,
            encoding=None,
            url=None
    ):
        self.content = content
        self.namespace = namespace
        self.encoding = encoding
        self.url = url
