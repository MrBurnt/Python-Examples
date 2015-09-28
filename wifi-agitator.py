import os
import time
Ip = "192.168.1.1" #name of your router
#response = os.system("ping -c 1 -W 1 " + routerIP) 
count = 0

#pings one time, only waits 1 second for a response
def ping(Ip):
	return os.system("ping -c 1 -W 1 " + Ip) 

while True:
#pings your router once a second, for ever	
	if ping(Ip) == 0:
		print ''  		
		print 'Wifi is working'
		time.sleep(1)
	else:
		print ''   		
		print 'Wifi busy :( ' + str(count)
	

	count = count + 1	#debugging
	if count > 100: count = 0
