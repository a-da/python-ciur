# main.lambda_handler
import ciur
from ciur.shortcuts import pretty_parse_from_url

def demo():
    with ciur.open_file("example.org.ciur", __file__) as f:
        print(pretty_parse_from_url(
            f,
            "http://example.org"
        ))


def lambda_handler(event, context):
    demo()


if __name__ == "__main__":
    lambda_handler(None, None)
