from . import *

kw = {
    
}

t1 = SupabaseTenant(**kw)
t1.delpoy()


time.sleep(60)


t1.undeploy()