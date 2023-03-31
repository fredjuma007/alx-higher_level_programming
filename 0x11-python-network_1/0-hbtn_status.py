#!/usr/bin/python3
"""
lets play fetch
"""

import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(f"The value of the X-Request-Id variable is: {x_request_id}")
