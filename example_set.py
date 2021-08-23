#undodered collection item
s ={2,23,5,4,8,2,3,"hello",2.5} #cannot store list or dict
s.add(10)
s.remove(3)
s.discard(55) #no error if not present
s1 = s.copy()
print(s)
s.clear()
print(s)
print(s1)

if 2 in s1:
    print("present")

for item in s1:
    print(item)

s2 = {2,3,4,6,7,8,0}
s3= {3,5,6,7,8,9}
union = s2 | s3  #not same 
print(union)

intersection  = s2 & s3 #print same
print(intersection)