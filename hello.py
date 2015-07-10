#!/usr/bin/env python
# coding: utf-8

import os
import time

print "Hello,", os.name, "! --", time.strftime("%Z %Y-%m-%d %A %H:%M:%S", time.localtime(time.time()))

raw_input("click any key to quit...")

