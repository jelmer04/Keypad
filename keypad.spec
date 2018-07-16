# -*- mode: python -*-

block_cipher = None


a = Analysis(['keypad.py'],
             pathex=['/Users/Jon/Projects/Keypad'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('share', prefix='share'),
          a.zipfiles,
          a.datas,
          name='keypad',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='Keypad.app',
             icon='share/Keypad.icns',
             bundle_identifier='red-box-labs.keypad',
             info_plist={
                 'LSUIElement': True,
                 'CFBundleName': 'Keypad',
                 'CFBundleDisplayName': 'Keypad',
                 'CFBundleGetInfoString': "Keypad emulator",
                 'CFBundleIdentifier': "red-box-labs.keypad",
                 'CFBundleVersion': '0.0.2',
                 'CFBundleShortVersionString': '0.0.2',
                 'NSHumanReadableCopyright': u"Copyright © 2018, Jon Elmer, All Rights Reserved"
             })
