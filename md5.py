import sys

from hashlib import md5

generator = md5(sys.argv[1].encode('utf8'))
print(generator.hexdigest())