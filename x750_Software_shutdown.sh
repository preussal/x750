#!/bin/bash
# X750 full shutdown through Software
# /usr/local/bin/x750_Software_shutdown.sh

BUTTON=18

echo "$BUTTON" > /sys/class/gpio/export;
echo "out" > /sys/class/gpio/gpio$BUTTON/direction
echo "1" > /sys/class/gpio/gpio$BUTTON/value

SLEEP=${1:-4}

re=^[0-9.]+
if ! [[ $SLEEP =~ $re ]] ; then
   echo "error: sleep time not a number" >&2; exit 1
fi

echo "X750 Shutting down..."
/bin/sleep $SLEEP

#restore GPIO 18
echo "0" > /sys/class/gpio/gpio$BUTTON/value
