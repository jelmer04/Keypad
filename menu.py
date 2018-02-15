import rumps
import os

class StatusBarApp(rumps.App):
    @rumps.clicked("Edit config file")
    def prefs(self, _):
        os.system("open -e "+"share/config.json")

    @rumps.clicked("Run server")
    def onoff(self, sender):
        sender.state = not sender.state
        if sender.state:
            rumps.notification("Keypad", "Server started", "Navigate to 0.0.0.0 on your device")

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
    StatusBarApp("Keypad").run()
