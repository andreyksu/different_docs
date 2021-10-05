#-*-coding:utf-8-*-

import requests
import kerberos

from krbcontext.context import krbContext

from subprocess import Popen, PIPE

def print_auth_headers_via_response(response):
     auth_fields = {}
     for field in response.headers.get("www-authenticate", "").split(","):
         kind, __, details = field.strip().partition(" ")
         auth_fields[kind.lower()] = details.strip()
     return auth_fields

#--------------------------------------------
def www_auth():
	r = requests.get("http://dev-15")
	print(r.status_code)
	print_headers_via_response(r)

#www_auth()

def www_auth_1():
	#__, krb_context = kerberos.authGSSClientInit("HTTP@dev-15.ald.dogmat.mil")
	__, krb_context = kerberos.authGSSClientInit("HTTP@dev-15.ald.dogmat.mil")#Не очень понятно что это, запрашиваем доступ к credential apache?
	kerberos.authGSSClientStep(krb_context, "")
	negotiate_details = kerberos.authGSSClientResponse(krb_context)
	print(negotiate_details)
	headers = {"Authorization": "Negotiate " + negotiate_details}
	r = requests.get("http://dev-15", headers=headers)
	print(r)
	print(r.status_code)
	print(r.text)
	print_headers_via_response(r)

#www_auth_1()

#TODO: Нужно будет разобраться с этими частями. Т.е. получение tgt через keytab.
def www_auth_2():
	with krbContext(using_keytab=True, principal='[username]@[REALM]', keytab_file='/etc/security/keytabs/[name].keytab', ccache_file='/tmp/krb5cc_pid_appname'):
    	pass

def www_auth_3():
	kinit_args - [ '/usr/bin/kinit', '-kt', '/home/username/username.keytab', 'username@realm' ]
	subp = Popen(kinit_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	subp.wait()