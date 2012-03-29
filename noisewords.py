import random
from optparse import OptionParser

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.+-'

parser = OptionParser()

parser.add_option('', "--rows", action="store", type="int", dest="rows", default=10000)
parser.add_option('', "--columns", action="store", type="int", dest="columns", default=8)
parser.add_option('', "--min-length", action="store", type="int", dest="min_length", default=8)
parser.add_option('', "--max-length", action="store", type="int", dest="max_length", default=255)
parser.add_option('', "--delimiter", action="store", type="string", dest="delimiter", default=',')

(options, args) = parser.parse_args()

for row in xrange(options.rows):
    print options.delimiter.join([''.join([random.choice(alphabet) for i in xrange(random.randint(options.min_length, options.max_length))]) for j in xrange(options.columns)])
