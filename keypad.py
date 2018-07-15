# -- coding: utf-8 --

import keypad_app
import keypad_server


if __name__ == '__main__':

    svr = keypad_server.KeypadServer()

    application = keypad_app.StatusBarApp("Keypad", quit_button=None, server=svr)

    application.notify("App starting", "Click run server to begin")
    application.run()
