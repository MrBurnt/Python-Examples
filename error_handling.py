#! python3
#      ERROR HANDLING     
#       MAKIN YOUR OWN ERROR DEFINITIONS     

try:
	i=1/0
except:
	print("that's impossible")

raise Exception('Error message that explains what went wrong!')