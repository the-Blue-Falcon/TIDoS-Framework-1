#!/usr/bin/env python2
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework 

import time, os, sys
sys.path.append('modules/VulnLysis/MiscBugs')

from icors import *
from ssscript import *
from clickjack import *
from zone import *
from vulnban1 import *
from webbugsban import *
from netmisc import *
from cloudflare import *
from headers import *
from colors import *
from xsstrace import *
from mailspoof import *
from cookiecheck import * 

def webbugs_alt(web):

    print W+'\n [*] Type Selected : Basic Web Bugs and Misconfigurations...'
    webbugsban()
    v = raw_input(O+B+' [#] \033[4mTID\033[1;0m '+GR+':> ' + color.END)
    print '\n'
    if v.strip() == '1':
	print B+' [!] Type Selected :'+C+' iCORS'
	icors(web)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '2':
	print B+' [!] Type Selected :'+C+' Same Site Scripting'
	ssscript(web)	
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '3':
	print B+' [!] Type Selected :'+C+' Clickjack'
	clickjack(web)	
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '4':
	print B+' [!] Type Selected :'+C+' Zone Transfer'
	zone(web)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '5':
	print B+' [!] Type Selected :'+C+' Cookie Check'
	cookiecheck(web)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '6':
	print B+' [!] Type Selected :'+C+' Sec. Headers'
	headers(web)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '7':
	print B+' [!] Type Selected :'+C+' Cloudflare Misconfig.'
	cloudflare(web)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '8':
	print B+' [!] Type Selected :'+C+' Cross Site Tracing'
	xsstrace(web)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '10':
	print B+' [!] Type Selected :'+C+' Telnet Enabled'
	netmisc(web)	
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '9':
	print B+' [!] Type Selected :'+C+' Cross Site Tracing'
	xsstrace(web)	
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == '11':
	print B+' [!] Type Selected :'+C+' Email Spoof'
	mailspoof(web)	
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
	webbugs_alt(web)

    elif v.strip() == 'A':
	print B+' [!] Type Selected : All Modules'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' iCORS'
	icors(web)
	print B+'\n [!] Module Completed -->'+C+' iCORS\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' SSS '
	ssscript(web)
	print B+'\n [!] Module Completed -->'+C+' SSS \n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' ClickJacking'
	clickjack(web)
	print B+'\n [!] Module Completed -->'+C+' ClickJacking\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Zone Transfer'
	zone(web)
	print B+'\n [!] Module Completed -->'+C+' Zone Transfer\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Cookie Check'
 	cookiecheck(web)
	print B+'\n [!] Module Completed -->'+C+' Cookie Check\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Security Headers '
	headers(web)
	print B+'\n [!] Module Completed -->'+C+' Security Headers \n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Cloudflare Misconfig.'
	cloudflare(web)
	print B+'\n [!] Module Completed -->'+C+' Cloudflare Misconfig.\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Mail Spoofing'
	mailspoof(web)
	print B+'\n [!] Module Completed -->'+C+' Mail Spoofing\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Cross Site Tracing'
	xsstrace(web)
	print B+'\n [!] Module Completed -->'+C+' Cross Site Tracing\n'
	time.sleep(1)

	print B+' [*] Firing up module -->'+C+' Telnet Enabled'
	netmisc(web)
	print B+'\n [!] Module Completed -->'+C+' Telnet Enabled\n'
	time.sleep(3)
	print G+B+' [+] All modules successfully completed!'
	time.sleep(1)
	raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')

    elif v.strip() == '99':
	print '[!] Back'
	time.sleep(0.7)

    else:
	print ''
	dope = ['You high dude?','Hey there! Enter a valid option','Whoops! Thats not an option','Sorry fam! You just typed shit']
	print dope[randint(0,3)]
	time.sleep(0.7)
	os.system('clear')
	webbugs_alt(web)

