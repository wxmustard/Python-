import sys
import libvirt
conn=libvirt.open('qemu:///system')
name = "/home/ubuntu/kvm/wx/" + sys.argv[1]
print(name)
xmldesc=open(name,'r').read()
dom = conn.defineXML(xmldesc)
dom.create()
conn.close()
exit(0)
