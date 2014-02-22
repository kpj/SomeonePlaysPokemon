#!/bin/bash

set -e
set -u

function shutdown {
	echo "Shutting down..."

	set +e
	kill $python_pid
	kill $node_pid
	kill -9 $vbam_pid # :-(
	set -e

	exit
}
trap shutdown 2

cd "$(dirname "$0")" # cwd will be directory of current script

vbam emerald.gba &>/dev/null &
vbam_pid=$!
echo "Press enter when ready to select window"
read

node backend/nodejs/main.js >/dev/null &
node_pid=$!

python3 backend/python/glue.py >/dev/null &
python_pid=$!

echo "Press enter to end this application"
read
shutdown