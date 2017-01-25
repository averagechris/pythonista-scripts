#!python3

import clipboard
import re
import sys
import webbrowser

from urllib.parse import quote_plus


DEBUG = True


def admin_search(query, EB_ENV):
	parsed_query = parse_query_string(query, "admin")
	EB_PATH = "admin/search/?search_query=" + quote_plus(parsed_query)
	safari_open_eb_url(EB_ENV, EB_PATH, "admin")
	

def order_lookup(query_string, EB_ENV):
	ID = parse_query_string(query_string, "order_id")
	EB_PATH = "admin/orderinfo/?order_id=" + ID
	safari_open_eb_url(EB_ENV, EB_PATH, EB_SUBDOMAIN="admin")
	
def manage_page(query_string, EB_ENV):
	ID = parse_query_string(query_string, "event_id")
	EB_PATH = "myevent?eid=" + ID
	safari_open_eb_url(EB_ENV, EB_PATH)
	
	
def edit_page(query_string, EB_ENV):
	ID = parse_query_string(query_string, "event_id")
	EB_PATH = "edit?eid=" + ID
	safari_open_eb_url(EB_ENV, EB_PATH)
	
	
def parse_query_string(string, kind):
	if kind == "event_id":
		ID = re.search(r"\b[0-9]{11}\b", string)
		if ID:
			return ID.group(0)

		print("cannot parse input:", string)
		sys.exit()

	elif kind == "order_id":
		ID = re.search(r"\b[0-9]{9}\b", string)
		if ID:
			return ID.group(0)
			
		print("cannot parse input:", string)
		sys.exit()
		
	elif kind == "admin":
		ID = re.search(r"\b[0-9]{11}\b", string)
		if ID:
			return ID.group(0)
			
		ID = re.search(r"\b[0-9]{9}\b", string)
		if ID:
			return ID.group(0)
		
		return string
		
	else:
		print("cannot parse input:", string)
		sys.exit()
		
		
def safari_open_eb_url(EB_ENV, EB_PATH, EB_SUBDOMAIN="www"):
	URL = "safari-https://" + EB_SUBDOMAIN + "." + EB_ENV + ".com/" + EB_PATH
	if DEBUG:
		print(URL)
	webbrowser.open(URL)
	
	
def main():
	if len(sys.argv) < 2:
		EB_FUNCTION = "order_lookup"
		EB_ENV = "eventbrite"
	else:
		EB_FUNCTION = sys.argv[1]
		EB_ENV = sys.argv[2]

	if EB_FUNCTION == "admin":
		admin_search(clipboard.get(), EB_ENV)
	elif EB_FUNCTION == "order_lookup":
		order_lookup(clipboard.get(), EB_ENV)
	elif EB_FUNCTION == "manage":
		manage_page(clipboard.get(), EB_ENV)
	elif EB_FUNCTION == "edit":
		edit_page(clipboard.get(), EB_ENV)

if __name__ == "__main__":
	main()
