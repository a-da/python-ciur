ARG PYTHON_VERSION=3.13.2

FROM python:${PYTHON_VERSION}
ARG CIUR_VERSION=0.2.2

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install ciur==${CIUR_VERSION}

# validate
RUN set -x && ciur --version | grep -qF "${CIUR_VERSION}"
