import csv
persons=[('Zera',23,40),('Zam',27,60),('Meha',21,50)]
csvfile=open('persons.csv','w',newline="")
obj=csv.writer(csvfile)
for person in persons:
    obj.writerow(person)
csvfile.close()
