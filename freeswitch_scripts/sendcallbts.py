# -*- coding:utf-8 -*-
import os
from freeswitch import *
import sqlite3

# work well with OPENBSC

def toBTS( extension ):

	# PATH to HLR
	HLR = "/dev/shm/hlr.sqlite3"

	inhlr = 0
	conn = sqlite3.connect( HLR )
	c = conn.cursor()
	c.execute("SELECT id FROM Subscriber WHERE lac = '1' AND extension LIKE '"+str(extension)+"'")
	
	for each in c:
		consoleLog('4',"\n\n DEBUG : "+str(each[0])+"\n\n")
		if each[0]:
			inhlr = 1
		else :
			inhlr = 0
	
	conn.close()
	return inhlr
	


def handler(session, args):

	# BTS IP
	bts_IP = "127.0.0.1:5050"
        
	bnumber = session.getVariable('destination_number')
        anumber = session.getVariable('caller_id_number')

	# User in HLR	
	if toBTS( str(bnumber) ):
		
		session.execute('bridge', '{ignore_early_media=true,origination_caller_id_number='+str(anumber)+'}sofia/external/sip:'+str(bnumber)+'@'+str(bts_IP))
                session.hangup()

	# ELSE send it to the default gateway
	else:
		session.execute('bridge', '{ignore_early_media=true,origination_caller_id_number='+str(anumber)+'}sofia/gateway/GATEWAYNAME/'+str(bnumber))
		session.hangup()
	
	session.destroy()


