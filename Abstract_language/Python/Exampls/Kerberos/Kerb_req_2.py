#-*-coding:utf-8-*-

import requests

r = requests.get("http://dev-15")
#print("r.status_code =====", r.status_code)
#print("r.headers['www-authenticate'] =====", r.headers['www-authenticate'])

def www_auth(response):
     auth_fields = {}
     for field in response.headers.get("www-authenticate", "").split(","):
         kind, __, details = field.strip().partition(" ")
         auth_fields[kind.lower()] = details.strip()
     return auth_fields

#print("www_auth(r) =====", www_auth(r))


#-----------------------------------------------------------

from requests_kerberos import HTTPKerberosAuth, REQUIRED, OPTIONAL

def www_auth_1():

	kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, principal='off0103@ALD.DOGMAT.MIL:_off0103')
	#off0103@ALD.DOGMAT.MIL так работает, но если указать пароль в формате off0103@ALD.DOGMAT.MIL:_off0103 - то почему-то не работает. 
	#kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED)
	print(kerberos_auth.__dir__)

	r = requests.get("http://dev-14", auth=kerberos_auth)
	print("r.status_code =====", r.status_code, "http://dev-14/")



	print("\n---Headers---")
	headers = r.headers
	for key in headers.keys():
		print(str(key).ljust(40), ":::" ,str(headers[key]).ljust(60))

	print("\n---Cookies---")
	cookies_items = r.cookies.items()
	for key in cookies_items:
		print(str(cookies_items))



	r = requests.get("http://dev-14/dogmat/server-mgmt/index.php/positions", auth=kerberos_auth)

	print("\nr.status_code =====", r.status_code, "http://dev-14/dogmat/server-mgmt/index.php/positions\n")
	#print(r.text)
	#print(r.json)

www_auth_1()