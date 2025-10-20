#!/bin/bash

VENV_NAME=VIR_ENV
TEST_DIR=/home/chakra/mytest

if [[ ! -f "requirements.txt" ]]; then
  echo "Error: requirements.txt is not found in the current directory"
  exit 1
fi

if [[ ! -d "$VENV_NAME" ]]; then
  echo "Creating Virtual Environment"
  python3 -m venv "$VENV_NAME"
  if [[ $? -ne 0 ]]; then
    echo "Error: failed to create Virtual environment"
    exit 1
  fi
else
  echo "Virtual Environment already exists"
fi

echo "Activating Virtual enviroment"
source "$VENV_NAME/bin/activate"
if [[ $? -ne 0 ]]; then
  echo "Error: unable to activate Virtual environment"
  exit 1
fi

echo "Installing requirements"
pip install -r requirements.txt
if [[ $? -ne 0 ]]; then
  echo "Error: error while installing requirements"
  exit 1
fi

echo "Running tests"
pytest --html=report.html --self-contained-html "$TEST_DIR"
