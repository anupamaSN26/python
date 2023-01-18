fobj=open("text5.txt",'r')
fobj1=open("text7.txt",'w')
lines=fobj.readlines()
for i in range(0,len(lines)):
    if i%2!=0:
        l=fobj1.write(lines[i])
fobj.close()

fobj1=open("text7.txt",'r')
print(fobj1.read())
fobj1.close()


