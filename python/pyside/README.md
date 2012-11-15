## Building self-contained EXEs of Python QT apps using PySide and PyInstaller

This rocks! It's incredible easy.

1. Install [PySide](http://qt-project.org/wiki/PySide)

    easy_install pyside

2. Install PyInstaller by unzipping [this](https://github.com/downloads/pyinstaller/pyinstaller/pyinstaller-2.0.zip) to `C:\pyinstaller`

3. Build your app

    python c:\pyinstaller\pyinstaller.py --onefile --windowed test.py

This will leave a `dist/test.exe` which is *completely* self-contained (it runs from a USB stick!).