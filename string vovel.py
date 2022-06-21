'''s=input("enter word")
v=0
c=0
for i in range(0,len(s)):
    if s[i] in ("a","e","i","o","u"):
        v=v+1
    else:
        c=c+1
print("total vovel is",v,"consonent is",c)
s="ramesh"
m=s[0]
for i in range(1,len(s)):
    if m<s[i]:
        m=s[i]
print(m)
s="ramesh"
s1=""
s1+=s[5]
s1+=s[1]
s1+=s[4]
s1+=s[3]
s1+=s[2]
s1+=s[0]
print(s1)'''  
s="madam"
c=len(s)-1

for i in range(0,len(s)//2):
    if s[i]!=s[c-i]:
        
        break
    if flag:
        print("pallindrom")

    else:
        print("np")









