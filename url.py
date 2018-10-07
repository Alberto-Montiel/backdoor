victima = raw_input("url: ") 

if victima.startswith("http://"): # si url empieza con http://
	print "url es http"

elif victima.startswith("https://"): # si url empieza con https://
	print "url tipo https"

else:
	print "url no es http ni https"