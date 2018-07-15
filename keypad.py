# -- coding: utf-8 --

import app

import server


if __name__ == '__main__':

    svr = server.KeypadServer()

    application = app.StatusBarApp("Keypad",
                                   quit_button=None, server=svr,
                                   )

    application.notify("App starting", "Click run server to begin")
    application.run()
