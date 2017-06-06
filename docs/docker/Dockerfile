# docker build -t ada/ec2-replica:0.0.1 .
# docker run --name temp-container-name ada/ec2-replica:0.0.1 /bin/true
# docker cp temp-container-name:/tmp/python_3.6.1_lambda.zip .
# docker rm temp-container-name
FROM amazonlinux

ENV VIRTUAL_ENV /tmp/virt
ENV WORK_DIR /tmp/a
ENV PYTHON_VERSION 3.6.1
ENV PIP ${VIRTUAL_ENV}/bin/pip
ENV PYTHON /usr/local/bin/python3.6
ENV zip_file /tmp/python_${PYTHON_VERSION}_lambda.zip

RUN mkdir ${WORK_DIR}
WORKDIR ${WORK_DIR}
COPY example.org.ciur ${WORK_DIR}
COPY lambda_handler.py ${WORK_DIR}
COPY requirements.txt ${WORK_DIR}

RUN yum update -y

# tools
RUN yum install -y \
    zip \
    wget \
    gcc \
    zlib \
    vim \
    unzip

# workarounf for Error unpacking rpm package iputils-20121221-7.13.amzn1.x86_64
RUN yum install -y git || echo "ok"

# libs
RUN yum install -y \
    zlib-devel \
    openssl \
    openssl-devel \
    plibxml2-devel \
    libxslt-devel

# becasue there is not `yum innstall -y python36`
# we are going to install python3.6.1 from the source
RUN wget -c https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
RUN tar -xzvf Python-${PYTHON_VERSION}.tgz
RUN cd Python-${PYTHON_VERSION} && ./configure && make
RUN cd Python-${PYTHON_VERSION} && make install

RUN ${PYTHON} -m venv ${VIRTUAL_ENV}

RUN ${PIP} install -r requirements.txt

RUN cd ${VIRTUAL_ENV}/lib/python*/site-packages/ && \
    zip -r9 ${zip_file} . && \
    cd ${WORK_DIR} && \
    zip -r9 ${zip_file} index.py && \
    zip -r9 ${zip_file} example.org.ciur

RUN mkdir /tmp/tmp_zip && \
    cd /tmp/tmp_zip && \
    unzip ${zip_file} && \
    rm -rf setuptools* pip* *info && \
    rm ${zip_file} && \
    zip -r9 ${zip_file} . && \
    rm -r /tmp/tmp_zip

RUN echo "Congradulation !, now download upload ${zip_file} on lambda-amazon"
