#!/bin/sh
set -e

if [ $# -ne 2 ]; then
   exit 1
fi

if [ "$2" = "on" ]; then
  curl "http://$1/cm?cmnd=Power%20On"
  exit 0
fi

if [ "$2" = "off" ]; then
  curl "http://$1/cm?cmnd=Power%20Off"
  exit 0
fi

exit 1
