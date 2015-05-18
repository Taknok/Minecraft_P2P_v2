# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:57:48 2015

@author: Paul
"""

#ping -l 10 -f -n 5 25.154.237.16

import speedtest_cli as sp

def test_connection():
    speedDwUp = sp.speedtest()
    speedDwUp = list(speedDwUp)
    speedDwUp[0] = speedDwUp[0] / 1000 / 1000 * 8 #converti en Mbits/s
    speedDwUp[1] = speedDwUp[1] / 1000 / 1000 * 8
    return speedDwUp