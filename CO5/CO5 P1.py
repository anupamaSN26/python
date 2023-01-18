fn=open('text5.txt',"r")
line=fn.readlines()
l=line.split()
l1=[line.strip() for line in lines]
print(l1)
#for x in range (0,len(line)):
   # print(line[x])
#fn.close()

#print([line.strip() for line in open('text5.txt','r')])