user_id =['user1','user2','user3']
names = ['sidd','alka','lala']
last_names = ['dhakad','dhakad','lala']

print(dict(zip(user_id,names))) # 3 value not possible

print(list(zip(user_id,names,last_names)))

user_id =['user1','user2','user3']
names = ['sidd','alka']
print(dict(zip(user_id,names)))

l1 = [1,4,5,8]
l2 = [2,3,6,7]

l = [(1,2),(3,4),(5,6)]

ll1,ll2 = list(zip(*l))
print(ll1)
print(ll2)

new_list =[]
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)


average_finder = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))
