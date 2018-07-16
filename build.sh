pyinstaller -w -y --hiddenimport email.mime.message keypad.spec
cp -r share/ dist/keypad.app/Contents/Resources/share
cd ./dist
zip -r ../Keypad.zip ./Keypad.app
cd ../
echo "Done"
