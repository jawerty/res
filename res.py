#!/usr/bin/env python

"""
res v0.1.7

HTTP it up with python. Use res to make command line http calls. I made this to make the development of my REST API to be a little bit easier.

Usage:
  res console
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
  -e --encoding             Return encoding of content
  -i --include              Include headers
  -h --help                 Show this screen.
  -v --version              Show version.
  
"""

import colors
import sys, ast, re
import urllib2, urllib

from docopt import docopt

import requests
from requests.auth import HTTPBasicAuth

try: import json
except ImportError: import simplejson


def parse_options(args):
	if args['--raw'] == True:
		raw = True
	else:
		raw = False	

	if args['--bytes'] == True:
		bytes = True
	else:
		bytes = False

	if args['--json'] == True:
		json = True
	else:
		json = False

	if args['--encoding'] == True:
		encoding = True
	else:
		encoding = False

	return raw, bytes, json, encoding

def parse_dict(dictionary):
	try:
		return ast.literal_eval(dictionary)
	except SyntaxError, e:
		colors.print_error("res error in ***"+dictionary+"***: " + str(e))
		return None

def headers(args, url):
	if args['--include'] == True:
		page = urllib2.urlopen(url)
		print page.info()

def http(args, method, url, bytes, raw, json, encoding):
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
		proxies=proxy,
		stream=raw
	)
	
	if bytes == True:
		print r.content
	elif raw == True:
		print r.raw
	elif json == True:
		try:
			print r.json()
		except ValueError, e:
			colors.print_error('res error: ' + str(e)) 
	elif encoding == True:
		print r.encoding
	else:
		print r.text

def run(args, allowed_methods, cmd=None):
	if any(args['<method>'] == val for val in allowed_methods):
		url = args['<url>']
		headers(args, url)
		raw, bytes, json, encoding = parse_options(args)
		http(args, args['<method>'], url, bytes, raw, json, encoding)
	else:
		if not args['<method>'] == None:
			colors.print_error('res error: <method> not valid')

def main():
	allowed_methods = ['POST', 'GET', 'DELETE', 'PUT', 'post', 'get', 'delete', 'put']
	args = docopt(__doc__, argv=sys.argv[1:], help=True, version='res v0.1.7', options_first=False)

	#########Run in interactive shell#########
	if args['console'] == True:
		while True:
			sys.stdout.write(">>> ")
			cmd_raw = raw_input()
			cmd = re.sub("[,]", " ",  cmd_raw).split()

			#the console can only run these options
			if '--bytes' in cmd or '-b' in cmd:
				args['--bytes'] = True
			else:
				args['--bytes'] = False

			if '-raw' in cmd or '-r' in cmd:
				args['--raw'] = True
			else:
				args['--raw'] = False

			if '--json' in cmd or '-j' in cmd:
				args['--json'] = True
			else:
				args['--json'] = False

			if '--encoding'in cmd or '-e' in cmd:
				args['--encoding'] = True
			else:
				args['--encoding'] = False


			if cmd[0]:
				args['<method>'] = cmd[0] 

			if cmd[1]:
				args['<url>'] = cmd[1]

			dict.fromkeys([args['--auth'], args['--cookie'], args['--data'], args['--params'], args['--proxy'], args['--HEADER']], None)
			run(args, allowed_methods)
	##########################################

	else:
		#####Run in normal mode#####
		run(args, allowed_methods)
		#############################

	sys.exit(1)
if __name__ == '__main__':
	main()