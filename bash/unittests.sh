#!/usr/bin/env bash

export PYTHONPATH=${PYTHONPATH}:../../
cd /code/ciur/originators/321auto_com/test
python -m unittest advert_test_case.py