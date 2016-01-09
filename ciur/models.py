"""
place where to hold all Models related class of ``ciur``
"""
from requests.models import Response


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
        if isinstance(content, Response):
            self.content = content.content
            self.encoding = content.apparent_encoding
            self.url = content.url
        else:
            self.content = content
            self.encoding = encoding
            self.url = url

        self.namespace = namespace

    def __str__(self):
        _ = {
            "content": self.content
        }
        if self.encoding:
            _["encoding"] = self.encoding

        if self.url:
            _["url"] = self.url

        if self.namespace:
            _["namespace"] = self.namespace

        return "Document%s" % _
