import PyInstaller.__main__


package_name = "The Spider Game"
PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--onedir',
    '--windowed',
    '--noconfirm',
    '--add-binary=bin;bin',
    '--add-binary=saves;saves',
    '--icon=icon.ico',
    'main.py',
])
