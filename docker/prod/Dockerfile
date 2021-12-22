FROM python:3.13.2

RUN pip install ciur==0.2.1.dev2

# validate
RUN set -x && ciur --version | grep -qF "0.2.1.dev2"
