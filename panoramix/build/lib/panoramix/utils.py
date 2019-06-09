import os
import hashlib
import locale
import itertools
import base64
import random

system_random = random.SystemRandom()

ENCODING = locale.getpreferredencoding() or 'UTF-8'


def hash_string(s):
    return hashlib.sha256(s).hexdigest()


def show_serial(serial):
    s = "" if serial is None else str(serial)
    s += "|"
    return s


def hash_message(text, sender, recipient, serial):
    hasher = hashlib.sha256()
    hasher.update(show_serial(serial))
    hasher.update(utf8(text))
    hasher.update(utf8(sender))
    hasher.update(utf8(recipient))
    return hasher.hexdigest()


def utf8(s):
    if type(s) is unicode:
        return s.encode("UTF-8")
    return s


def locale_to_unicode(s):
    if type(s) is unicode:
        return s
    return unicode(s, ENCODING)


def unicode_to_locale(s):
    if type(s) is unicode:
        return s.encode(ENCODING)
    return s


def int_to_unicode(i):
    return unicode('%x' % i)


def unicode_to_int(u):
    return int(u, base=16)


def unzip(lst):
    aa = []
    bb = []
    for a, b in lst:
        aa.append(a)
        bb.append(b)
    return aa, bb


def with_recipient(messages, default=None):
    return zip(itertools.repeat(default), messages)


def generate_random_key():
    s = os.urandom(32)
    return base64.urlsafe_b64encode(s).rstrip('=')


def secure_shuffle(lst):
    random.shuffle(lst, random=system_random.random)


class NoProcessing(Exception):
    pass
