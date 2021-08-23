# w, a, r+
f = open('file1.txt')
print(f.tell())
print(f.read())
print(f.read(10)) #read 10 char
print(f.tell()) #cursor position
print(f.read())  #nothing print cursor is at EOF

f.seek(0)
print(f.tell())
print(f.read())

f.seek(0)
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.seek(0)
lines = f.readlines() #[:1]
print(lines)
print(len(lines))

f.seek(0)
for line in f:
    print(line,end=" ")

#named, closed
print(f.name)

print(f.closed)
f.close()
print(f.closed)

print("############################")

with open("file1.txt") as f:  #context manager // no need to close file
    print(f.tell())
    print(f.read())
print(f.closed)

with open("file2.txt", 'w') as f:  #create file also if not present
    f.write("hello") #overwrite data

with open("file2.txt", 'a') as f:  #create file also if not present
    f.write("\nplease do it") #append data    

with open("file2.txt", 'r+', encoding='utf-8') as f:  #do not create file 
    print(f.encoding)
    f.seek(len(f.read()))
    f.write("\nplease do it") #overwrite data and leave extra lines


#read write simultaneously


#################################READ/write CSV####################################
from csv import reader
with open('file.csv','r') as f:
    csv_reader = reader(f)
    print(csv_reader)
    next(csv_reader)
    print(type(csv_reader))
    for row in csv_reader:
        print(row)

with open('file.csv','r') as f:
    csv_reader = reader(f)
    print(csv_reader)
    next(csv_reader)
    print(type(csv_reader))
    for row in list(csv_reader):
        print(row[0])

from csv import DictReader
with open('file.csv','r') as f:
    csv_reader = DictReader(f,delimiter=',')
    for row in list(csv_reader):
        print(row)
        print(row.get('phone'))

from csv import writer
with open('file4.csv','w',newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['alka','lala'])
    csv_writer.writerow(['sidd','lala'])

    csv_writer.writerows([['alka','lala'],['sidd','lala']])

from csv import DictWriter
with open('file4.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['name','surname'])
    csv_writer.writeheader()
    csv_writer.writerow({'name' :'alka','surname':'lala'})
    csv_writer.writerow({'name' :'sidd','surname':'lala'})

    csv_writer.writerows([{'name' :'alka','surname':'lala'},{'name' :'sidd','surname':'lala'}])