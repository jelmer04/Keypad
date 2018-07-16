# -- coding: utf-8 --

import sys
import os, os.path

scd = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
print(scd)

#pyncdir = os.path.join(scd, 'Resources/share/pync')
#print(pyncdir)
#sys.path.append(pyncdir)

resources = os.path.join(scd, 'Resources/')
try:
    os.chdir(resources)
except:
    pass

import keypad_app
import keypad_server


if __name__ == '__main__':

    svr = keypad_server.KeypadServer()

    application = keypad_app.StatusBarApp("Keypad", quit_button=None, server=svr)

    application.notify("App starting", "Click run server to begin")
    application.run()
