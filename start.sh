#!/bin/bash

set -e
set -u

cd "$(dirname "$0")" # cwd will be directory of current script

vbam emerald.gba &>/dev/null &
vbam_pid=$!
echo "Please press enter when ready to select a window"
read

node frontend/main.js &
node_pid=$!

python3 backend/glue.py >/dev/null &
python_pid=$!

echo "Press enter to end this application"
read
kill $python_pid $node_pid
kill -9 $vbam_pid # :-(
