import ldap, sys,ldif
import base64
import hashlib
from SearchResult import LDAPSearchResult
server = 'LDAP://ldap.dlcloud.info'
l = ldap.initialize(server)
# try:
#     l.start_tls_s()
# except ldap.LDAPError as e:
#     print(e)

#验证dn与pw是否正确，97为正确，错误则抛出异常
dn = "cn=admin,dc=dlcloud,dc=info"
pw = "blcc@asc161"
# dn = "cn=xin wang,ou=People,dc=dlcloud,dc=info"
# pw = "123456"
try:
    bind = l.simple_bind_s(dn, pw)
    print(bind)
except ldap.LDAPError as e:
    print(e)
base_dn = 'ou=people,dc=dlcloud,dc=info'
# filter = '(objectclass=inetOrgPerson)'
filter = 'uid=xwang' 
# attrs = ['sn','password']
attrset = l.search_s(base_dn, ldap.SCOPE_SUBTREE, filter)

def get_search_results(results):
    """Given a set of results, return a list of LDAPSearchResult
    objects.
    """
    res = []
    if type(results) == tuple and len(results) == 2 :
        (code, arr) = results
    elif type(results) == list:
        arr = results

    if len(results) == 0:
        return res

    for item in arr:
        res.append( LDAPSearchResult(item) )

    return res

res = get_search_results(attrset)
print(res[0].get_dn())
print(res[0].get_attr_values('userpassword'))
try:
    bind = l.simple_bind_s(res[0].get_dn(), '123451')
    print(bind)
except ldap.LDAPError as e:
    print(e)

def hash_md5(data):         
    md = hashlib.md5()
    md.update(str(data).encode(encoding='UTF-8'))
    a = md.digest()
    b = '{MD5}' +  str(base64.b64encode(a))
    return b
print(hash_md5('123456'))

# print(LDAPSearchResult(attrset))
# attr_name = 'sn'
# attr_val = 'wang'
# l.compare_s(dn, attr_name, attr_val)
    # print(e.message['info']   )
    # if type(e.message) == dict and e.message.has_key('desc'):
    #     print(e.message['desc'])   
    # else:
    #     print(e)

