#!/bin/bash
if [ -z "$VIRTUAL_ENV" ]; then
    echo "WARNING: virtual environment is not set!"
fi

python ./setup.py sdist
python ./setup.py check
