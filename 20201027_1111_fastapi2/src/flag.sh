#!/bin/sh

echo $FLAG > /flag
export FLAG=not_flag
FLAG=not_flag

rm -rf flag.sh
