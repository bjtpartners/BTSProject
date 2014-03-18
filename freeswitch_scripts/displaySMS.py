# -*- coding:utf-8 -*-
import os
from freeswitch import *

# Install mod_sms first

def handler(session, args):

	session.execute('info')
	session.destroy()
