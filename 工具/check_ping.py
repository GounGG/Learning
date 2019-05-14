#!/usr/bin/python
# coding:utf-8

import ping
import argparse
import re

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-d', '--dest', type=str, help='remote dest host ip or domain')
parser.add_argument('-t', '--timeout', type=int, help='ping timeout', default=3)
parser.add_argument('-c', '--count', type=int, help='send package count', default=4)
parser.add_argument('-p', '--psize', type=int, help='send package size', default=64)


args = parser.parse_args()

print ping.quiet_ping(args.dest, args.timeout, args.count, args.psize)[0]

