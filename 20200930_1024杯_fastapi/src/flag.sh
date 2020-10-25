#!/bin/sh

echo $FLAG > /mnt/f1a9
export FLAG=not_flag
FLAG=not_flag

rm -rf flag.sh