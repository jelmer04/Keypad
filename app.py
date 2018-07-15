# -- coding: utf-8 --

import rumps, objc
import pync
import os.path

# TODO: remove the need for this!!
import cherrypy

cwd = os.path.abspath(os.getcwd())

class StatusBarApp(rumps.App):
    def __init__(self, *args, **kwargs):

        self.enabled_icon=cwd+"/share/Keypad.icns"
        self.disabled_icon=cwd+"/share/Disabled.icns"
        kwargs['icon'] = self.disabled_icon

        try:
            self.server = kwargs.pop("server")
        except KeyError:
            print("server not supplied")
            self.server = type('dummy_server', (object,),
                 {'start':lambda *args: 0,
                  'stop':lambda *args: 0,
                  'running':None})()


        super(StatusBarApp, self).__init__(*args, **kwargs)

        self.notifier = pync.Notifier
        self.server_running = False

    @rumps.clicked("Edit config file")
    def prefs(self, _):
        os.system("open -e "+cwd+"/share/config.json")

    @rumps.clicked("Run server")
    def onoff(self, sender):
        sender.state = not sender.state
        if sender.state:
            self.icon=self.enabled_icon
            address = self.server.start()
            self.notify("Server started", "Navigate to {} on your device".format(address))
            self.server_running = True

        else:
            self.icon=self.disabled_icon
            self.notify("Server stopped", "Click run server to begin")
            self.server.stop()
            self.server_running = False

    @rumps.clicked('Quit')
    def clean_up_before_quit(self, _):
        print '*** Quitting ***'
        if self.server.running:
            self.notify("Server stopped", "Application closed")
            self.server.stop()
        rumps.quit_application()

    def notify(self, subtitle, message=None):
        if message is not None:
            self.notifier.notify(message, subtitle=subtitle, title=self.name,
                    sender="red-box-labs.keypad")
        else:
            self.notifier.notify(subtitle, title=self.name,
                    sender="red-box-labs.keypad")
