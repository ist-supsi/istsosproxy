# istsosproxy
Secure Istsos token managment through a server side proxy

# Settings

Add not versioned file `settings_private.py` whith the following content adapted:

```py
# logger settings
LOGGERS = [
    "info:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

ISTSOS_SERVICES = 'ceresiohourly'
ISTSOS_USERNAME = '<username>'
ISTSOS_PASSWORD = '<password>'

```