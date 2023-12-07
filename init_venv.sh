#!/bin/bash

rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -U pip
pip3 install -U setuptools
pip3 install --no-cache-dir -r requirements.txt
source enviroment.sh
