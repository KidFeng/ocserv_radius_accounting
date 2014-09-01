# ocserv RADIUS accounting
Because ocserv (0.8.x) does not suppot RADIUS and the pam_radius just suppot RADIUS auth but not accounting, this scirpt implements RADIUS traffic counter with ocserv connect/disconnect-script hook.

## dependencies
[pyrad 2.0](https://pypi.python.org/pypi/pyrad)

## configuration
edit radacct.py to configure radius server infomation:
```
server = "your_server_ip"
secret = "your_server_secret"
dict_path = "/path/to/dictionary"
```
and edit ocserv.conf to use radacct.py
```
connect-script = /path/to/radacct.py
disconnect-script = /path/to/radacct.py
```

configure radius server dictionary files to suppot "AnyConnect" Framed-Protocol
* copy dictionary.anyconnect to radius dictionary folder, if you install radius from freeradius source, the path could be "/usr/local/share/freeradius".
* add the following line in file "dictionary" to include dictionary.anyconnect
```
$INCLUDE dictionary.anyconnect
```


