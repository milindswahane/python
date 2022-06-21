x={"rno":1001,"sname":"manish","branch":"cs","fees":15000}
'''for key in x:
    print(x[key])
for k,v in x.items():
    print(k,' ',v)
x["rno"]=1002
del x["rno"]
x.update({"sem":"3rd"})
for key in x:
    print(key,x[key])
x={}
item=int(input("enter number of items in dictionary"))
for i in range(0,item):
    key = input("enter key")
    value =input("enter value")
    x.update({key:value})
    print(x)'''
del x ["rno"]
x.update({"fees":55000})
l=[]
for k in x:
    print("key is ",k,"and value is",x[k])
    l.append(k)
for i in range(len(1)-1,-1,-1):
    print("key is ",l[i],"and value is ",x[l[i]])





    
