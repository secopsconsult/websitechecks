#!/usr/bin/env python

''' 
Script to check for the presence of Security headers and rate the site

More info:
https://securityheaders.io/

'''

import optparse
import mechanize
import tkinter

def validateHeaders(header, debug):
	if (debug):
		print "[+] Validating headers"
		print "[~] Headers: " + str(header)

	if (debug):
		if (len(header.getheaders('Public-Key-Pins')) > 0):
			print "[+] HPKP Header: Header not Empty"
	if (len(header.getheaders('Public-Key-Pins')) > 0):
		print "[+] HPKP Header: " + str(header.getheaders('Public-Key-Pins')[0])
	else:
		print "[~] No HPKP Header present"

	if (debug):
		if (len(header.getheaders('Content-Security-Policy')) > 0):
			print "[+] CSP Header: Header not Empty"
	if (len(header.getheaders('Content-Security-Policy')) > 0):
		print "[+] CSP Header: " + str(header.getheaders('Content-Security-Policy')[0])
	else:
		print "[~] No CSP Header present"

        if (debug):
		if (len(header.getheaders('Strict-Transport-Security')) > 0):
			print "[+] HSTS Header: Header not Empty"
	if (len(header.getheaders('Strict-Transport-Security')) > 0):
		print "[+] HSTS Header: " + str(header.getheaders('Strict-Transport-Security')[0])
	else:
		print "[-] No HSTS Header present"

	return

def viewPage(url, agent, debug):
	if ((url.startswith("http://") == False) and (url.startswith("https://") == False)):
		url = "https://" + url	

	if (debug):
		print "[+] Browsing : "  +url.strip() +" As " + agent.strip()

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent',agent)]
	browser.addheaders = [('Accept','test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
	browser.set_handle_refresh(False)
	        
        try:
		page = browser.open(url.strip())
		if (debug):
			print "[+] Response Code: " +str(page.code)
			
		return page.info()
	finally:
		return page.info()
	
	
def main():

	# Options for the script
	parser = optparse.OptionParser('Usage %prog% ' + " -u <url> -a <agent>")
        parser.add_option('-u', dest='url', type='string', help='Specify the URL')	
	parser.add_option('-a', dest='agent', type='string', help='Specify the user agent')
	parser.add_option('-d', dest='debug', action="store_true", default=False, help='Debug Mode')
	
	(options, args) = parser.parse_args()
	
	
	if (options.url == None):
		print parser.usage
		exit(0)
	if (options.agent == None):
		if (options.debug):
			print "[-] No Useragent Set. Defaulting to Mozilla"
		options.agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"	
	
	header = viewPage(options.url, options.agent, options.debug)
	validateHeaders(header, options.debug)
	

if __name__ == '__main__':

        main()
        
