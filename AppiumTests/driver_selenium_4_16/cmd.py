import os
import subprocess

x = subprocess.getoutput('adb shell am force-stop com.android.vending')
y = subprocess.getoutput('adb devices')
get_chrome_versions_from_device = os.popen(
            "adb shell dumpsys package com.google.android.webview | grep versionNam"
        ).read()
# print(x, y, sep="\n")
print(get_chrome_versions_from_device)
