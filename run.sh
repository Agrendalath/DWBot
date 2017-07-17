#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

if [ ! -d "venv" ]; then
  virtualenv venv
  . venv/bin/activate
  pip install -r requirements.txt
fi

. venv/bin/activate
PATH=$PATH+':.' ./darkwarezbot.py