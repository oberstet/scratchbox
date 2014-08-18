# When on Windows and starting GNU make from Git bash, we need to set this:
ifdef COMSPEC
   SHELL=C:/Windows/System32/cmd.exe
endif

all:
	@echo Targets:
	@echo    windows          Build WebMQ EXE Windows
	@echo    windows_oracle   Build WebMQ for Oracle EXE Windows
	@echo    linux            Build WebMQ EXE Linux
	@echo    linux_oracle     Build WebMQ for Oracle EXE Linux
	@echo    clean            Clean everything
	@echo    upload           Upload build artifacts to Amazon S3
	@echo    release          Clean, build and upload artifacts

windows:
	python c:\pyinstaller\pyinstaller.py --onefile --icon=tavendo.ico spec_webmq_windows.spec

windows_oracle:
	python c:\pyinstaller\pyinstaller.py --onefile --icon=tavendo.ico spec_webmq_windows_oracle.spec

linux:
	python c:\pyinstaller\pyinstaller.py --onefile --icon=tavendo.ico spec_webmq_linux.spec

linux_oracle:
	python c:\pyinstaller\pyinstaller.py --onefile --icon=tavendo.ico spec_webmq_linux_oracle.spec

clean:
	rm -rf ./dist
	rm -rf ./build
	rm -f *.log

upload:
	python upload.py

release: clean windows windows_oracle upload
