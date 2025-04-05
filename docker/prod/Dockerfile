ARG PYTHON_VERSION=3.13.2
ARG CIUR_VERSION=3.13.2

FROM python:${PYTHON_VERSION}

RUN pip install ciur==${CIUR_VERSION}

# validate
RUN set -x && ciur --version | grep -qF "${CIUR_VERSION}"
