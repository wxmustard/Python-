import ldap, sys, ldif
from SearchResult import LDAPSearchResult
'''
LDAP user authentication：
    1）use admin‘s dn and pw information to initialize ldap
    2) look for dn by usrname
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
        print(bind)
        return con
    except ldap.LDAPError as e:
        print(e)
        return e

# 2) get dn information according to usrname 
def getdn_by_usrname(con, usr_base_dn, usrname):
    filter = 'uid=' + usrname
    attrest  = con.search_s(usr_base_dn, ldap.SCOPE_SUBTREE, filter)
    res = LDAPSearchResult.get_search_results(attrest)
    # res = get_search_results(attrest)
    usr_dn = res[0].get_dn()
    return usr_dn

# 3) verify user dn and pw
def verify_usr(con, dn, pw):
    try:
        bind = con.simple_bind_s(dn, pw)
        print(bind)
        return True
    except ldap.LDAPError as e:
        print(e)
        return False

if __name__ == "__main__":
    con = ds3_ldap_init(config)
    usr_base_dn = 'ou=people,dc=dlcloud,dc=info'
    dn = getdn_by_usrname(con, usr_base_dn,'xwang')
    print(verify_usr(con, dn, '123456'))
    pass