#-*-coding:utf-8-*-

import requests
import kerberos

#r = requests.get("http://dev-15")
#print(r.status_code)
#print(r.headers['www-authenticate'])

def www_auth(response):
     auth_fields = {}
     for field in response.headers.get("www-authenticate", "").split(","):
         kind, __, details = field.strip().partition(" ")
         auth_fields[kind.lower()] = details.strip()
     return auth_fields

#www_auth(r)

#__, krb_context = kerberos.authGSSClientInit("HTTP@dev-15.ald.dogmat.mil")
__, krb_context = kerberos.authGSSClientInit("HTTP@dev-15.ald.dogmat.mil")
kerberos.authGSSClientStep(krb_context, "")
negotiate_details = kerberos.authGSSClientResponse(krb_context)
print(negotiate_details)
headers = {"Authorization": "Negotiate " + negotiate_details}
r = requests.get("http://dev-15", headers=headers)
#req.addHeader("Authorization", "Negotiate " + negotiate_details)
print(r)
print(r.status_code)
print(r.text)