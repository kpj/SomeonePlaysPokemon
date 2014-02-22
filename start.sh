#!/bin/bash
cd "$(dirname "$0")"

vbam emerald.gba &
sleep 2
node frontend/main.js &
python3 backend/glue.py
kill %1
killall -9 vbam