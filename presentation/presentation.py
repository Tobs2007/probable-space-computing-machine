import os
global dir
dir = __file__[:-15]


def build():
    foils=[]
    os.remove(dir+"dyn.typ")
    f=open(dir+"dyn.typ","a")
    for x in os.listdir(dir+"folien"):
        if x[0]=="f" and x[-3:]:
            foils.append(x)
    print(foils)
    for x in range(len(foils)-1):
        f.write('#include "folien/f'+str(x)+'.typ"\n#pagebreak()\n')
    f.write('#include "folien/f'+str(len(foils)-1)+'.typ"')

def presentation():
    foils=[]
    for x in os.listdir(dir+"folien"):
        if x[0]=="f" and x[-3:]:
            foils.append(x)
    print(foils)
    for x in range(len(foils)):
        input()
        f = open(dir+"dyn.typ","w")
        f.write('#include "folien/f'+str(x)+'.typ"')
        f.close()





inp=input("0: build  |  1: presentation:")
if inp=="1":
    presentation()
elif inp=="0":
    build()