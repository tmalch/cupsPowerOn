# poweron cups backend
A cups backend to automatically power on a printer when a print job gets received for it.

### Requires
python3, systemd

tested on Ubuntu 18.04
### Installation
Copy file *poweron* and folder *poweron_scripts* into cups backend folder (_/usr/lib/cups/backend_).
Ensure that *poweron* and *poweron_scripts* are owned by root and have the correct rights
`chown -R root:root poweron_scripts/ poweron`
`chmod -R o-w,u+x poweron_scripts/ poweron`
restart cups to be sure

### Usage
First get the URI for your printer eg. `usb://Brother/HL-2030%20series`  
then add a new printer, select Network Printer poweron - continue  
as Connection URI use *poweron://script/args/original_URI* where
+ *script*: the name of the script file in *poweron_scripts/*
+ *args*: additional arguments for *script* 
+ *original_URI*: is the URI of the printer your retrieved in the first step  

eg. `poweron://tasmota.sh/192.168.0.11/usb://Brother/HL-2030%20series`

When a print job gets send to the backend it calls *script args on* 
eg. `poweron_scripts/tasmota.sh 192.168.0.11 on` and starts a timer to power off with `poweron_scripts/tasmota.sh 192.168.0.11 off` after 15 minuntes.
If another job gets received within those 15 minutes the timer gets reset.
