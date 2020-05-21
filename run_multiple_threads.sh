#!/bin/bash

# run web crawler with more threads
chmod +x webcrawler_with_threads.py
python3 webcrawler_with_threads.py &>output.txt 2>error.txt

# kill connections if any left
fuser -k webcrawler_with_threads.py
fuser -k sites.db

# delete output files
rm output.txt
rm error.txt
