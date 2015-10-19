#!/usr/bin/env python
import argparse
import sys
import sh

if __name__ == "__main__":
    print sys.argv
    print "===============", len(sys.argv)

    sh.Command("wget").bake("--help")()

    if not sys.stdin.isatty():
        html = sys.stdin.read()
        print "html", html
