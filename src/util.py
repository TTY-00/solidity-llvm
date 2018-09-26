# coding:utf-8
#!/usr/bin/env python3

'''
This file defines the basic infomationß.
'''

import sys
import os
import logging.config
import coloredlogs

# set workdir to the current folder which uril.py in
os.chdir(os.path.split(os.path.realpath(__file__))[0])

# init the logging module 
logging.config.fileConfig('conf/logger_conf.ini')
parseLog=logging.getLogger('parse')
coloredlogs.install(level='DEBUG')