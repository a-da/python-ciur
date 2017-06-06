==========================================================================================================================
Deploy `python ciur lib <https://bitbucket.org/ada/python-ciur>`_ project into `lambda <https://aws.amazon.com/lambda/>`_
==========================================================================================================================

Requirements
============

1. Create `<aws.amazon.com>`_ account
2. Install `AWS Command Line Interface <https://aws.amazon.com/cli/>`_

3. Build ``python_3.6.1_lambda.zip`` with docker

.. code-block:: bash

    docker build -t ada/ec2-replica:0.0.1 .
    docker run --name temp-container-name ada/ec2-replica:0.0.1 /bin/true
    docker cp temp-container-name:/tmp/python_3.6.1_lambda.zip .
    docker rm temp-container-name

4. Go to aws lambda, upload python_3.6.1_lambda.zip and test lambda_function

