from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import helpers
from googleplay_api.googleplay import GooglePlayAPI
import axmlparserpy.apk as apk
ap = apk.APK('Apps/temp.apk')

request =ap.get_package()

# read config from config.py
config = GooglePlayAPI.read_config()

# connect to GooglePlayStore
api = GooglePlayAPI(config['ANDROID_ID'])
api.login(config['GOOGLE_LOGIN'], config['GOOGLE_PASSWORD'], config['AUTH_TOKEN'])

message = api.search(request, 1, None)

helpers.print_header_line()
doc = message.doc[0]
for c in doc.child:
    helpers.print_result_line(c) 