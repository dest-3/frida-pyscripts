from __future__ import print_function
import frida
import sys

session = frida.attach(sys.argv[1])
script = session.create_script("""
for (var className in ObjC.classes){ 
    if (ObjC.classes.hasOwnProperty(className))         
        {console.log(className);} }
""")

script.load()
