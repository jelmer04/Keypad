# -- coding: utf-8 --

import json
import socket
from keyboard import send
import cherrypy
from cherrypy.lib import auth_digest
import os, os.path
import rumps, objc
import pync

notifier = pync.Notifier


keys = ['.', 0x47, 0x51, 0x4B, 0x43, 0x59, 0x5B, 0x5C, 0x4E, 0x56,
        0x57, 0x58, 0x45, 0x53, 0x54, 0x55, 0x4C, 0x52, 0x41]
user = {'user': 'password'}
cwd = os.path.abspath(os.getcwd())

# work around for notifications:
def notification(title, line_one, line_two):

    notifier.notify(line_two, subtitle=line_one, title=title,
                    sender="org.pythonmac.unspecified.keypad")

running = False

cherrypy.config.update({
     'global': {
        'environment' : 'production'
      }
 })

class Keypad(object):
    @cherrypy.expose
    def index(self):
        return open(cwd+'/share/index.html')

@cherrypy.expose
class KeypadWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return "This is the generator"

    def POST(self):
        send(keys[int(key_index)])

    def PUT(self, key_index):
        send(keys[int(key_index)])

    def DELETE(self):
        pass

def load_config():
    print("*** Loading config from file ***")
    jsonify_quotes(cwd+'/share/config.json')

    j = json.loads(open(cwd+"/share/config.json").read())

    user = {str(j["user"]): str(j["pass"])}

    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.server.socket_port = int(j["port"])

    print("*** Setting up server ***")

    ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
    print("*** Navigate to {}:{} on your device ***".format(ip, cherrypy.server.socket_port))

    conf = {
        '/': {
            'tools.sessions.on': True,
            #'tools.staticdir.root': cwd,

            'tools.auth_digest.on': True,
            'tools.auth_digest.realm': 'localhost',
            'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(user),
            'tools.auth_digest.key': 'a565c27146791cfb'
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': cwd+'/share/public'
        },
        '/favicon.ico': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': cwd+'/share/Keypad.ico'
        }
    }
    webapp = Keypad()
    webapp.generator = KeypadWebService()
    cherrypy.tree.mount(webapp, '/', conf)

    print("*** Server ready ***")

    return "{}:{}".format(ip, cherrypy.server.socket_port)

def jsonify_quotes(filename):
    os.system("sed s/[”“]/'\"'/g {} > {}.clean".format(filename, filename))
    os.system("mv {}.clean {}".format(filename, filename))


if __name__ == '__main__':

    class StatusBarApp(rumps.App):
        @rumps.clicked("Edit config file")
        def prefs(self, _):
            os.system("open -e "+cwd+"/share/config.json")

        @rumps.clicked("Run server")
        def onoff(self, sender):
            sender.state = not sender.state
            if sender.state:
                self.icon=cwd+"/share/Keypad.icns"
                address = load_config()
                cherrypy.engine.start()
                notification("Keypad", "Server started", "Navigate to {} on your device".format(address))
                running = True

            else:
                self.icon=cwd+"/share/Disabled.icns"
                notification("Keypad", "Server stopped", "Click run server to begin")
                cherrypy.engine.exit()
                running = False

        @rumps.clicked('Quit')
        def clean_up_before_quit(self, _):
            print '*** Quitting ***'
            if running:
                notification("Keypad", "Server stopped", "Application closed")
                cherrypy.engine.exit()
            rumps.quit_application()

    notification("Keypad", "App starting", "Click run server to begin")
    app = StatusBarApp("Keypad", icon=cwd+"/share/Disabled.icns", quit_button=None)
    app.run()
