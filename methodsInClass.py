from __future__ import print_function
import frida
import sys

session = frida.attach(sys.argv[1])
script = session.create_script("""
console.log("[*] Starting..."); 
if (ObjC.available) { 
    try { 
        var className = "%s"; 
        var methods = eval('ObjC.classes.' + className + '.$methods'); 
        for (var i = 0; i < methods.length; i++) { 
            try { console.log("[-] " + methods[i]); } 
            catch(err) { console.log("[!] ERROR (forloop): " + err.message); } 
            } } 
        catch(err) { console.log("[!] ERROR (try): " + err.message); } } 
else { console.log("Is Objective-C available on run-time?"); } 
console.log("[*] EXIT");
""" % str(sys.argv[2]))

script.load()
