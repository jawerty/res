HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def print_warning(text):
	print WARNING+text+ENDC

def print_header(text):
	print HEADER+text+ENDC
	
def print_error(text):
	print FAIL+text+ENDC