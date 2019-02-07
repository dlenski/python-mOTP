[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

What is this for?
=================

If you need to generate [one-time passwords](//en.wikipedia.org/wiki/One-time_password)
using the [Mobile-OTP / mOTP algorithm](http://motp.sourceforge.net/), from the command-line,
without futzing around with your phone.

This is a confusing and seemingly-almost-obsolete standard(-ish?) algorithm for one-time
passwords that appears to mainly be used in German-speaking countries.

* Swiss SafeLab OTP authenticator for iOS: [on iTunes](https://itunes.apple.com/us/app/otp-authenticator/id915359210?mt=8)
* Swiss SafeLab OTP authenticator for Android: [APK download](https://www.swiss-safelab.com/en-us/products/otpauthenticator.aspx)
* Android app that supports this algorithm: [DroidOTP on Google Play Store](https://play.google.com/store/apps/details?id=net.marinits.android.droidotp&hl=de&rdid=net.marinits.android.droidotp)

How does it work?
=================

The principle of the algorithm is very simple: you have a token secret
(an ASCII string, usually hexadecimal or alphanumeric) and a PIN (an
ASCII string, usually 4 digits), and this is converted to a 6-digit
code using:

```
counter = ASCII((UNIX epoch time) / 10s)
digest = MD5HEX(counter || secret || pin)
code = LEFT(digest, 6 characters)
```

That's it. ¯\\\_\(ツ\)\_\/¯

Use it
======

Requires Python **3.x**.

```
$ ./motp.py SECRET PIN
a1b329
```

More verbosely:

```
$ ./motp.py -v SECRET PIN
Epoch time: 1549323786
Counter:    154932378

a1b329 (current)
```

All available options:

```
$ ./motp.py --help
usage: motp.py [-h] [-s SECONDS] [-l LENGTH] [-w WINDOW] [-v] secret pin

positional arguments:
  secret                mOTP secret value (often hex or alphanumeric digits)
  pin                   mOTP PIN value (usually 4 digits)

optional arguments:
  -h, --help            show this help message and exit
  -s SECONDS, --seconds SECONDS
                        Duration of mOTP codes in seconds (default 30 seconds)
  -l LENGTH, --length LENGTH
                        Length of mOTP output (default 6 characters)
  -w WINDOW, --window WINDOW
                        Number of counter values before and after current one
                        to show (for testing time-skew)
  -v, --verbose
```

License
=======

[MIT](LICENSE.txt)
