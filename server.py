# -- coding: utf-8 --

import json
import socket
from keyboard import send
import cherrypy
from cherrypy.lib import auth_digest

import os, os.path
cwd = os.path.abspath(os.getcwd())


cherrypy.config.update({
     'global': {
        'environment' : 'production'
      }
 })


@cherrypy.expose
class KeypadWebService(object):

    def __init__(self):
        self.keys=['.',
                   0x47, 0x51, 0x4B, 0x43,
                   0x59, 0x5B, 0x5C, 0x4E,
                   0x56, 0x57, 0x58, 0x45,
                   0x53, 0x54, 0x55, 0x4C,
                   0x52,       0x41]

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return "This is the generator"

    # TODO: handle bad key_index
    def POST(self):
        send(self.keys[int(key_index)])

    def PUT(self, key_index):
        send(self.keys[int(key_index)])

    def DELETE(self):
        pass


class KeypadServer(object):
    def __init__(self):
        self.running = False
        self.generator = KeypadWebService()

    def start(self):
        print("*** Setting up server ***")

        conf, port = load_config()

        cherrypy.tree.mount(self, '/', conf)
        print("*** Mounted ***")

        cherrypy.server.socket_host = "0.0.0.0"
        cherrypy.server.socket_port = port
        print("*** Socket set ***")

        cherrypy.engine.start()

        self.running = True

        print("*** Server ready ***")

        ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
        port = cherrypy.server.socket_port

        print("*** Navigate to {}:{} on your device ***".format(ip, port))


        return "{}:{}".format(ip, cherrypy.server.socket_port)

    def stop(self):
        cherrypy.engine.exit()


    @cherrypy.expose
    def index(self):
        return open(cwd+'/share/index.html')



def load_config():

    # TODO: handle errors in input!!
    print("*** Loading config from file ***")
    jsonify_quotes(cwd+'/share/config.json')

    j = json.loads(open(cwd+"/share/config.json").read())

    user = {str(j["user"]): str(j["pass"])}

    port = int(j["port"])

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

    return conf, port


def jsonify_quotes(filename):
    os.system("sed s/[”“]/'\"'/g {} > {}.clean".format(filename, filename))
    os.system("mv {}.clean {}".format(filename, filename))
