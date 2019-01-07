# LDAP
## 安装

```bash
# 安装开发环境
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
# 官方文档提供的安装方式，安装在mac的系统python中，/usr/bin/python
# python2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
sudo python -m pip install python-ldap
# 在python3.7中安装ldap库，路径为/usr/local/bin/python3
# python3.7 -> ../Cellar/python/3.7.1/bin/python3.7
sudo pip3.7 install python-ldap
```

## 参考文档
![官方文档](http://www.python-ldap.org/en/latest/resources.html)
![第三方文档1](https://hub.packtpub.com/python-ldap-applications-part-1-installing-and-configuring-python-ldap-library-and-bin/#)
![第三方文档2](https://hub.packtpub.com/configuring-and-securing-python-ldap-applications-part-2/)

### 用户验证

- 基本操作
```python
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
        
# example：
if __name__ == "__main__":
    con = ds3_ldap_init(config)
    usr_base_dn = 'ou=people,dc=dlcloud,dc=info'
    dn = getdn_by_usrname(con, usr_base_dn,'xwang')
    print(verify_usr(con, dn, '123456'))
    pass
```

#### 结果分析
```python
from ldap.cidict import cidict
class LDAPSearchResult:
    """A class to model LDAP results.
    """

    dn = ''

    def __init__(self, entry_tuple):
        """Create a new LDAPSearchResult object."""
        (dn, attrs) = entry_tuple
        if dn:
            self.dn = dn
        else:
            return

        self.attrs = cidict(attrs)

    def get_attributes(self):
        """Get a dictionary of all attributes.
        get_attributes()->{'name1':['value1','value2',...], 
				'name2: [value1...]}
        """
        return self.attrs

    def set_attributes(self, attr_dict):
        """Set the list of attributes for this record.

        The format of the dictionary should be string key, list of
        string alues. e.g. {'cn': ['M Butcher','Matt Butcher']}

        set_attributes(attr_dictionary)
        """

        self.attrs = cidict(attr_dict)

    def has_attribute(self, attr_name):
        """Returns true if there is an attribute by this name in the
        record.

        has_attribute(string attr_name)->boolean
        """
        return self.attrs.has_key( attr_name )

    def get_attr_values(self, key):
        """Get a list of attribute values.
        get_attr_values(string key)->['value1','value2']        """
        return self.attrs[key]
    def get_attr_names(self):
        """Get a list of attribute names.
        get_attr_names()->['name1','name2',...]        """
        return self.attrs.keys()

    def get_dn(self):
        """Get the DN string for the record.
        get_dn()->string dn
        """
        return self.dn


    def pretty_print(self):
        """Create a nice string representation of this object.

        pretty_print()->string
        """
        str = "DN: " + self.dn + "n"
        for a, v_list in self.attrs.iteritems():
            str = str + "Name: " + a + "n"
            for v in v_list:
                str = str + "  Value: " + v + "n"
        str = str + "========"
        return str

    def to_ldif(self):
        """Get an LDIF representation of this record.

        to_ldif()->string
        """
        out = StringIO()
        ldif_out = ldif.LDIFWriter(out)
        ldif_out.unparse(self.dn, self.attrs)
        return out.getvalue()
    def get_search_results(results):
        """
        Given a set of results, return a list of LDAPSearchResult  objects.
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

```