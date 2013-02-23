#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

"""res
REST it up with python. Use res to make command line http calls.

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
  -c --cookie=<cookie>      Defines cookies
  -x --proxy                Sends proxy dictionary with protocal as key and the port as value
  -i --include              Include headers
  -h --help                 Show this screen.
  -v --version              Show version.

"""

import colors
import sys, ast
import urllib2, urllib

from docopt import docopt

import requests
from requests.auth import HTTPBasicAuth

try: import json
except ImportError: import simplejson

def parse_dict(dictionary):
	try:
		return ast.literal_eval(dictionary)
	except SyntaxError, e:
		colors.print_error("res error in ***"+dictionary+"***: " + str(e))
		return None

def get_bytes(args):
	if args['--bytes'] == True:
		bytes = True
	else:
		bytes = False
	return bytes

def headers(args, url):
	if args['--include'] == True:
		page = urllib2.urlopen(url)
		print page.info()

def rest(args, method, url, bytes):
	if args['--proxy'] != None:
		proxy = parse_dict(args['--proxy'])
	else:
		proxy = None

	if args['--cookie'] != None:
		cookies = parse_dict(args['--cookie'])
	else:
		cookies = None

	if args['--params'] != None:
		params = parse_dict(args['--params'])
	else:
		params = None

	if args['--HEADER'] != None:
		headers = parse_dict(args['--HEADER'])
	else:
		headers = None

	if args['--auth'] != None:
		auth = parse_dict(args['--auth'])
		try:
			if auth.has_key('user') and auth.has_key('password'):
				user = auth['user']
				password = auth['password']
				auth = HTTPBasicAuth(user,password)
			else:
				colors.print_warning("res warning: Authorization keys invalid (correct format=> \"{'user':'<username>', 'password':'<password>'}\")")
				auth = None
		except AttributeError, e:
			colors.print_error('res error: ' + str(e))
	else:
		auth = None

	if args['--data'] != None:
		data = parse_dict(args['--data'])
	else:
		data = None

	r = requests.request(
		method, 
		url,
		params=params, 
		data=data, 
		headers=headers, 
		auth=auth,
		cookies=cookies,
		proxies=proxy
	)
	
	if bytes == True:
		print r.content
	else:
		print r.text

def main():
	allowed_methods = ['POST', 'GET', 'DELETE', 'PUT', 'post', 'get', 'delete', 'put']

	args = docopt(__doc__, argv=None, help=True, version='res v0.1.0', options_first=False)
	
	#####For all methods#####
	if any(args['<method>'] == val for val in allowed_methods):
		url = args['<url>']
		headers(args, url)
		bytes = get_bytes(args)

		rest(args, args['<method>'], url, bytes)
	else:
		colors.print_error('res error: <method> not valid')
	#########################

	sys.exit(1)
if __name__ == '__main__':
	main()