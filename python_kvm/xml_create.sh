#!/bin/bash
echo "<domain type='kvm'>
    <name>vm$1</name>
    <memory>4096000</memory>
    <currentMemory>4096000</currentMemory>
    <vcpu>2</vcpu>

   <os>
      <type arch='x86_64' machine='pc'>hvm</type>
      <boot dev='hd'/> 
   </os>

   <features>
     <acpi/>
     <apic/>
     <pae/>
   </features>

   <clock offset='localtime'/>
   <on_poweroff>destroy</on_poweroff>
   <on_reboot>restart</on_reboot>
   <on_crash>destroy</on_crash>
   <devices>
	 <emulator>/usr/bin/kvm-spice</emulator>
	 <disk type='file' device='disk'>
		<driver name='qemu' type='qcow2'/>
        <source file='/home/ubuntu/kvm/wx/vm$1.qcow2'/>
        <target dev='hda' bus='ide'/>
     </disk>
	
     <interface type='bridge'>
		<mac address='52:54:00:33:a4:$1' />
      <source bridge='virbr0'/>
     </interface>

    <input type='mouse' bus='ps2'/>
     <graphics type='vnc' port='59$1' autoport='no' listen = '0.0.0.0' keymap='en-us'/>
   </devices>
</domain>" >vm$1
