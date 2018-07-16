# Keypad

Simple http num-pad emulator for macOS.



## Installation

 1. Download the latest [release](https://github.com/jelmer04/Keypad/releases).
 1. Unzip and run!


## Building for development

 1. Create a virtual environment for development [(see here.)](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/)
 1. Clone the repo with `git clone https://github.com/jelmer04/Keypad.git`
 1. Install the requirements `pip install -r requirements.txt`
 1. Install PyNC and from /share/pync with `python setup.py install`
 1. Build in alias mode with `python setup.py py2app -A`
 1. Or build for distribution with `python setup.py py2app` (don't forget to delete the build and dist folders which switching between modes)
