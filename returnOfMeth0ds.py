from __future__ import print_function
import frida
import sys

session = frida.attach(sys.argv[1])
script = session.create_script("""
if (ObjC.available) { 

try { var className = "%s"; 
var funcName = "%s"; 
var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');

Interceptor.attach(hook.implementation, { 
    onLeave: function(retval) { console.log("[*] Class Name: " + className);
    console.log("[*] Method Name: " + funcName); 
    console.log("\t[-] Type of return value: " + typeof retval);
    console.log("\t[-] Return Value: " + retval); } }); } 
catch(err) { console.log("[!] ERROR: " + err.message); } } 

else { console.log("Objective-C Runtime is not available!"); }
""" % (str(sys.argv[2]), str(sys.argv[3])))
script.load()