import ldap, sys, ldif
from SearchResult import LDAPSearchResult
'''
LDAP user authentication：
    1）use admin‘s dn and pw information to initialize ldap
    2) look for dn by username
    3) verify user dn and pw
notes:
ldap.simple_bind_s() return 97 denote verification successful
Verification failed will thrown exception
'''

config={
    'ldap_server':'LDAP://ldap.dlcloud.info',
    'base_dn':'cn=admin,dc=dlcloud,dc=info',
    'base_pw':'blcc@asc161'
}

# 1) ldap initilaize
def ds3_ldap_init(config):
    # print(config['base_dn'])
    dn = config['base_dn']
    pw = config['base_pw'] 
    server = config['ldap_server']
    con = ldap.initialize(server)
    try:
        bind = con.simple_bind_s(dn, pw)

if __name__ == "__main__":
    ds3_ldap_init(config)
    pass