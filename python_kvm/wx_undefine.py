import sys
import libvirt
conn=libvirt.open('qemu:///system')
domName = sys.argv[1]
pool = conn.lookupByName(domName)
pool.undefine()
conn.close()
exit(0)
