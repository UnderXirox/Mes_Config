#!/usr/bin/env pytohn

# fonction de calcule des hash

import hashlib

def sumFileMD5(filePath):
	fichier = open(filePath, 'r')
	c = hashlib.md5()
	while 1:
		try:
			d = fichier.next()
			c.update(d)
		except: break
	fichier.close()
	return c.hexdigest()

def sumFileSHA1(filePath):
	fichier = open(filePath, 'r')
	c = hashlib.sha1()
	while 1:
		try:
			d = fichier.next()
			c.update(d)
		except: break
	fichier.close()
	return c.hexdigest()

md5 = sumFileMD5('')
sha1 = sumFileSHA1('')
 
print "Empreinte md5 = %s"%md5
print "Empreinte sha1 = %s"%sha1
	
