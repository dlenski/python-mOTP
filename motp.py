#!/usr/bin/python3

# mOTP algorithm, based on:
#   http://motp.sourceforge.net/bash/otpverify.sh
#
# counter = ASCII((UNIX epoch time) / 10s)
# digest = MD5HEX(counter || secret || pin)
# code = LEFT(digest, 6 characters)

import argparse, hashlib, time

p = argparse.ArgumentParser()
p.add_argument('-s', '--seconds', default=30, type=int, help="Duration of mOTP codes in seconds (default %(default)s seconds)")
p.add_argument('-l', '--length', default=6, type=int, help="Length of mOTP output (default %(default)s characters)")
p.add_argument('-w', '--window', default=0, type=int, help="Number of counter values before and after current one to show (for testing time-skew)")
p.add_argument('-v', '--verbose', action='count')
p.add_argument('secret', help="mOTP secret value (often hex or alphanumeric digits)")
p.add_argument('pin', help="mOTP PIN value (usually 4 digits)")
args = p.parse_args()

epoch_time = int(time.time())
counter = epoch_time // 10
secret = args.secret.strip().encode('ascii')
pin = args.pin.strip().encode('ascii')

codes = [ hashlib.md5(b"%d%s%s" % (counter + ii, secret, pin)).hexdigest()[:args.length]
          for ii in range(-args.window, args.window+1) ]

if args.verbose:
    print("Epoch time: %d" % epoch_time)
    print("Counter: %d\n" % counter)
    for ii, code in enumerate(codes, -args.window):
        print("%s%s" % (code, ' (current)' if ii==0 else ''))
else:
    for code in codes:
        print(code)
