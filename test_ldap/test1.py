#coding: utf-8

import  ldap
'''
实现LDAP用户登录验证，首先获取用户的dn，然后再验证用户名和密码
'''

ldappath = "LDAP://ldap.dlcloud.info"#ldap服务器地址
baseDN = "dc=dlcloud,dc=info"#根目录
ldapuser = "cn=admin";#ldap服务器用户名
ldappass = "blcc@asc161";#ldap服务器密码

#获取用户的dn
def _validateLDAPUser(user):
    try:
        l = ldap.initialize(ldappath)
        l.protocol_version = ldap.VERSION3
        l.simple_bind(ldapuser,ldappass)

        searchScope  = ldap.SCOPE_SUBTREE
        searchFiltername = "sAMAccountName"
        retrieveAttributes = None
        searchFilter = '(' + searchFiltername + "=" + user +')'

        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_type, result_data = l.result(ldap_result_id,1)
        if(not len(result_data) == 0):
          r_a,r_b = result_data[0]
          print(r_b["distinguishedName"])
          return 1, r_b["distinguishedName"][0]
        else:
          return 0, ''
    except ldap.LDAPError as e:
        print(e)
        return 0, ''
    finally:
        l.unbind()
        del l

#连接超时，尝试多次连接
def GetDn(user, trynum = 30):
    i = 0
    isfound = 0
    foundResult = ""
    while(i < trynum):
        isfound, foundResult = _validateLDAPUser(user)
        if(isfound):
          break
        i+=1
    return foundResult

def LDAPLogin(userName,Password):
    try:
        if(Password==""):
            print("PassWord empty")
            return
        dn = GetDn(userName,5)
        if(dn==''):
            print("Not Exist User")
            return
        my_ldap = ldap.initialize(ldappath)
        print(my_ldap.simple_bind_s(dn,Password))
        print("Login Ok")
    except Exception as e:
        print("Login Fail")
        # print str(e)

LDAPLogin("cn=xin wang,ou=People","123456")