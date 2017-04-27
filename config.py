# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from __future__ import unicode_literals

LANG            = "en_US" # can be en_US, fr_FR, ...
ANDROID_ID      = "33ad1b61974cab0e" # "38c6523ac43ef9e1"
GOOGLE_LOGIN    = 'subham.jodha@gmail.com'
GOOGLE_PASSWORD = 'subhamjodha12345'
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if ANDROID_ID == None or all([each is None for each in [GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN]]):
    raise Exception("config.py not updated")

