# Tavendo WebMQ Portable EXEs

This builds and uploads the portable executable versions of Tavendo WebMQ:

  * [Tavendo WebMQ (Portable Windows EXE)](https://webmq.s3.amazonaws.com/webmq.exe)
  * [Tavendo WebMQ for Oracle (Portable Windows EXE)](https://webmq.s3.amazonaws.com/webmqora.exe)

## Release

To build and upload, make sure the release version of WebMQ is installed locally

	cd webmq
    python setup.py install

Then

	make release


# Prerequisites

## Pyinstaller

We are using the development version of Pyinstaller from [here](https://github.com/pyinstaller/pyinstaller/zipball/develop).

Unzip the file to `C:\pyinstaller`.

Alternative:

    git clone git://github.com/pyinstaller/pyinstaller.git

## Boto

Install the Python Amazon S3 API by doing

	easy_install boto

You will need to provide S3 credentials by creating a file

	C:\Users\oberstet\.boto

with content

	[Credentials]
	aws_access_key_id = XXXXX
	aws_secret_access_key = XXXXX
	
obviously replacing XXXX with our AWS credentials.

# Issues

Patches definitely needed and applied:

1. Pyinstaller does not handled `pkg_resources` other when included in *egg*. Hence, adjusted the `setup.py` to `zip_safe = True` (unsure why I didn't specify that in the first place anyway).

2. Werkzeug is doing some magic importing, see the workaround [here](https://github.com/mitsuhiko/werkzeug/issues/221)

3. On CentOS, I need to extract the egg files for `pycrypto` and `cx_Oracle` within `site-packages`

Patches I experimented with, but are no longer applied:

1. Our monkey patching of `__builtin__.open = io.open` was at least at some point breaking stuff

2. At least at some point, I needed to add a `import encodings` to avoid breaking stuff

