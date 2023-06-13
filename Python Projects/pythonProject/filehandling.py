import os
f=open("sample.txt","x")
f.write("HEllo World")
f.close()
f=open("sample.txt","r")
content=f.read()
#print(f.tell())
f.close()

g=open("sample2.txt","x")
g.write(content)
print(g.read())
g.close()





