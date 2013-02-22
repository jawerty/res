# res
A tiny command-line HTTP client. Easily interact with REST APIs at a faster speed within your terminal. Built on top of the requests library and meant to be a command line wrapper for requests. 

Current version: v0.1.0

```
REST it up with python. Use res to make command line http calls.

Usage:
  res (-h | --help)
  res (-v | --version)
  res <method> <url> [options]

Options:
  -d --data=<data>          Send request data
  -H --HEADER=<header>      Defines custom headers
  -a --auth=<auth>          Authenticaton
  -p --params=<params>      Send request parameters
  -b --bytes                Returns content response in bytes
  -c --cookie=<cookie>      Defines cookies
  -i --include              Include headers
  -h --help                 Show this screen.
  -v --version              Show version.
```

# Install
To download and install res, you must follow the instructions below.

## Install via PIP
```
$ pip install res
```

## Install via setup.py
First you need to get a copy of the source. I'm going to use git and clone it to my local machine. 

Clone the repository into a folder
```
git clone https://github.com/jawerty/res.git res
```

Install via setup.py
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
$ res POST http://example.com -p "{ 'q':'names' } "
```

There are many more HTTP options to use with res. Run the command at `$ res -h` to see all of the functions res wraps around.

# Contact
If you would like to contact me for further information on the project, see the info below.

Email: jawerty210@gmail.com

Github: jawerty

Twitter: @jawerty

Blog: <http://wrightdev.herokuapp.com>
