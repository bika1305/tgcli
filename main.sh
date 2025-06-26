#!/bin/bash
cd "$(dirname "$0")" || exit
source telegram/bin/activate  
python3 main.py