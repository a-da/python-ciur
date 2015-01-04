import sys

if sys.version > '3':
    long = int
    basestring = str

    def iteritems23(dict_):
        for key, val in dict_.items():
            yield key, val
else:
    def iteritems23(dict_):
        for key, val in dict_.iteritems():
            yield key, val
