# res
A tiny command-line HTTP client. Easily interact with HTTP calls at a faster speed within your terminal. Built on top of the requests library and meant to be a command line wrapper for requests. 

Current version: v0.1.7

```
res v0.1.7

HTTP it up with python. Use res to make command line http calls. I made this to make
the development of my REST API to be a little bit easier.

Usage:
  res (-h | --help)
  res (-v | --version)
  res <method> <url> [options]

Options:
  -d --data=<data>          Send request data
  -H --HEADER=<header>      Defines custom headers
  -a --auth=<auth>          Authenticaton with 'user' and 'password' keys
  -p --params=<params>      Send request parameters
  -b --bytes                Returns content response in bytes
  -r --raw                  Returns content response in raw format
  -j --json                 Decodes content response from json
  -c --cookie=<cookie>      Defines cookies
  -x --proxy=<proxy>        Sends proxy with protocal as key and the port as value
  -i --include              Include headers
  -h --help                 Show this screen.
  -v --version              Show version.
```

# Install
To download and install res, you must follow the instructions below.

### Install via PIP
```
$ pip install res
```

### Install via setup.py
First you need to get a copy of the source. I'm going to use git and clone it to my local machine. 

Clone the repository into a folder
```
git clone https://github.com/jawerty/res.git res
```

Install with setup.py
```
$ cd res
$ python setup.py install
```

# Usage
Example GET, POST, PUT and DELETE calls
```
$ res GET http://example.com

$ res POST http://example.com

$ res PUT http://example.com

$ res DELETE http://example.com
```

Include headers
```
$ res GET http://example.com -i
```

Send request data to the body
```
$ res POST http://example.com -d "{
						'Hello':'World',
						'REST':'API'
					}"
```

Authorization
```
$ res POST http://example.com -a "{
						'user':'jawerty',
						'password':'noneofyourbusiness'
					}"
```

Parameters
```
$ res POST http://example.com -p "{ 'q':'names' }" 
```

### Change data response content (new in v0.1.7)

Binary response -> bytes 
```
$ res GET http://example.com -b
```
or
```
$ res GET http://example.com --bytes
```


Raw socket response -> raw
```
$ res GET http://example.com -r
```
or
```
$ res GET http://example.com --raw
```


JSON response decoder -> json
```
$ res GET http://example.com -j
```
or
```
$ res GET http://example.com --json
```

### Interactive Console
The interactive console current (v0.1.7) cannot pass any arguments that require dictionaries (i.e. --data, --proxy, --cookie, etc.). However, arguments like --bytes, --encoding, --raw, etc., are allowed.
```
$ res console
>>> get http://example.com -e `// -e is for encoding`
UTF-8
>>> get http://example.com
`response content....`
>>>
```

There are even more HTTP options that are compatible with res. Run the command at `$ res -h` to see all of the functions res wraps around.

# Contact
If you would like to contact me for further information on the project, see the info below.

Email: jawerty210@gmail.com

Github: jawerty

Twitter: @jawerty

Blog: <http://wrightdev.herokuapp.com>
