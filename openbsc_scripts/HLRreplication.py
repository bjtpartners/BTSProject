#!/usr/bin/python
#######################
import shutil,datetime,os

now = datetime.datetime.now()
now = '.'+str(now.day)+'.'+str(now.month)+'.'+str(now.year)+'.'+str(now.hour)+'h'+str(now.minute)

#########################
#### EDIT
#########################

HLRfile = 'hlr.sqlite3'
HLRfilesave = 'hlr'+now+'.sqlite3'
HLRfilelatest = 'hlr.latest.sqlite3'

HLRdir = '/dev/shm/'
HLRdirsave = '/home/OpenBSC/archives/'

#######################
#######################
#######################
#######################

shutil.copy2( HLRdir+HLRfile , HLRdir+HLRfilesave )

## Verify the path to save
if not os.path.exists(HLRdirsave):
	os.makedirs(HLRdirsave)

shutil.copy2( HLRdir + HLRfilesave , HLRdirsave + HLRfilelatest )
shutil.move( HLRdir + HLRfilesave , HLRdirsave + HLRfilesave )

#######################
