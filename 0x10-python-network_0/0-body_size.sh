#!/bin/bash
# script that takes URL, sends request, and displays the size of the body of the response
curl -s "$1" | wc -c
