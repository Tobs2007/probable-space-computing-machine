print(__file__)
for x in range(0,7):
    f = open("dyn.typ","w")
    f.write('#include "folien/f'+str(x)+'.typ"')
    f.close()
    input()
