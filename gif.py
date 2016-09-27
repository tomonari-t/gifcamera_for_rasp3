#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def makeGif():
    cmdStr = "/usr/bin/convert -layers optimize -loop 0 -delay 40 ./photo/photo*.jpg anim.gif"
    os.system(cmdStr)