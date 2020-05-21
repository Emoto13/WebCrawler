#!/bin/bash

#echo Choose on how many threads you want your program to run:
# shellcheck disable=SC2162
#read threads

# shellcheck disable=SC2004
#for ((i=0;i<$threads;i++))
#do
chmod +x webcrawler_with_threads.py
python3 webcrawler_with_threads.py

echo "Press enter to kill"
read kill

fuser -k webcrawler_with_threads.py
fuser -k sites.db
