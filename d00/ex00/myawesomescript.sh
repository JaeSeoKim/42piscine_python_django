#!/bin/sh

if [ $1 ]; then
  curl -s $1 | grep "moved here" | cut -d \" -f 2
fi
