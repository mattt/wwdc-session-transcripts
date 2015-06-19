#!/usr/bin/env python3

import sys
import re
import html

f = open(sys.argv[1], 'r')

count = 1
for line in f.readlines():
  if line[:6] == 'WEBVTT':
    continue
  line = re.sub(r'(:\d+)\.(\d+)', r'\1,\2', line)
  if line == '\n':
    print('\n' + str(count))
    count += 1
  else:
    print(html.unescape(line.strip()))
