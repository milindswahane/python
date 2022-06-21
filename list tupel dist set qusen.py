'#multipal dict to convert list,tuple,set,dict

d={'a':[1,2,2,3,5,6],"b":("hello",12),'c':{'hello',12,88,'rahul'},'d':{'hello':1,'name':'king}}}
for i in d:
    
    for j in i:
        
        print(i,':',d[j],end=' ')
        
    print()

##a : [1, 2, 2, 3, 5, 6] 
##b : ('hello', 12) 
##c : {88, 12, 'hello', 'rahul'} 
##d : {'hello': 1, 'name': 'king}}'''

'''#dict to list

d={'a':4,'b':5,'c':6,'d':7,'e':8}

for k in d:
    print(d.get(k),end=' ')

# 4 5 6 7 8''' 

'''#list to dict
l=[4,5,6,7,8 ]
d={}
for k in l:
        d.update({k:'k'})
print(d)
#{4: 'k', 5: 'k', 6: 'k', 7: 'k', 8: 'k'}'''

'''#dict to set

d={'h':88,'n':12,'hello':'rahul'}
s=set()
for i in d:
    s.add(i)
print(s)
# {'n', 'h', 'hello'}'''

'''#set to dict
set={1,2,5,8}
d={}
for i in set:
    d.update({i:'value'})
print(d)

#{8: 'value', 1: 'value', 2: 'value', 5: 'value'}'''

'''# dict to tuple
d={"A":1,"x":2,"s":5,"p":8}
l=[]
for i in d:
    l.append(i)
print(tuple(l))

#('A', 'x', 's', 'p')'''

'''
#set to list
s={1,2,5,2,6,3,6,7}
l=[]
for i in s:
    l.append(i)
print(l)
#[1, 2, 3, 5, 6, 7]'''

'''
#set to tuple
s={1,2,5,2,6,3,6,7}
l=[]
for i in s:
    l.append(i)
print(tuple(l))
#(1, 2, 3, 5, 6, 7)'''

'''
#list to set
l=[1, 2, 3, 5, 6, 7]
s=set()
for i in l:
    s.add(i)
print(s)
# {1, 2, 3, 5, 6, 7}'''

'''
#tuple to set
l=(1, 2, 3, 5, 6, 7)
s=set()
for i in l:
    s.add(i)
print(s)
#{1, 2, 3, 5, 6, 7}'''

'''
#tuple to dict
l=(1, 2, 3, 5, 6, 7)
s={}
for i in l:
    s.update({i:'value'})
print(s)
#{1: 'value', 2: 'value', 3: 'value', 5: 'value', 6: 'value', 7: 'value'}'''

'''
#tuple to list
t=(1, 2, 3, 5, 6, 7)
l=[]
for i in t:
    l.append(i)
print(l)
#[1, 2, 3, 5, 6, 7]'''
