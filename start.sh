#!/bin/bash

set -e
set -u

cd "$(dirname "$0")" # cwd will be directory of current script

vbam emerald.gba &>/dev/null &
vbam_pid=$!
echo "Please press enter when ready to select a window"
read # wait for user to select window

node frontend/main.js >/dev/null &
node_pid=$!

python3 backend/glue.py >/dev/null &
python_pid=$!

echo "Press enter to end this application"
read
kill $python_pid $node_pid
kill -9 $vbam_pid # :-(