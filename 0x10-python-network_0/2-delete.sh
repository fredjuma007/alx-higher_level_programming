#!/bin/bash
#Take in URL, send DELETE request

curl -sX delete "$1"
