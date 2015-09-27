#!/usr/bin/env python
import argparse
import sys
import fileinput


if __name__ == "__main__":
    print sys.argv
    print "===============", len(sys.argv)
    if not sys.stdin.isatty():
        html = sys.stdin.read()
        print "html", html
