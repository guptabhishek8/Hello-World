a=0
f=open("name.txt","wt")
f.close()
print("Enter names, And type ext , if wann exit entering names")
while 1:
    f=open("name.txt","at")
    st=input("Enter names of students ")
    if st!="ext":
        f.write(st)
        f.write("\n")
    else:
        break
    f.close()
f=open("name.txt")
for x in f:
    a=a+1
print("No. of lines are",a)
f.close()

f=open("name.txt")
c=0
for i in f:
    if (i[0]=="A")or(i[0]=="E")or(i[0]=="I")or(i[0]=="O")or(i[0]=="U"):
            c=c+1
print(c)

t=0
r=0
h=0
f=open("name.txt")
r=len(f.readline())
for i in f:
    t=len(i)
    if t>r:
        r=t
        h=f.readline()
print("Longest name",h)
    

'''

b=0
c=0
f=open("names.txt","rt")
for x in f:
    c= f.readline(1)
    if (c == "A"or"a"or"E"or"e"or"I"or "i"or"O"or"o"or"u"or"U") :
        b=b+1
print(b)'''

    
