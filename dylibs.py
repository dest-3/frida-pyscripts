import sys
import frida

session = frida.attach(sys.argv[1])
script = session.create_script("""
var c = 0;
console.log('[+] Starting...')
Process.enumerateModules({
    onMatch: function(dylib){
        c += 1;
        console.log('Dylib: ' + dylib.name);
    },
    onComplete: function(){
        console.log('[+] ' + c + ' libraries loaded');
    }
});
""")
script.load()
