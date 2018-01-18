#!/bin/bash

## **Updates to this file are now at https://github.com/giovtorres/kvm-install-vm.**
## **This updated version has more options and less hardcoded variables.**

# Take one argument from the commandline: VM name
if ! [ $# -eq 6 ]; then
    echo "Usage: $0 <node-name>"
    echo "Usage: $1 <node-mac>"
    echo "Usage: $2 <node-vncport>"
    echo "Usage: $3 <node-mem>"
    echo "Usage: $4 <node-cpus>"
    echo "Usage: $5 <node-size>"
    echo "Usage: $5 <node-keys>"
    exit 1
fi

# Check if domain already exists
virsh dominfo $1 > /dev/null 2>&1
if [ "$?" -eq 0 ]; then
    echo -n "[WARNING] $1 already exists.  "
    read -p "Do you want to overwrite $1 (y/[N])? " -r
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        virsh destroy $1 > /dev/null
        virsh undefine $1 > /dev/null
    else
        echo -e "\nNot overwriting $1. Exiting..."
        exit 1
    fi
fi

# Directory to store images
DIR=/home/mustard/virt/images

# Location of cloud image

IMAGE=$DIR/xenial-server-cloudimg-amd64-disk.img

# Amount of RAM in MB
MEM=$4

# Number of virtual CPUs
CPUS=$5

# Start the vm afterwards?
DISK_SIZE=$6

# Cloud init files
USER_DATA=user-data
META_DATA=meta-data
CI_ISO=$1-cidata.iso
DISK=$1.qcow2

# Bridge for VMs (default on Fedora is virbr0)
BRIDGE=virbr0

# SSH keys
#PUBFILE="/home/ubuntu/pub_keys/$3.pub"
#if [ $# -gt 2 ]; then
#    if [ -e "$PUBFILE" ]; then
#       KEYS=$(<$PUBFILE)
#        echo "This pub key will be used."
#    else
#        echo "There is no this pub key. Exiting..."
#        exit 1
#    fi
#else
#    KEYS=$(<~/pub_keys/lab7.pub)
#    echo "The local pub key will be used."
#fi
KEYS=$(</home/mustard/.ssh/id_rsa.pub)
# Start clean
rm -rf $DIR/$1
mkdir -p $DIR/$1

pushd $DIR/$1 > /dev/null

    # Create log file
    touch $1.log

    echo "$(date -R) Destroying the $1 domain (if it exists)..."

    # Remove domain with the same name
    virsh destroy $1 >> $1.log 2>&1
    virsh undefine $1 >> $1.log 2>&1

    # cloud-init config: set hostname, remove cloud-init package,
    # and add ssh-key 
    cat > $USER_DATA << _EOF_
#cloud-config
# Hostname management
preserve_hostname: false
hostname: $1
fqdn: $1
# Remove cloud-init when finished with it
runcmd:
  - [ locale-gen, zh_CN.UTF-8]
  - [ apt, remove, cloud-init ]
apt:
  primary:
    - arches: [default]
      uri: https://mirrors.shu.edu.cn/ubuntu/
package_update: true
write_files:
    - content: |
        #!/bin/sh
        printf "\n"
        printf " * Documentation:  https://help.ubuntu.com\n"
        printf " * Management:     https://landscape.canonical.com\n"
        printf " * Support:        https://ubuntu.com/advantage\n"
        printf "\n"
        printf " * Welcome to bdlab Compute Service!\n"
        printf " * If you have a problem in use, please contact @zhonger(zhonger@live.cn)!\n"
        printf "\n"
      path: /etc/update-motd.d/10-help-text
      permissions: "0755"
    - content: |
        #!/bin/sh
      path: /etc/update-motd.d/51-cloudguest
      permissions: "0755"
timezone: Asia/Shanghai
# Configure where output will go
output: 
  all: ">> /var/log/cloud-init.log"
# configure interaction with ssh server
ssh_svcname: ssh
ssh_deletekeys: True
ssh_genkeytypes: ['rsa', 'ecdsa']
# Install my public ssh key to the first user-defined user configured 
# in cloud.cfg in the template (which is centos for CentOS cloud images)
ssh_authorized_keys:
   -  $KEYS
_EOF_

    echo "instance-id: $1; local-hostname: $1" > $META_DATA
    cp $IMAGE $DISK
    qemu-img resize $DISK $DISK_SIZE
    # Create CD-ROM ISO with cloud-init config
    genisoimage -output $CI_ISO -volid cidata -joliet -r $USER_DATA $META_DATA &>> $1.log
    
    virt-install --import --name $1 --ram $MEM --vcpus $CPUS --disk \
    $DISK,format=qcow2,bus=virtio --disk $CI_ISO,device=cdrom --network \
    bridge=virbr0,model=virtio --os-type=linux --graphics vnc,listen=0.0.0.0,port=$3 --os-variant=rhel7 --noautoconsole --mac=$2

    MAC=$(virsh dumpxml $1 | awk -F\' '/mac address/ {print $2}')
    while true
    do
        IP=$(grep -B1 $MAC /var/lib/libvirt/dnsmasq/$BRIDGE.status | head \
             -n 1 | awk '{print $2}' | sed -e s/\"//g -e s/,//)
        if [ "$IP" = "" ]
        then
            sleep 1
        else
            break
        fi
    done

    # Eject cdrom
    echo "$(date -R) Cleaning up cloud-init..."
    virsh change-media $1 hda --eject --config >> $1.log

    # Remove the unnecessary cloud init files
    rm -rf $USER_DATA $CI_ISO

    echo "$(date -R) DONE. SSH to $1 using $IP with  username 'ubuntu'."

popd > /dev/null
