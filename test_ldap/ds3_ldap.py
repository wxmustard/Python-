import ldap
ldapServer = 'LDAP://ldap.dlcloud.info'
# base 域
base='dc=dlcloud,dc=info'
userName = 'cn=admin'
domainUserName = userName + ',' + base
password = 'blcc@asc161'
test_user = 'dc=dlcloud,dc=info,ou=people,cn=demo'
try:
    conn = ldap.initialize(ldapServer)
    # conn.start_tls_s()
except ldap.LDAPError as e:
    print(e)
    print(type(e))

r = conn.search_s('ou=people,dc=dlcloud,dc=info',ldap.SCOPE_SUBTREE,'(objectClass=*)',['cn','demo'])
print(r)
# def list_stooges(ldap_base_dn, stooge_filter=None, attrib=None):
#     s = self.ldapconn.search_s(ldap_base_dn, SCOPE_SUBTREE,stooge_filter, attrib)
#     print("Here is the complete list of stooges:")
#     stooge_list = []
#     for stooge in s:
#         attrib_dict = stooge[1]
#         for a in attrib:
#             out = "%s: %s" % (a, attrib_dict[a])
#             print out
#             stooge_list.append(out)
#     return stooge_list